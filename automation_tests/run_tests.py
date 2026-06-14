# run_tests.py - Runner script to execute placeholder Appium and Selenium tests and generate an Excel report

import importlib
from pathlib import Path

# Import test case definitions
from test_cases import MOBILE_TESTS, WEB_TESTS

# Dynamically import the test modules (they expose functions named in the test case dicts)
test_mobile = importlib.import_module("test_mobile")
test_web = importlib.import_module("test_web")

# Import the report generator
from generate_report import write_report

def execute_tests():
    """Execute all mobile and web placeholder tests, collect results, and write an Excel report.
    Returns a list of result dictionaries.
    """
    results = []
    # Mobile tests
    for case in MOBILE_TESTS:
        func_name = case["function"]
        test_func = getattr(test_mobile, func_name)
        try:
            passed = test_func()
        except Exception as e:
            print(f"Mobile test {case['id']} raised an exception: {e}")
            passed = False
        results.append({
            "id": case["id"],
            "description": case["description"],
            "type": "mobile",
            "status": "Pass" if passed else "Fail",
        })
    # Web tests
    for case in WEB_TESTS:
        func_name = case["function"]
        test_func = getattr(test_web, func_name)
        try:
            passed = test_func()
        except Exception as e:
            print(f"Web test {case['id']} raised an exception: {e}")
            passed = False
        results.append({
            "id": case["id"],
            "description": case["description"],
            "type": "web",
            "status": "Pass" if passed else "Fail",
        })
    return results

if __name__ == "__main__":
    all_results = execute_tests()
    # Write the Excel report to the automation_tests directory
    report_path = Path(__file__).parent / "test_report.xlsx"
    write_report(all_results, output_file=report_path)
    print("Unified test execution completed.")
