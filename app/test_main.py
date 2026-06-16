import pytest

from app.main import get_human_age, MAX_CAT_AGE, MAX_DOG_AGE


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(14, 14, [0, 0]),
        pytest.param(15, 15, [1, 1]),
        pytest.param(23, 23, [1, 1]),
        pytest.param(24, 24, [2, 2]),
        pytest.param(27, 27, [2, 2]),
        pytest.param(28, 28, [3, 2]),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param("23", 23, TypeError),
        pytest.param(24, "24", TypeError),
        pytest.param(27.5, 24, TypeError),
        pytest.param(27.5, 27.5, TypeError),
        pytest.param([24], [24], TypeError),
    ]
)
def test_get_human_age_for_correct_parameters(
        cat_age: int,
        dog_age: int,
        expected: TypeError
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(MAX_CAT_AGE + 1000, MAX_DOG_AGE + 1000, ValueError),
        pytest.param(MAX_CAT_AGE + 1000, 24, ValueError),
        pytest.param(24, MAX_DOG_AGE + 1000, ValueError),
    ]
)
def test_get_human_age_with_unrealistic_number(
        cat_age: int,
        dog_age: int,
        expected: ValueError
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(-1, -1, ValueError),
        pytest.param(24, -1, ValueError),
        pytest.param(-1, 24, ValueError),
    ]
)
def test_get_human_age_with_negative_age(
        cat_age: int,
        dog_age: int,
        expected: ValueError
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(0, 24, ValueError),
        pytest.param(24, 0, ValueError),
        pytest.param(0, 0, ValueError),
    ]
)
def test_get_human_age_with_zero_age(
        cat_age: int,
        dog_age: int,
        expected: ValueError
) -> None:
    with pytest.raises(expected):
        get_human_age(cat_age, dog_age)
