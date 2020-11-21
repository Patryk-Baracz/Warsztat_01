from random import randint

def roll_dice(dice_type):
    d_list = [3, 4, 6, 8, 10, 12, 20, 100]
    if int(dice_type) not in d_list:
        raise ValueError(f"There are no {dice_type}D dice's")
    return randint(1, int(dice_type))


def dice_code_test(xDyz):
    """test the dice code (xDy+z) and return list [x, y, z]"""
    if 'D' not in xDyz:
        raise ValueError('There must be "D" in your code')
    code = list(xDyz.split("D"))
    if '+' in code[1]:
        code.extend(list(code.pop().split('+')))
    elif '-' in code[1]:
        code.extend(list(code.pop().split('-')))
        substraction = True
    else:
        pass
    if not "".join(code).isdigit():
        raise ValueError('Wrong code! it has to be xDy+z')
    elif substraction == True:
        code.append(f'-{code.pop()}')
    return code

def dice():
    xdyz = input("type your dice code (xDy+z):")
    code = dice_code_test(xdyz)
    value = int(code[2])
    for i in range(1, int(code[0])+1):
        value += roll_dice(code[1])
    return value

print(dice())

