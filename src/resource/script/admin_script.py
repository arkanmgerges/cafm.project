"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import csv
import os
import sys
from time import sleep
from uuid import uuid4

from elasticsearch_dsl.connections import connections

sys.path.append("../../../")
from src.port_adapter.repository.db_model.City import City
from src.port_adapter.repository.db_model.Country import Country
from src.port_adapter.repository.db_model.Tag import Tag


from src.port_adapter.messaging.common.model.ProjectCommand import ProjectCommand
from src.port_adapter.messaging.common.model.ProjectEvent import ProjectEvent

import click
from confluent_kafka.avro import CachedSchemaRegistryClient
from confluent_kafka.admin import AdminClient, NewTopic
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker

from src.port_adapter.repository.es_model.lookup.subcontractor.Subcontractor import (
    Subcontractor as EsSubcontractor,
)

from src.port_adapter.repository.es_model.lookup.equipment.Equipment import (
    Equipment as EsEquipment,
)

from src.port_adapter.repository.es_model.lookup.daily_check_procedure.DailyCheckProcedure import (
    DailyCheckProcedure as EsDailyCheckProcedure,
)

@click.group()
def cli():
    pass


@cli.command(help="Init db")
def init_db():
    dbName = os.getenv("CAFM_PROJECT_DB_NAME", "cafm-project")
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{dbName}"
    )
    click.echo(click.style(f"Creating database {dbName}", fg="green"))
    if not database_exists(engine.url):
        create_database(engine.url)


@cli.command(help="Check if elastic search is ready")
def check_elasticsearch_readiness():
    click.echo(click.style("Check if elastic search is ready", fg="green", bold=True))
    counter = 5
    sleepPeriod = 10
    while counter > 0:
        try:
            connection = connections.create_connection(
                hosts=[
                    f'{os.getenv("CAFM_PROJECT_ELASTICSEARCH_HOST", "elasticsearch")}:{os.getenv("CAFM_PROJECT_ELASTICSEARCH_PORT", 9200)}'
                ]
            )
            connection.info()
            click.echo(click.style("elasticsearch is ready", fg="green", bold=True))
            exit(0)
        except Exception as e:
            click.echo(click.style(f"Error thrown ... {e}", fg="red"))
            click.echo(
                click.style(f"Sleep {sleepPeriod} seconds ...", fg="green", bold=True)
            )
            click.echo(click.style(f"Remaining retries: {counter}", fg="green"))
            sleepPeriod += 3
            sleep(sleepPeriod)
    exit(1)


@cli.command(help="Init elastic search indexes")
def init_elasticsearch_indexes():
    connections.create_connection(
        hosts=[
            f'{os.getenv("CAFM_PROJECT_ELASTICSEARCH_HOST", "elasticsearch")}:{os.getenv("CAFM_PROJECT_ELASTICSEARCH_PORT", 9200)}'
        ]
    )
    click.echo(click.style(f"Creating elasticsearch indexes", fg="green"))
    models = [EsSubcontractor, EsEquipment, EsDailyCheckProcedure]
    for model in models:
        if not model._index.exists():
            model.createIndex()


@cli.command(help="Import maxmind countries and cities")
def import_maxmind_data():
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
    )
    cities = []
    countries = []
    Session = sessionmaker(bind=engine)
    session = Session()
    click.echo(click.style("Importing countries", fg="green"))
    dbObject = session.query(Country).first()
    currentDir = os.path.dirname(os.path.realpath(__file__))
    if dbObject is None:
        with open(
            f"{currentDir}/../maxmind/GeoLite2-Country-Locations-en.csv", newline=""
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            cnt = 0
            for row in reader:
                countryIsoCode = row["country_iso_code"]
                if row["country_iso_code"] == "":
                    countryIsoCode = f"VAL-{cnt}"
                    cnt += 1
                countries.append(
                    Country(
                        geoNameId=row["geoname_id"],
                        localeCode=row["locale_code"],
                        continentCode=row["continent_code"],
                        continentName=row["continent_name"],
                        countryIsoCode=countryIsoCode,
                        countryName=row["country_name"],
                        isInEuropeanUnion=row["is_in_european_union"] == "1",
                    )
                )
        session.add_all(countries)
    click.echo(click.style("Importing cities", fg="green"))
    dbObject = session.query(City).first()
    if dbObject is None:
        with open(
            f"{currentDir}/../maxmind/GeoLite2-City-Locations-en.csv", newline=""
        ) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                metroCode = row["metro_code"]
                if row["metro_code"] == "":
                    metroCode = None

                cities.append(
                    City(
                        geoNameId=row["geoname_id"],
                        localeCode=row["locale_code"],
                        continentCode=row["continent_code"],
                        continentName=row["continent_name"],
                        countryIsoCode=row["country_iso_code"],
                        countryName=row["country_name"],
                        subdivisionOneIsoCode=row["subdivision_1_iso_code"],
                        subdivisionOneIsoName=row["subdivision_1_name"],
                        subdivisionTwoIsoCode=row["subdivision_2_iso_code"],
                        subdivisionTwoIsoName=row["subdivision_2_name"],
                        cityName=row["city_name"],
                        metroCode=metroCode,
                        timeZone=row["time_zone"],
                        isInEuropeanUnion=row["is_in_european_union"] == "1",
                    )
                )
        session.add_all(cities)
    if len(countries) > 0 or len(cities) > 0:
        session.commit()
    click.echo(click.style("Done importing countries and cities", fg="green"))
    session.close()


@cli.command(help="Add role tags")
def add_role_tags():
    engine = create_engine(
        f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
    )
    tags = []
    Session = sessionmaker(bind=engine)
    session = Session()
    click.echo(click.style("Adding role tags", fg="green"))

    dbObject = session.query(Tag).filter_by(name="provider").first()
    if dbObject is None:
        tags.append(Tag(id=str(uuid4()),name="provider"))

    dbObject = session.query(Tag).filter_by(name="beneficiary").first()
    if dbObject is None:
        tags.append(Tag(id=str(uuid4()),name="beneficiary"))

    dbObject = session.query(Tag).filter_by(name="tenant").first()
    if dbObject is None:
        tags.append(Tag(id=str(uuid4()),name="tenant"))

    dbObject = session.query(Tag).filter_by(name="projectAccess").first()
    if dbObject is None:
        tags.append(Tag(id=str(uuid4()),name="projectAccess"))

    dbObject = session.query(Tag).filter_by(name="organizationAccess").first()
    if dbObject is None:
        tags.append(Tag(id=str(uuid4()),name="organizationAccess"))

    dbObject = session.query(Tag).filter_by(name="userAccess").first()
    if dbObject is None:
        tags.append(Tag(id=str(uuid4()),name="userAccess"))

    if len(tags) > 0:
        session.add_all(tags)
        session.commit()

    click.echo(click.style("Done adding role tags", fg="green"))
    session.close()


@cli.command(help="Initialize kafka topics and schema registries")
def init_kafka_topics_and_schemas():
    # Create topics
    requiredTopics = [
        "cafm.project.cmd",
        "cafm.project.evt",
        "cafm.project.failed-cmd-handle",
        "cafm.project.failed-lookup-evt-handle",
        "cafm.project.identity-failed-evt-handle",
    ]
    click.echo(
        click.style(f"Initializing kafka topics and schema registries", fg="green")
    )
    newTopics = []
    admin = AdminClient({"bootstrap.servers": os.getenv("MESSAGE_BROKER_SERVERS", "")})
    installedTopics = admin.list_topics().topics.keys()

    for requiredTopic in requiredTopics:
        if requiredTopic not in installedTopics:
            newTopics.append(
                NewTopic(
                    requiredTopic,
                    num_partitions=int(
                        os.getenv("KAFKA_PARTITIONS_COUNT_PER_TOPIC", 1)
                    ),
                    replication_factor=1,
                )
            )

    if len(newTopics) > 0:
        fs = admin.create_topics(newTopics)
        for topic, f in fs.items():
            try:
                f.result()  # The result itself is None
                click.echo(click.style("Topic {} created".format(topic), fg="green"))
            except Exception as e:
                click.echo(
                    click.style(f"Failed to create topic {topic}: {e}", fg="red")
                )

    # Create schemas
    c = CachedSchemaRegistryClient(
        {"url": os.getenv("MESSAGE_SCHEMA_REGISTRY_URL", "")}
    )
    requiredSchemas = [
        {"name": "cafm.project.Command", "schema": ProjectCommand.get_schema()},
        {"name": "cafm.project.Event", "schema": ProjectEvent.get_schema()},
    ]
    newSchemas = []
    for requiredSchema in requiredSchemas:
        click.echo(
            click.style(
                f'Verify if schema {requiredSchema["name"]} is available', fg="green"
            )
        )
        r = c.get_latest_schema(subject=f'{requiredSchema["name"]}')
        if r[0] is None:
            click.echo(
                click.style(
                    f'Schema {requiredSchema["name"]} will be created', fg="green"
                )
            )
            newSchemas.append(requiredSchema)
    [c.register(schema["name"], schema["schema"]) for schema in newSchemas]


@cli.command(help="Drop kafka topics and schema registries")
def drop_kafka_topics_and_schemas():
    # Delete topics
    topics = [
        "cafm.project.cmd",
        "cafm.project.evt",
        "cafm.project.failed-cmd-handle",
        "cafm.project.failed-lookup-evt-handle",
        "cafm.project.identity-failed-evt-handle",
    ]
    click.echo(click.style(f"Dropping kafka topics and schema registries", fg="green"))
    admin = AdminClient({"bootstrap.servers": os.getenv("MESSAGE_BROKER_SERVERS", "")})
    fs = admin.delete_topics(topics, operation_timeout=30)
    for topic, f in fs.items():
        try:
            f.result()  # The result itself is None
            click.echo(click.style("Topic {} deleted".format(topic), fg="green"))
        except Exception as e:
            click.echo(click.style(f"Failed to delete topic {topic}: {e}", fg="red"))

    # Delete schemas
    schemas = ["cafm.project.Command", "cafm.project.Event"]
    c = CachedSchemaRegistryClient(
        {"url": os.getenv("MESSAGE_SCHEMA_REGISTRY_URL", "")}
    )
    [c.delete_subject(schema) for schema in schemas]


@cli.command(help="Check if mysql is ready")
def check_mysql_readiness():
    from sqlalchemy import create_engine

    click.echo(click.style("Check if mysql is ready", fg="green", bold=True))
    counter = 5
    sleepPeriod = 10
    while counter > 0:
        try:
            counter -= 1
            create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
            click.echo(click.style("mysql is ready", fg="green", bold=True))
            exit(0)
        except Exception as e:
            click.echo(click.style(f"Error thrown ... {e}", fg="red"))
            click.echo(
                click.style(f"Sleep {sleepPeriod} seconds ...", fg="green", bold=True)
            )
            click.echo(click.style(f"Remaining retries: {counter}", fg="green"))
            sleepPeriod += 3
            sleep(sleepPeriod)
    exit(1)


@cli.command(help="Check if schema registry is ready")
def check_schema_registry_readiness():
    from confluent_kafka.avro import CachedSchemaRegistryClient

    click.echo(click.style("Check if schema registry is ready", fg="green", bold=True))
    counter = 15
    sleepPeriod = 10
    while counter > 0:
        try:
            counter -= 1
            click.echo(click.style("Sending a request ...", fg="green", bold=True))
            c = CachedSchemaRegistryClient(
                {"url": os.getenv("MESSAGE_SCHEMA_REGISTRY_URL", "")}
            )
            c.get_latest_schema(subject="test")
            click.echo(click.style("Schema registry is ready", fg="green", bold=True))
            exit(0)
        except Exception as e:
            click.echo(click.style(f"Error thrown ... {e}", fg="red"))
            click.echo(
                click.style(f"Sleep {sleepPeriod} seconds ...", fg="green", bold=True)
            )
            click.echo(click.style(f"Remaining retries: {counter}", fg="green"))
            sleepPeriod += 3
            sleep(sleepPeriod)
    exit(1)


if __name__ == "__main__":
    cli()
