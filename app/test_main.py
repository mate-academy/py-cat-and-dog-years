from typing import Any

import pytest
from app.main import get_human_age

"""
Я прошу внести зміни, оскільки все ще залишаються дві проблеми, пов’язані з контрольним списком, 
які впливають на коректність та відповідність проекту вимогам. 
У файлі app/main.py перевірки типів для cat_age та dog_age виконуються після порівнянь із від’ємними значеннями 
(приблизно у рядках 2–6 функції get_human_age), що означає: 
введення таких значень, 
як -1.5, спричинятиме виняток ValueError замість необхідного TypeError для даних, 
що не є цілими числами; вам слід перемістити перевірки isinstance(..., int) 
у самий початок функції, перед будь-якими порівняннями < 0, 
щоб усі нецілочисельні вхідні дані послідовно викликали TypeError. 
У файлі app/test_main.py у вас все ще є три окремі тести @pytest.mark.parametrize 
(дійсні значення, від’ємні віки, недійсні вхідні дані), 
але завдання вимагає одного параметризованого тесту; об'єднайте їх в один @pytest.mark.parametrize, 
де кожен випадок включає як вхідні віки, так і очікуваний результат або очікуваний тип винятку, 
а всередині тіла тесту розгалужуйтеся між assert get_human_age(...) == expected 
та with pytest.raises(expected_exception). 
Виконуючи це об’єднання, також переконайтеся, що будь-які оманливі імена тестових функцій виправлені 
(наприклад, тест, який зараз названо так, ніби він очікує TypeError, 
але насправді перевіряє ValueError, слід перейменувати відповідно до поведінки). 
Ці зміни необхідні для виконання явної вимоги контрольного списку щодо виклику правильного винятку 
для неправильних типів та вимоги об’єднати тести в один параметризований тест. 
Після того як ви переупорядкували перевірки в get_human_age та об’єднали тести 
в одну параметризовану функцію, рішення має повністю відповідати функціональним та структурним вимогам проєкту.
"""
@pytest.mark.parametrize(
    "cat, dog, result",
    [
        (0, 0, [0, 0]),
        (15, 15, [1, 1]),
        (24, 24, [2, 2]),
        (14, 14, [0, 0]),
        (23, 23, [1, 1]),
        (27, 27, [2, 2]),
        (28, 28, [3, 2]),
        (100, 100, [21, 17]),
    ],
    ids=[
        "test cat age and dog age are both years",
        "test cat age and dog age equal one year",
        "test cat age and dog age equal two years",
        "test value slightly less the first limit",
        "test between first and second limit",
        "test on the border of the next block without cat",
        "test on the verge of transition to next block cat gets year",
        "test large number for checking multiple block repetitions",
    ]
)
def test_valid_values(cat: int, dog: int, result: list[int]) -> None:
    assert get_human_age(cat, dog) == result


@pytest.mark.parametrize(
    "cat, dog",
    [
        (0, -5),
        (-4, 2),
        (-7, -7),
    ],
    ids=[
        "test dog's age is negative",
        "test cat's age is negative",
        "test all age is negative"
    ]
)
def test_negative_age_raises_type_error(cat: int, dog: int) -> None:
    with pytest.raises(ValueError):
        get_human_age(cat, dog)


@pytest.mark.parametrize(
    "cat, dog",
    [
        ("str", [0, 0, 0]),
        (12.5, 3),
        (3, "5"),
        ("5", None),
    ],
    ids=[
        "test input cat age is str and dog age is list",
        "test cat age is double",
        "test dog age is str",
        "test cat age is str and dog age is None",
    ],
)
def test_invalid_input(cat: Any, dog: Any) -> None:
    with pytest.raises(TypeError):
        get_human_age(cat, dog)
