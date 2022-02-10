from resources.config import configuration
from users.users_models import User


def log_in(username, password):
    if configuration.users.get(username) is not None:
        if configuration.users.get(username).get('password') is password:
            configuration.user = configuration.users.get(username)


def sign_up(username, password, type='Free'):
    if configuration.users.get(username) is None:
        configuration.user = User(username, password, type)
        configuration.users.update({username: {'password': password, 'type': type}})
