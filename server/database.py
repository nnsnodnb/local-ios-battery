from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
import logging


class Database(object):

    shared = None
    engine = None
    metadata = None
    batteries = None

    def __new__(cls, *args, **keys):
        if cls.shared is None:
            cls.shared = object.__new__(cls)
            cls.engine = create_engine('sqlite:///db.sqlite3', echo=True)
            cls.metadata = MetaData()
            cls.metadata.bind = cls.engine

            cls.batteries = Table(
                'batteries', cls.metadata,
                Column('id', Integer, primary_key=True),
                Column('name', String),
                Column('battery', Float),
                Column('uuid', String(36)),  # Include hyphen
                Column('datetime', DateTime(timezone=True), default=func.now())
            )

            cls.metadata.create_all(cls.engine)
            logging.info('Created table')

        return cls.shared

    def insert(self, json):
        self.batteries.insert().execute(name=json['name'], battery=float(json['battery']), uuid=json['uuid'])

    def delete(self, batteries_id):
        self.batteries.delete().where(self.batteries.id == batteries_id).execute()

    def select_all(self):
        return self.batteries.select().execute().fetchall()

    def select_filter_device(self, uuid):
        return self.batteries.select().where(self.batteries.uuid == uuid).order_by('datetime').execute().fetchall()
