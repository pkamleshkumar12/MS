import json


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User('Max', 27)


# encode a custom object
def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


from json import JSONEncoder


class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User):
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct

# userJson = json.dumps(user, default=encode_user)
userJson = UserEncoder().encode(user)
print(userJson)

userJson = json.loads(userJson, object_hook=decode_user)
print(type(user))
# user is dictionary, inorder to access user.name, it need to be decoded
