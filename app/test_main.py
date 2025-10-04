import pytest
from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        # Provided examples
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
)
def test_examples(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


@pytest.mark.parametrize(
    "cat_age,expected_cat",
    [
        # Cat thresholds: 0–14 => 0; 15–23 => 1; then +1 per full 4 years after 24
        (14, 0),  # just below first threshold
        (15, 1),  # at first threshold
        (23, 1),  # just below second threshold
        (24, 2),  # at second threshold
        (27, 2),  # just below next 4-year block
        (28, 3),  # crosses a full 4-year block after 24
    ],
)
def test_cat_threshold_transitions(cat_age: int, expected_cat: int) -> None:
    human_cat, human_dog = get_human_age(cat_age, 0)
    assert human_cat == expected_cat
    assert human_dog == 0  # dog age unaffected when dog_age == 0


@pytest.mark.parametrize(
    "dog_age,expected_dog",
    [
        # Dog thresholds: 0–14 => 0; 15–24 => 1..2; then +1 per full 5 years after 24
        (14, 0),  # just below first threshold
        (15, 1),  # at first threshold
        (24, 2),  # at second threshold
        (28, 2),  # fewer than 5 years past 24 -> no extra yet
        (29, 2),  # still no extra
        (30, 3),  # first full 5-year block after 24
    ],
)
def test_dog_threshold_transitions(dog_age: int, expected_dog: int) -> None:
    human_cat, human_dog = get_human_age(0, dog_age)
    assert human_cat == 0  # cat age unaffected when cat_age == 0
    assert human_dog == expected_dog


@pytest.mark.parametrize(
    "cat_age,dog_age,expected",
    [
        (28, 27, [3, 2]),  # asymmetric: cat crosses a block, dog does not
        (27, 30, [2, 3]),  # asymmetric: dog crosses a block, cat does not
    ],
)
def test_asymmetric_inputs(cat_age: int, dog_age: int, expected: list[int]) -> None:
    assert get_human_age(cat_age, dog_age) == expected


def test_large_values() -> None:
    """A broader sanity check with large inputs."""
    # Manually derive expectations by the rules:
    # Cat: 15->1, next 9->+1, then +1 per full 4 after 24
    # Dog: 15->1, next 9->+1, then +1 per full 5 after 24
    cat_age, dog_age = 400, 400

    cat_human = 0
    if cat_age >= 15:
        cat_human += 1
        if cat_age >= 24:
            cat_human += 1
            cat_human += (cat_age - 24) // 4
        else:
            # between 15 and 23 inclusive
            cat_human += 0

    dog_human = 0
    if dog_age >= 15:
        dog_human += 1
        if dog_age >= 24:
            dog_human += 1
            dog_human += (dog_age - 24) // 5
        else:
            # between 15 and 23 inclusive
            dog_human += 0

    assert get_human_age(cat_age, dog_age) == [cat_human, dog_human]
