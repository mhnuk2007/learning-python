""" file-errors.py """

def read_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File does not exist.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    read_file("example.txt")