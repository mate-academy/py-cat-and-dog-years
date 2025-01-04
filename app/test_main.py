from app.main import get_human_age


def test_should_return_zero_for_age_below_threshold() -> None:
    assert get_human_age(4, 5) == [0, 0], (
        "Expected [0, 0] for ages below 15."
    )


def test_should_return_one_for_age_between_15_and_24() -> None:
    assert get_human_age(15, 23) == [1, 1], (
        "Expected [1, 1] for ages between 15 and 24."
    )


def test_should_return_two_for_age_at_second_threshold() -> None:
    assert get_human_age(27, 28) == [2, 2], (
        f"Expected [2, 2] for get_human_age(27, 28), "
        f"but got {get_human_age(27, 28)}."
    )


def test_should_return_correct_values_for_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17], (
        "incorrect values for large ages."
    )


def test_should_handle_negative_ages_as_zero() -> None:
    assert get_human_age(-13, -256) == [0, 0], (
        "Expected [0, 0] for negative ages."
    )
