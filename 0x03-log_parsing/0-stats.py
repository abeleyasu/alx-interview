#!/usr/bin/python3
import sys

def print_stats(file_size, status_codes):
    """
    Print the accumulated statistics:
    - Total file size
    - Number of lines for each status code
    """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        # Split the line by spaces and validate the format
        parts = line.split()
        if len(parts) < 7:
            continue

        # Extract the file size (last element) and the status code (second to last element)
        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
            total_file_size += file_size

            # Update the count of the corresponding status code
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        except (ValueError, IndexError):
            continue

        # Increment the line counter
        line_count += 1

        # After every 10 lines, print the statistics
        if line_count % 10 == 0:
            print_stats(total_file_size, status_code_counts)

except KeyboardInterrupt:
    # Print final stats upon keyboard interruption
    print_stats(total_file_size, status_code_counts)
    raise

# Print final stats when the input stream ends
print_stats(total_file_size, status_code_counts)
