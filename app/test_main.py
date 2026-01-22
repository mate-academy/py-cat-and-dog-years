import pytest

from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (10, 14, [0, 0]),

            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (20, 23, [1, 1]),

            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (24, 25, [2, 2]),

            (28, 30, [3, 3]),
            (40, 40, [6, 5]),

            (28, 38, [3, 4]),
            (23, 24, [1, 2]),
            (24, 29, [2, 3]),
            (100, 100, [21, 17]),
        ],
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            ("5", 10),
            (10, "7"),
            (None, 10),
            (10, None),
            (None, None),
            ([], {}),
        ],
    )
    def test_get_human_age_invalid_types(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (-1, 10),
            (10, -5),
            (-100, -200),
        ],
    )
    def test_get_human_age_negative_values(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert result == [0, 0]

    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (10 ** 6, 10 ** 6),
            (999_999, 15),
            (20, 888_888),
        ],
    )
    def test_get_human_age_large_values(
            self,
            cat_age: int,
            dog_age: int
    ) -> None:
        result = get_human_age(cat_age, dog_age)
        assert isinstance(result[0], int)
        assert isinstance(result[1], int)
        assert result[0] >= 0 and result[1] >= 0
