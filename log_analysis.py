import re
import csv
from collections import defaultdict

# Read the log file
log_file = "sample.log"

def parse_log_file(filepath):
    logs = []
    with open(filepath, "r") as f:
        logs = f.readlines()
    return logs

logs = parse_log_file(log_file)

ip_no_of_requests = defaultdict(int)
endpoints = defaultdict(int)
failed_login = defaultdict(int)
failed_threshold = 10

# Action 3: For every log entry
for log in logs:
    match_ip = re.match(r"(\d+\.\d+\.\d+\.\d+)", log)
    if match_ip:
        ip_address = match_ip.group(1)
        ip_no_of_requests[ip_address] += 1

    match_endpoint = re.search(r'"(GET|POST) (/[^ ]*)', log)
    if match_endpoint:
        endpoint = match_endpoint.group(2)
        endpoints[endpoint] += 1

    # Count the number of failed login attempts for each user
    if '401' in log or "Invalid credentials" in log:
        if match_ip:
            failed_login[ip_address] += 1
# Step 4: Sort and analyze results

sorted_ip_requests = sorted(ip_no_of_requests.items(), key=lambda item: item[1], reverse=True)
most_accessed_endpoint = max(endpoints.items(), key=lambda item: item[1])
flagged_ips = {ip: count for ip, count in failed_login.items() if count > failed_threshold}

# Step 5: Output the result in the terminal:
print("Requests per IP Address:")
for i, c in sorted_ip_requests:
    print("{:<20} {}".format(i, c))

print("\nMost Frequently Accessed Endpoint :")
print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")

print("\nSuspicious Activity Detected :")
if flagged_ips:
    for ip, count in flagged_ips.items():
        print(f"{ip:<20} {count}")
else:
    print("No suspicious activity detected.")

# Step 6: Write results to a csv file
output_file = "log_analysis_results.csv"