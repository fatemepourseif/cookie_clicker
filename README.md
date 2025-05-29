🍪 Cookie Clicker Bot – Selenium Automation

This project automates the Cookie Clicker experiment game using Python + Selenium.
It clicks the cookie as fast as possible and purchases the most expensive affordable upgrade every 5 seconds. After 5 minutes, it reports the cookies-per-second (CPS) rate and stops.

🚀 Features

Automatically clicks the cookie continuously
Every 5 seconds, checks your money and buys the best upgrade you can afford
Avoids purchasing locked or grayed-out upgrades
After 5 minutes, prints your Cookies per Second rate and stops

📦 Requirements

Python 3.7+
Google Chrome browser
ChromeDriver installed and in your system PATH

🧪 Install Dependencies

pip install selenium

📝 How to Run

Clone or copy this script
Make sure ChromeDriver is installed and matches your Chrome version
Run the Python script:
python main.py

🧠 How It Works

Uses Selenium to open the Cookie Clicker web game
Finds the cookie and all upgrade items
Continuously clicks the cookie
Every 5 seconds:
Gets current money
Collects available upgrade prices
Filters to only affordable upgrades
Picks the most expensive affordable one and clicks it
After 5 minutes, retrieves and prints your cookies-per-second rate and exits
