# Кальулятор целых чисел от 1 до 10

## Формат ввода строки:

`{операнд_1} {оператор} {операнд_2}`

## Примеры работы программы:

Input:

`1 + 2`

Output:

`3`

Input:

`1`

Output:

`throws Exception //т.к. строка не является математической операцией`

Input:

`1 + 2 1`

Output:

`throws Exception` 

Input:

`1 + 2 + 3`

Output:

`throws Exception //т.к. формат математической операции не удовлетворяет заданию - два операнда и один оператор (+, -, /, *)`