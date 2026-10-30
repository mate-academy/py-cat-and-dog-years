from app.main import get_human_age
import pytest


class TestHumanAge:
    @pytest.mark.parametrize(
        ("cat_years,dog_years,list_of_human_yers"),
        [
            pytest.param(0, 0, [0, 0],
                         id="test_should_list_with_zero_arguments"),
            pytest.param(14, 14, [0, 0],
                         id="test_should_list_with_no_zero_arguments"),
            pytest.param(15, 15, [1, 1],
                         id="test_should_one_with_argument_15"),
            pytest.param(24, 24, [2, 2],
                         id="test_should_second_human_year_at_24"),
            pytest.param(28, 28, [3, 2],
                         id="test_should_every_four_years_above_24"),
            pytest.param(29, 29, [3, 3],
                         id="test_should_five_years_above_24"),
            pytest.param(100, 100, [21, 17],
                         id="test_should_convert_large_ages"),
            pytest.param(15, 29, [1, 3],
                         id="test_should_cat_and_dog_ages_independently"),
        ]
    )
    def test_should_return_all_human_ages(
            self,
            cat_years: int,
            dog_years: int,
            list_of_human_yers: list
    ) -> None:
        assert get_human_age(cat_years, dog_years) == list_of_human_yers

    @pytest.mark.parametrize(
        ("cat_age,dog_age,expected"),
        [
            (-1, -1, [0, 0]),
            (-1, 15, [0, 1]),
            (15, -1, [1, 0]),
        ],
    )
    def test_should_return_zero_for_negative_age(
            self,
            cat_age: int,
            dog_age: int,
            expected: list,
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        ("cat_age,dog_age"),
        [
            ("15", 15),
            (15, "15"),
            (None, 15),
            (15, None),
        ],
    )
    def test_should_raise_type_error_for_invalid_types(self, cat_age: int,
                                                       dog_age: int) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
