from mongoengine import Document,EmailField,StringField,DictField,ListField,DateTimeField,EmbeddedDocument,EmbeddedDocumentField,ObjectIdField

POST_STATUS = ('pending','publishing','feleted','draft',)

class PostMetatag(EmbeddedDocument):
    id = ObjectIdField()
    title = StringField()
    description = StringField()
    encode = StringField(default='utf-8')

class PostCategory(EmbeddedDocument):
    id = ObjectIdField()
    title = StringField()



class Posts(Document):
    title = StringField(db_field='blog-title')
    url = StringField()
    content = StringField()
    metatag = EmbeddedDocumentField(PostMetatag)
    categorys = ListField(EmbeddedDocumentField(PostCategory))
    authors = ListField(ObjectIdField())
    status = StringField(choices = POST_STATUS)
    updated_at = DateTimeField()
    created_at = DateTimeField()


    meta = {
        'collection': 'mycol',
        'auto_create_index': True,
        'index_background': True,
        'indexes': [{
            'name': 'status',
            'fields': ('status', 'created_at',)
            },{
                'name': 'url',
                'fields': ('url',),
                'unique': True
            }]
    }