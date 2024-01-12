# server_health_check
Server Health Check is a Python program designed to monitor the status of websites listed in website_monitor.json and maintain a detailed history log in status.txt.

Features
Website Status Check: Monitors the status of websites listed in website_monitor.json.
Status Logging: Keeps a detailed log of website status changes in status.txt.
Alerts: Generates alerts for different status scenarios, including a warning tone for website downtime.
Usage
Clone the Repository:

bash
Copy code
git clone https://github.com/123sachithra123/server_health_check.git
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Websites:
Modify the website_monitor.json file to add or remove websites for monitoring.

Run the Program:

bash
Copy code
python website_status_checker.py
Status Codes
Website Down:

Generates a warning tone.
Logs the status as "Web site down."
Warning:

Displays other status scenarios as warnings.
Logs the detailed status in status.txt.
Website Up:

Displays the message "Web site is up and running smoothly."
Logs the status as "Web site is up."
Configuration
Modify the website_monitor.json file to add or remove websites for monitoring.

License
This project is licensed under the MIT License - see the LICENSE file for details.

