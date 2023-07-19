import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                37, 37,
                id="should return list"
            ),
        ]
    )
    def test_should_return_list(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        assert isinstance(get_human_age(cat_age, dog_age), list)

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                24, 24,
                id="should return list with length = 2"
            ),
        ]
    )
    def test_should_return_list_with_length_of_2(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        assert len(get_human_age(cat_age, dog_age)) == 2

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_list",
        [
            pytest.param(
                14, 14, [0, 0],
                id="should return zeros when animal_age < first_year"
            ),
            pytest.param(
                0, -33, [0, 0],
                id="should return zeros when animal_age is negative or 0"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return ones when animal_age is less then 23"
            ),
            pytest.param(
                1000000, 1000000, [249996, 199997],
                id="should return integers when animal_age are large number"
            )
        ]
    )
    def test_convert_ages_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_list: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_list

    @pytest.mark.parametrize(
        "cat_age_argument,dog_age_argument,expected_error",
        [
            pytest.param(
                "28",
                28,
                TypeError,
                id="should raise error when cat_age not integer"
            ),
            pytest.param(
                12,
                [28],
                TypeError,
                id="should raise error when dog_age not integer"
            )
        ]
    )
    def test_raising_errors_correctly(
            self,
            cat_age_argument: int,
            dog_age_argument: int,
            expected_error: TypeError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age_argument, dog_age_argument)
