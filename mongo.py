from mongoengine import connect
from orm.user import User
from mongoengine import NotUniqueError

connect(db='test',
        host='localhost',
        port=27017
        )

meta = {
        'collection': 'users'  # Replace with your desired collection name
    }
try:
    user = User(email='ffff2@astm.net')
    user.first_name = 'Ayman'
    user.last_name = 'Alheraki'
    user.save()
except NotUniqueError as e:
    print('Email not allready correct')


