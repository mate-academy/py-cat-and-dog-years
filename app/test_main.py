import pytest


from app.main import get_human_age


class TestGetHumanAge:

    @pytest.mark.parametrize("cat_age, dog_age, expected", [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17]),
    ])
    def test_valid_ages(self, cat_age: int,
                        dog_age: int, expected: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected

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
