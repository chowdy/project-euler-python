import argparse
import importlib

parser = argparse.ArgumentParser(description='Project Euler solutions written in Python 3.')
parser.add_argument('solution', metavar='S', type=str, help='The solution to run')
args = parser.parse_args()

# Add leading zeroes to solution argument if necessary
solution_input = args.solution
while len(solution_input) < 3:
    solution_input = '0' + solution_input

# Import the solution script
solution = None
# noinspection PyBroadException
try:
    solution = importlib.import_module(f'solutions.{solution_input}')
except Exception as err:
    print(f'Error Importing solutions.{solution_input}')
    exit(1)

# Run the solution and print the answer it returns
answer = solution.solution()
print(f'{answer}')
