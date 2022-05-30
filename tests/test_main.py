import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                26,
                29,
                [2, 3],
                id="should get correct result"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="should get zero list when ages are zero"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should get zero list"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should get age if ages are similar"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="shouldn't round to ceil"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should get extra ages"
            )
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age,
            dog_age,
            expected_result
    ):
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param(
                26,
                "29",
                TypeError,
                id="should raise error when dog age is string"
            )
        ]
    )
    def test_raise_error_correctly(
            self,
            cat_age,
            dog_age,
            expected_error
    ):
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
