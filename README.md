Here’s a `README.md` file for your project:

---

# Log Analysis Script

## **Overview**

This project is a Python script for analyzing log files to extract key insights. It processes logs to identify:
- The number of requests per IP address.
- The most frequently accessed endpoint.
- Suspicious activity (e.g., brute force login attempts).

The script outputs the analysis results to the terminal and saves them in a CSV file for further review.

---

## **Features**

1. **Requests per IP Address**:
   - Counts and sorts the number of requests made by each IP address.

2. **Most Accessed Endpoint**:
   - Identifies the most frequently accessed resource (URL or endpoint).

3. **Suspicious Activity Detection**:
   - Flags IP addresses with failed login attempts exceeding a configurable threshold.

4. **Results Export**:
   - Saves the analysis results in a CSV file named `log_analysis_results.csv`.

---

## **Directory Structure**

```plaintext
log_analysis/
│
├── log_analysis.py          # Main Python script
├── sample.log               # Sample log file
└── log_analysis_results.csv # Output CSV file (generated after script execution)
```

---

## **Setup and Usage**

### Prerequisites
- Python 3.x installed on your system.
- A text editor or IDE for running the Python script.

### Steps to Run
1. **Clone or Download the Project**:
   - Save the files in a directory named `log_analysis`.

2. **Prepare the Log File**:
   - Use the provided log content in the `sample.log` file, or add your own logs in the same format.

3. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Execute the script:
     ```bash
     python log_analysis.py
     ```

4. **View the Output**:
   - The analysis results will be displayed in the terminal.
   - The results will also be saved in a CSV file named `log_analysis_results.csv`.

---

## **Sample Output**

### Terminal Output:
```plaintext
Requests per IP Address:
192.168.1.1          6
203.0.113.5          9
10.0.0.2             6

Most Frequently Accessed Endpoint:
/home (Accessed 6 times)

Suspicious Activity Detected:
203.0.113.5          7
192.168.1.100        5
```

### CSV File (`log_analysis_results.csv`):
```csv
IP Address	Request Count
192.168.1.1	7
203.0.113.5	8
10.0.0.2	6
198.51.100.23	8
192.168.1.100	5
Most Accessed Endpoint	Access Count
/login	13
IP Address	Failed Login Count
```

---

## **Configuration**

You can adjust the threshold for suspicious activity detection by modifying the `FAILED_LOGIN_THRESHOLD` variable in `log_analysis.py`:

```python
FAILED_LOGIN_THRESHOLD = 10
```

---

## **Log File Format**

The script expects log entries in the following format:
```
<IP Address> - - [<Timestamp>] "<Request Method> <Endpoint> <Protocol>" <Status Code> <Response Size> "<Optional Message>"
```

### Example:
```plaintext
192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
```

---

## **License**

This project is licensed under the MIT License. You are free to use, modify, and distribute it.

---

## **Author**

Developed by **Vaishnavi Ghodake** as part of a cybersecurity programming assessment.

---

Let me know if you need further changes or additions!
 
