from code.third_party.quotes import daodejing
import random


def test_dao_output():
    assert None is random.choice(daodejing.dao)
