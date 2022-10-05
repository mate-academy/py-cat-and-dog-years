from app.main import get_human_age
import pytest


class TestDogAge:
    @pytest.mark.parametrize(
        "age,result",
        [
            (0, 0),
            (14, 0),
            (15, 1),
            (23, 1),
            (24, 2),
            (27, 2),
            (29, 3),
            (100, 17)
        ]
    )
    def test_for_dog(self, age: int, result: int) -> None:

        assert get_human_age(0, age)[1] == result


class TestCatAge:
    @pytest.mark.parametrize(
        "age,result",
        [
            (0, 0),
            (14, 0),
            (15, 1),
            (23, 1),
            (24, 2),
            (27, 2),
            (28, 3),
            (100, 21)
        ]
    )
    def test_for_dog(self, age: int, result: int) -> None:

        assert get_human_age(age, 0)[0] == result
