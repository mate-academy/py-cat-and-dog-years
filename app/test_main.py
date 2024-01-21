from app.main import get_human_age
import pytest


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            -6, -8, [0, 0],
            id="Test negative value of cat and dog age."
        ),

        pytest.param(
            0, 0, [0, 0],
            id="Test zeros value of cat and dog age."
        ),

        pytest.param(
            100, 100, [21, 17],
            id="Test big value numbers of cat and dogs age."
        ),

        pytest.param(
            15, 15, [1, 1],
            id="Test value of cat and dog age, if it's equal 1 human year."
        ),

        pytest.param(
            23, 23, [1, 1],
            id=("Test value of cat and dog age, if it's bigger"
                "than 1 but not equal 2 human years.")
        ),

        pytest.param(
            24, 24, [2, 2],
            id="Test value of cat and dog age, if it's equal 2 human years."
        ),

        pytest.param(
            28, 28, [3, 2],
            id=("Test value of cat and dog age, if they "
                "are the same, but equal to different human years.")
        )
    ]
)
def test_work_of_function_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list[int]
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_of_raising_the_correct_exception_if_data_is_incorrect() -> None:
    with pytest.raises(TypeError):
        get_human_age("100", 50)
