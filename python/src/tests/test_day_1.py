import pytest

from src.day_1 import solution_a, solution_b, get_inputs


@pytest.fixture
def inputs():

    return [
        199,
        200,
        208,
        210,
        200,
        207,
        240,
        269,
        260,
        263,
    ]


def test_solution_a(inputs):
    assert solution_a(inputs) == 7


def test_final_solution_a():
    assert solution_a(get_inputs()) == 1162


def test_final_solution_b():
    assert solution_b(get_inputs()) == 1190