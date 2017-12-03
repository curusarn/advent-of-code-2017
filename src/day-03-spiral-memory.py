
from sys import argv

def get_layer(n):
    n = int((n + 6) / 8)

    layer = 0 
    value = 0 
    prev_value = 0 #None
    while n > value:
        prev_value = value
        layer += 1
        value += layer

    return layer, value * 8 + 1, prev_value * 8 + 1 

def get_distance(n):
    layer, layer_end_value, layer_start_value = get_layer(n)
    layer_start_value += 1 
    print('layer: {0}'.format(layer))
    print('layer_end_value: {0}'.format(layer_end_value))
    print('layer_start_value: {0}'.format(layer_start_value))
    if layer == 0:
        return 0

    group_size = int((layer_end_value - layer_start_value + 1) / 4)
    layer_idx = (n - layer_start_value) % group_size
    print('layer_idx: {0}'.format(layer_idx))
    
    layer_middle = layer - 1
    print('layer_middle: {0}'.format(layer_middle))

    distance_in_layer = abs(layer_middle - layer_idx)
    print('distance_in_layer: {0}'.format(distance_in_layer))

    return layer + distance_in_layer
     

with open(argv[1]) as f:
    for line in f:
        n = int(line.strip())
        print('\npuzzle input: {0}'.format(n))

        dist = get_distance(n)

        print('DISTANCE: {0}'.format(dist))

