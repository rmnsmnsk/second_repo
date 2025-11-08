import random
from src.heap import heap_sort
from src.bubble import bubble
from src.merge import merge
from src.quick import quick

def test_empty():
    assert heap_sort([]) == []
    assert bubble([]) == []
    assert merge([]) == []
    assert quick([]) == []

def test_single():
    assert heap_sort([5]) == [5]
    assert bubble([5]) == [5]
    assert merge([5]) == [5]
    assert quick([5]) == [5]

def test_sorted():
    assert heap_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse():
    assert heap_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_duplicates():
    assert heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert bubble([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert merge([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert quick([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_negative():
    assert heap_sort([-2, -10, 100, 9]) == [-10, -2, 9, 100]
    assert bubble([-2, -10, 100, 9]) == [-10, -2, 9, 100]
    assert merge([-2, -10, 100, 9]) == [-10, -2, 9, 100]
    assert quick([-2, -10, 100, 9]) == [-10, -2, 9, 100]

def test_heap_bubble():
    for _ in range(20):
        array = [random.randint(-50, 50) for _ in range(10)]
        assert heap_sort(array) == bubble(array)

def test_heap_merge():
    for _ in range(20):
        array = [random.randint(-50, 50) for _ in range(10)]
        assert heap_sort(array) == merge(array)

def test_heap_quick():
    for _ in range(20):
        array = [random.randint(-50, 50) for _ in range(10)]
        assert heap_sort(array) == quick(array)

def test_all_equal():
    assert heap_sort([1, 2, 3]) == bubble([1, 2, 3]) == merge([1, 2, 3]) == quick([1, 2, 3])
    assert heap_sort([3, 2, 1]) == bubble([3, 2, 1]) == merge([3, 2, 1]) == quick([3, 2, 1])
    assert heap_sort([1, 1, 1]) == bubble([1, 1, 1]) == merge([1, 1, 1]) == quick([1, 1, 1])
    assert heap_sort([5, -1, 0]) == bubble([5, -1, 0]) == merge([5, -1, 0]) == quick([5, -1, 0])