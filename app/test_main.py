import pytest
from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_for_under_first_year_threshold() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_for_first_threshold() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_for_second_threshold_end() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_for_second_threshold_crossed() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_for_dog_but_two_for_cat_before_next_jump() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_return_three_for_cat_and_two_for_dog() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_large_example_case() -> None:
    assert get_human_age(100, 100) == [21, 17]


@pytest.mark.parametrize(
    "cat_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (28, 3),
        (100, 21),
    ],
)
def test_cat_age_cases(cat_age: int, expected: int) -> None:
    human_cat, _ = get_human_age(cat_age, 0)
    assert human_cat == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [
        (0, 0),
        (14, 0),
        (15, 1),
        (23, 1),
        (24, 2),
        (27, 2),
        (28, 2),
        (33, 3),
        (100, 17),
    ],
)
def test_dog_age_cases(dog_age: int, expected: int) -> None:
    _, human_dog = get_human_age(0, dog_age)
    assert human_dog == expected


# --- edge cases ---

def test_negative_ages_should_return_zero() -> None:
    assert get_human_age(-10, -10) == [0, 0]
    assert get_human_age(-1, 20)[0] == 0
    assert get_human_age(20, -5)[1] == 0


def test_should_raise_typeerror_for_incorrect_types() -> None:
    with pytest.raises(TypeError):
        get_human_age("cat", "dog")

    with pytest.raises(TypeError):
        get_human_age(15.5, 20.2)

    with pytest.raises(TypeError):
        get_human_age(None, None)
