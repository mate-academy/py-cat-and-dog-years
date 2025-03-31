from app.main import get_human_age

def test_should_return_list():
    goals = get_human_age(2, 2)
    assert isinstance(goals, list)

def test_should_return_list_of_two_values():
    goals = get_human_age(20, 30)
    assert len(goals) == 2

def test_should_return_expected_goals_when_animal_years_are_equal_to_zero_human_years():
    goals = get_human_age(14, 14)
    assert goals == [0, 0]

def test_should_return_expected_goals_when_animal_years_are_equal_to_one_human_years():
    goals = get_human_age(23, 23)
    assert goals == [1, 1]

def test_should_return_expected_goals_when_animal_years_are_equal_to_two_human_years():
    goals = get_human_age(27, 27)
    assert goals == [2, 2]

def test_should_return_expected_goals_when_animal_years_are_equal_to_three_human_years():
    goals = get_human_age(28, 29)
    assert goals == [3, 3]

def test_should_return_expected_goals_value_of_animals_is_one_hundred():
    goals = get_human_age(100, 100)
    assert goals == [21, 17]