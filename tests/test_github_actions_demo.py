from github_actions_demo import __version__
from github_actions_demo.birthday import get_birthday


def test_version():
    assert __version__ == "0.1.0"


def test_birthday():
    assert get_birthday() == "23rd September"
