def calculate(expression: str) -> float:

    # Removing spaces
    expression = expression.replace(" ", "")

    stack = []
    num = 0
    sign = '+'
    i = 0

    while i < len(expression):
        char = expression[i]

        # Building the number until a operator occurs
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            i -= 1

            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(stack.pop() / num)

        elif char in '+-*/':
            sign = char

        i += 1

    result = sum(stack)

    return round(float(result), 2)

#Team name-{CLP}
