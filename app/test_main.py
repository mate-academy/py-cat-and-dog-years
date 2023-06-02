from app.main import get_human_age


def test_age_below_15_should_be_zero() -> None:
    assert (
        get_human_age(0, 0) == [0, 0]
    ), "Only first 15 dog/cat years give 1 human year"
    assert (
        get_human_age(14, 14) == [0, 0]
    ), "Only first 15 dog/cat years give 1 human year"


def test_from_15_years_to_24() -> None:
    assert (
        get_human_age(15, 15) == [1, 1]
    ), "Only next 9 dog/cat years after 15 give 1 more year"
    assert (
        get_human_age(23, 23) == [1, 1]
    ), "Only next 9 dog/cat years after 15 give 1 more year"
    assert (
        get_human_age(24, 24) == [2, 2]
    ), "Only next 9 dog/cat years after 15 give 1 more year"


def test_after_24_years() -> None:
    assert (
        get_human_age(27, 27) == [2, 2]
    ), "Every 5 next dog(4 for cat) years after 24 give 1 extra human year"
    assert (
        get_human_age(28, 28) == [3, 2]
    ), "Every 5 next dog(4 for cat) years after 24 give 1 extra human year"
    assert (
        get_human_age(28, 29) == [3, 3]
    ), "Every 5 next dog(4 for cat) years after 24 give 1 extra human year"

    assert (
        get_human_age(100, 100) == [21, 17]
    ), "Every 5 next dog(4 for cat) years after 24 give 1 extra human year"
