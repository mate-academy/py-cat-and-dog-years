from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, get_human_age_res",
        [
            pytest.param(28, 28, [3, 2], id="test should return list"),
            pytest.param(28, 28, [3, 2], id="test should return integer result"),
            (28, 28, [3, 2]),
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ],
    )
    def test_should_return_list(self, cat_age, dog_age, get_human_age_res):
        goals = get_human_age(cat_age, dog_age)
        assert isinstance(goals, list)

    def test_should_return_integer_result(self, cat_age, dog_age, get_human_age_res):
        goals = get_human_age(cat_age, dog_age)
        assert isinstance(goals[0], int) and isinstance(goals[1], int)

    def test_should_return_list_of_given_length(self, cat_age, dog_age):
        goals = get_human_age(cat_age, dog_age)
        assert len(goals) == 2

    def test_should_return_expected_goals(self, cat_age, dog_age, get_human_age_res):
        goals = get_human_age(cat_age, dog_age)
        assert goals == get_human_age_res

    def test_should_return_full_year(self, cat_age, dog_age):
        goals = get_human_age(cat_age, dog_age)
        assert goals[0] % 1 == 0 and goals[1] % 1 == 0

    def test_should_return_only_positive_values(self):
        goals = get_human_age(28, 28)
        assert goals[0] >= 0 and goals[1] >= 0

    def test_should_return_extant_age(self):
        goals = get_human_age(28, 28)
        assert goals[0] < 40 and goals[1] < 40

    def test_should_raise_there_is_not_parameter(self):
        cat_age = 28

        with pytest.raises(KeyError):
            goals = get_human_age(cat_age)


class TestConvertToHuman:
    pass