import pytest
from app import main
from app.main import get_human_age, convert_to_human


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
        (29, 29, [3, 3]),
        (100, 100, [21, 17]),
    ],
)
def test_get_human_age_normal_cases(
    cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (100, 100),
        (50, 60),
        (200, 150),
    ],
)
def test_get_human_age_large_numbers(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert all(isinstance(x, int) for x in result)
    assert result[0] >= 0 and result[1] >= 0


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        (-1, 10),
        (10, -5),
        (-3, -7),
        (-100, -200),
    ],
)
def test_get_human_age_negative_values(cat_age: int, dog_age: int) -> None:
    result = get_human_age(cat_age, dog_age)
    assert all(x >= 0 for x in result)


@pytest.mark.parametrize(
    "first_year, second_year, each_year_cat, each_year_dog, "
    "cat_age, dog_age, expected",
    [
        (14, 9, 4, 5, 14, 14, [1, 1]),
        (15, 9, 4, 5, 15, 15, [1, 1]),
        (15, 9, 4, 5, 23, 23, [1, 1]),
        (15, 9, 4, 5, 24, 24, [2, 2]),
        (15, 9, 4, 5, 27, 28, [2, 2]),
        (15, 9, 4, 5, 28, 29, [3, 3]),
    ],
)
def test_ages(
    monkeypatch: pytest.MonkeyPatch,
    first_year: int,
    second_year: int,
    each_year_cat: int,
    each_year_dog: int,
    cat_age: int,
    dog_age: int,
    expected: list[int],
) -> None:
    def mock_get_human_age(
            cat_age_param: int,
            dog_age_param: int) -> list[int]:
        cat_human = convert_to_human(
            cat_age_param, first_year, second_year, each_year_cat
        )
        dog_human = convert_to_human(
            dog_age_param, first_year, second_year, each_year_dog
        )
        return [cat_human, dog_human]

    monkeypatch.setattr(main, "get_human_age", mock_get_human_age)
    result = main.get_human_age(cat_age, dog_age)
    assert result == expected
