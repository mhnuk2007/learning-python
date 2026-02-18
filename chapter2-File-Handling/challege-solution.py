import os

# Flags for debugging or hints
show_expected_result = False
show_hints = False

def file_info():
    """
    Calculate the total size in bytes of all `.txt` files
    inside the 'deps' directory.
    """
    
    # List all .txt files in the 'deps' directory
    text_files = [os.path.join("deps", f) for f in os.listdir("deps") if f.endswith(".txt")]

    total_bytes = 0  # Initialize counter

    # Sum up the sizes of all files
    for file in text_files:
        if os.path.isfile(file):  # Ensure it's a file
            filesize = os.path.getsize(file)
            total_bytes += filesize

    return total_bytes

# Example usage
if __name__ == "__main__":
    print("Total bytes of .txt files in 'deps':", file_info())