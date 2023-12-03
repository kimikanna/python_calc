def main(input_str: str):
    splitted_input = input_str.split()
    if len(splitted_input) == 3:
        a, b = splitted_input[0], splitted_input[2]
        operator = splitted_input[1]
        check_operand(a)
        check_operand(b)
        operator = check_operator(operator)
        result = eval(a + operator + b)
        return result
    else:
        raise ValueError('Формат не удовлетворяет заданию – два операнда и один оператор (+, -, /, *)')


def check_operand(a: str):
    if a.isdigit():
        int_a = int(a)
        if 0 < int_a < 11:
            return int_a
        else:
            raise ValueError(f'Операнд "{int_a}" не соответствует промежутку: [1, 10]')
    else:
        raise ValueError(f'Операнд "{a}" не является целым числом')


def check_operator(operator: str):
    operator_set = {'+', '-', '*', '/'}
    if operator in operator_set:
        if operator == '/':
            operator = '//'
        return operator
    else:
        raise ValueError(f'Оператор "{operator}" не соответствует списку допустимых операций (+, -, *, /)')


if __name__ == '__main__':
    print(main(input('Введите выражение: ')))
