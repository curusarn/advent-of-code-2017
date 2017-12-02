
from sys import argv


with open(argv[1]) as f:
    captcha = f.readline().strip()
    print('CAPTCHA input: {0}'.format(captcha))

    result = 0
    for i, char in enumerate(captcha):
        x = int(i +  len(captcha) / 2) % len(captcha)
        if captcha[i] == captcha[x]:
            result += int(char)

    print('CAPTCHA result: {0}'.format(result))


