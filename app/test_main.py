import importlib
import pytest


main = importlib.import_module("app.main")


def test_returns_list_of_two_ints() -> None:
    res = main.get_human_age(0, 0)
    assert isinstance(res, list), "result must be a list"
    assert len(res) == 2, "list must contain exactly two elements"
    assert all(isinstance(x, int) for x in res), \
        "both elements must be integers"


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_examples_from_readme(
        cat_age: int,
        dog_age: int,
        expected: int
) -> None:
    assert main.get_human_age(cat_age, dog_age) == expected


def test_cat_boundary_transitions() -> None:

    assert main.get_human_age(14, 0)[0] == 0
    assert main.get_human_age(15, 0)[0] == 1
    assert main.get_human_age(23, 0)[0] == 1
    assert main.get_human_age(24, 0)[0] == 2
    assert main.get_human_age(27, 0)[0] == 2
    assert main.get_human_age(28, 0)[0] == 3
    assert main.get_human_age(32, 0)[0] == 4


def test_dog_boundary_transitions() -> None:

    assert main.get_human_age(0, 14)[1] == 0
    assert main.get_human_age(0, 15)[1] == 1
    assert main.get_human_age(0, 23)[1] == 1
    assert main.get_human_age(0, 24)[1] == 2
    assert main.get_human_age(0, 28)[1] == 2
    assert main.get_human_age(0, 29)[1] == 3
    assert main.get_human_age(0, 30)[1] == 3
    assert main.get_human_age(0, 35)[1] == 4
