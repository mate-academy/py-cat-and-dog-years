import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(0, 0, [0, 0],
                     id="should_return_zero_for_age_0_0"),
        pytest.param(14, 14, [0, 0],
                     id="should_return_zero_for_ages_14_14"),
        pytest.param(15, 15, [1, 1],
                     id="should_return_one_for_ages_15_15"),
        pytest.param(23, 23, [1, 1],
                     id="should_return_one_for_ages_23_to_23"),
        pytest.param(24, 24, [2, 2],
                     id="should_return_two_for_exactly_24"),
        pytest.param(27, 27, [2, 2],
                     id="should_return_two_for_exactly_27"),
        pytest.param(28, 28, [3, 2],
                     id="should_calculate_cat_and_dog_differently"),
        pytest.param(100, 100, [21, 17],
                     id="should_handle_large_numbers"),
    ]
)
def test_get_human_age(
        cat_age: int,
        dog_age: int,
        expected_result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == expected_result


def test_for_negative_age() -> None:
    with pytest.raises(ValueError):
        get_human_age(-1, -1)


def test_for_correct_atributes() -> None:
    with pytest.raises(TypeError):
        get_human_age("1", "1")
