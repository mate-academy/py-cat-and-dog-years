import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0,
                     0,
                     [0, 0],
                     id="when input is zero, output should be too"),

        pytest.param(12,
                     12,
                     [0, 0],
                     id="when animal`s years are less than 15, "
                        "output should be equal to zero"),

        pytest.param(15,
                     15,
                     [1, 1],
                     id="output of this limit values should be equal to 1"),

        pytest.param(23,
                     23,
                     [1, 1],
                     id="output should be equal to 1 year"),

        pytest.param(24,
                     24,
                     [2, 2],
                     id="output of this limit values should be equal to 2"),

        pytest.param(27,
                     27,
                     [2, 2],
                     id="output of this limit value for cat "
                        "equals 2 and for dog too"),

        pytest.param(28,
                     28,
                     [3, 2],
                     id="output of this limit value "
                        "for cat equals 3 but for dog 2"),

        pytest.param(29,
                     29,
                     [3, 3],
                     id="output of this limit value "
                        "for cat equals 3 and for dog too"),

        pytest.param(100,
                     100,
                     [21, 17],
                     id="checking big values")
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, result: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(-2,
                     -36,
                     ValueError,
                     id="function should raise error if input is negative"),

        pytest.param(987654321,
                     1000000,
                     ValueError,
                     id="function should raise "
                        "error if input is large numbers")
    ]
)
def test_get_human_age_errors(cat_age: int,
                              dog_age: int,
                              expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        get_human_age(cat_age, dog_age)
