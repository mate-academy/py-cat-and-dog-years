import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, cat_to_human, dog_to_human",
    [
        pytest.param(
            1, 14, 0, 0,
            id="return 0 when given years less than 15"
        ),
        pytest.param(
            0, -10, 0, 0,
            id="return 0 when given years is negative number or 0"
        ),
        pytest.param(
            23, 15, 1, 1,
            id="return 1 when given years less than 24"
        ),
        pytest.param(
            24, 27, 2, 2,
            id="return 2 and more when given years more than 24"
        ),
        pytest.param(
            1000, 1000, 246, 197,
            id="return correct value when given years really large number"
        )
    ]
)
def test_convert_age_correctly(
    cat_age: int,
    dog_age: int,
    cat_to_human: int,
    dog_to_human: int
) -> None:
    assert get_human_age(cat_age, dog_age) == [cat_to_human, dog_to_human]


@pytest.mark.parametrize(
    "cat_age, dog_age, excepted_error",
    [
        pytest.param(
            [], "24", TypeError,
            id="should raise error when incorrect type"
        )
    ]
)
def test_raising_error_correctly(
    cat_age: int,
    dog_age: int,
    excepted_error: type
) -> None:
    with pytest.raises(excepted_error):
        get_human_age(cat_age, dog_age)
