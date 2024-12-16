import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, result", [
        pytest.param(0, 0, [0, 0], id="test_should_return_correct_result_1"),
        pytest.param(14, 14, [0, 0], id="test_should_return_correct_result_2"),
        pytest.param(15, 15, [1, 1], id="test_should_return_correct_result_3"),
        pytest.param(23, 23, [1, 1], id="test_should_return_correct_result_4"),
        pytest.param(24, 24, [2, 2], id="test_should_return_correct_result_5"),
        pytest.param(27, 27, [2, 2], id="test_should_return_correct_result_6"),
        pytest.param(28, 28, [3, 2], id="test_should_return_correct_result_7"),
        pytest.param(
            100,
            100,
            [21, 17],
            id="test_should_return_correct_result_8"
        )
   ]
)
def test_should_return_correct_result(
    cat_age: int, dog_age: int, result: list
) -> None:
    with open("log.txt", "a") as log:
        log.write(str(get_human_age(cat_age, dog_age)) + "\n")
    assert get_human_age(cat_age, dog_age) == result
