from typing import List
import math


def find_difference(first_salary: int, second_salary: int, third_salary: int) -> int:
    """В отделе работают 3 сотрудника, которые получают заработную плату в рублях.

    Требуется определить: на сколько зарплата самого высокооплачиваемого из них отличается от самого низкооплачиваемого.

    На входе три числа типа int вернуть разницу зарплат.
    """

    max_salary = first_salary
    min_salary = first_salary

    if second_salary > first_salary and second_salary > third_salary:
        max_salary = second_salary
        min_salary = third_salary if third_salary < first_salary else first_salary

    elif third_salary > first_salary and third_salary > second_salary:
        max_salary = third_salary
        min_salary = first_salary if first_salary < second_salary else second_salary

    return max_salary - min_salary


def get_max_value(values: List[int]) -> int:
    """Дан список из сравнимаемых элементов, выведите на экран наибольшее значение в списке,
    не используя встроенную функцию.
    """

    max_value = -math.inf
    for value in values:
        if value > max_value:
            max_value = value

    return max_value


def get_max_list(structure: List[List[int]]) -> List[int]:
    """Напишите функцию, которая принимает на вход список из списков и возвращает тот список, чей максимум превосходит остальные.
    """

    max_value = -math.inf
    max_list = None
    for curr_list in structure:
        current_max_value = get_max_value(curr_list)
        if current_max_value > max_value:
            max_value = current_max_value
            max_list = curr_list
    return max_list


def simple_merge(list1: List[int], list2: List[int]):
    """Дано два отсортированных списка по возрастанию.

    Напишите функцию, которая сольёт их в один также отсортированный список. Не использовать sort.
    """

    i, j = 0, 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    res += list1[i:]
    res += list2[j:]
    # один из list1[i:] и list2[j:] будет уже пустой, поэтому добавится только нужный остаток
    return res


if __name__ == '__main__':
    print(find_difference(1, 2, 3))
    print(get_max_value([1, 2, 3]))
    print(get_max_list([[1, 4, 5], [1, 200, 12], []]))
    print(simple_merge([1, 100, 103], [25, 30, 40, 101, 104]))
