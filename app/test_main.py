from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(
            0, 0, [0, 0],
            id="should return [0, 0] if cat and dog age < 15"
        ),
        pytest.param(
            -1, -1, [0, 0],
            id="should return [0, 0] if cat and dog age < 15"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="should return [0, 0] if cat and dog age < 15"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="should return [1, 1] if 15 <= cat and dog age <= 23"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="should return [1, 1] if 15 <= cat and dog age <= 23"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="should return [2, 2] if 24 <= cat age <= 28 "
               "and 24 <= dog age <= 29"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="should return [2, 2] if 24 <= cat age <= 28 "
               "and 24 <= dog age <= 29"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="should return [3, 3] if 24 <= cat age <= 28 "
               "and 24 <= dog age <= 29"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="should return [21, 17] if cat and dog age is 100"
        )
    ]
)
def test_checking_limit_values(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result


@pytest.mark.parametrize(
    "cat_age,dog_age,exception",
    [
        pytest.param(
            10, "10", TypeError,
            id="should raise TypeError if dog age is not int"
        ),
        pytest.param(
            "10", 10, TypeError,
            id="should raise TypeError if cat age is not int")
    ]
)
def test_should_raises_the_correct_exception(
        cat_age: int,
        dog_age: int,
        exception: TypeError
) -> None:
    with (pytest.raises(exception)):
        get_human_age(cat_age, dog_age)
