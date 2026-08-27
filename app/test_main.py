import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="should return zero when cat and dog age is zero"),
        pytest.param(
            14,
            14,
            [0, 0],
            id="should calculate human age correctly"),
        pytest.param(
            15,
            15,
            [1, 1],
            id="should calculate human age correctly"),
        pytest.param(
            23,
            23,
            [1, 1],
            id="should calculate human age correctly"),
        pytest.param(
            24,
            24,
            [2, 2],
            id="should calculate human age correctly"),
        pytest.param(
            27,
            27,
            [2, 2],
            id="should calculate human age correctly"),
        pytest.param(
            28,
            28,
            [3, 2],
            id="should calculate human age correctly"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="should calculate human age correctly for large values"),
    ]
)
def test_should_convert_cat_and_dog_age_to_human_age(
        cat_age: int,
        dog_age: int,
        expected: list[int] | Exception
) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_exception",
    [
        pytest.param(
            -1,
            -1,
            ValueError,
            id="should raise ValueError for negative ages"
        ),
        pytest.param(
            "cat",
            15,
            TypeError,
            id="should return error when input is str type"),
        pytest.param(
            15,
            None,
            TypeError,
            id="should return error when input is None"),
        pytest.param(
            1.5,
            1.5,
            TypeError,
            id="should return error when input is float type")
    ]
)
def test_should_raise_exception_for_invalid_input(
    cat_age: int,
    dog_age: int,
    expected_exception: type[Exception]
) -> None:
    with pytest.raises(expected_exception):
        get_human_age(cat_age, dog_age)
