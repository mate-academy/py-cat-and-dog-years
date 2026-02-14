from app.main import get_human_age
import pytest


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
def test_get_human_age_examples(
        cat_age: int, dog_age: int, expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, expected_cat",
    [
        (-1, None),
        (25, 2),
    ],
)
def test_cat_age_boundaries(cat_age: int, expected_cat: int | None) -> None:
    if cat_age < 0:
        with pytest.raises(ValueError):
            get_human_age(cat_age, 0)
    else:
        result = get_human_age(cat_age, 0)
        assert result[0] == expected_cat


@pytest.mark.parametrize(
    "dog_age, expected_dog",
    [
        (-5, None),
        (29, 3),
    ],
)
def test_dog_age_boundaries(dog_age: int, expected_dog: int | None) -> None:
    if dog_age < 0:
        with pytest.raises(ValueError):
            get_human_age(0, dog_age)
    else:
        result = get_human_age(0, dog_age)
        assert result[1] == expected_dog


@pytest.mark.parametrize(
    "cat_age, dog_age",
    [
        ("15", 15),
        (15.0, 15),
        (15, "20"),
        (15, 20.5),
    ],
)
def test_get_human_age_invalid_types(
        cat_age: object, dog_age: object
) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat_age, dog_age)
