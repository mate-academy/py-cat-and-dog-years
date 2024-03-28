import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,human_age",
    [
        pytest.param(0, 0, [0, 0],
                     id="Pet zero age should equal [0, 0] human age"),
        pytest.param(14, 14, [0, 0],
                     id="Pet age less 15 should equal [0, 0] human age"),
        pytest.param(15, 15, [1, 1],
                     id="Should equal [1, 1] human age"),
        pytest.param(23, 23, [1, 1],
                     id="Should equal [1, 1] human age"),
        pytest.param(24, 24, [2, 2],
                     id="Should equal [2, 2] human age"),
        pytest.param(28, 29, [3, 3],
                     id="Should equal [3, 3] human age"),
        pytest.param(32, 34, [4, 4],
                     id="Should equal [4, 4] human age"),
        pytest.param(100, 100, [21, 17],
                     id="Should equal [21, 17] human age"),
        pytest.param(-100, -100, [0, 0],
                     id="Negative age should equal [0, 0]"),
        pytest.param(15.25, 25.15, [1.0, 2.0],
                     id="Should float age")
    ]
)
def test_should_changed_with_different_inputs(
    cat_age: int,
    dog_age: int,
    human_age: int
) -> None:
    assert (
        get_human_age(cat_age, dog_age) == human_age
    )


@pytest.mark.parametrize(
    "pet_age",
    [
        ((15,)),
        ([15]),
        ({15}),
        ("15")
    ],
)
def test_should_rise_correct_exception(pet_age: int) -> None:
    with pytest.raises(TypeError):
        get_human_age(pet_age, pet_age)
