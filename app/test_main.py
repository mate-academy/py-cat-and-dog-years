import pytest
from app.main import get_human_age

class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (14, 15, [0, 1]),
            (23, 50, [1, 7]),
            (28, 24, [3, 2]),
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
        assert get_human_age(-20, -10) == [0, 0]

    def test_raise_type_error(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("123", 43)