import pytest


from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
        ]
    )
    def test_get_human_age(
            self,
            dog_age: int,
            cat_age: int,
            expected: list,
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            pytest.param("1", "1", id="values is str"),
            pytest.param([1], [1], id="values is list"),
        ]
    )
    def test_incorrect_type(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
