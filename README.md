# WhatsApp Message Automation

This script automates the process of sending WhatsApp messages to multiple recipients using the Selenium WebDriver. The recipients' phone numbers and the message content are read from external files.

## Requirements
Python 3.x
Google Chrome Browser
Chrome WebDriver (managed automatically by webdriver_manager)

## Dependencies
Install the required Python packages using the following command:

```
pip install selenium webdriver-manager
```

## Files

### message.txt: A text file containing the message to be sent.
### numbers.txt: A text file containing the phone numbers of the recipients, one per line.

## Usage

### Prepare the Message and Numbers Files:

Create a file named message.txt and write the message you want to send.
Create a file named numbers.txt and list the phone numbers of the recipients, one per line.

### Run the Script:

#### Execute the script using Python:

```
python main.py
```

### WhatsApp Web Login:

The script will open WhatsApp Web in a new browser window.
You have 30 seconds (login_time) to scan the QR code with your phone to log in.

### Message Sending:

The script will iterate through the phone numbers, open a chat with each number, and send the message.
Each message is sent with a delay of 5 seconds (new_msg_time and send_msg_time) between actions to ensure proper loading and sending.

## Script Explanation
### Imports and Setup:
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
```
### Timing and Country Code Configuration:
```
login_time = 30
new_msg_time = 5
send_msg_time = 5
country_code = 91
```
### WebDriver Initialization:
```
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```
### Read the Message:
```
with open('message.txt', 'r') as file:
    msg = file.read()
```
### Navigate to WhatsApp Web:
```
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)
```
### Read and Send Messages:
```
with open('numbers.txt', 'r') as file:
    for n in file.readlines():
        num = n.rstrip()
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        driver.get(link)
        time.sleep(new_msg_time)
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(send_msg_time)
```
### Close the Browser:
```
driver.quit()
```
## Notes
Ensure your message.txt and numbers.txt files are in the same directory as the script.
Adjust the login_time, new_msg_time, and send_msg_time variables if needed to accommodate different loading times or network speeds.
