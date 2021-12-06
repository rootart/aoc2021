import pytest

from src.day_2 import solution_b


@pytest.fixture
def inputs():
    return [
        ['forward', 5],
        ['down', 5],
        ['forward', 8],
        ['up', 3],
        ['down', 8],
        ['forward', 2],
    ]


def test_solution_b(inputs):
    assert solution_b(inputs) == 900