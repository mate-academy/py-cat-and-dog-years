from app.main import get_human_age


def test_should_return_zeros_when_animals_ages_less_then_15() -> None:
    goal1 = get_human_age(0, 0)
    goal2 = get_human_age(14, 14)

    assert goal1 == goal2 == [0, 0]


def test_should_return_1_when_ages_more_than_14_and_no_extra_life() -> None:
    goal1 = get_human_age(15, 15)
    goal2 = get_human_age(23, 23)

    assert goal1 == goal2 == [1, 1]


def test_should_return_many_animals_extra_life() -> None:
    goals = get_human_age(100, 100)

    assert goals == [21, 17]
