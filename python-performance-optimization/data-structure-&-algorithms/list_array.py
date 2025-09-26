import numpy

def double_list(size):
    initialize_list = list(range(size))
    return [2 * i for i in initialize_list]

def double_array(size):
    initialize_array = numpy.arange(size)
    return 2 * initialize_array

double_list(1_000_000)
double_array(1_000_000)