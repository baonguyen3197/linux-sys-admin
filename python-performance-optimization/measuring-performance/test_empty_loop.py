from empty_loop import heavy_work

def test_benchmark_heavy_work(benchmark):
    benchmark(heavy_work)

# To run the benchmark, use the command:
# pytest test_empty_loop.py
