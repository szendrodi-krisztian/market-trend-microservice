from time import sleep
from peewee import *
import os
from pathlib import Path

def get_mysql_password():
    api_key_path = os.environ.get('MYSQL_PASSWORD_FILE')
    api_key_value = Path(api_key_path).read_text()
    return api_key_value

db = MySQLDatabase("trading", host="database", port=3306, user="dmlab", passwd=get_mysql_password())

class ModelBase(Model):
    class Meta:
        database = db

class Trade(ModelBase):
    price = FloatField()
    symbol = CharField()
    time = TimestampField()
    volume = FloatField()

def connect_to_database():
    while True:
        try:
            db.connect()
            break
        except DatabaseError:
            sleep(1)

    db.create_tables([Trade])