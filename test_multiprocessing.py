import multiprocessing
import math

def calculate_square_root(number):
    return math.sqrt(number)


if __name__ == "__main__" :
    numbers = [16,25,36,49,64,81]

    num_processing = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processing)
    print(f"number of processors {num_processing}")
    square_root = pool.map(calculate_square_root, numbers)
    pool.close()
    pool.join()

    for number, sq in zip(numbers, square_root):
        print(f"Square root number of {number} is {sq}")


