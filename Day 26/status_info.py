# Filter and display only active users with formatted details
users = [
    {"name": "Alice", "role": "Admin", "active": True},
    {"name": "Bob", "role": "User", "active": False},
    {"name": "Clara", "role": "Moderator", "active": True},
]

for user in users:
    if user["active"]:
        print(f"{user['name']:<10} | Role: {user['role']:<10} | Status: ACTIVE")
