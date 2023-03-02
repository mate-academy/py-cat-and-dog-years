import pytest


from app.main import get_human_age


class TestAnimalYears:
    @pytest.mark.parametrize(
        "cat, dog, years",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return 0 years if animals year equal to zero"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="both dog and cat years under 15 give 0 human years"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="both first 15 years give 1 human year"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="next 9 years after 15 for both animals add 1 human year"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="every 4 next cat years give 1 human year"
            ),
            pytest.param(
                27,
                29,
                [2, 3],
                id="every 5 next dog years give 1 human year"
            ),
            pytest.param(
                -5,
                -20,
                [0, 0],
                id="should return 0 for both if years are negative"
            ),
            pytest.param(
                100000,
                9999999,
                [24996, 1999997],
                id="should return unreal years if animal years are very large"
            )
        ]
    )
    def test_calculate_human_age_correctly(
            self,
            cat: int,
            dog: int,
            years: list
    ) -> None:
        assert get_human_age(cat, dog) == years

    def test_should_raise_error_when_passed_not_integer_to_age(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("Hello", 3.5)
