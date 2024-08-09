import pytest
from typing import Any


from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(-3, 0, [0, 0], id="0 when less then first year"),
            pytest.param(23, 24, [1, 2], id="age > first and second year"),
            pytest.param(33, 47, [4, 6], id="big age"),
            pytest.param(28, 29, [3, 3], id="third step"),
            pytest.param(-63, -29, [0, 0], id="two negative"),
            pytest.param(20, -4, [1, 0], id="one negative")

        ]
    )
    def test_correct_age(
            self,
            cat_age: int,
            dog_age: int,
            expected_result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("a", "b"),
            (3.5, 4.2),
            ([1], [2])
        ]
    )
    def test_incorrect_types(self, cat_age: Any, dog_age: Any) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
