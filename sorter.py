import time
import os

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def number_sorter(input_file, output_file):
    clear_terminal()
    with open(input_file, 'r') as f:
        numbers = [int(x) for x in f.read().strip().split()]
    start_time = time.time()
    sorted_numbers = sorted(numbers)
    end_time = time.time()
    elapsed_time = end_time - start_time
    with open(output_file, 'w') as f:
        for num in sorted_numbers:
            f.write(str(num) + '\n')
    print(f"Sorted numbers written to {output_file}")
    print(f"Time taken to sort: {elapsed_time:.12f} seconds")

# Example usage:
input_file = 'md.txt'
output_file = 'mdn.txt'
number_sorter(input_file, output_file)