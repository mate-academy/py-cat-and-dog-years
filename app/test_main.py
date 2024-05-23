import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0,
            0,
            [0, 0],
            id="Should return zeros for 0 animal years"
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="Should return zeros for animal years < 15"
        ),
        pytest.param(
            23,
            23,
            [1, 1],
            id="Should return 1 human year for animal years between 15...23"
        ),
        pytest.param(
            27,
            28,
            [2, 2],
            id="Should return 2 human years for 27 cat years 28 dog years"
        ),
        pytest.param(
            28,
            29,
            [3, 3],
            id="Should return 3 human years for 28 cat years 29 dog years"
        ),
        pytest.param(
            1000,
            1000,
            [246, 197],
            id="Should return proper result for large animal years"
        ),
        pytest.param(
            -1,
            -10,
            [0, 0],
            id="Should return zeros for animal years < 0"
        ),
        pytest.param(
            15.5,
            15.9999,
            [1, 1],
            id="Should return proper result for floating animal years"
        )
    ]
)
def test_should_return_result_correctly(
        cat_age: int,
        dog_age: int,
        result: list[int]
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == result
    ), f"{cat_age} cat years, {dog_age} dog years should be equal to {result}"


def test_should_raise_error_when_input_is_not_int() -> None:
    with pytest.raises(TypeError):
        get_human_age("10", [1])
