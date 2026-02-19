def main():
    # Write to file
    with open("textfile.txt", "w") as f:
        for i in range(10):
            f.write(f"This is line {i+1}\n")

    # Read from file
    with open("textfile.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())  # strip removes extra newline


if __name__ == "__main__":
    main()