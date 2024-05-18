import pytest


@pytest.mark.check
def test_name(user):
    assert user.name == 'Oleksandr'


@pytest.mark.check
def test_second_name(user):
    assert user.second_name == 'Shchapov'
