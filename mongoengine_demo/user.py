import mongoengine


class User(mongoengine.Document):
    username = mongoengine.StringField()
    password = mongoengine.StringField()
    email = mongoengine.StringField()
    created_at = mongoengine.DateTimeField()

    meta = {
        'db_alias': 'core',
        'collection': 'users',
    }
