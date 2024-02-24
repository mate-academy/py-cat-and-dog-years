# from typing import Type
import pytest
from app.main import get_human_age


@pytest.mark.parametrize("input_age, next_age, expected_result", [
    (0, 0, [0, 0]),
    (14, 14, [0, 0]),
    (15, 15, [1, 1]),
    (16, 16, [1, 1]),
    (24, 24, [2, 2]),
    (28, 28, [3, 2]),
    (30, 30, [3, 3]),
])
def test_get_human_age(
        input_age: int,
        next_age: int,
        expected_result: list
) -> None:
    assert get_human_age(input_age, next_age) == expected_result


# @pytest.mark.parametrize("input_age, next_age, expected_error", [
#     (-10, 5, ValueError),
#     (30, 1000, AttributeError),
#     ("string", 25, KeyError),
#     (20, "string", KeyError),
# ])
# def test_invalid_input_types(
#         input_age: int,
#         next_age: int,
#         expected_error: Type[BaseException]
# ) -> None:
#     with pytest.raises(expected_error):
#         get_human_age(input_age, next_age)
