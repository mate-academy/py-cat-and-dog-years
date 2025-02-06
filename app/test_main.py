import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
        ],
        ids=[
            "under 15 years of age the result should return 0",
            "under 15 years of age the result should return 0",
        ]
    )
    def test_animal_age_if_animal_human_age_less_than_15(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result

    @pytest.mark.parametrize(
        "cat_age,dog_age,result",
        [
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ],
        ids=[
            "The first 15 years should be equal to 1 human",
            "Up to 24 years of age should be equal to 1 human",
            "At 24 the return is equal to 2 human",
            "At 28 cats will have 3 and dogs will still have 2",
            "At 100 years old, cats are 21 and dogs are 17",
        ]
    )
    def test_animal_age_if_animal_human_age_is_15_or_more(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:
        assert get_human_age(cat_age, dog_age) == result


class TestInvalidInput:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("", 15),
            (15, ""),
            ("", ""),
        ],
        ids=[
            "String instead of cat age",
            "String instead of dog age",
            "Strings instead of both ages",
        ]
    )
    def test_raise_other_type_of_attribute(self, cat_age, dog_age) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            (-1, -1, [0, 0]),
            (15, -1, [1, 0]),
            (-1, 15, [0, 1]),
        ],
        ids=[
            "Both values are negative",
            "Negative dog age",
            "Negative cat age",
        ]
    )
    def test_negative_attributes_passed(self, cat_age, dog_age, result) -> None:
        assert get_human_age(cat_age, dog_age) == result