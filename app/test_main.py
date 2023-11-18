import pytest


from app.main import get_human_age


def print_fstring_with_all_related_info(
        cat_age: int,
        dog_age: int,
        current_result: list,
        expected_result: int
) -> str:
    return (
        f"For cat age {cat_age} and {dog_age}, "
        f"expected result is {expected_result}, but got {current_result}"
    )


@pytest.mark.parametrize(
    "cat_age, dog_age, expected_result",
    [
        pytest.param(
            14, 14, [0, 0],
            id="human_age_should_be_equal_to_0"
        ),
        pytest.param(
            23, 23, [1, 1],
            id="human_age_should_be_equal_to_1"
        ),
        pytest.param(
            27, 28, [2, 2],
            id="human_age_should_be_equal_to_2"
        ),
        pytest.param(
            100, 100, [21, 17],
            id="human_age_should_be_more_than_2"
        ),
        pytest.param(
            - 1, - 1, [0, 0],
            id="test_if_function_receives_negative_number"
        ),
        pytest.param(
            0, 0, [0, 0],
            id="test_if_function_receives_zero"
        ),
        pytest.param(
            1000, 1000, [246, 197],
            id="test_if_function_receives_really_large_numbers"
        )
    ]
)
def test_human_age_should_be_equal_to_0(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    current_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        current_result == expected_result
    ), (
        print_fstring_with_all_related_info
        (cat_age, dog_age, current_result, expected_result)
    )


def test_human_age_should_be_equal_to_1(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    current_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        current_result == expected_result
    ), (
        print_fstring_with_all_related_info
        (cat_age, dog_age, current_result, expected_result)
    )


def test_human_age_should_be_equal_to_2(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    current_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        current_result == expected_result
    ), (
        print_fstring_with_all_related_info
        (cat_age, dog_age, current_result, expected_result)
    )


def test_human_age_should_be_more_than_2(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    current_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        current_result == expected_result
    ), (
        print_fstring_with_all_related_info
        (cat_age, dog_age, current_result, expected_result)
    )


def test_human_age_should_change_with_integer_value() -> None:
    cat_age = 14
    dog_age = 14
    previous_result = get_human_age(cat_age=cat_age, dog_age=dog_age)

    cat_age += 1
    dog_age += 1
    new_result = get_human_age(cat_age=cat_age, dog_age=dog_age)

    assert (
        previous_result != new_result
    ), (
        f"For {cat_age - 1} and {dog_age - 1}, "
        f"expected result is not equal to "
        f"{previous_result}, but got {new_result}"
    )


def test_if_function_receives_negative_number(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    current_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        current_result == expected_result
    ), (
        print_fstring_with_all_related_info
        (cat_age, dog_age, current_result, expected_result)
    )


def test_if_function_receives_zero(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    current_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        current_result == expected_result
    ), (
        print_fstring_with_all_related_info
        (cat_age, dog_age, current_result, expected_result)
    )


def test_if_function_receives_really_large_numbers(
        cat_age: int,
        dog_age: int,
        expected_result: int
) -> None:
    current_result = get_human_age(cat_age=cat_age, dog_age=dog_age)
    assert (
        current_result == expected_result
    ), (
        print_fstring_with_all_related_info
        (cat_age, dog_age, current_result, expected_result)
    )


def test_if_function_receives_incorrect_type_of_data() -> None:
    with pytest.raises(TypeError):
        cat_age = 15
        dog_age = "abc"
        get_human_age(cat_age=cat_age, dog_age=dog_age)
