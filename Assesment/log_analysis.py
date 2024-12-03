import csv
from collections import Counter, defaultdict

# File names
LOG_FILE = "sample.log"
OUTPUT_FILE = "log_analysis_results.csv"

# Configurable threshold for suspicious activity detection
FAILED_LOGIN_THRESHOLD = 10


def parse_log_file(log_file):
    """Parse the log file and extract relevant data."""
    ip_requests = Counter()
    endpoint_access = Counter()
    failed_logins = defaultdict(int)

    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split()
            ip = parts[0]
            request = parts[5][1:]  # Extracting GET/POST/PUT etc.
            endpoint = parts[6]
            status_code = parts[8]
            message = line.split('"')[-1].strip()

            # Count requests per IP
            ip_requests[ip] += 1

            # Count endpoint accesses
            if request in {"GET", "POST"}:
                endpoint_access[endpoint] += 1

            # Detect failed logins (status code 401 or "Invalid credentials" message)
            if status_code == "401" or "Invalid credentials" in message:
                failed_logins[ip] += 1

    return ip_requests, endpoint_access, failed_logins


def write_to_csv(ip_requests, most_accessed, failed_logins):
    """Write analysis results to a CSV file."""
    with open(OUTPUT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write Requests per IP
        writer.writerow(["IP Address", "Request Count"])
        for ip, count in ip_requests.items():
            writer.writerow([ip, count])

        writer.writerow([])

        # Write Most Accessed Endpoint
        writer.writerow(["Most Accessed Endpoint", "Access Count"])
        writer.writerow([most_accessed[0], most_accessed[1]])

        writer.writerow([])

        # Write Suspicious Activity
        writer.writerow(["IP Address", "Failed Login Count"])
        for ip, count in failed_logins.items():
            if count > FAILED_LOGIN_THRESHOLD:
                writer.writerow([ip, count])


def main():
    # Parse log file
    ip_requests, endpoint_access, failed_logins = parse_log_file(LOG_FILE)

    # Get the most accessed endpoint
    most_accessed = endpoint_access.most_common(1)[0]

    # Print results
    print("\nRequests per IP Address:")
    for ip, count in ip_requests.items():
        print(f"{ip:<20} {count}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity Detected:")
    for ip, count in failed_logins.items():
        if count > FAILED_LOGIN_THRESHOLD:
            print(f"{ip:<20} {count}")

    # Write results to CSV
    write_to_csv(ip_requests, most_accessed, failed_logins)
    print(f"\nResults saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
