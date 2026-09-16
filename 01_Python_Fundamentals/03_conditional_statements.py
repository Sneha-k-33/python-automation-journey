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

# ============================================
# Step 4.10 - Split Text Using split()
# ============================================

email = "testing@gmail.com"

result = email.split("@")

print(result)
