'''

File Operations
File I/O

'''
input_file = input("Enter the name of the file: ")
output_file = input("Enter the name of the result file:")

try:
    with open(input_file, "r") as infile:
        content = infile.read()
    uppercase_content = content.upper()

    with open(output_file, "w") as result:
        result.write(uppercase_content)

except FileNotFoundError as err:
    print(f'File not found {input_file}: ', err)

