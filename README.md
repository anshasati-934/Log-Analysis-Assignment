# Log Analysis Tool

## Project Overview

This Python-based log analysis tool is designed to parse and analyze web server log files, providing insights into network traffic, endpoint usage, and potential security threats. The script processes log entries and generates detailed reports on IP address request patterns, most accessed endpoints, and suspicious login activities.

## Features

- **IP Address Request Tracking**
  - Counts the number of requests from each unique IP address
  - Sorts IP addresses by request volume
  - Helps identify potential high-traffic sources

- **Endpoint Analysis**
  - Tracks the most frequently accessed endpoints
  - Provides insights into user navigation patterns
  - Helps understand popular pages or services

- **Security Monitoring**
  - Detects and flags suspicious login attempts
  - Identifies IP addresses with multiple failed login attempts
  - Configurable threshold for flagging suspicious activity

## Prerequisites

- Python 3.x
- Standard Python libraries:
  - `re` (Regular Expressions)
  - `csv`
  - `collections`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Log-Analysis-Assignment.git
   cd Log-Analysis-Assignment
   ```

2. Ensure you have Python 3 installed:
   ```bash
   python3 --version
   ```

## Usage

1. Place your log file in the project directory (default: `sample.log`)
2. Run the script:
   ```bash
   python3 log_analysis.py
   ```

3. The script will generate two outputs:
   - Terminal output with detailed analysis
   - `log_analysis_results.csv` with structured data

### Configurable Parameters

- `failed_threshold`: Adjust the number of failed login attempts to trigger a suspicious activity flag (default: 10)
- `log_file`: Specify the path to your log file
- `output_file`: Customize the CSV output filename

## Output Explanation

### Terminal Output
- **Requests per IP Address**: Shows the number of requests from each IP
- **Most Frequently Accessed Endpoint**: Identifies the most visited URL
- **Suspicious Activity**: Lists IP addresses with excessive failed login attempts

### CSV File
The `log_analysis_results.csv` contains structured data with:
- IP Address and Request Count
- Most Accessed Endpoint
- Suspicious IP Addresses and Failed Login Counts

## Log Format Support

The script is designed to parse Apache/Nginx-style log files with the following format:
```
IP_ADDRESS - - [TIMESTAMP] "METHOD /ENDPOINT HTTP/VERSION" STATUS SIZE
```

## Customization

- Modify regular expressions in `parse_log_file()` to support different log formats
- Adjust `failed_threshold` to fine-tune security monitoring
- Add more sophisticated analysis methods as needed

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
