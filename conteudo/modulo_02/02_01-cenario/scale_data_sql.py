# Read the content of the original SQL file
file_path = './script.sql'
output_path = './modified_script.sql'
# Python script to modify SQL for 1000x data scaling

with open(file_path, 'r') as file:
    file_content = file.read()

# Modify the INSERT INTO statements to simulate 1000 times more data
modified_content = file_content

# Scaling up the INSERT INTO logic by adding 1000 times repetition
modified_content = modified_content.replace("INSERT INTO products", "/* Scaled up INSERT INTO products */\n" + "INSERT INTO products\n" * 50000)
modified_content = modified_content.replace("INSERT INTO customers", "/* Scaled up INSERT INTO customers */\n" + "INSERT INTO customers\n" * 50000)
modified_content = modified_content.replace("INSERT INTO employees", "/* Scaled up INSERT INTO employees */\n" + "INSERT INTO employees\n" * 50000)

# Write the modified content to a new SQL file
with open(output_path, 'w') as output_file:
    output_file.write(modified_content)

print(f"Modified SQL file created at {output_path}")
