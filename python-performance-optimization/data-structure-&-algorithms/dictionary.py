import random

def search_list(big_list, items):
    count = 0
    for item in items:
        for order in big_list:
            if item == order[0]:
                count += 1
    return count

def search_dictionary(some_dictionary, items):
    count = 0
    for item in items:
        if item in some_dictionary:
            count += 1
    return count

@profile
def main():
    SIZE = 100_000

    big_list = []
    big_dictionary = {}

    for i in range(SIZE):
        big_list.append([i, 2 * i, i * i])
        big_dictionary[i] = [2 * i, i * i]

    orders_to_search = [random.randint(0, SIZE) for _ in range(1000)]
    search_list(big_list, orders_to_search)
    search_dictionary(big_dictionary, orders_to_search)

main()

# To run the profiler, use the command:
# kernprof -lv dictionary.py

# To view the results, use the command:
# python -m line_profiler dictionary.py.lprof

# cmd
# python -m timeit "{'order_id':1}"

# python -m timeit -s "from collections import namedtuple; Order=namedtuple('Order','order_id')" "Order(1)"

# python -m timeit -s """
# >> from dataclasses import dataclass
# >> @dataclass  
# >> class Order:     
# >>     order_id: int
# >> """ "Order(1)"

# python -m timeit -s "order={'order_id':1}" "order['order_id']"

# python -m timeit -s "from collections import namedtuple; Order=namedtuple('Order','order_id'); order=Order(1)" "order.order_id"

# python -m timeit -s """                                                                                                 
# >> from dataclasses import dataclass    
# >> @dataclass                     
# >> class Order:
# >>     order_id: int
# >> order=Order(1)""" "order.order_id"