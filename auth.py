# Hardcoded credentials - DO NOT DO THIS
ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

def login_user(username, password):
    if username == ADMIN_USER and password == ADMIN_PASS:
        return f"Welcome back, {username}!"
    else:
        return "Invalid credentials", 403