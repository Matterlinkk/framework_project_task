import pytest


class User:
    def __init__(self):
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Oleksandr'
        self.second_name = 'Shchapov'

    def remove(self):
        self.name = ''
        self.name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()
