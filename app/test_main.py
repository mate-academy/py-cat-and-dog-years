import pytest

from app.main import get_human_age


def assert_human_age(
    cat_age: int,
    dog_age: int,
    expected_cat: int,
    expected_dog: int
) -> None:
    result: list[int] = get_human_age(cat_age, dog_age)
    assert result == [expected_cat, expected_dog]


INVALID_TYPE_INPUTS: list[tuple[object, object]] = [
    ("15", 15),
    (15, "15"),
    ([15], 15),
    (15, [15]),
    (None, 15),
    (15, None),
    ({15: 1}, 15),
    (15, {15: 1})
]


class TestGetHumanAgeCommon:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_cat, expected_dog",
        [
            (0, 0, 0, 0),
            (14, 14, 0, 0),
            (15, 15, 1, 1),
            (23, 23, 1, 1),
            (24, 24, 2, 2),
            (27, 27, 2, 2),
            (28, 28, 3, 2),
            (100, 100, 21, 17)
        ]
    )
    def test_known_values(
        self,
        cat_age: int,
        dog_age: int,
        expected_cat: int,
        expected_dog: int
    ) -> None:
        assert_human_age(cat_age, dog_age, expected_cat, expected_dog)


class TestGetHumanAgeCat:
    @pytest.mark.parametrize(
        "cat_age, expected",
        [
            (1, 0),
            (10, 0),
            (14, 0)
        ]
    )
    def test_should_return_0_for_cat_younger_than_15(
        self,
        cat_age: int,
        expected: int
    ) -> None:
        assert_human_age(cat_age, 0, expected, 0)


class TestGetHumanAgeDog:
    @pytest.mark.parametrize(
        "dog_age, expected",
        [
            (1, 0),
            (10, 0),
            (14, 0)
        ]
    )
    def test_should_return_0_for_dog_younger_than_15(
        self,
        dog_age: int,
        expected: int
    ) -> None:
        assert_human_age(0, dog_age, 0, expected)


class TestGetHumanAgeTypeErrors:
    @pytest.mark.parametrize("cat_age, dog_age", INVALID_TYPE_INPUTS)
    def test_should_raise_type_error_on_non_int_input(
        self,
        cat_age: object,
        dog_age: object
    ) -> None:
        with pytest.raises(TypeError):
            get_human_age(cat_age, dog_age)


class TestGetHumanAgeOutputStructure:
    def test_should_return_list_of_two_elements(self) -> None:
        result = get_human_age(15, 15)
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(i, int) for i in result)


class TestGetHumanAgeLargeNumbers:
    @pytest.mark.parametrize(
        "cat_age, dog_age, expected_cat, expected_dog",
        [
            (10_000, 10_000, 2496, 1997),
            (1_000_000, 1_000_000, 249996, 199997)
        ]
    )
    def test_should_handle_large_numbers(
        self,
        cat_age: int,
        dog_age: int,
        expected_cat: int,
        expected_dog: int
    ) -> None:
        assert_human_age(cat_age, dog_age, expected_cat, expected_dog)


class TestGetHumanAgeNegativeNumbers:
    @pytest.mark.parametrize(
        "cat_age, dog_age",
        [
            (-1, 10),
            (10, -1),
            (-100, -100)
        ]
    )
    def test_should_return_zero_for_negative_ages(
        self,
        cat_age: int,
        dog_age: int
    ) -> None:
        assert_human_age(cat_age, dog_age, 0, 0)
