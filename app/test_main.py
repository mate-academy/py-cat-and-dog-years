import pytest


from app.main import get_human_age


class TestAgesClasses:

    @pytest.mark.parametrize(
        "dog_age, cat_age, result",
        [pytest.param(0, 0, [0, 0]),
         pytest.param(14, 14, [0, 0])]
    )
    def test_should_good_result(
            self,
            dog_age: int,
            cat_age: int,
            result: int
    ) -> None:
        wyn = get_human_age(dog_age, cat_age)
        assert wyn == result

    @pytest.mark.parametrize(
        "dog_age, cat_age",
        [
            (14, 16),  # za mały wiek psa
            (16, 14),  # za mały wiek kota
            (14, 14),  # oba za małe
        ]
    )
    def test_cat_and_dog_minimal_age(
            self,
            dog_age: int,
            cat_age: int
    ) -> None:
        assert dog_age > 15, "Dog age must be greater than 15"
        assert cat_age > 15, "Cat age must be greater than 15"
