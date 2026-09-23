# ==========================================
# MarinBytes - Sign In Test
# ==========================================

registered_email = "testuser@gmail.com"
registered_password = "Test@123"

entered_email = "testuser@gmail.com"
entered_password = "Test@123"

# ==========================================
# Login Validation
# ==========================================

if entered_email.strip() == "" and entered_password.strip() == "":
    print("Email and Password are required")

elif entered_email.strip() == "":
    print("Email is required")

elif entered_password.strip() == "":
    print("Password is required")

elif entered_email != registered_email and entered_password != registered_password:
    print("Invalid Email and Invalid Password")

elif entered_email != registered_email:
    print("Invalid Email")

elif entered_password != registered_password:
    print("Invalid Password")

else:
    print("Login Successful")

# ==========================================
# Logical Operators - Add and, or, and not
# ==========================================

email = "wrong@gmail.com"
password = "Test@123"

# AND - both conditions must be True
if email == registered_email and password == registered_password:
    print("Both Email and Password are correct")


# OR - at least one condition must be True
if email != registered_email or password != registered_password:
    print("Email or Password is incorrect")


# NOT - reverses the condition
if not email == "":
    print("Email field is not blank")


# ==========================================
# Comparison Operators
# ==========================================

age = 32

print(age == 32)   # Equal to
print(age != 30)   # Not equal to
print(age > 18)    # Greater than
print(age < 50)    # Less than
print(age >= 18)   # Greater than or equal to
print(age <= 32)   # Less than or equal to


# ==========================================
# QA Validation Examples
# ==========================================

# Password length validation
password = "Test@123"

if len(password) >= 8:
    print("Password length is valid")
else:
    print("Password must contain at least 8 characters")


# Phone number validation
phone_number = "9876543213"

if len(phone_number) == 10:
    print("Phone number is valid")
else:
    print("Phone number must contain 10 digits")


# Crew count validation
total_crew = 15

if total_crew > 0:
    print("Crew count is valid")
else:
    print("Crew count must be greater than 0")



# ==========================================
# Boundary Value Analysis - Password
# ==========================================

password = "Test1678"

if len(password) < 8:
    print("Password validation FAILED")
else:
    print("Password validation PASSED")

# ==========================================
# Boundary Value Analysis - Phone Number
# ==========================================

phone_number = "9876543789"

if len(phone_number) != 10:
    print("Phone number validation FAILED")
else:
    print("Phone number validation PASSED")


# ==========================================
# Boundary Value Analysis - Crew Count
# ==========================================

total_crew = 1

if total_crew <= 0:
    print("Crew count validation FAILED")
else:
    print("Crew count validation PASSED")


# ============================================
# Step 4 - Email String & Boundary Validation
# ============================================

# Email Length Validation
email = "test123@gmail.com"

if len(email) >= 10:
    print("Email length validation PASSED")
else:
    print("Email length validation FAILED")

# ============================================
# Step 4.2 - Leading / Trailing Spaces
# ============================================

email = "  sneha36@gmail.com  "

print("\nOriginal Email:", email)

clean_email = email.strip()

print("Clean Email   :", clean_email)


 # ============================================
# Step 4.3 - Missing @ Symbol
# ============================================

email = "sneha36gmail.com"

if "@" not in email:
    print("Invalid Email: @ symbol is missing")
else:
    print("Email contains @ symbol")

# ============================================
# Step 4.4 - Missing Domain
# ============================================

email = "sneha36@"

username, domain = email.split("@")

if domain == "":
    print("Invalid Email: Domain is missing")
else:
    print("Domain is present")


# ============================================
# Step 4.5 - Missing Username
# ============================================

email = "@gmail.com"

username, domain = email.split("@")

if username == "":
    print("Invalid Email: Username is missing")
else:
    print("Username is present")


# ============================================
# Step 4.6 - Multiple @ Symbols
# ============================================

email = "sneha@@gmail.com"

if email.count("@") != 1:
    print("Invalid Email: Email must contain exactly one @ symbol")
else:
    print("Email contains one @ symbol")

    # ============================================
# Step 4.7 - Missing Dot in Domain
# ============================================

email = "sneha@gmail"

if "." not in email.split("@")[1]:
    print("Invalid Email: Domain must contain a dot")
else:
    print("Valid domain format")


email = "sneha36gmail.com"

if "@" not in email:
    print("Invalid Email: @ symbol is missing")
else:
    print("Email contains @ symbol")


# ============================================
# Step 4.8 - Replace Text
# ============================================

status = "Test Failed"

updated_status = status.replace("Failed", "Passed")

print("Original Status:", status)
print("Updated Status:", updated_status)


# ============================================
# Step 4.9 -Understanding replace()
# ============================================

status = "Test Failed"

status.replace("Failed", "Passed")

print(status)

status = status.replace("Failed", "Passed")

print(status)

status ="Login Failed"
status.replace ("Failed", "Passed")
print(status)

status = status.replace ("Failed", "Passed")
print(status)

api_response = "API Test Failed" 
api_response = api_response.replace ("Failed", "Passed") 
print(api_response)

# Step 4.11 - Understanding split()
# ============================================

api_response = "Login,Success,200"
result = api_response.split(",")

print(result[0])
print(result[1])
print(result[2])

test_data = "Login| Sucess|200"
result = test_data.split("|")
print(result)

test_result = "Signup|Passed|201"
result = test_result.split("|")
print(result)
print(result[0])
print(result[1])
print(result[2])

test_data = "Registration|Passed|201"
result = test_data.split("|")
print(result)
print(result[0])
print(result[1])
print(result[2])

# Step 4.13 - split() with spaces
# ============================================

message = "Login Test Passed"

result = message.split()

print(result)
print(result[0])
print(result[1])
print(result[2])

# Step 4.13 Practice
# ============================================

test_message = "API Test Failed"

result = test_message.split()

print(result)
print(result[0])
print(result[1])
print(result[2])

# ============================================
# Step 4.14 - split() and variables
# ============================================

api_response = "Login,Passed,200"

result = api_response.split(",")

test_name = result[0]
status = result[1]
status_code = result[2]

print(test_name)
print(status)
print(status_code)

# ============================================
# Step 4.14 Practice
# ============================================

api_response = "Registration,Failed,400"

result = api_response.split(",")

test_name = result[0]
status = result[1]
status_code = result[2]

print(test_name)
print(status)
print(status_code)

# ============================================
# Step 4.15 - Unpacking split() result
# ============================================

api_response = "Registration,Failed,400"

test_name, status, status_code = api_response.split(",")

print(test_name)
print(status)
print(status_code)

# ============================================
# Step 4.15 Practice
# ============================================

api_response = "Login,Passed,200"

test_name, status, status_code = api_response.split(",")

print(test_name)
print(status)
print(status_code)

# ============================================
# Step 4.16 - len() with split()
# ============================================

api_response = "Login,Passed,200"

result = api_response.split(",")

print(result)
print(len(result))

# ============================================
# Step 4.16 Practice
# ============================================

api_response = "Registration,Passed,201"

result = api_response.split(",")

print(result)
print(len(result))

if len(result) == 3:
    print("Response format is valid")
else:
    print("Response format is invalid")

# ============================================
# Step 4.17 - Checking a Specific Value After split()
# ============================================

api_response = "Login,Passed,200"

result = api_response.split(",")

if result[1] == "Passed":
    print("Test Passed")
else:
    print("Test Failed")

# ============================================
# Step 4.17 Practice
# ============================================

api_response = "SignUp,Passed,201"

result = api_response.split(",")

if result[1] == "Passed":
    print("Sign Up Test Passed")
else:
    print("Sign Up Test Failed")

    
api_response = "registration,Failed,400"
result = api_response.split(",")
if result[1] == "Passed":
    print("Registration Test Passed")
else: print("Registration Test Failed")

4.18
api_response = "Login,Passed,200"
result = api_response.split(",")
if result[1] == "Passed" and result[2] == "200":
 print("Login API Test Passed")
else: print("Login API Test Failed")

api_response = "Registration,Passed,200"
result = api_response.split(",")
if result[1] == "Passed" and result[2] == "200":
    print("Registration API Test Passed")
else: print("Registration API Test Failed")

4.19
api_response = "Registration, Passed,400" 
result = api_response.split(",")
if result[1] == "Passed" and (result[2] == "499"):
 print("registration API Test Passed")
else: print("registartion API Test Failed")

4.20
api_response = "Login, Failed, 401"
result = api_response.split(",")
if not result[1] == "Passed":
    print("Login Test Failed")
else:
    print("Login Test Passed")

4.21
message = "Login Test Passed"
if "Passed" in message:
    print("Success Message Found")
else:
    print("success Message Not Found")

api_response = "Login test Passed Successfully"
if "Passed" in api_response:
    print("Expected result found")
else:
    print("Expected result not found")

    4.22

    message = "Login Test Passed"
    if "Failed" not in message:
        print("Failure message not found")
    else: 
        print("Failure message found")
print(message)
print("Failed" in message)
print("Failed" not in message)

api_response = "Login completed successfully"
if "Error" not in api_response:
    print("Login completed without error")
else: 
    print("Error found is login response") 

4.23
api_response = "Login, Passed, 200"
result = api_response.split(",")
if "Passed" in result:
    print("Passed status found")
else: print("Passed status not found")

api_response = "Registration, Passed, 400"
result = api_response.split(",")
if "Failed" in result:
 print("Failed status found")
else: 
  print("Failed status not found")

4.24
api_response = "Login, Passed, 200"
result = api_response.split(",")
if "Passed" in result:
    print("Test status found")
if "Failed" not in result:
    print("No failure status found")

4.25
status ="Passed"
status = status.lower()
print(status)

status = "PASSED"
if status.lower() =="passed":
    print("Test Passed")
else: print("Test Failed")

4.26
status = "Passed"
print(status.upper())


4.27
message = "API Test Passed"
print(message.startswith("API"))
print(message.endswith("Passed"))

4.28
test_cases = ["Login", "Registration", "Logout"]
for test in test_cases:
    print(test)

4.29
test_results = ["Passed", "Failed", "Passed"]
for result in test_results:
    if result == "Passed":
        print("Test Passed")
else: print("Test Failed")

4.30
for attempt in range(3):
    print("Login attempt", attempt + 1)

4.31
attempt = 1
while attempt <=3:
    print("Login attempt", attempt)
    attempt +=1

4.32
statuses = ["Passed", "Passed", "Failed", "Passed"]
for status in statuses:
    if status == "Failed":
        print("Failure Found")
        break

4.33
statuses = ["Passed", "Failed", "Passed"]
for status in statuses:
    if status =="Failed":
        continue
    print(status)

4.34
def login_test():
    print ("Login Test Exceuted")
login_test()

4.35
def check_status(status):

    if status == "Passed":
        print("Test Passed")
    else:
        print("Test Failed")

check_status("Passed")
check_status("Failed")

4.36
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)

print(result)


def check_status(status):
    return status == "Passed"

result = check_status("Passed")

print(result)

4.37
test_cases = ["Login", "Signup", "Logout"]
print(test_cases[0])
test_cases.append("Payment")
test_cases.remove("Logout")
print(len(test_cases))

# 4.38 - Dictionaries
user = {
    "name": "Sneha",
    "role": "QA",
    "status": "Active"
}

print(user["name"])
print(user["role"])


response = {
    "status": "Passed",
    "status_code": 200
}

if response["status_code"] == 200:
    print("API Passed")

# 4.39 - Dictionary Methods
response = {
    "status": "Passed",
    "status_code": 200
}

print(response.keys())
print(response.values())
if "status" in response:
    print("Status field exists")
            
# 4.40 -Tuples
status_codes = (200, 201, 400, 404, 500)

print(status_codes[0])

#4.41 — Sets
roles = {"QA", "Developer", "QA"}

print(roles)


  
 
