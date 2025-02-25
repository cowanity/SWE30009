import os
import shutil
import subprocess

# Define the paths to the original files
original_sort_path = 'counting_sort.py'
original_test_path = 'test_counting_sort.py'

# Read the content of the original files
with open(original_sort_path, 'r') as file:
    original_sort_code = file.readlines()

with open(original_test_path, 'r') as file:
    original_test_code = file.readlines()

# Define mutation operators and their replacements
mutations = [
    ("coll_max + 1 - coll_min", "coll_max - 1 - coll_min"),
    ("coll_max + 1 - coll_min", "coll_max + 1 + coll_min"),
    ("[0] * counting_arr_length", "[0] / counting_arr_length"),
    ("[0] * counting_arr_length", "[0] // counting_arr_length"),
    ("[0] * counting_arr_length", "[0] ** counting_arr_length"),
    ("counting_arr[number - coll_min] -= 1", "counting_arr[number + coll_min] -= 1"),
    ("counting_arr[number - coll_min] += 1", "counting_arr[number + coll_min] += 1"),
    ("counting_arr[i] + counting_arr[i - 1]", "counting_arr[i] - counting_arr[i - 1]"),
    ("counting_arr[i] + counting_arr[i - 1]", "counting_arr[i] + counting_arr[i + 1]"),
    ("[0] * coll_len", "[0] / coll_len"),
    ("[0] * coll_len", "[0] // coll_len"),
    ("[0] * coll_len", "[0] ** coll_len"),
    ("ordered[counting_arr[collection[i] - coll_min] - 1]", "ordered[counting_arr[collection[i] + coll_min] - 1]"),
    ("ordered[counting_arr[collection[i] - coll_min] - 1]", "ordered[counting_arr[collection[i] - coll_min] + 1]"),
    ("counting_arr[collection[i] - coll_min] -= 1", "counting_arr[collection[i] + coll_min] -= 1"),
    ("counting_arr[collection[i] - coll_min] -= 1", "counting_arr[collection[i] - coll_min] += 1"),
    ("counting_arr[collection[i] - coll_min] += 1", "counting_arr[collection[i] - coll_min] -= 1"),
    ("if collection == []", "if not (collection == [])"),
    ("if number == 7", "if not (number == 7)"),
    ("if __name__ == '__main__'", "if not (__name__ == '__main__')"),
    ("if __name__ == '__main__'", "if name != 'main'"),
    ("if collection == []", "if collection != []"),
    ("if number == 7", "if number != 7"),
    ("assert counting_sort_string('thisisthestring') == 'eghhiiinrsssttt'", "assert counting_sort_string('thisisthestring') != 'eghhiiinrsssttt'")
]

# Create a directory to store mutants
mutants_dir = 'mutants'
if not os.path.exists(mutants_dir):
    os.makedirs(mutants_dir)

# Function to write mutant file
def write_mutant_file(mutant_code, mutant_id):
    mutant_file_path = os.path.join(mutants_dir, f'counting_sort_mutant_{mutant_id}.py')
    with open(mutant_file_path, 'w') as mutant_file:
        mutant_file.writelines(mutant_code)
    return mutant_file_path

# Create mutant files
mutant_paths = []
for i, (original, mutant) in enumerate(mutations, start=1):
    mutant_code = [line.replace(original, mutant) for line in original_sort_code]
    mutant_file_path = write_mutant_file(mutant_code, i)
    mutant_paths.append(mutant_file_path)

# Create a test file that can dynamically import the mutant
test_file_template = original_test_code[:]
test_import_line = "from counting_sort import counting_sort\n"

# Directory for test results
results_dir = os.path.join(mutants_dir, "results")
os.makedirs(results_dir, exist_ok=True)

# Run tests for each mutant
results = []
for i, mutant_file_path in enumerate(mutant_paths, start=1):
    # Modify the import statement to import from the mutant file
    test_code = test_file_template.copy()
    test_code[1] = f"from counting_sort_mutant_{i} import counting_sort\n"
    
    # Write the modified test file
    test_file_path = os.path.join(mutants_dir, f'test_counting_sort_mutant_{i}.py')
    with open(test_file_path, 'w') as test_file:
        test_file.writelines(test_code)
    
    # Run pytest on the mutant test file
    result = subprocess.run(['pytest', test_file_path], capture_output=True, text=True)
    survived = "failed" not in result.stdout
    results.append((i, survived, result.stdout))
    
    # Save the result output
    result_file_path = os.path.join(results_dir, f"result_{i}.txt")
    with open(result_file_path, 'w') as result_file:
        result_file.write(result.stdout)

# Print the summary results
for mutant_id, survived, _ in results:
    status = "survived" if survived else "killed"
    print(f"Mutant #{mutant_id} {status}")

print(f"Detailed test results are saved in: {results_dir}")
