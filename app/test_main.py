from app.main import get_human_age

import pytest


class TestGetHumanAge:
    def test_should_return_type_of_result_is_list(self) -> None:
        assert isinstance(get_human_age(0, 0), list)

    @pytest.mark.parametrize(
        "cat_age,dog_age,human_age",
        [
            pytest.param(
                -5,
                15,
                [0, 1],
                id="negative cat/dog age turn into to 0"
            ),
            pytest.param(
                0,
                0,
                [0, 0],
                id=(
                    "from 0 to 14 cat/dog years "
                    "should convert into 0 human age."
                )
            ),
            pytest.param(
                14,
                14,
                [0, 0],
                id="14 cat/dog years should convert into 0 human age."
            ),
            pytest.param(
                15,
                15,
                [1, 1],
                id="15 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                23,
                23,
                [1, 1],
                id="23 cat/dog years should convert into 1 human age."
            ),
            pytest.param(
                24,
                24,
                [2, 2],
                id="24 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                27,
                28,
                [2, 2],
                id="27/28 cat/dog years should convert into 2 human age."
            ),
            pytest.param(
                28,
                29,
                [3, 3],
                id="28/29 cat/dog years should convert into 3 human age."
            ),
            pytest.param(
                100,
                100,
                [21, 17]
            ),
            pytest.param(
                155,
                208,
                [34, 38]
            )
        ]
    )
    def test_finds_human_age_correctly(
            self,
            cat_age: int,
            dog_age: int,
            human_age: list[int]
    ) -> None:
        assert get_human_age(cat_age, dog_age) == human_age

    @pytest.mark.parametrize(
        "first_element,second_element,expected_error",
        [
            pytest.param(
                "14",
                0,
                TypeError,
                id="cat/dog age should be type of int"
            ),
            (
                None,
                [],
                TypeError
            ),
            (
                0,
                {},
                TypeError
            )
        ]
    )
    def test_should_return_error_when_invalid_types(
            self,
            first_element: any,
            second_element: any,
            expected_error: EOFError
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(first_element, second_element)
