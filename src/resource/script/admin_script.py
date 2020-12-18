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
from sqlalchemy.orm import sessionmaker

@click.group()
def cli():
    pass

@cli.command(help='Import maxmind countries and cities')
def import_maxmind_data():
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
    cities = []
    countries = []
    Session = sessionmaker(bind=engine)
    session = Session()
    click.echo(click.style("Importing countries", fg='green'))

    with open('../maxmind/GeoLite2-Country-Locations-en.csv', newline='') as csvfile:
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
    with open('../maxmind/GeoLite2-City-Locations-en.csv', newline='') as csvfile:
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
    session.commit()
    click.echo(click.style("Done importing countries and cities", fg='green'))
    session.close()

@cli.command(help='Initialize kafka topics and schema registries')
def init_kafka_topics_and_schemas():
    # Create topics
    topics = ['cafm.project.cmd', 'cafm.project.evt']
    newTopics = [NewTopic(topic, num_partitions=int(os.getenv('KAFKA_PARTITIONS_COUNT_PER_TOPIC', 1)), replication_factor=1) for topic in topics]
    admin = AdminClient({'bootstrap.servers': 'kafka:9092'})
    fs = admin.create_topics(newTopics)
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            click.echo(click.style("Topic {} created".format(topic), fg='green'))
        except Exception as e:
            click.echo(click.style(f'Failed to create topic {topic}: {e}', fg='red'))

    # Create schemas
    c = CachedSchemaRegistryClient({'url': os.getenv('MESSAGE_SCHEMA_REGISTRY_URL', '')})
    schemas = [{'name': 'cafm.project.Command', 'schema': ProjectCommand.get_schema()},
               {'name': 'cafm.project.Event', 'schema': ProjectEvent.get_schema()}]
    [c.register(schema['name'], schema['schema']) for schema in schemas]


@cli.command(help='Drop kafka topics and schema registries')
def drop_kafka_topics_and_schemas():
    # Delete topics
    topics = ['cafm.project.cmd', 'cafm.project.evt']
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
