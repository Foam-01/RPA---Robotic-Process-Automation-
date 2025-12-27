🤖 YouTube Automation Upload Bot (RPA)
An automated RPA tool designed to streamline the YouTube video upload process. Built with Python and PyAutoGUI to simulate human interactions, saving time and ensuring precision in scheduling.

🔧 Tech Stack
Language: Python 3.x

Library: PyAutoGUI (GUI Automation)

Environment: Windows OS

Browser: Google Chrome (Optimized for YouTube Studio)

🚀 Key Features
⚡ Lightning Fast Upload: Automated file selection and navigation.

📂 Smart Directory Access: Auto-types "Downloads" path to locate video files accurately.

⚙️ Detail Configuration: Automatically selects "Not made for kids" and skips through setup tabs.

🕒 Scheduled Publishing: Automated scheduling specifically set for 18:00 with text-clearing shortcuts (Ctrl+A).

🖥️ Workflow & Coordinates
The bot follows a precise 14-point coordinate system to navigate the UI:

1. Create Button ➔ 2. Upload Menu ➔ 3. Select File ➔ 4. Path Entry ➔ 5. Confirm Path ➔ 6. File Selection (Triple Click) ➔ 7. Audience Setting ➔ ... and more until Publish.

🏁 Getting Started
1. Prerequisites
Before running the bot, ensure your system is configured as follows:

Display Scaling: Set to 100%.

Keyboard Language: Set to English (US).

Browser Mode: Open YouTube Studio in Full Screen.

2. Installation
Bash

# Clone this repository
git clone https://github.com/Foam-01/RPA---Robotic-Process-Automation-.git

# Navigate to the project directory
cd RPA---Robotic-Process-Automation-

# Install required library
pip install pyautogui
3. Usage
Open Google Chrome and navigate to YouTube Studio.

Run the automation script:

Bash

python bot.py
You have 5 seconds to switch to the browser window before the bot starts.

🔗 Project Links
Repository: https://github.com/Foam-01/RPA---Robotic-Process-Automation-

👤 Author
Foam-01 - GitHub Profile
