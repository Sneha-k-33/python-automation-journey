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





























