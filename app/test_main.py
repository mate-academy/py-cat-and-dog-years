import pytest

from app.main import get_human_age


class TestMain:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(-1, -6, [0, 0],
                         id="when value negative result equal 0"),
            pytest.param(0, 0, [0, 0],
                         id="0 cat/dog years equal 0 human age"),
            pytest.param(14, 14, [0, 0],
                         id="14 cat/dog years equal 0 human age"),
            pytest.param(15, 15, [1, 1],
                         id="15 cat/dog years equal 1 human age"),
            pytest.param(23, 23, [1, 1],
                         id="23 cat/dog years equal 1 human age"),
            pytest.param(24, 24, [2, 2],
                         id="24 cat/dog years equal 2 human age"),
            pytest.param(27, 28, [2, 2],
                         id="27/28 cat/dog years equal 2 human age"),
            pytest.param(28, 29, [3, 3],
                         id="28/29 cat/dog years equal 3 human age"),
            pytest.param(100, 100, [21, 17],
                         id="function works correctly when value too great")
        ]
    )
    def test_get_human_age(
            self,
            cat_age: int,
            dog_age: int,
            result: list
    ) -> None:

        assert (
            get_human_age(cat_age, dog_age) == result
        ), (f"When cats_age equal {cat_age}, "
            f"dogs_age equal {dog_age} result should be {result}")

    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_error",
        [
            pytest.param("2", 8, TypeError,
                         id="expected type value - integer not str"),
        ]
    )
    def test_get_human_age_with_incorrect_values(
            self,
            cat_age: int,
            dog_age: int,
            expected_error: type
    ) -> None:
        with pytest.raises(expected_error):
            get_human_age(cat_age, dog_age)
