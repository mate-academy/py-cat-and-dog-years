import pytest
from app.main import get_human_age


class TestGetHumanAge:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                0, 0, [0, 0],
                id="should return array of zeros when both ages are zero"
            ),
            pytest.param(
                14, 14, [0, 0],
                id="should return array of zeros when both ages are 14"
            ),
            pytest.param(
                15, 15, [1, 1],
                id="should return array of ones when both ages are 15"
            ),
            pytest.param(
                23, 23, [1, 1],
                id="should return array of ones when both ages are 23"
            ),
            pytest.param(
                24, 24, [2, 2],
                id="should return array of twos when both ages are 24"
            ),
            pytest.param(
                27, 27, [2, 2],
                id="should return array of twos when both ages are 27"
            ),
            pytest.param(
                28, 28, [3, 2],
                id="should return [3, 2] when both ages are 28"
            ),
            pytest.param(
                100, 100, [21, 17],
                id="should return [21, 17] when both ages are 100"
            ),
            pytest.param(
                15, 24, [1, 2],
                id="should return different values when ages are 15 and 24"
            ),
            pytest.param(
                35, 40, [4, 5],
                id="should return different values when ages are 35 and 40"
            ),
            pytest.param(
                0, 40, [0, 5],
                id="should return different values when ages are 0 and 40"
            ),
        ],
    )
    def test_get_human_age(
        self,
        cat_age: int,
        dog_age: int,
        expected: list[int],
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected


class TestGetHumanAgeErrors:
    @pytest.mark.parametrize(
        "cat_age,dog_age,expected",
        [
            pytest.param(
                -1, 15, [0, 1],
                id="should handle negative cat age"
            ),
            pytest.param(
                15, -1, [1, 0],
                id="should handle negative dog age"
            ),
            pytest.param(
                -1, -1, [0, 0],
                id="should handle both negative ages"
            ),
            pytest.param(
                10000, 10000, [2496, 1997],
                id="should handle large ages"
            ),
        ],
    )
    def test_get_human_age_with_out_of_range_values(
            self,
            cat_age: int,
            dog_age: int,
            expected: list[int],
    ) -> None:
        assert get_human_age(cat_age, dog_age) == expected

    @pytest.mark.parametrize(
        "cat_age,dog_age",
        [
            pytest.param(
                "15", 15,
                id="should raise type error for string cat age"
            ),
            pytest.param(
                15, "15",
                id="should raise type error for string dog age"
            ),
            pytest.param(
                None, 15,
                id="should raise type error for none cat age"
            ),
            pytest.param(
                15, None,
                id="should raise type error for none dog age"
            ),
            pytest.param(
                15.5, 15,
                id="should raise type error for float cat age"
            ),
            pytest.param(
                15, 15.5,
                id="should raise type error for float dog age"
            ),
            pytest.param(
                [], 15,
                id="should raise type_error for list cat age"
            ),
            pytest.param(
                15, [],
                id="should raise type_error for list dog age"
            ),
            pytest.param(
                True, 15,
                id="should raise type_error for boolean cat age"
            ),
            pytest.param(
                15, True,
                id="should raise type_error for boolean dog age"
            ),
            pytest.param(
                False, 15,
                id="should raise type_error for boolean cat age"
            ),
            pytest.param(
                15, False,
                id="should raise type_error for boolean dog age"
            ),
            pytest.param(
                {}, 15,
                id="should raise type_error for dict cat age"
            ),
            pytest.param(
                15, {},
                id="should raise type_error for dict dog age"
            ),
            pytest.param(
                (), 15,
                id="should raise type_error for tupple cat age"
            ),
            pytest.param(
                15, (),
                id="should raise type_error for tupple dog age"
            ),
            pytest.param(
                set(), 15,
                id="should raise type_error for set cat age"
            ),
            pytest.param(
                15, set(),
                id="should raise type_error for set dog age"
            ),
        ],
    )
    def test_get_human_age_with_invalid_types(
        self,
        cat_age: object,
        dog_age: object,
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)
