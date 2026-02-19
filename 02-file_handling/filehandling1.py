# Opening a file in read mode
# Note: Make sure "example.txt" exists in the same directory as this script
# Open the file for reading if it exists, otherwise it will raise an error
# file = open("example.txt", "r") 

# # Reading the entire content of the file
# content = file.read()

# print("File Content:")
# print(content)  

# # Closing the file after reading
# file.close()

# # Reading the file line by line using a loop
# file = open("example.txt", "r")
# print("\nReading line by line:")
# for line in file:
#     print(line)
# file.close()


# # Writing to a file (Overwrite mode)
# file = open("example.txt", "w")
# file.write("This is a new line written to the file.")
# file.close()

# # # Writing to a file (Append mode)
# file = open("example.txt", "a")
# file.write("\nThis line is appended to the file.")
# file.close()

# # Using with statement to handle files (automatically closes the file)
# with open("example.txt", "r") as file:
#     content = file.read()
#     print("File Content using with statement:")
#     print(content)

# Reading a specific line from the file
with open("example.txt", "r") as file:
    # Read the first line of the file
    line = file.readline()
    print("First line of the file:")
    print(line)

    # Read the second line of the file
    line = file.readline()
    print("Second line of the file:")
    print(line)

    # Alternatively, you can read all lines into a list and access them by index
    file.seek(0)  # Move the cursor back to the beginning of the file
    lines = file.readlines()  # Read all lines into a list
    print("All lines in the file:")
    for i, line in enumerate(lines):
        print(f"Line {i + 1}: {line}")
        