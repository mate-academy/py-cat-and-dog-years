from app.main import get_human_age
import pytest


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_correct_answear(self,
                             cat_age: int,
                             dog_age: int,
                             result: int) -> None:
        assert get_human_age(cat_age, dog_age) == result

    def test_length_of_result(self) -> None:
        assert len(get_human_age(16, 16)) == 2

    def test_negative_numbers(self) -> None:
        assert get_human_age(-20,-10) == [0,0]

    def test_very_big_numbers(self) -> None:
        assert get_human_age(10000, 20000) == [2496, 3997]

    def test_raise_TypeError(self):
        with pytest.raises(TypeError):
            get_human_age("123", 43)
