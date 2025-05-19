# Show users whose last login exceeds a threshold (simulated days)
users = [
    {"name": "Alice", "last_login_days": 2},
    {"name": "Bob", "last_login_days": 10},
    {"name": "Clara", "last_login_days": 1},
]

threshold = 5
for user in users:
    if user["last_login_days"] > threshold:
        print(f"User: {user['name']:<8} | Last Login: {user['last_login_days']} days ago ⏰")
# Show users whose last login is within the threshold
for user in users:
    if user["last_login_days"] <= threshold:
        print(f"User: {user['name']:<8} | Last Login: {user['last_login_days']} days ago ✅")   