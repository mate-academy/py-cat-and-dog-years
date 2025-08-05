from app.main import get_human_age


def test_should_return_correct_values() -> None:
    result = get_human_age(cat_age=21, dog_age=17)
    assert result == [1, 1], f"Expected [1, 1], got {result}"


def test_should_return_zeros_if_not_enough_age_to_calculate() -> None:
    result = get_human_age(cat_age=10, dog_age=10)
    assert result == [0, 0], f"Expected [0, 0], got {result}"
