import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(
                15, 15, [1, 1],
                id="15 animal years should convert into 1 human age."
            ),
            pytest.param(
                27, 28, [2, 2],
                id="27/28 animal years should convert into 2 human age."
            ),
            pytest.param(
                10, 10, [0, 0],
                id="Until 15 animal years should convert into 0 human age"
            ),
            pytest.param(
                -1, -1, [0, 0],
                id="Negative animals numbers should return 0 human age."
            ),
            pytest.param(
                1000000, 1000000, [249996, 199997],
                id="Really big numbers should work correctly."
            ),
            pytest.param(
                0, 0, [0, 0],
                id="Animals age 0 should return 0"
            )
        ]
    )
    def test_human_age_should_return_list_of_correct_values(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            ("cat", "dog", TypeError),
            (15, "dog", TypeError),
            ("cat", 15, TypeError)
        ]
    )
    def test_get_human_age_invalid_input(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type(Exception)
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
