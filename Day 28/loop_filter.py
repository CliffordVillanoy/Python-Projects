# Show only modules with failed test cases
test_results = {
    "Login": {"passed": 10, "failed": 2},
    "Registration": {"passed": 12, "failed": 0},
    "Dashboard": {"passed": 15, "failed": 1},
}

for module, result in test_results.items():
    if result["failed"] > 0:
        print(f"Module: {module:<12} | Failed: {result['failed']} | Status: ⚠️ Attention Needed")
