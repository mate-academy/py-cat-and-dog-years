import pytest

from app.main import get_human_age


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_result",
        [
            pytest.param(
                0,
                0,
                [0, 0],
                id="it should return [0, 0] if animals' ages equal to 0 in their years"
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="it should return [0, 0] if animals' ages less than 15 in their years"
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="it should return [1, 1] if animals' ages equal to 15 in their years"
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="it should return [2, 2] if animals' ages equal to 23 in their years"
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="is should return [2, 2] if animals' ages equal to 24 in their years"
            ),
            pytest.param(
                27,
                27,
                [2, 2],
                id="it should return [2, 2] if animals' ages are equal to 27 in their years"
            ),
            pytest.param(
                28,
                28,
                [3, 2],
                id="it should return [3, 2] if both animals' ages are equal to 28 in their years"
            ),
            pytest.param(
                100,
                100,
                [21, 17],
                id="it should return [21, 17] if both animals' ages are equal to 100 in their years"
            )
        ]
    )

    def test_convert_to_human(self, cat_age: int, dog_age: int, expected_result: list) -> None:
        assert get_human_age(cat_age, dog_age) == expected_result
