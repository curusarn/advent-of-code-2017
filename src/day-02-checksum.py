
from sys import argv


with open(argv[1]) as f:
    checksum = 0
    for row in f:
        print('\nrow: {0}'.format(row.strip()))

        cols = row.split('\t')
        cols = list(map(lambda x : int(x), cols))
        print('values: {0}'.format(cols))

        min_val = min(cols)  
        max_val = max(cols) 
        print('min: {0}'.format(min_val))
        print('max: {0}'.format(max_val))

        row_checksum = max_val - min_val
        checksum += row_checksum 
        print('row CHECKSUM: {0}'.format(row_checksum))

    print('\nspreadsheet CHECKSUM: {0}'.format(checksum))

