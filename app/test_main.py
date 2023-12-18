import pytest
from app.main import get_human_age


class TestMain:
    @pytest.mark.parametrize(
        "cat_age, dog_age, result",
        [
            pytest.param(0, 0, [0, 0], id="both values equal 0"),
            pytest.param(14, 14, [0, 0], id="both values equal 14"),
            pytest.param(15, 15, [1, 1], id="both values equal 15"),
            pytest.param(28, 28, [3, 2], id="both values equal 28"),

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
        "cat_age, dog_age, error",
        [
            pytest.param(0, -1, pytest.raises(AttributeError),
                         id="age less 0 does not exist"),
            pytest.param(31, 31, pytest.raises(AttributeError),
                         id="life was over"),

        ]
    )
    def test_get_human_age_with_incorrect_args(
            self,
            cat_age: int,
            dog_age: int,
            error: AttributeError
    ) -> None:
        with pytest.raises(AttributeError):
            assert get_human_age(cat_age, dog_age)
