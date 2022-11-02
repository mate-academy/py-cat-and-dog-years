import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="zero ages"
            ),
            pytest.param(
                9,
                11,
                [0, 0],
                id="under 15 ages"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="equal 15 ages"
            ),
            pytest.param(
                16,
                20,
                [1, 1],
                id="between 15 and 24 ages"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="equal 24 ages"
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="between 24 and 28 years "
            ),
            pytest.param(
                28,
                34,
                [3, 4],
                id="after 28 years"
            ),
        ]
    )
    def test_get_human_ages(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    def test_should_raise_error_when_input_not_int(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("16", 15)
