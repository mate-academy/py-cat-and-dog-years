import pytest
import app.main as main


# --- KROK PO 24 ROKU: dokładnie co 4 lata kot i co 5 lat pies ---
@pytest.mark.parametrize("delta", list(range(0, 21)))  # 24..44 włącznie
def test_cat_step_every_4_years_after_24(delta: int) -> None:
    age = 24 + delta
    cat, _ = main.get_human_age(age, 0)
    # 24..27 -> 2, 28..31 -> 3, itd.
    assert cat == 2 + (delta // 4)


@pytest.mark.parametrize("delta", list(range(0, 26)))  # 24..49 włącznie
def test_dog_step_every_5_years_after_24(delta: int) -> None:
    age = 24 + delta
    _, dog = main.get_human_age(0, age)
    # 24..28 -> 2, 29..33 -> 3, itd.
    assert dog == 2 + (delta // 5)


# --- CAŁE PRZEDZIAŁY: złapie manipulacje 14/15 i 8/9 ---
def test_cat_first_interval_is_0_from_0_to_14_inclusive() -> None:
    for age in range(0, 15):
        cat, _ = main.get_human_age(age, 0)
        assert cat == 0


def test_cat_second_interval_is_1_from_15_to_23_inclusive() -> None:
    for age in range(15, 24):
        cat, _ = main.get_human_age(age, 0)
        assert cat == 1


def test_dog_first_interval_is_0_from_0_to_14_inclusive() -> None:
    for age in range(0, 15):
        _, dog = main.get_human_age(0, age)
        assert dog == 0


def test_dog_second_interval_is_1_from_15_to_23_inclusive() -> None:
    for age in range(15, 24):
        _, dog = main.get_human_age(0, age)
        assert dog == 1


# --- Ujemne wartości: traktowane jak < 15 → 0 ---
@pytest.mark.parametrize(
    "cat,dog,expected",
    [
        (-1, 0, [0, 0]),
        (0, -5, [0, 0]),
        (-2, -3, [0, 0]),
    ],
)
def test_negative_inputs_are_treated_as_less_than_first_year(
    cat: int,
    dog: int,
    expected: list[int],
) -> None:
    assert main.get_human_age(cat, dog) == expected


# --- Niepoprawne typy, które realnie rzucą TypeError ---
@pytest.mark.parametrize(
    "cat,dog",
    [
        ("3", 5),   # str vs int
        (None, 1),  # None vs int
        (3, [2]),   # list vs int
    ],
)
def test_non_integer_invalid_types_raise_type_error(
    cat: object,
    dog: object,
) -> None:  # noqa: ANN001
    with pytest.raises(TypeError):
        main.get_human_age(cat, dog)


# --- Floats: akceptowane i liczone zgodnie z regułami ---
def test_float_inputs_follow_rules_without_exceptions() -> None:
    # < 15 -> 0
    assert main.get_human_age(4.5, 2.0) == [0, 0]
    # 24.0 dla kota = 2, 29.0 dla psa = 3
    assert main.get_human_age(24.0, 29.0) == [2, 3]
