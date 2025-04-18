# Create the Python script that will read the SQL content, modify the insert logic, and write to a new file

python_script = """
# Python script to modify SQL for 1000x data scaling

# Read the content of the original SQL file
file_path = './script.sql'
output_path = './modified_script.sql'

with open(file_path, 'r') as file:
    file_content = file.read()

# Modify the INSERT INTO statements to simulate 1000 times more data
modified_content = file_content

# Example: Scaling the INSERT INTO logic
modified_content = modified_content.replace("INSERT INTO products", "/* Scaled up INSERT INTO products */\n" + ("INSERT INTO products\n" * 1000))
modified_content = modified_content.replace("INSERT INTO customers", "/* Scaled up INSERT INTO customers */\n" + ("INSERT INTO customers\n" * 1000))
modified_content = modified_content.replace("INSERT INTO employees", "/* Scaled up INSERT INTO employees */\n" + ("INSERT INTO employees\n" * 1000))

# Write the modified content to a new SQL file
with open(output_path, 'w') as output_file:
    output_file.write(modified_content)

print(f"Modified SQL file created at {output_path}")
"""

# Save the Python script to a Python file
script_file_path = './scale_data_sql.py'
with open(script_file_path, 'w') as script_file:
    script_file.write(python_script)

script_file_path  # Provide the path to the saved Python script
