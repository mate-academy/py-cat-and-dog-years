import pytest

from app.main import get_human_age

INVALID_AGE_CASES: list[tuple[object, object]] = [
    ("15", 15),
    (15, "15"),
    (15.1, 15),
    (15, 15.1),
    (None, 15),
    (15, None),
    (None, None),
    ({}, 15),
    (15, {}),
    (
        {"a": 1, "b": 2},
        15
    ),
]

INVALID_AGE_VALUE_CASES = [(102, 101), (-1, -7), (-1, 15), (0, 1), (1, 0)]


@pytest.mark.parametrize("cat_age, dog_age", INVALID_AGE_VALUE_CASES)
def test_invalid_age_values(cat_age: int, dog_age: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize("cat_age, dog_age", INVALID_AGE_CASES)
def test_invalid_age_types(cat_age: object, dog_age: object) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)


def provide_test_data(pet_age: int, human_age: int) -> int:
    if pet_age < 15:
        return 0
    elif pet_age < 24:
        return 1
    else:
        return 2 + ((pet_age - 24) // human_age)


def provide_test_id(case: int) -> str:
    return f"{case}_cat_dog_years."


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (i, i, [provide_test_data(i, 4),
                provide_test_data(i, 5)]) for i in range(1, 101)]
    + [
        (i, i - 2, [provide_test_data(i, 4),
                    provide_test_data(i - 2, 5)]) for i in range(3, 101)],
    ids=provide_test_id,
)
def test_get_human_age(cat_age: int, dog_age: int, expected: int) -> None:
    assert get_human_age(cat_age, dog_age) == expected
