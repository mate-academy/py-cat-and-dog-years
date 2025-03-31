from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected_human_age"),
    [
        pytest.param(
            0,
            - 1,
            [0, 0],
            id="expected human age should equal zeros if animal age <= 0"
        ),
        pytest.param(
            14,
            23,
            [0, 1],
            id="expected human age should be zero if 0 < animal age < 15"
               "and should be one if 14 < animal age < 24"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="expected human age should be correct if animal age > 24"
        )
    ]
)
def test_correct_expected_human_age(cat_age: int,
                                    dog_age: int,
                                    expected_human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected_type_error"),
    [
        pytest.param(
            "8",
            8,
            TypeError,
            id="raise TypeError when type of animal age is not `int`"
        )
    ]
)
def test_correct_error(
        cat_age: int,
        dog_age: int,
        expected_type_error: any
) -> None:
    with pytest.raises(expected_type_error):
        get_human_age(cat_age, dog_age)
