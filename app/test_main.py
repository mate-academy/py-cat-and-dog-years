from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, result",
    [
        pytest.param(
            0, 0, [0, 0], id="cat and dog zero ages should return zeroes"
        ),
        pytest.param(
            -2, -5, [0, 0], id="cat and dog negative ages should return zeroes"
        ),
        pytest.param(
            15,
            -5,
            [1, 0],
            id="cat only positive age should return zero for dog",
        ),
        pytest.param(
            0,
            29,
            [0, 3],
            id="dog only positive age should return zero for cat",
        ),
        pytest.param(
            27,
            27,
            [2, 2],
            id="cat and dog positive ages should return both positive",
        ),
        pytest.param(
            14,
            14,
            [0, 0],
            id="cat and dog less than one human year should return zeroes",
        ),
        pytest.param(
            15, 15, [1, 1], id="cat and dog one human year should return ones"
        ),
        pytest.param(
            28,
            28,
            [3, 2],
            id="cat and dog different calculation \
            should return different human ages",
        ),
        pytest.param(
            4532,
            5700,
            [1129, 1137],
            id="cat and dog big ages should return correct values",
        ),
    ],
)
def test_with_different_input_params(
    cat_age: int, dog_age: int, result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


def test_previous_params_should_not_interfere() -> None:
    result_one = get_human_age(16, 28)
    result_two = get_human_age(116, 165)
    result_three = get_human_age(16, 28)
    assert result_one == result_three != result_two


@pytest.mark.parametrize(
    "cat_age, dog_age, exception",
    [
        pytest.param(
            "4", 5, TypeError, id="should raise error if data is string"
        ),
        pytest.param(
            None, None, TypeError, id="should raise error if no data"
        ),
    ],
)
def test_should_raise_correct_exception(
    cat_age: str | None, dog_age: int | None, exception: type(Exception)
) -> None:
    with pytest.raises(exception):
        get_human_age(cat_age, dog_age)
