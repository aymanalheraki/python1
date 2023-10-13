from mongoengine import Document, StringField, IntField

class User(Document):
    username = StringField(max_length=50, required=True, unique=True)
    age = IntField()
    title = StringField(max_length=15, required=True, uniqe=True)

    meta = {
        'collection': 'users'  # Replace with your desired collection name
    }

from mongoengine import connect

# Replace these with your MongoDB connection details
db_name = 'test'
host = 'localhost'

connect(db_name, host=host)    


# Querying for documents
user = User.objects(username='Ayman').first()

# Creating a new user document
if not user:
    new_user = User(username='Ayman'
                    , age=40
                    , title='Dr.')
    new_user.save()
 #   user.age = 45

else:
    print("Ther is One...........")
# Deleting a document
