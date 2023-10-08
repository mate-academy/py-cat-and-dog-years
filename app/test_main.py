import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_human_age",
    [
        pytest.param(
            -1, -1, [0, 0],
            id="should return 0 if animal ages is negative integer"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="should return 0 if animals ages is zeros"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="a value less than 15 is equivalent to 0 human years"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="a value less than 24 is equivalent to 1 human years"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="a value less than 27 for cat "
               "and 28 for dog is equivalent to 2 human years"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="verification of the equivalent of 3 human years"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="long life check"
        ),
        pytest.param(
            10000, 10000, [2496, 1997],
            id="REALLY LARGE NUMBERS"
        ),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_human_age: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_human_age


@pytest.mark.parametrize("cat_age, dog_age, expected_result", [
    pytest.param(
        "23", 23, TypeError,
        id="TypeError for cat age"
    ),
    pytest.param(
        23, "23", TypeError,
        id="TypeError for dog age"
    ),
])
def test_get_human_age_type_error(
        cat_age: int,
        dog_age: int,
        expected_result: type[Exception]
) -> None:
    with pytest.raises(expected_result):
        get_human_age(cat_age, dog_age)
