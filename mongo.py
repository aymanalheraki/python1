from mongoengine import connect,ObjectIdField
from orm.user import User
from mongoengine import NotUniqueError
from orm.posts import Posts,PostMetatag,PostCategory
connect(db='test',
        host='localhost',
        port=27017
        )

meta = {
        'collection': 'users'  # Replace with your desired collection name
    }
# try:
#     user = User(email='aym@astm.net')
#     user.first_name = 'Ayman2'
#     user.last_name = 'Alheraki2'
#     user.save()
# except NotUniqueError as e:
#     print('Email not allready correct')

# user = User.objects(first_name='Hammad')

# fields = {
#     'first_name': 'Bessan',
#     'last_name': 'Saud'
# }


# user.update(**fields)
post = Posts.objects.get(pk='652be657e8b556ddb9d8d550')
update_dict = {
    'set__metatag__title': 'new sddsfdsfdsfsdfsd',
    'set__metatag__description': 'new desc',
    'set__categorys__0__title': 'hay hay hay'

}

post.update(**update_dict)

# post_metatag = PostMetatag()
# post_metatag.title = 'Tets meta tag'
# post_metatag.description = 'vxvxvxdfgdfg dfg df gdf ggfd'
# post_metatag.encode = 'ar-sa'
# post_category = PostCategory()
# post_category.title = 'Any Thing'
# post_category.id = '652966f59a8e399065dff87f'



# post = Posts()
# post.title = 'Hello World'
# post.url = 'hello-world'
# post.content = 'World is nice :)'


# post.categorys.append(post_category)
# post.metatag = post_metatag
# post.status = 'pending'
# post.authors.append('652966f59a8e399065dff87f')
# post.authors.append('652966f59a8e399065dff87c')
# post.authors.append('652966f59a8e399065dff87e')
# post.save()


