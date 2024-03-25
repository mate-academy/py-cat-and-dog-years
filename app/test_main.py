from app.main import get_human_age
import pytest


class TestConvertHumanAge:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected",
        [
            pytest.param(14, 14, [0, 0],
                         id="14 cat/dog years should "
                         "convert into 0 human age."),
            pytest.param(15, 15, [1, 1],
                         id="15 cat/dog years should "
                         "convert into 0 human age."),
            pytest.param(23, 23, [1, 1],
                         id="23 cat/dog years should "
                         "convert into 1 human age."),
            pytest.param(24, 24, [2, 2],
                         id="24 cat/dog years should "
                         "convert into 2 human age."),
            pytest.param(27, 28, [3, 2],
                         id="27/28 cat/dog years should "
                         "convert into 2 human age."),
            pytest.param(29, 28, [3, 3],
                         id="28/29 cat/dog years should "
                         "convert into 3 human age."),
            pytest.param(-1, -1, [0, 0],
                         id="-1 cat/dog years should "
                            "convert into 0 human age."),
        ]
    )
    def test_convert_human_age(self,
                               dog_age: int,
                               cat_age: int,
                               expected: list
                               ) -> None:

        assert get_human_age(dog_age, cat_age) == expected

    def test_invalid_input_type(self) -> None:
        with pytest.raises(TypeError):
            get_human_age("string", 10)
        with pytest.raises(TypeError):
            get_human_age(10, "string")
        with pytest.raises(TypeError):
            get_human_age("string", "string")
