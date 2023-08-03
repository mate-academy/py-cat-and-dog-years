from app.main import get_human_age
import pytest


class TestGetHumanAge:

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (28, 28),
            (0, 0),
            (14, 14),
        ]
    )
    def test_should_return_list(self, cat_age, dog_age):
        goals = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert isinstance(goals, list)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (28, 28),
            (0, 0),
            (14, 14),
        ],
    )
    def test_should_return_integer_result(self, cat_age, dog_age):
        goals = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert isinstance(goals[0], int) and isinstance(goals[1], int)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (28, 28),
            (0, 0),
            (14, 14),
        ],
    )
    def test_should_return_list_of_given_length(self, cat_age, dog_age):
        goals = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert len(goals) == 2

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (28, 28),
            (0, 0),
            (14, 14),
        ],
    )
    def test_should_return_full_year(self, cat_age, dog_age):
        goals = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert goals[0] % 1 == 0 and goals[1] % 1 == 0

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (28, 28),
            (0, 0),
            (14, 14),
        ],
    )
    def test_should_return_only_positive_values(self, cat_age, dog_age):
        goals = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert goals[0] >= 0 and goals[1] >= 0

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (28, 28),
            (0, 0),
            (14, 14),
            pytest.param(100, 100, id="test should return extant age"),
        ],
    )
    def test_should_return_extant_age(self,  cat_age, dog_age):
        goals = get_human_age(cat_age=cat_age, dog_age=dog_age)
        assert goals[0] < 40 and goals[1] < 40

    @pytest.mark.parametrize(
        "cat_age, dog_age, get_human_age_res",
        [
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
    def test_should_return_expected_goals(self, cat_age, dog_age, get_human_age_res):
        goals = get_human_age(cat_age, dog_age)
        assert goals == get_human_age_res

    def test_should_raise_there_is_not_parameter_cat(self):
        cat_age = 28

        with pytest.raises(KeyError):
            goals = get_human_age(cat_age)

    def test_should_raise_there_is_not_parameter_dog(self):
        dog_age = 28

        with pytest.raises(KeyError):
            goals = get_human_age(dog_age=dog_age)


class TestConvertToHuman:
    pass
