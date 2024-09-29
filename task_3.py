import re


def is_balanced(text: str) -> str:
    # Видаляємо всі символи, крім дужок
    parsed_text = re.sub(r'[^()\[\]{}]', '', text)

    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    # Проходимося по кожному символу в рядку
    for char in parsed_text:
        if char in brackets.values():
            # Якщо символ - відкрита дужка, додаємо її до стека
            stack.append(char)
        elif char in brackets.keys():
            # Якщо символ - закрита дужка, перевіряємо відповідність останній відкритій дужці
            if stack == [] or brackets[char] != stack.pop():
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"


if __name__ == '__main__':
    examples = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]
    for i in examples:
        print(f"{i} - {is_balanced(i)}")
