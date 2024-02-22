from app.main import get_human_age


def test_age_conversion_for_newborns() -> None:
    assert get_human_age(0, 0) == [0, 0], "Newborns = 0 human age"


def test_age_at_first_milestone() -> None:
    assert get_human_age(15, 15) == [1, 1], "Age 15 = 1 human age"


def test_age_between_milestones() -> None:
    assert get_human_age(23, 23) == [1, 1], "Age 23 = 1 human age"


def test_age_at_third_milestone_for_cats() -> None:
    assert get_human_age(28, 0) == [3, 0], "Cats age 28 = 3 human age"


def test_age_for_older_pets() -> None:
    assert get_human_age(100, 100) == [21, 17], "Older pets conversion"
