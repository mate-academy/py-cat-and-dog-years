import pytest

from app.main import get_human_age


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "cat_age,dog_age,converted_to_human_age",
        [
            (3, 3, [0, 0]),
            (23, 23, [1, 1]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_if_convertion_works_correctly(
            self,
            cat_age: int,
            dog_age: int,
            converted_to_human_age: list
    ) -> None:

        assert get_human_age(cat_age, dog_age) == converted_to_human_age

    def test_check_if_entering_valid_type_data(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("1", [1])
