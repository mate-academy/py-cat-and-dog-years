import pytest
from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0, 14, [0, 0],
                id="Should be 0 for age less than 15."
            ),
            pytest.param(
                15, 23, [1, 1],
                id="Should be 1 when age between 15 and 23"
            ),
            pytest.param(
                24, 28, [2, 2],
                id="Should be 2 when: 23 < cat age < 28 or 23 < dog age < 29",
            ),
            pytest.param(
                28, 29, [3, 3],
                id="Should increase by 1 every 4 or 5 for cat and dog over 24",
            ),
            pytest.param(
                -42, 1337, [0, 264],
                id="Should correctly works with numbers out of normal range",
            )
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "wrong_type",
        [
            str(),
            list(),
            set(),
            tuple()
        ]
    )
    def test_raising_error(self, wrong_type: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(wrong_type, 0)

        with pytest.raises(TypeError):
            get_human_age(0, wrong_type)
