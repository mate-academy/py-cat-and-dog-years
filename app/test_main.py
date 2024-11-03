import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_converted_ages",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return zeroes if animal\'s age equal zeroes"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return zeroes if animal\'s age less than 15"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should calculate first human year "
                   "if animal\'s age equal 15"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should calculate first human year "
                   "if animal\'s age are between 15 and 24"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should calculate second human year "
                   "if animal\'s age equal 24"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="should calculate second human year "
                   "if animal\'s age are between 24 and 28"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should increase cat age to third human year after 28"
            ),
            pytest.param(
                26,
                29,
                [2, 3],
                id="should increase dog age to third human year after 29"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should accurately convert large cat and dog ages"
            ),
            pytest.param(
                10000,
                10000,
                [2496, 1997],
                id="should accurately convert extremely large cat and dog ages"
            ),
            pytest.param(
                -1,
                -1,
                [0, 0],
                id="should return zeroes if animal\'s age is negative"
            ),
            pytest.param(
                10000,
                10000,
                [2496, 1997],
                id="should accurately convert float cat and dog ages"
            ),
        ]
    )
    def test_convert_ages_correctly(
            self,
            cat_age: int | float,
            dog_age: int | float,
            expected_converted_ages: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_converted_ages

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                "a",
                "b",
                TypeError,
                id="should raise error for string ages"
            ),
            pytest.param(
                None,
                None,
                TypeError,
                id="should raise error for None types"
            ),
        ]
    )
    def test_get_human_age_exceptions(
            self,
            cat_age: str | None,
            dog_age: str | None,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)