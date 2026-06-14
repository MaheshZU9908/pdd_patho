# selenium_test_runner.py
# Selenium Test Runner - Executes all 100 test cases for PathoAI Web Application

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from automation_tests.test_cases_selenium_100 import TEST_CASES_SELENIUM
from automation_tests.generate_selenium_excel_report import SeleniumExcelReportGenerator
import openpyxl
from datetime import datetime
import json
import os

class SeleniumTestRunner:
    def __init__(self, base_url="http://localhost:3000", browser="chrome"):
        self.base_url = base_url
        self.browser = browser
        self.driver = None
        self.test_results = []
        self.passed_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        self.wait = None
        
    def setup_driver(self):
        """Initialize Selenium WebDriver"""
        try:
            if self.browser == "chrome":
                options = webdriver.ChromeOptions()
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--start-maximized')
                self.driver = webdriver.Chrome(options=options)
            elif self.browser == "firefox":
                options = webdriver.FirefoxOptions()
                self.driver = webdriver.Firefox(options=options)
            else:
                self.driver = webdriver.Chrome()
            
            self.wait = WebDriverWait(self.driver, 10)
            print(f"✓ Selenium WebDriver initialized successfully ({self.browser})")
            return True
        except Exception as e:
            print(f"✗ Failed to initialize WebDriver: {str(e)}")
            return False
    
    def close_driver(self):
        """Close WebDriver"""
        if self.driver:
            self.driver.quit()
            print("✓ WebDriver closed")
    
    # ========== TEST CASES IMPLEMENTATION ==========
    
    def test_WEB_001_page_load(self):
        """WEB-001: Verify web app loads and displays splash"""
        try:
            self.driver.get(self.base_url)
            splash_element = self.wait.until(EC.presence_of_element_located((By.ID, "view-splash")))
            return splash_element is not None
        except Exception as e:
            print(f"WEB-001 Error: {str(e)}")
            return False
    
    def test_WEB_002_logo_display(self):
        """WEB-002: Verify logo displays"""
        try:
            logo = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "splash-logo")))
            return logo.is_displayed()
        except Exception as e:
            print(f"WEB-002 Error: {str(e)}")
            return False
    
    def test_WEB_003_tagline(self):
        """WEB-003: Verify tagline displays"""
        try:
            tagline = self.driver.find_element(By.CLASS_NAME, "splash-sub")
            return "Precision Pathology" in tagline.text
        except Exception as e:
            print(f"WEB-003 Error: {str(e)}")
            return False
    
    def test_WEB_005_auto_navigation(self):
        """WEB-005: Verify auto-transition to login"""
        try:
            start_time = time.time()
            self.wait.until(EC.presence_of_element_located((By.ID, "view-login")))
            elapsed_time = time.time() - start_time
            return elapsed_time < 5
        except Exception as e:
            print(f"WEB-005 Error: {str(e)}")
            return False
    
    def test_WEB_011_login_form(self):
        """WEB-011: Verify login form loads"""
        try:
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "loginBtn")
            return (email_field.is_displayed() and 
                   password_field.is_displayed() and 
                   login_button.is_displayed())
        except Exception as e:
            print(f"WEB-011 Error: {str(e)}")
            return False
    
    def test_WEB_015_valid_login(self):
        """WEB-015: Verify login with valid credentials"""
        try:
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "loginBtn")
            
            email_field.clear()
            email_field.send_keys("test@pathoai.com")
            password_field.clear()
            password_field.send_keys("TestPassword123!")
            login_button.click()
            
            dashboard = self.wait.until(EC.presence_of_element_located((By.ID, "dashboard")))
            return dashboard is not None
        except Exception as e:
            print(f"WEB-015 Error: {str(e)}")
            return False
    
    def test_WEB_016_invalid_email(self):
        """WEB-016: Verify error for invalid email"""
        try:
            email_field = self.wait.until(EC.presence_of_element_located((By.ID, "email")))
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "loginBtn")
            
            email_field.clear()
            email_field.send_keys("notanemail")
            password_field.clear()
            password_field.send_keys("TestPassword123!")
            login_button.click()
            
            error_msg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message")))
            return "invalid" in error_msg.text.lower()
        except Exception as e:
            print(f"WEB-016 Error: {str(e)}")
            return False
    
    def test_WEB_017_empty_email(self):
        """WEB-017: Verify error when email empty"""
        try:
            email_field = self.driver.find_element(By.ID, "email")
            password_field = self.driver.find_element(By.ID, "password")
            login_button = self.driver.find_element(By.ID, "loginBtn")
            
            email_field.clear()
            password_field.clear()
            password_field.send_keys("TestPassword123!")
            login_button.click()
            
            error_msg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message")))
            return "required" in error_msg.text.lower()
        except Exception as e:
            print(f"WEB-017 Error: {str(e)}")
            return False
    
    def test_WEB_041_registration_form(self):
        """WEB-041: Verify registration form loads"""
        try:
            register_link = self.driver.find_element(By.ID, "registerLink")
            register_link.click()
            
            name_field = self.wait.until(EC.presence_of_element_located((By.ID, "fullName")))
            email_field = self.driver.find_element(By.ID, "regEmail")
            password_field = self.driver.find_element(By.ID, "regPassword")
            
            return (name_field.is_displayed() and 
                   email_field.is_displayed() and 
                   password_field.is_displayed())
        except Exception as e:
            print(f"WEB-041 Error: {str(e)}")
            return False
    
    def test_WEB_043_valid_registration(self):
        """WEB-043: Verify successful registration"""
        try:
            name_field = self.wait.until(EC.presence_of_element_located((By.ID, "fullName")))
            email_field = self.driver.find_element(By.ID, "regEmail")
            password_field = self.driver.find_element(By.ID, "regPassword")
            confirm_password = self.driver.find_element(By.ID, "confirmPassword")
            register_btn = self.driver.find_element(By.ID, "registerBtn")
            
            name_field.send_keys("John Doe")
            email_field.send_keys(f"user{int(time.time())}@test.com")
            password_field.send_keys("TestPassword123!")
            confirm_password.send_keys("TestPassword123!")
            register_btn.click()
            
            success_msg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success-message")))
            return "success" in success_msg.text.lower()
        except Exception as e:
            print(f"WEB-043 Error: {str(e)}")
            return False
    
    def test_WEB_066_dashboard_load(self):
        """WEB-066: Verify dashboard loads"""
        try:
            dashboard = self.wait.until(EC.presence_of_element_located((By.ID, "dashboard")))
            return dashboard.is_displayed()
        except Exception as e:
            print(f"WEB-066 Error: {str(e)}")
            return False
    
    def test_WEB_067_user_profile(self):
        """WEB-067: Verify user profile displays"""
        try:
            profile_section = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-profile")))
            return profile_section.is_displayed()
        except Exception as e:
            print(f"WEB-067 Error: {str(e)}")
            return False
    
    def test_WEB_068_navigation_menu(self):
        """WEB-068: Verify navigation menu"""
        try:
            menu = self.wait.until(EC.presence_of_element_located((By.ID, "navigationMenu")))
            menu_items = menu.find_elements(By.TAG_NAME, "li")
            return len(menu_items) > 0
        except Exception as e:
            print(f"WEB-068 Error: {str(e)}")
            return False
    
    def test_WEB_071_logout(self):
        """WEB-071: Verify logout"""
        try:
            logout_button = self.wait.until(EC.presence_of_element_located((By.ID, "logoutBtn")))
            logout_button.click()
            
            login_view = self.wait.until(EC.presence_of_element_located((By.ID, "view-login")))
            return login_view is not None
        except Exception as e:
            print(f"WEB-071 Error: {str(e)}")
            return False
    
    def test_WEB_081_upload_image(self):
        """WEB-081: Verify image upload"""
        try:
            upload_zone = self.wait.until(EC.presence_of_element_located((By.ID, "uploadZone")))
            file_input = self.driver.find_element(By.ID, "imageInput")
            
            # Simulate file upload
            test_image_path = "/path/to/test/image.jpg"
            file_input.send_keys(test_image_path)
            
            preview = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "image-preview")))
            return preview.is_displayed()
        except Exception as e:
            print(f"WEB-081 Error: {str(e)}")
            return False
    
    def test_WEB_088_analyze_button(self):
        """WEB-088: Verify analyze button"""
        try:
            analyze_btn = self.wait.until(EC.presence_of_element_located((By.ID, "analyzeBtn")))
            return analyze_btn.is_enabled()
        except Exception as e:
            print(f"WEB-088 Error: {str(e)}")
            return False
    
    def test_WEB_096_add_patient(self):
        """WEB-096: Verify add patient"""
        try:
            add_patient_btn = self.wait.until(EC.presence_of_element_located((By.ID, "addPatientBtn")))
            add_patient_btn.click()
            
            name_field = self.wait.until(EC.presence_of_element_located((By.ID, "patientName")))
            email_field = self.driver.find_element(By.ID, "patientEmail")
            save_btn = self.driver.find_element(By.ID, "savePatientBtn")
            
            name_field.send_keys("Jane Doe")
            email_field.send_keys("jane@example.com")
            save_btn.click()
            
            success = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success-message")))
            return "added" in success.text.lower()
        except Exception as e:
            print(f"WEB-096 Error: {str(e)}")
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
        print("PATHOAI WEB APPLICATION - SELENIUM TEST EXECUTION")
        print("="*80 + "\n")
        
        if not self.setup_driver():
            return False
        
        try:
            # Define test mapping (sample of key tests)
            test_mapping = {
                "WEB-001": self.test_WEB_001_page_load,
                "WEB-002": self.test_WEB_002_logo_display,
                "WEB-003": self.test_WEB_003_tagline,
                "WEB-005": self.test_WEB_005_auto_navigation,
                "WEB-011": self.test_WEB_011_login_form,
                "WEB-015": self.test_WEB_015_valid_login,
                "WEB-016": self.test_WEB_016_invalid_email,
                "WEB-017": self.test_WEB_017_empty_email,
                "WEB-041": self.test_WEB_041_registration_form,
                "WEB-043": self.test_WEB_043_valid_registration,
                "WEB-066": self.test_WEB_066_dashboard_load,
                "WEB-067": self.test_WEB_067_user_profile,
                "WEB-068": self.test_WEB_068_navigation_menu,
                "WEB-071": self.test_WEB_071_logout,
                "WEB-081": self.test_WEB_081_upload_image,
                "WEB-088": self.test_WEB_088_analyze_button,
                "WEB-096": self.test_WEB_096_add_patient,
            }
            
            # Execute mapped tests
            for test_id, test_func in test_mapping.items():
                self.execute_test(test_id, test_func)
                time.sleep(1)
            
            # Mark remaining tests as pending
            for test_case in TEST_CASES_SELENIUM:
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
        generator = SeleniumExcelReportGenerator()
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
        print(f"Total Tests: {len(TEST_CASES_SELENIUM)}")
        print(f"Passed: {self.passed_count}")
        print(f"Failed: {self.failed_count}")
        print(f"Skipped: {self.skipped_count}")
        print(f"Pass Rate: {(self.passed_count / (self.passed_count + self.failed_count) * 100):.2f}%" if (self.passed_count + self.failed_count) > 0 else "N/A")
        print("="*80 + "\n")

if __name__ == "__main__":
    # Configuration
    BASE_URL = "http://localhost:3000"
    BROWSER = "chrome"  # or "firefox"
    
    runner = SeleniumTestRunner(base_url=BASE_URL, browser=BROWSER)
    runner.run_all_tests()
