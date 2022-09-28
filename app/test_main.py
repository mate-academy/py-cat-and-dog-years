from app.main import get_human_age
import pytest


class TestPetAgeInHumanYears:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_list",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="given zero age"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="given age is under 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="given age is equal to 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="given age is under 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="given age is equal to 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="given age is under cat and dog limitation"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="given age return plus year to cat"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="given age for long-living pets"
            )
        ])
    def test_pets_age_for_correct_results(self, cat_age: int,
                                          dog_age: int,
                                          expected_list: list):
        assert get_human_age(cat_age, dog_age) == expected_list
