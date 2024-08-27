from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(-1, -1, [0, 0], id="negative ages should return zeros"),
        pytest.param(0, 0, [0, 0], id="0 dog/cat years should convert to 0 human years"),
        pytest.param(14, 14, [0, 0], id="14 dog/cat years should convert to 0 human years"),
        pytest.param(15, 15, [1, 1], id="15 dog/cat years should convert to 1 human year"),
        pytest.param(23, 23, [1, 1], id="23 dog/cat years should convert to 1 human years"),
        pytest.param(24, 24, [2, 2], id="24 dog/cat years should convert to 2 human years"),
        pytest.param(28, 27, [3, 2], id="28/27 dog/cat years should convert to 3/2 human years"),
        pytest.param(27, 29, [2, 3], id="27/29 dog/cat years should convert to 2/3 human years"),
    ]
)
def test_get_human_age_calculates_correctly(cat_age, dog_age, result) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age, dog_age, error",
    [
        pytest.param(
            "one",
            "two",
            TypeError,
            id="should raise error with strings"
        ),
        pytest.param(
            [1, 2, 3],
            [4, 5, 6],
            TypeError,
            id="should raise error with lists"
        ),

    ]
)
def test_get_human_age_raise_correct_error(cat_age, dog_age, error) -> None:
    with pytest.raises(error):
        get_human_age(cat_age, dog_age)
