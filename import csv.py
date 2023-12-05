import csv
import re
from datetime import datetime

# Input and output file paths
log_file_path = 'filename.log' # file path of your log file
csv_file_path = 'filename.csv' # output file path to drop 

# Open log file for reading and CSV file for writing
with open(log_file_path, 'r') as log_file, open(csv_file_path, 'w', newline='') as csv_file:
    # Define CSV writer
    csv_writer = csv.writer(csv_file)

    # Write header to CSV file
    csv_writer.writerow(['IP Address', 'Timestamp', 'Method', 'URL', 'Status', 'User Agent'])

    # Define a regular expression pattern to extract information
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[([^\]]+)\] "(\w+) ([^"]+)" (\d+) \d+ "([^"]+)" "([^"]+)"')

    # Process each line in the log file
    for line in log_file:
        # Use regular expression to match log entry components
        match = log_pattern.match(line)
        if match:
            ip_address, timestamp_str, method, url, status, _, user_agent = match.groups()

            # Convert timestamp string to datetime object
            timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')

            # Write components to CSV file
            csv_writer.writerow([ip_address, timestamp, method, url, status, user_agent])

print(f'Conversion complete. CSV file saved at: {csv_file_path}')
