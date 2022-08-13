# asks user for a range of numbers to generate
values = int(input('enter a range '))

# opens file
with open('arithmetic.py', 'w') as file:

    # generates add function
    file.write('def add(a: int, b: int):\n    \"\"\"\n    adds 2 numbers together\n\n    :param a: the first number to '
               'add\n    :param b: the second number to add\n\n    :return: the 2 numbers added together\n    \"\"\"\n'
               '\n    # adds 0 and 0\n    if a == 0 and b == 0:\n        return 0')
    skip = True
    for x in range(values):
        for y in range(values):
            if skip:
                skip = False
            else:
                file.write(f'\n\n    # adds {x} and {y}\n    elif a == {x} and b == {y}:\n        return {x + y}')
    file.write('\n\n    # displays error if other values are added\n    else:\n        raise NotImplementedError(f\''
               'adding {a} and {b} has not been implemented yet\')\n\n\n')

    # generates subtraction function
    file.write('def subtract(a: int, b: int):\n    \"\"\"\n    subtracts 2 numbers\n\n    :param a: the first number to'
               ' subtract\n    :param b: the second number to subtract\n\n    :return: the 2 numbers subtracted\n    '
               '\"\"\"\n\n    # subtracts 0 and 0\n    if a == 0 and b == 0:\n        return 0')
    skip = True
    for x in range(values):
        for y in range(values):
            if skip:
                skip = False
            else:
                file.write(f'\n\n    # subtracts {x} and {y}\n    elif a == {x} and b == {y}:\n        return {x - y}')
    file.write('\n\n    # displays error if other values are subtracted\n    else:\n        raise NotImplementedError('
               'f\'subtracting {a} and {b} has not been implemented yet\')\n\n\n')

    # generates multiplication function
    file.write('def multiply(a: int, b: int):\n    \"\"\"\n    multiplies 2 numbers together\n\n    :param a: the '
               'first number to multiply\n    :param b: the second number to multiply\n\n    :return: the 2 numbers '
               'multiplied together\n    \"\"\"\n\n    # multiplies 0 and 0\n    if a == 0 and b == 0:\n        return '
               '0')
    skip = True
    for x in range(values):
        for y in range(values):
            if skip:
                skip = False
            else:
                file.write(f'\n\n    # multiplies {x} and {y}\n    elif a == {x} and b == {y}:\n        return {x * y}')
    file.write('\n\n    # displays error if other values are added\n    else:\n        raise NotImplementedError(f\''
               'multiplying {a} and {b} has not been implemented yet\')\n\n\n')

    # generates division function
    file.write('def divide(a: int, b: int):\n    \"\"\"\n    divide 2 numbers\n\n    :param a: the first number to '
               'divide\n    :param b: the second number to divide\n\n    :return: the 2 numbers divided together\n    '
               '\"\"\"\n\n    # divides 0 and 0\n    if a == 0 and b == 0:\n        raise ZeroDivisionError')
    skip = True
    for x in range(values):
        for y in range(values):
            if skip:
                skip = False
            else:
                try:
                    file.write(f'\n\n    # divides {x} and {y}\n    elif a == {x} and b == {y}:\n        '
                               f'return {x / y}')
                except ZeroDivisionError:
                    file.write(
                        f'\n\n    # divides {x} and {y}\n    elif a == {x} and b == {y}:\n        '
                        f'raise ZeroDivisionError')
    file.write('\n\n    # displays error if other values are divided\n    else:\n        raise NotImplementedError(f\''
               'dividing {a} and {b} has not been implemented yet\')\n')
