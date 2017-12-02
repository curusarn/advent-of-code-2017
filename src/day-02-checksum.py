
from sys import argv

def find_one_divides_the_other(cols):
    cols = sorted(cols)
    for x, value_x in enumerate(cols):
        for y, value_y in enumerate(cols):
            if x == y:
                continue
            if value_x % value_y == 0:
                return value_x, value_y
            if value_y % value_x == 0:
                return value_y, value_x

    assert False 

with open(argv[1]) as f:
    checksum = 0
    for row in f:
        print('\nrow: {0}'.format(row.strip()))

        cols = row.split('\t')
        cols = list(map(lambda x : int(x), cols))
        print('values: {0}'.format(cols))

        val_x, val_y = find_one_divides_the_other(cols)

        row_checksum = val_x / val_y
        checksum += row_checksum 
        print('row CHECKSUM: {0}'.format(row_checksum))

    checksum = int(checksum)
    print('\nspreadsheet CHECKSUM: {0}'.format(checksum))

