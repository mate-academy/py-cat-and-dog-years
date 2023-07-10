from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    ("cat_age", "dog_age", "expected_human_age"),
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="expected human age should equal zero if animal age equals 0"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="expected human age should equal zero if animal age less 15"
        ),
        pytest.param(
            15,
            15,
            [1, 1],
            id="expected human age should equal one if animal age is 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="expected human age should equal one if animal age less 24"
        ),
        pytest.param(
            24,
            24,
            [2, 2],
            id="expected human age should equal two if animal age 24"
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="expected human age should equal two if animal age less 28"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="expected human age should equal two if animal age 28"
        ),
        pytest.param(
            100,
            100,
            [21, 17],
            id="expected human age should equal two if animal age 100"
        )
    ]
)
def test_correct_expected_human_age(cat_age: int,
                                    dog_age: int,
                                    expected_human_age: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age
