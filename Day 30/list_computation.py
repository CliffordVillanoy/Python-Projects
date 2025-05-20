# Calculate and display pass rate of each test suite
test_suites = [
    {"name": "Smoke", "passed": 18, "total": 20},
    {"name": "Regression", "passed": 45, "total": 50},
    {"name": "Sanity", "passed": 10, "total": 10},
]

for suite in test_suites:
    pass_rate = (suite["passed"] / suite["total"]) * 100
    print(f"{suite['name']:<12} | Pass Rate: {pass_rate:.1f}%")
# Calculate and display the average pass rate of all test suites   
average_pass_rate = sum(
    (suite["passed"] / suite["total"]) * 100 for suite in test_suites
) / len(test_suites)
print(f"Average Pass Rate: {average_pass_rate:.1f}%")                       