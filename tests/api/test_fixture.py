import pytest


@pytest.mark.check
def test_change_name(user):
    assert user.name == 'Oleksandr'
    assert user.second_name == 'Shchapov'


@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Shchapov'


@pytest.mark.change
def test_remove_name(user):
    user.remove()
    assert user.name == ''
