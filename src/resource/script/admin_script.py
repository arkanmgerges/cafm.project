"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import csv
import sys
import os

sys.path.append("../../../")
from src.port_adapter.repository.db_model.City import City
from src.port_adapter.repository.db_model.Country import Country

from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.port_adapter.messaging.common.model.ProjectEvent import ProjectEvent


import click
from confluent_kafka.avro import CachedSchemaRegistryClient
from confluent_kafka.admin import AdminClient, NewTopic
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

@click.group()
def cli():
    pass

@cli.command(help='Init db')
def init_db():
    dbName = os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{dbName}")
    click.echo(click.style(f"Creating database {dbName}", fg='green'))
    if not database_exists(engine.url):
        create_database(engine.url)

@cli.command(help='Import maxmind countries and cities')
def import_maxmind_data():
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
    cities = []
    countries = []
    Session = sessionmaker(bind=engine)
    session = Session()
    click.echo(click.style("Importing countries", fg='green'))
    dbObject = session.query(Country).first()
    currentDir = os.path.dirname(os.path.realpath(__file__))
    if dbObject is None:
        with open(f'{currentDir}/../maxmind/GeoLite2-Country-Locations-en.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cnt = 0
            for row in reader:
                countryIsoCode = row['country_iso_code']
                if row['country_iso_code'] == '':
                    countryIsoCode = f'VAL-{cnt}'
                    cnt += 1
                countries.append(Country(geoNameId=row['geoname_id'], localeCode=row['locale_code'],
                                         continentCode=row['continent_code'],
                                         continentName=row['continent_name'],
                                         countryIsoCode=countryIsoCode,
                                         countryName=row['country_name'],
                                         isInEuropeanUnion=row['is_in_european_union'] == '1'))
        session.add_all(countries)
    click.echo(click.style("Importing cities", fg='green'))
    dbObject = session.query(City).first()
    if dbObject is None:
        with open(f'{currentDir}/../maxmind/GeoLite2-City-Locations-en.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                metroCode = row['metro_code']
                if row['metro_code'] == '':
                    metroCode = None

                cities.append(
                    City(geoNameId=row['geoname_id'], localeCode=row['locale_code'],
                         continentCode=row['continent_code'],
                         continentName=row['continent_name'], countryIsoCode=row['country_iso_code'],
                         countryName=row['country_name'],
                         subdivisionOneIsoCode=row['subdivision_1_iso_code'],
                         subdivisionOneIsoName=row['subdivision_1_name'],
                         subdivisionTwoIsoCode=row['subdivision_2_iso_code'],
                         subdivisionTwoIsoName=row['subdivision_2_name'],
                         cityName=row['city_name'],
                         metroCode=metroCode,
                         timeZone=row['time_zone'],
                         isInEuropeanUnion=row['is_in_european_union'] == '1'))
        session.add_all(cities)
    if len(countries) > 0 or len(cities) > 0:
        session.commit()
    click.echo(click.style("Done importing countries and cities", fg='green'))
    session.close()

@cli.command(help='Initialize kafka topics and schema registries')
def init_kafka_topics_and_schemas():
    # Create topics
    requiredTopics = ['cafm.project.cmd', 'cafm.project.evt']
    click.echo(click.style(f"Initializing kafka topics and schema registries", fg='green'))
    newTopics = []
    admin = AdminClient({'bootstrap.servers': os.getenv('MESSAGE_BROKER_SERVERS', '')})
    installedTopics = admin.list_topics().topics.keys()

    for requiredTopic in requiredTopics:
        if requiredTopic not in installedTopics:
            newTopics.append(
                NewTopic(requiredTopic, num_partitions=int(os.getenv('KAFKA_PARTITIONS_COUNT_PER_TOPIC', 1)),
                         replication_factor=1))

    if len(newTopics) > 0:
        fs = admin.create_topics(newTopics)
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                click.echo(click.style("Topic {} created".format(topic), fg='green'))
            except Exception as e:
                click.echo(click.style(f'Failed to create topic {topic}: {e}', fg='red'))

    # Create schemas
    c = CachedSchemaRegistryClient({'url': os.getenv('MESSAGE_SCHEMA_REGISTRY_URL', '')})
    requiredSchemas = [{'name': 'cafm.project.Command', 'schema': ProjectCommand.get_schema()},
               {'name': 'cafm.project.Event', 'schema': ProjectEvent.get_schema()}]
    newSchemas = []
    for requiredSchema in requiredSchemas:
        click.echo(click.style(f'Verify if schema {requiredSchema["name"]} is available', fg='green'))
        r = c.get_latest_schema(subject=f'{requiredSchema["name"]}')
        if r[0] is None:
            click.echo(click.style(f'Schema {requiredSchema["name"]} will be created', fg='green'))
            newSchemas.append(requiredSchema)
    [c.register(schema['name'], schema['schema']) for schema in newSchemas]


@cli.command(help='Drop kafka topics and schema registries')
def drop_kafka_topics_and_schemas():
    # Delete topics
    topics = ['cafm.project.cmd', 'cafm.project.evt']
    click.echo(click.style(f"Dropping kafka topics and schema registries", fg='green'))
    admin = AdminClient({'bootstrap.servers': os.getenv('MESSAGE_BROKER_SERVERS', '')})
    fs = admin.delete_topics(topics, operation_timeout=30)
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            click.echo(click.style("Topic {} deleted".format(topic), fg='green'))
        except Exception as e:
            click.echo(click.style(f'Failed to delete topic {topic}: {e}', fg='red'))

    # Delete schemas
    schemas = ['cafm.project.Command', 'cafm.project.Event']
    c = CachedSchemaRegistryClient({'url': os.getenv('MESSAGE_SCHEMA_REGISTRY_URL', '')})
    [c.delete_subject(schema) for schema in schemas]


if __name__ == '__main__':
    cli()
