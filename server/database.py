from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
import logging


class Database(object):

    instance = None
    engine = None
    metadata = None
    batteries = None
    device_tokens = None

    def __new__(cls, *args, **keys):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
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
            cls.device_tokens = Table(
                'device_tokens', cls.metadata,
                Column('id', Integer, primary_key=True),
                Column('token', String(64)),
                Column('uuid', String(36))
            )

            cls.metadata.create_all(cls.engine)
            logging.info('Created table')

        return cls.instance

    def battery_insert(self, json):
        self.batteries.insert().execute(name=json['name'], battery=float(json['battery']), uuid=json['uuid'])

    def battery_delete(self, batteries_id):
        self.batteries.delete().where(self.batteries.c.id == batteries_id).execute()

    def battery_select_all(self):
        return self.batteries.select().execute().fetchall()

    def battery_select_all_group_by_uuid(self):
        return self.batteries.select().group_by(self.batteries.c.uuid).execute().fetchall()

    def battery_select_filter_device(self, uuid):
        return self.batteries.select().where(self.batteries.c.uuid == uuid).order_by('datetime').execute().fetchall()

    def is_token(self, uuid):
        return True \
            if len(self.device_tokens.select().where(self.device_tokens.c.uuid == uuid).execute().fetchall()) \
            else False

    def token_insert(self, json):
        self.device_tokens.insert().execute(token=json['token'], uuid=json['uuid'])

    def token_update(self, json):
        self.device_tokens.update().where(self.device_tokens.c.token == json['uuid']).execute(token=json['token'])

    def token_select_all(self):
        return self.device_tokens.select().execute().fetchall()
