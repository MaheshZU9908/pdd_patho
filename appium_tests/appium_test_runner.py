# appium_test_runner.py
# Appium Test Runner - Executes all 100 test cases for PathoAI Mobile App (Android)

import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium_tests.test_cases_100 import TEST_CASES_APPIUM
from appium_tests.generate_appium_excel_report import AppiumExcelReportGenerator
import json
import openpyxl
from datetime import datetime
import os

class AppiumTestRunner:
    def __init__(self, app_path=None, device_id=None):
        self.app_path = app_path or "path/to/PathoAI.apk"
        self.device_id = device_id
        self.driver = None
        self.test_results = []
        self.passed_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        
    def setup_appium_connection(self):
        """Initialize Appium driver for Android"""
        try:
            options = UiAutomator2Options()
            options.platform_name = "Android"
            options.device_name = "emulator-5554" if not self.device_id else self.device_id
            options.app = self.app_path
            options.app_package = "com.pathoai"
            options.app_activity = "com.pathoai.SplashActivity"
            options.automation_name = "UiAutomator2"
            options.full_reset = False
            options.no_reset = True
            
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
            print("✓ Appium driver initialized successfully")
            return True
        except Exception as e:
            print(f"✗ Failed to initialize Appium driver: {str(e)}")
            return False
    
    def close_driver(self):
        """Close Appium driver"""
        if self.driver:
            self.driver.quit()
            print("✓ Appium driver closed")
    
    # ========== TEST CASES IMPLEMENTATION ==========
    
    def test_TC_001_splash_screen_load(self):
        """TC-001: Verify app launches and displays splash screen"""
        try:
            wait = WebDriverWait(self.driver, 5)
            splash_element = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/splash_view")))
            return splash_element is not None
        except Exception as e:
            print(f"TC-001 Error: {str(e)}")
            return False
    
    def test_TC_002_logo_display(self):
        """TC-002: Verify logo is displayed on splash"""
        try:
            logo = self.driver.find_element(By.ID, "com.pathoai:id/app_logo")
            return logo.is_displayed()
        except Exception as e:
            print(f"TC-002 Error: {str(e)}")
            return False
    
    def test_TC_003_splash_transition_timing(self):
        """TC-003: Verify splash transition timing"""
        try:
            start_time = time.time()
            wait = WebDriverWait(self.driver, 5)
            wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/login_view")))
            elapsed_time = time.time() - start_time
            return 1.8 < elapsed_time < 2.5
        except Exception as e:
            print(f"TC-003 Error: {str(e)}")
            return False
    
    def test_TC_004_auto_navigation(self):
        """TC-004: Verify auto-navigation from splash to login"""
        try:
            wait = WebDriverWait(self.driver, 5)
            login_view = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/login_view")))
            return login_view is not None
        except Exception as e:
            print(f"TC-004 Error: {str(e)}")
            return False
    
    def test_TC_005_activity_stack(self):
        """TC-005: Verify splash activity is cleared from backstack"""
        try:
            self.driver.press_keycode(4)  # Back button
            time.sleep(0.5)
            activities = self.driver.get_activity()
            return activities is None or "SplashActivity" not in str(activities)
        except Exception as e:
            print(f"TC-005 Error: {str(e)}")
            return False
    
    def test_TC_011_login_form_load(self):
        """TC-011: Verify login form loads"""
        try:
            email_field = self.driver.find_element(By.ID, "com.pathoai:id/email_input")
            password_field = self.driver.find_element(By.ID, "com.pathoai:id/password_input")
            login_button = self.driver.find_element(By.ID, "com.pathoai:id/login_button")
            return email_field.is_displayed() and password_field.is_displayed() and login_button.is_displayed()
        except Exception as e:
            print(f"TC-011 Error: {str(e)}")
            return False
    
    def test_TC_015_valid_login(self):
        """TC-015: Verify login with valid credentials"""
        try:
            email_field = self.driver.find_element(By.ID, "com.pathoai:id/email_input")
            password_field = self.driver.find_element(By.ID, "com.pathoai:id/password_input")
            login_button = self.driver.find_element(By.ID, "com.pathoai:id/login_button")
            
            email_field.clear()
            email_field.send_keys("test@pathoai.com")
            password_field.clear()
            password_field.send_keys("TestPassword123!")
            login_button.click()
            
            wait = WebDriverWait(self.driver, 5)
            dashboard = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/dashboard_view")))
            return dashboard is not None
        except Exception as e:
            print(f"TC-015 Error: {str(e)}")
            return False
    
    def test_TC_016_invalid_email(self):
        """TC-016: Verify error for invalid email"""
        try:
            email_field = self.driver.find_element(By.ID, "com.pathoai:id/email_input")
            password_field = self.driver.find_element(By.ID, "com.pathoai:id/password_input")
            login_button = self.driver.find_element(By.ID, "com.pathoai:id/login_button")
            
            email_field.clear()
            email_field.send_keys("notanemail")
            password_field.clear()
            password_field.send_keys("TestPassword123!")
            login_button.click()
            
            wait = WebDriverWait(self.driver, 3)
            error_msg = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/error_message")))
            return "invalid email" in error_msg.text.lower()
        except Exception as e:
            print(f"TC-016 Error: {str(e)}")
            return False
    
    def test_TC_071_upload_image(self):
        """TC-071: Verify image upload"""
        try:
            upload_button = self.driver.find_element(By.ID, "com.pathoai:id/upload_button")
            upload_button.click()
            time.sleep(1)
            
            # Select image from gallery
            wait = WebDriverWait(self.driver, 5)
            gallery_image = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/gallery_image_1")))
            gallery_image.click()
            
            confirm_button = self.driver.find_element(By.ID, "com.pathoai:id/confirm_button")
            confirm_button.click()
            
            preview = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/image_preview")))
            return preview.is_displayed()
        except Exception as e:
            print(f"TC-071 Error: {str(e)}")
            return False
    
    def test_TC_079_analysis_start(self):
        """TC-079: Verify analysis starts"""
        try:
            analyze_button = self.driver.find_element(By.ID, "com.pathoai:id/analyze_button")
            analyze_button.click()
            
            wait = WebDriverWait(self.driver, 5)
            progress_indicator = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/progress_bar")))
            return progress_indicator.is_displayed()
        except Exception as e:
            print(f"TC-079 Error: {str(e)}")
            return False
    
    def test_TC_086_add_patient(self):
        """TC-086: Verify adding new patient"""
        try:
            add_patient_button = self.driver.find_element(By.ID, "com.pathoai:id/add_patient_button")
            add_patient_button.click()
            
            wait = WebDriverWait(self.driver, 5)
            name_field = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/patient_name")))
            email_field = self.driver.find_element(By.ID, "com.pathoai:id/patient_email")
            phone_field = self.driver.find_element(By.ID, "com.pathoai:id/patient_phone")
            save_button = self.driver.find_element(By.ID, "com.pathoai:id/save_button")
            
            name_field.send_keys("John Doe")
            email_field.send_keys("john@example.com")
            phone_field.send_keys("1234567890")
            save_button.click()
            
            success_msg = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/success_message")))
            return "Patient added" in success_msg.text
        except Exception as e:
            print(f"TC-086 Error: {str(e)}")
            return False
    
    def test_TC_061_logout(self):
        """TC-061: Verify logout"""
        try:
            settings_button = self.driver.find_element(By.ID, "com.pathoai:id/settings_button")
            settings_button.click()
            
            wait = WebDriverWait(self.driver, 3)
            logout_button = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/logout_button")))
            logout_button.click()
            
            login_view = wait.until(EC.presence_of_element_located((By.ID, "com.pathoai:id/login_view")))
            return login_view.is_displayed()
        except Exception as e:
            print(f"TC-061 Error: {str(e)}")
            return False
    
    def execute_test(self, test_id, test_func):
        """Execute a single test and record result"""
        try:
            result = test_func()
            status = "PASS" if result else "FAIL"
            error = None
        except Exception as e:
            status = "FAIL"
            result = False
            error = str(e)
        
        # Record result
        test_record = {
            "id": test_id,
            "status": status,
            "execution_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "error": error
        }
        self.test_results.append(test_record)
        
        if status == "PASS":
            self.passed_count += 1
            print(f"✓ {test_id}: PASSED")
        else:
            self.failed_count += 1
            print(f"✗ {test_id}: FAILED {f'- {error}' if error else ''}")
        
        return result
    
    def run_all_tests(self):
        """Run all test cases"""
        print("\n" + "="*80)
        print("PATHOAI MOBILE APP - APPIUM TEST EXECUTION")
        print("="*80 + "\n")
        
        if not self.setup_appium_connection():
            return False
        
        try:
            # Define test mapping (sample of key tests)
            test_mapping = {
                "TC-001": self.test_TC_001_splash_screen_load,
                "TC-002": self.test_TC_002_logo_display,
                "TC-003": self.test_TC_003_splash_transition_timing,
                "TC-004": self.test_TC_004_auto_navigation,
                "TC-005": self.test_TC_005_activity_stack,
                "TC-011": self.test_TC_011_login_form_load,
                "TC-015": self.test_TC_015_valid_login,
                "TC-016": self.test_TC_016_invalid_email,
                "TC-071": self.test_TC_071_upload_image,
                "TC-079": self.test_TC_079_analysis_start,
                "TC-086": self.test_TC_086_add_patient,
                "TC-061": self.test_TC_061_logout,
            }
            
            # Execute mapped tests
            for test_id, test_func in test_mapping.items():
                self.execute_test(test_id, test_func)
                time.sleep(1)
            
            # Mark remaining tests as pending
            for test_case in TEST_CASES_APPIUM:
                if test_case['id'] not in test_mapping:
                    self.skipped_count += 1
            
            # Generate report
            self.generate_report()
            
            # Print summary
            self.print_summary()
            
        finally:
            self.close_driver()
        
        return True
    
    def generate_report(self):
        """Generate Excel report with results"""
        # First generate template
        generator = AppiumExcelReportGenerator()
        report_path = generator.generate_report()
        
        # Update with actual test results
        workbook = openpyxl.load_workbook(report_path)
        sheet = workbook.active
        
        for i, result in enumerate(self.test_results, 2):
            sheet[f'H{i}'] = result['status']
            sheet[f'I{i}'] = result['execution_time']
            sheet[f'M{i}'] = result['error'] or ""
        
        workbook.save(report_path)
        print(f"\n✓ Detailed report saved: {report_path}")
    
    def print_summary(self):
        """Print test execution summary"""
        print("\n" + "="*80)
        print("TEST EXECUTION SUMMARY")
        print("="*80)
        print(f"Total Tests: {len(TEST_CASES_APPIUM)}")
        print(f"Passed: {self.passed_count}")
        print(f"Failed: {self.failed_count}")
        print(f"Skipped: {self.skipped_count}")
        print(f"Pass Rate: {(self.passed_count / (self.passed_count + self.failed_count) * 100):.2f}%" if (self.passed_count + self.failed_count) > 0 else "N/A")
        print("="*80 + "\n")

if __name__ == "__main__":
    # Configuration
    APP_PATH = "path/to/PathoAI.apk"
    DEVICE_ID = None  # Use default device, or specify "emulator-5554"
    
    runner = AppiumTestRunner(app_path=APP_PATH, device_id=DEVICE_ID)
    runner.run_all_tests()
