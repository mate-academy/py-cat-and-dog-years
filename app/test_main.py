from app.main import get_human_age
"""
Котячі та собачі роки

У файлі app/test_main.py напишіть тести для функції get_human_age, 
яка приймає два цілих числа cat_age (вік мого кота в котячих роках) 
та dog_age (вік мого собаки в собачих роках) і повертає масив, де:

перший елемент — вік мого кота в людських роках;
другий елемент — вік мого собаки в людських роках.
Як правило, вік є цілим числом років (останки відкидаються).

Котячі роки перетворюються на людські роки за такими правилами:

перші 15 котячих років дають 1 людський рік;
наступні 9 котячих років дають ще 1 людський рік;
кожні наступні 4 котячі роки дають 1 додатковий людський рік.
Собачі роки:

перші 15 собачих років дають 1 людський рік;
наступні 9 собачих років дають ще 1 людський рік;
кожні наступні 5 собачих років дають 1 додатковий людський рік.
Зверніть увагу: для написання тестів потрібно використовувати pytest.

Приклади:
"""
# write your code here
def test_cat_age_and_dog_age_are_both_years() -> None:
    assert get_human_age(0,0) == [0, 0]

def test_cat_age_and_dog_age_equal_one_year() -> None:
    assert get_human_age(15, 15) == [1, 1]

def test_cat_age_and_dog_age_equal_two_years() -> None:
    assert get_human_age(24, 24) == [2, 2]

def test_value_slightly_less_the_first_limit() -> None:
    assert get_human_age(14, 14) == [0, 0]

def test_between_first_and_second_limit() -> None:
    assert get_human_age(23, 23) == [1, 1]

def test_on_the_border_of_the_next_block_without_cat() -> None:
    assert get_human_age(27, 27) == [2, 2]

def test_on_the_verge_of_transition_to_next_block_cat_gets_year() -> None:
    assert get_human_age(28, 28) == [3, 2]

def test_large_number_for_checking_multiple_block_repetitions() -> None:
    assert get_human_age(100, 100) == [21, 17]