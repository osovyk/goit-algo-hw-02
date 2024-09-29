import re
from collections import deque


def is_palindrome(text: str) -> str:
    # Видалення цифр, пробілів та символів
    parsed_text = re.sub(r"[^a-zA-Zа-яА-Я]", "", text)

    # Створення двосторонньої черги
    d_queue = deque(parsed_text)

    # Порівняння символів з обох кінців черги
    while len(d_queue) > 1:
        if d_queue.popleft().casefold() != d_queue.pop().casefold():
            return "Рядок не є паліндромом"
    return "Рядок є паліндромом"


if __name__ == '__main__':
    examples = ["Видалення пробілів", "Madam in Eden, I’m Adam"]
    for i in examples:
        print(f"{i} - {is_palindrome(i)}")
