import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "test_cat_age,test_dog_age,expected_result",
    [
        pytest.param(
            -1, -11, [0, 0],
            id="Test negative value of cat and dog age"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="Test zero value of cat and dog age"
        ),
        pytest.param(
            14, 14, [0, 0],
            id="Test values less than one human year"
        ),
        pytest.param(
            15, 15, [1, 1],
            id="Test values equal to one human year"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="Test values less than two human years"
        ),
        pytest.param(
            24, 24, [2, 2],
            id="Test values equal to two human year"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="Test values less than three human years"
        ),
        pytest.param(
            28, 29, [3, 3],
            id="Test values equal to three human years"
        ),
        pytest.param(
            55, 66, [9, 10],
            id="Test values much bigger than three human years"
        )
    ]
)
def test_function_get_human_age(
        test_cat_age: int,
        test_dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(test_cat_age, test_dog_age) == expected_result


def test_raise_if_valid_data_was_entered() -> None:
    with pytest.raises(TypeError):
        get_human_age("58", 25)
