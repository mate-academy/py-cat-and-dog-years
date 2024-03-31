from app.main import get_human_age
import pytest


class TestConvertToHuman:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17])
        ]
    )
    def test_should_return_age_normal_range_values(
            self,
            cat_age: int,
            dog_age: int,
            expected: int) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            (0, 0, [0, 0]),
            (-1, -1, [0, 0]),
            (-15, -15, [0, 0]),
            (-24, -24, [0, 0]),
            (-100, -100, [0, 0]),
            (500, 600, [121, 117]),
            (2345272727234, 34563473457, [586318181804, 6912694688])
        ],
    )
    def test_should_return_age_edge_range_values(
            self,
            cat_age: int,
            dog_age: int,
            expected: int) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            ("0", 1),
            ((1,), (1,)),
            ([1], [1]),
            ([0], 1),
            ([0], "1"),
            ({"1": 1}, {"2": None}),
            ({1}, {0})
        ]
    )
    def test_should_raise_error_if_age_not_int(
            self,
            cat_age: int,
            dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
