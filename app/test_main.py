import pytest


from app.main import get_human_age


class TestYearClass:
    @pytest.mark.parametrize(
        "cat_years, dog_years, expect_res",
        [
            (0, 0, [0, 0]),
            (14, 14, [0, 0]),
            (15, 15, [1, 1]),
            (23, 23, [1, 1]),
            (24, 24, [2, 2]),
            (27, 27, [2, 2]),
            (28, 28, [3, 2]),
            (100, 100, [21, 17]),
            (-3213332, -3213, [0, 0]),
            (123456, 123456, [30860, 24688])])
    def test_base_calculated_years(self,
                                   cat_years: int,
                                   dog_years: int,
                                   expect_res: list[int]) -> None:
        assert get_human_age(cat_years, dog_years) == expect_res

    @pytest.mark.parametrize(
        "cat_years, dog_years",
        [
            (7, [7],),
            ((7,), 7),
            ("7", 7),
        ]
    )
    def test_expect_wright_type(self, cat_years: int, dog_years: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_years, dog_years)
