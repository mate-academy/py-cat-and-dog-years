from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_year,dog_year,result",
    [
        (
            0, 0, [0, 0]
        ),
        (
            14, 14, [0, 0]
        ),
        (
            27, 27, [2, 2]
        ),
        (
            100, 100, [21, 17]
        ),
    ]
)
def test_get_human_age(cat_year: int, dog_year: int, result: list) -> None:
    assert get_human_age(cat_year, dog_year) == result


@pytest.mark.parametrize(
    "cat_year,dog_year,exception",
    [
        (
            1, "1", TypeError
        )
    ]
)
def test_should_raise_correct_exception(
        cat_year: int, dog_year: int, exception: Exception
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_year, dog_year)
