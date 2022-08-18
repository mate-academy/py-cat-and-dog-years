import pytest

from app.main import get_human_age


class TestCatAge:
    @pytest.mark.parametrize(
        "cat_age, expected_value",
        [pytest.param(
            0,
            [0, 0],
            id="Should return 0"
        ), pytest.param(
            14,
            [0, 0],
            id="Should return 0"
        ), pytest.param(
            15,
            [1, 0],
            id="Should return 1"
        ), pytest.param(
            24,
            [2, 0],
            id="Should return 2"
        ), pytest.param(
            28,
            [3, 0],
            id="Should return 3"
        )]
    )
    def test_cat_age_from_0_to_29(self, cat_age, expected_value):
        assert get_human_age(cat_age, 0) == expected_value


class TestDogAge:
    @pytest.mark.parametrize(
        "dog_age, expected_value", [
            pytest.param(
                0,
                [0, 0],
                id="Should return 0"
            ),
            pytest.param(
                14,
                [0, 0],
                id="Should return 0"
            ),
            pytest.param(
                15,
                [0, 1],
                id="Should return 1"
            ),
            pytest.param(
                24,
                [0, 2],
                id="Should return 2"
            ),
            pytest.param(
                29,
                [0, 3],
                id="Should return 3"
            )
        ])
    def test_dog_age_from_0_to_29(self, dog_age, expected_value):
        assert get_human_age(0, dog_age) == expected_value
#
#
# class TestAllAges:
#     pass
#
#


class TestErrors:
    def test_all_values_must_be_greater_or_equal_0(self):
        assert get_human_age(-1, -1) == [0, 0]

    def test_on_float(self):
        assert get_human_age(25.9, 25.9) == [2, 2]
