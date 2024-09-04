import pytest
from app.main import get_human_age


class TestResultAnimalAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
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
                27, 28, [2, 2]
            ),
            (
                28, 28, [3, 2]
            ),
            (
                28, 29, [3, 3]
            ),
            (
                100, 100, [21, 17]
            ),
            (
                100500, 100500, [25121, 20097]
            ),
            (
                -5, 4, [0, 0]
            ),
            (
                12445678, 12345677, [3111415, 2469132]
            )
        ]
    )
    def test_age_animal_transform_to_age_human(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestRaiseError:
    @pytest.mark.parametrize(
        "cat_age,dog_age,error",
        [
            (2, {3: 0}, TypeError),
            ("0", 0, TypeError),
            (4, (1, 2), TypeError),
            (2, {2}, TypeError)
        ],
        ids=[
            "Should raise TypeError with dict",
            "Should raise TypeError with string",
            "Should raise TypeError with tuple",
            "Should raise TypeError with tes"
        ]
    )
    def test_raise_error(
            self,
            cat_age: int,
            dog_age: int,
            error: Exception
    ) -> None:
        with pytest.raises(error):
            get_human_age(cat_age, dog_age)
