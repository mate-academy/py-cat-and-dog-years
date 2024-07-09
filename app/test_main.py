import pytest

from app.main import get_human_age


class TestRegularValues:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result", [
            (
                0, 0, [0, 0]
            ),
            (
                14, 14, [0, 0]
            ),
            (
                15, 15, [1, 1]
            ),
            (
                23, 23, [1, 1]
            ),
            (
                24, 24, [2, 2]
            ),
            (
                27, 27, [2, 2]
            ),
            (
                28, 28, [3, 2]
            ),
            (
                100, 100, [21, 17]
            )
        ]
    )
    def test_examples(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestIfRaisesErrors:
    @pytest.mark.parametrize(
        "cat_age, dog_age, error", [
            (2, {3: 0}, TypeError),
            ("0", 0, TypeError),
            (4, (1, 2), TypeError),
            (2, {2}, TypeError),
            (-1, 2, ValueError),
            (100, 100, ValueError),


        ],
        ids=[
            "Should raise TypeError with dict",
            "Should raise TypeError with string",
            "Should raise TypeError with tuple",
            "Should raise TypeError with set",
            "Should raise ValueError with negative numbers",
            "Should raise ValueError with unrealistic numbers"
        ]
    )
    def test_if_raises_errors(
            self,
            cat_age: int,
            dog_age: int,
            error: Exception
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
