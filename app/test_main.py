import pytest


from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_human_ages",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="shouldn't return data out of normal range"
            ),
            pytest.param(
                -5,
                0,
                [0, 0],
                id="shouldn't return data out of normal range"
            ),
            pytest.param(
                0,
                -10,
                [0, 0],
                id="shouldn't return data out of normal range"
            ),
            pytest.param(
                -3,
                -7,
                [0, 0],
                id="shouldn't return data out of normal range"
            ),
            pytest.param(
                300,
                200,
                [71, 37],
                id="shouldn't return data out of normal range"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should change data at precise thresholds"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should change data at precise thresholds"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should change data at precise thresholds"
            )
        ]
    )
    def test_get_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            expected_human_ages: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_human_ages

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_error",
        [
            pytest.param(
                None,
                10,
                TypeError,
                id="should raises the correct exception"
            ),
            pytest.param(
                41,
                "37",
                TypeError,
                id="should raises the correct exception"
            ),
        ]
    )
    def test_raising_test_correctly(
            self,
            cat_age: any,
            dog_age: any,
            expected_error: Exception
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
