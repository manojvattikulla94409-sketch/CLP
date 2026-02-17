team name-pywarriors
def calculate(expression: str) -> float:

    # Removing spaces
    expression = expression.replace(" ", "")

    stack = []
    number= 0
    sign = '+'
    i = 0

    while i < len(expression):
        ch = expression[i]

        # Building the number until a operator occurs
        if ch.isdigit():
            number= 0
            
            while i < len(expression) and expression[i].isdigit():
                number = number * 10 + int(expression[i])
                i += 1
            i -= 1

            if sign == '+':
                stack.append(number)
            elif sign == '-':
                stack.append(-number)
            elif sign == '*':
                stack.append(stack.pop() * number)
            elif sign == '/':
                stack.append(stack.pop() / number)

        elif ch in '+-*/':
            sign = ch

        i += 1

    result = sum(stack)

    return round(float(result), 2)

#Team name-{CLP}
calculate('2 + 3')
