import argparse
import sys
import os

parser = argparse.ArgumentParser(description="Manage the daily_coding_problems repository.")
parser.add_argument('--np', action='store_true', help='Create a new directory for the new problem')
parser.add_argument('--pn', type=int, required='--np' in sys.argv, help='The problem number')
parser.add_argument('--pd', type=str, help='The problem description')

problem_directory = 'problem_{pn}'
problem_file = 'problem.md'
solution_file = 'solution.py'

def create_problem_directory(number):
    directory_name = problem_directory.format(pn=number)

    directory_created = False

    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        directory_created = True
    else:
        print('Folder - {directory_name}, already exists.'.format(directory_name=directory_name))
    
    return directory_created, directory_name


def create_problem_file(directory, description=None):
    if description is not None:
        with open('{directory}/{problem_file}'.format(directory=directory, problem_file=problem_file), 'w') as f:
            f.write(problem_description)

    return True


def create_solution_file(directory):
    os.mknod('{directory}/{solution_file}'.format(directory=directory, solution_file=solution_file))
    return True


def create_new_problem(number, description):
    print('Creating new problem...')

    directory_created, directory = create_problem_directory(number)

    if not directory_created:
        return False
    else:
        print('Directory created - {directory}'.format(directory=directory))

    if not create_problem_file(directory, description):
        return False
    else:
        print('Problem file created - {problem_file}'.format(problem_file=problem_file))
        if description is not None:
            print('The following problem description was added: \n{pd}'.format(pd=description))

            
    
    if not create_solution_file(directory):
        return False
    else:
        print('Solution file created - {solution_file}'.format(solution_file=solution_file))

    return True


if __name__ == "__main__":
    args = parser.parse_args()
    
    if args.np:
        problem_number = args.pn
        problem_description = args.pd
        successful_creation = create_new_problem(problem_number, problem_description)
