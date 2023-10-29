import os
import shutil
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import upwork

username = os.getlogin()
# Specify the directories for the new profiles
profile_directories = [
    # f'C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\Default',
    "C:\\path\\to\\profile1\\directory"
    ]

# Specify the paths to the extensions (CRX files or directories)
extension_paths = [
    "adblocker.crx",
    "XBlocker 1.0.4",
    "XBlocker 1.0.4 - langpack"
]

# Install multiple extensions on each Chrome profile
def profiles(profile_directories, extension_paths):
    for profile_directory in profile_directories:
        driver = upwork.install_extensions_on_profile( profile_directory, extension_paths )
        # openTempMail(driver)
        email = upwork.openMinuteInBox(driver)
        # open Upwork
        upwork.openUpwork(driver, email)

# Call the function to create profiles and install the extensions
profiles(profile_directories, extension_paths)
