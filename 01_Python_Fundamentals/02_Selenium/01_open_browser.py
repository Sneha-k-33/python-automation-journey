from selenium import webdriver
import time

# ==============================
# Launch Browser
# ==============================

driver = webdriver.Chrome()

# ==============================
# Open MarinBytes
# ==============================

driver.get("https://dev.marinbytes.com/")

# ==============================
# Capture Actual Results
# ==============================

actual_title = driver.title
actual_url = driver.current_url

print("Page Title:", actual_title)
print("Current URL:", actual_url)

# ==============================
# Expected Results
# ==============================

expected_title = "Marine Bytes"
expected_url = "https://dev.marinbytes.com/"

# ==============================
# Validate Title
# ==============================

if actual_title == expected_title:
    print("Title Test Passed")
else:
    print("Title Test Failed")

# ==============================
# Validate URL
# ==============================

if actual_url == expected_url:
    print("URL Test Passed")
else:
    print("URL Test Failed")

# ==============================
# Keep Browser Open
# ==============================

time.sleep(10)

# ==============================
# Close Browser
# ==============================

driver.quit()

assert actual_title == expected_title

