import pytest

from typing import Any

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected_result",
        [
            pytest.param(
                -1,
                -2,
                [0, 0],
                id="should return zeros when animals ages less then 0"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id="should return zeros when animals ages equal zeros"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="should return zeros when animals ages equal 14"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="should return 1 when ages more then 14 and no extra life"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="should return 1 when ages more then 14 and no extra life"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="should return 2 when ages more then 23 (one extra life)"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="should return [3, 2] when different one extra life numbers"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="should return many animals extra life"
            )
        ]
    )
    def test_should_return_some_values(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                None,
                None,
                id="should return TypeError when animals ages is None"
            ),
            pytest.param(
                "",
                "",
                id="should return TypeError when animals ages is str"
            ),
            pytest.param(
                [0],
                [0],
                id="should return TypeError when animals ages is list"
            ),
            pytest.param(
                {0: 0},
                {0: 0},
                id="should return TypeError when animals ages is dict"
            )
        ]
    )
    def test_should_return_incorrect_input_types_error(
            self,
            cat_age: Any,
            dog_age: Any
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
