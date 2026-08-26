import pytest

from app.main import get_human_age


class TestConvertCatAge():
    @pytest.mark.parametrize(
        "cat_age, expected",
        [
            pytest.param(
                0,
                0,
                id="0_years_gives_0"
            ),
            pytest.param(
                14,
                0,
                id="14_years_still_0_lower_boundary"
            ),
            pytest.param(
                15,
                1,
                id="15_years_gives_1_upper_boundary"
            ),
            pytest.param(
                23,
                1,
                id="23_years_still_1_lower_boundary"
            ),
            pytest.param(
                24,
                2,
                id="24_years_gives_2_upper_boundary"
            ),
            pytest.param(
                27,
                2,
                id="27_years_still_2_before_4yr_step"
            ),
            pytest.param(
                28,
                3,
                id="28_years_gives_3_first_4yr_step"
            ),
            pytest.param(
                100,
                21,
                id="100_years_gives_21"
            ),
        ]
    )
    def test_cat_boundaries(self, cat_age: int, expected: int) -> None:
        assert get_human_age(cat_age, 0)[0] == expected


class TestConvertDogAge():
    @pytest.mark.parametrize(
        "dog_age, expected",
        [
            pytest.param(
                0,
                0,
                id="0_years_gives_0"
            ),
            pytest.param(
                14,
                0,
                id="14_years_still_0_lower_boundary"
            ),
            pytest.param(
                15,
                1,
                id="15_years_gives_1_upper_boundary"
            ),
            pytest.param(
                23,
                1,
                id="23_years_still_1_lower_boundary"
            ),
            pytest.param(
                24,
                2,
                id="24_years_gives_2_upper_boundary"
            ),
            pytest.param(
                27,
                2,
                id="27_years_still_2"
            ),
            pytest.param(
                28,
                2,
                id="28_years_still_2_before_5yr_step"
            ),
            pytest.param(
                29,
                3,
                id="29_years_gives_3_first_5yr_step"
            ),
            pytest.param(
                100,
                17,
                id="100_years_gives_17"
            ),
        ]
    )
    def test_dog_boundaries(self, dog_age: int, expected: int) -> None:
        assert get_human_age(0, dog_age)[1] == expected


class TestCombined:
    def test_returns_two_element_list(self) -> None:
        result = get_human_age(0, 0)
        assert len(result) == 2

    def test_cat_and_dog_independent(self) -> None:
        assert get_human_age(28, 0) == [3, 0]
        assert get_human_age(0, 29) == [0, 3]
