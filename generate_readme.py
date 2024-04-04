import os

# Function to generate markdown links
def generate_markdown_link(label, path):
    return f"[{label}]({path})"

# List all directories and files
entries = os.listdir('.')
readme_template = "# LeetCode Solutions Repository\n\n" \
                  "This repository contains my solutions to LeetCode problems in C and Python 3.\n\n" \
                  "## Solutions\n\n" \
                  "| Problem | Problem Statement | Python 3 |   C   |\n" \
                  "| ------- | ----------------- | -------- | ----- |\n"

# Filter out directories that have a numeric prefix (indicative of problem number)
problem_dirs = [d for d in entries if os.path.isdir(d) and d.split('-')[0].isdigit()]

# Sort directories by problem number
problem_dirs.sort(key=lambda x: int(x.split('-')[0]))

# Iterate over each problem directory and add links to the README and solution files
for problem_dir in problem_dirs:
    readme_path = os.path.join(problem_dir, 'README.md')
    # Look for solution files with .py and .c extensions
    python_solution = next((f for f in os.listdir(problem_dir) if f.endswith('.py')), None)
    c_solution = next((f for f in os.listdir(problem_dir) if f.endswith('.c')), None)
    
    # Generate markdown links for the solutions, if they exist
    python_link = generate_markdown_link('Python', os.path.join(problem_dir, python_solution)) if python_solution else ''
    c_link = generate_markdown_link('C', os.path.join(problem_dir, c_solution)) if c_solution else ''

    row_header_elements = problem_dir.split("-")
    
    # Generate markdown table row
    table_row = f"| {row_header_elements[0]}. {" ".join(row_header_elements[1:])} | {generate_markdown_link('Readme', readme_path)} | {python_link} | {c_link} |\n"
    readme_template += table_row

# Write the generated markdown to the README.md file
with open('README.md', 'w') as readme_file:
    readme_file.write(readme_template)
