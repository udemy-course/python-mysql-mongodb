from datetime import datetime

import mongoengine


class Address(mongoengine.EmbeddedDocument):

    city = mongoengine.StringField(required=True)
    zip_code = mongoengine.IntField(required=True)


class Hobby(mongoengine.EmbeddedDocument):
    type = mongoengine.StringField(required=True)
    rating = mongoengine.IntField(default=8)


class User(mongoengine.Document):
    username = mongoengine.StringField(
        max_length=10, min_length=4, required=True)
    password = mongoengine.StringField(
        max_length=20, min_length=4, required=True)
    email = mongoengine.EmailField(required=True)
    age = mongoengine.IntField(required=True)
    created_at = mongoengine.DateTimeField(default=datetime.utcnow)
    address = mongoengine.EmbeddedDocumentField(Address, required=True)
    hobbies = mongoengine.EmbeddedDocumentListField(Hobby, required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'users',
        'ordering': ['-age']
    }
