import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(
            0, 0, [0, 0],
            id="Should return zero if cat or dog age equal to zero"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Should return zero if cat or dog age less than 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="Should return 1 if cat or dog age is 15"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="Should return one if cat or dog "
               "age more than 14 and less than 24"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Should return 2 if cat or dog age more than 23"
        ),
        pytest.param(
            27, 27, [2, 2],
            id="Should return 2 if cat or dog age is 27"
        ),
        pytest.param(
            28, 28, [3, 2],
            id="Should return 3 for cat and 2 for dog if ages are 28"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="Should return 21 for cat and 17 for dog if ages are 100"
        ),
    ]
)
def test_get_human_age(cat_age: int,
                       dog_age: int,
                       human_age: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected_error",
    [
        pytest.param(
            [], {}, TypeError,
            id="should rise error if age not integer"
        ),
        pytest.param(
            -1000, 1000, AssertionError,
            id="Ages should be in range(0, 101)"
        )
    ]
)
def test_of_correct_data(cat_age: int,
                         dog_age: int,
                         expected_error: Exception) -> None:
    with pytest.raises(expected_error):
        assert 0 <= cat_age <= 100, "cat age must be in range from 0 to 101"
        assert 0 <= dog_age <= 100, "dog age must be in range from 0 to 101"
        get_human_age(cat_age, dog_age)
