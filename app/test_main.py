import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "first_value, second_value, expected_value",
    [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (28, 28, [3, 2]),
        (21, 28, [1, 2]),
        (100, 100, [21, 17])
    ]
)
def test_should_return_correct_value(first_value: int,
                                     second_value: int,
                                     expected_value: list) -> None:

    age = get_human_age(first_value, second_value)

    assert age == expected_value
