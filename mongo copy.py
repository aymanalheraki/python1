"""
This module contains a sample class 'User' and establishes a connection to a MongoDB database.

Author: Your Name
Date: 2023-10-10
"""

from mongoengine import connect,Document, StringField, IntField

class User(Document):  # pylint: disable=no-member
    # ...
    """
    Represents a user document in the MongoDB collection.

    This class defines the structure of the 'User' document with fields for
    'username', 'age', and 'title'.
    """
    username = StringField(max_length=50, required=True, unique=True)
    age = IntField()
    title = StringField(max_length=15, required=True, unique=True)

    meta = {
        'collection': 'users'  # Replace with your desired collection name
    }


# Replace these with your MongoDB connection details
DB_NAME = 'test'
HOST = 'localhost'

connect(DB_NAME, host=HOST)

# Querying for documents
user = User.objects(age=40).first()

# Creating a new user document
if not user:
    new_user = User(username='Ayman', age=40, title='Dr.')
    new_user.save()
else:
    print("There is one existing user with the username 'Ayman'.")

# Deleting a document
