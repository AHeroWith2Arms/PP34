from src.proccesing import filter_by_state, sort_by_date

# данные для теста
test_data: list[dict] = [
    {"id": 1, "name": "Task A", "date": "2023-10-01T12:00:00", "state": "PENDING"},
    {"id": 2, "name": "Task B", "date": "2023-09-30T15:00:00", "state": "EXECUTED"},
    {"id": 3, "name": "Task C", "date": "2023-10-02T18:00:00", "state": "CANCELED"},
    {"id": 4, "name": "Task D", "date": "2023-10-03T20:00:00", "state": "EXECUTED"},
]

"""
проверка фильтрации функции filter_by_date
"""

# Проверка функции filter_by_state
filtered_executed = filter_by_state(test_data)
assert len(filtered_executed) == 2
assert {"id": 2, "name": "Task B", "date": "2023-09-30T15:00:00", "state": "EXECUTED"} in filtered_executed
assert {"id": 4, "name": "Task D", "date": "2023-10-03T20:00:00", "state": "EXECUTED"} in filtered_executed

filtered_pending = filter_by_state(test_data, state="PENDING")
assert len(filtered_pending) == 1
assert {"id": 1, "name": "Task A", "date": "2023-10-01T12:00:00", "state": "PENDING"} in filtered_pending


"""
Тестирование функции сортировки - sort_by_date
"""

# Проверка функции sort_by_date
sorted_descending = sort_by_date(test_data)
expected_descending = [
    {"id": 4, "name": "Task D", "date": "2023-10-03T20:00:00", "state": "EXECUTED"},
    {"id": 3, "name": "Task C", "date": "2023-10-02T18:00:00", "state": "CANCELED"},
    {"id": 1, "name": "Task A", "date": "2023-10-01T12:00:00", "state": "PENDING"},
    {"id": 2, "name": "Task B", "date": "2023-09-30T15:00:00", "state": "EXECUTED"},
]
assert sorted_descending == expected_descending

sorted_ascending = sort_by_date(test_data, order="ascending")
expected_ascending = [
    {"id": 2, "name": "Task B", "date": "2023-09-30T15:00:00", "state": "EXECUTED"},
    {"id": 1, "name": "Task A", "date": "2023-10-01T12:00:00", "state": "PENDING"},
    {"id": 3, "name": "Task C", "date": "2023-10-02T18:00:00", "state": "CANCELED"},
    {"id": 4, "name": "Task D", "date": "2023-10-03T20:00:00", "state": "EXECUTED"},
]
assert sorted_ascending == expected_ascending
