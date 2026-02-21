"""
==============================================
PYTHON FILE INPUT & OUTPUT – COMPLETE REVISION
==============================================

This program demonstrates:

1. Reading from a text file
2. Writing to a file
3. Using 'with' (context manager)
4. Safe integer conversion
5. Error handling
6. Proper resource management
"""

print("Processing input ...")

total = 0

# ===========================================
# Using context manager (Best Practice)
# ===========================================

with open('io-input-values.txt', 'rt') as inputfile, \
     open('io-output-totaled.txt', 'wt') as outputfile:

    for line in inputfile:
        clean_line = line.strip()

        # Skip empty lines
        if not clean_line:
            continue

        try:
            number = int(clean_line)
            total += number

            # Write cleaned value to output file
            print(number, file=outputfile)

        except ValueError:
            # Handle non-numeric lines safely
            print(f"Invalid number skipped: {clean_line}", file=outputfile)

    # Write final total
    print("\n---------------------", file=outputfile)
    print(f"Total: {total}", file=outputfile)

print("Output Complete")