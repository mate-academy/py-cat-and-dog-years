import pytest
from app.main import get_human_age


class TestCatAndDogYears:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_years",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="zero values"
            ),
            pytest.param(
                -2,
                -2,
                [0, 0],
                id="negative numbers should return 0"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="age less than 15 should return zero"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="age 15 should return 1"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="age less than 24 should return 1"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="age 24 should return 2"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="every next 4 cat and 5 dog years should add 1"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="function should work with extremely big years numbers"
            )
        ]
    )
    def test_count_years_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_years: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_years

    def test_should_return_array(self) -> None:
        human_age = get_human_age(5, 10)
        assert isinstance(human_age, list)

    def test_result_array_should_have_two_elements(self) -> None:
        human_age = get_human_age(5, 10)
        assert len(human_age) == 2

    def test_elements_in_array_should_be_integers(self) -> None:
        human_age = get_human_age(5, 10)
        first = human_age[0]
        second = human_age[1]
        assert (isinstance(first, int) and isinstance(second, int))
