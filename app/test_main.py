import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                -1, -1, [0, 0], id="negative age gives 0 human age"
            ),
            pytest.param(
                0, 0, [0, 0], id="should return zero"
            ),
            pytest.param(
                2, 2, [0, 0], id="check cat or dog first year"
            ),
            pytest.param(
                14, 14, [0, 0], id="check cat_dog less than first year"
            ),
            pytest.param(
                15, 15, [1, 1], id="check cat_dog first year"
            ),
            pytest.param(
                23, 23, [1, 1], id="check cat/dog first year"
            ),
            pytest.param(
                24, 24, [2, 2], id="check cat/dog second year"
            ),
            pytest.param(
                27, 28, [2, 2], id="check cat_dog second year"),
            pytest.param(
                28, 28, [3, 2], id="check second cat and third dog year"
            ),
            pytest.param(
                28, 29, [3, 3], id="check cat/dog third year"
            ),
            pytest.param(
                100, 100, [21, 17], id="check cat_dog extra years"),
        ],
    )
    def test_get_human_age(
        self, cat_age: int, dog_age: int, expected_result: list
    ) -> None:
        result = get_human_age(cat_age, dog_age)

        assert result == expected_result

    def test_if_raises_error(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("10", 2)
