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

phone_number = "98765435"

if len(phone_number) != 10:
    print("Phone number validation FAILED")
else:
    print("Phone number validation PASSED")













