
from sys import argv


with open(argv[1]) as f:
    captcha = f.readline().strip()
    print('CAPTCHA input: {0}'.format(captcha))
    captcha += captcha[0]

    result = 0
    prev_char = None
    for char in captcha:
        if prev_char == char:
            result += int(char)
        prev_char = char

    print('CAPTCHA result: {0}'.format(result))


