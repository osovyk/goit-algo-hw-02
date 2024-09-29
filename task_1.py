import queue
import random
import time
import uuid

# Створити чергу заявок
queue = queue.Queue()


def generate_request():
    """
    Функція generate_request():
        Створити нову заявку
        Додати заявку до черги
    """
    request_id = uuid.uuid4()
    queue.put(request_id)
    print(f"Заявка {request_id} додана до черги.")


def process_request():
    """
    Функція process_request():
        Якщо черга не пуста:
            Видалити заявку з черги
            Обробити заявку
        Інакше:
            Вивести повідомлення, що черга пуста
    """
    if not queue.empty():
        request_id = queue.get()
        print(f"Заявка {request_id} обробляється.")
        # Імітація часу обробки заявки
        time.sleep(random.randint(1, 3))
        print(f"Заявка {request_id} оброблена.")
    else:
        print("Черга пуста, немає заявок для обробки.")


if __name__ == '__main__':
    """
    Головний цикл програми:
        Поки користувач не вийде з програми:
            Виконати generate_request() для створення нових заявок
            Виконати process_request() для обробки заявок
    """
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(random.randint(1, 3))
    except KeyboardInterrupt:
        print("Програма завершена користувачем")
