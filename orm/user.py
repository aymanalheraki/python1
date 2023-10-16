from mongoengine import Document,EmailField,StringField,DictField,ListField,DateTimeField

class User(Document):
    email = EmailField(required=True,unique=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Posts(Document):
    title = StringField()
    content = StringField()
    metatag = DictField()
    categorys = ListField()
    authors = ListField()
    status = StringField()
    updated_at = DateTimeField()
    created_at = DateTimeField()



