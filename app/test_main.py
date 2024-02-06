import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            (-1, -1, [0, 0]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "Function should return 0 for negative numbers",
            "Function should return 0 with both 0 parameters",
            "Function should return 0 with both parameters less than 15",
            "Function should return 1 with both parameters equal to 15",
            "Function should return 1 with both parameters less than 24",
            "Function should return 2 with both parameters equal to 24",
            "Function should return 2 with both parameters less than 28",
            "Function should return 3 and 2 with both parameters equal to 28",
            "Function should return 21 and 17 with both parameters equal to 100"
        ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       expected_result: list) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


@pytest.mark.parametrize("cat_age,dog_age,expected_error", [
    pytest.param("10", 5, TypeError, id="String cat age"),
    pytest.param("cat", "dog", TypeError, id="String cat and dog Ages"),
])
def test_get_human_exceptions(cat_age: int,
                              dog_age: int,
                              expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
