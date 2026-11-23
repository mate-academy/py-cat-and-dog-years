import pytest

from app.main import get_human_age


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
def test_should_return_human_age_as_in_examples(
        cat_age: int,
        dog_age: int,
        expected: list[int],
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected",
    [(31, 3), (32, 4), (35, 4), (36, 5)],
)
def test_cat_age_should_grow_every_four_years_after_24(
        cat_age: int,
        expected: int,
) -> None:
    assert get_human_age(cat_age, 0)[0] == expected


@pytest.mark.parametrize(
    "dog_age, expected",
    [(28, 2), (29, 3), (33, 3), (34, 4)],
)
def test_dog_age_should_grow_every_five_years_after_24(
        dog_age: int,
        expected: int,
) -> None:
    assert get_human_age(0, dog_age)[1] == expected


def test_cat_and_dog_ages_should_be_calculated_independently() -> None:
    assert get_human_age(15, 100) == [1, 17]
    assert get_human_age(100, 15) == [21, 1]


def test_should_return_list_of_two_elements() -> None:
    result = get_human_age(20, 20)
    assert isinstance(result, list)
    assert len(result) == 2
