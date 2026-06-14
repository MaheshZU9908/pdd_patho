# test_cases_100.py
# Complete 100 test cases for PathoAI Mobile Application (Android)
# Categories: Splash Screen, Login, Registration, Dashboard, Image Analysis, Patient Management, Settings, Edge Cases

TEST_CASES_APPIUM = [
    # ========== 1. SPLASH SCREEN (TC-001 to TC-010) ==========
    {
        "id": "TC-001",
        "category": "Splash Screen",
        "feature": "App Launch",
        "description": "Verify app launches successfully and displays the Splash screen",
        "steps": "1. Launch PathoAI mobile application\n2. Observe active activity name",
        "expected": "SplashActivity is launched and visible within 2 seconds",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-002",
        "category": "Splash Screen",
        "feature": "Logo Display",
        "description": "Verify app logo/branding is displayed correctly on Splash screen",
        "steps": "1. Launch app\n2. Inspect content view elements\n3. Verify logo visibility",
        "expected": "App logo drawable is visible and centered on splash screen",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-003",
        "category": "Splash Screen",
        "feature": "Transition Timing",
        "description": "Verify splash screen stays active for exactly 2 seconds",
        "steps": "1. Launch app and start timer\n2. Stop timer when LoginActivity starts",
        "expected": "Transition occurs after 2000ms delay (±200ms tolerance)",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-004",
        "category": "Splash Screen",
        "feature": "Auto-Navigation",
        "description": "Verify automatic transition from Splash to Login without user interaction",
        "steps": "1. Launch app\n2. Wait for 2.5 seconds without interaction",
        "expected": "LoginActivity automatically starts in foreground",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-005",
        "category": "Splash Screen",
        "feature": "Activity Stack",
        "description": "Verify SplashActivity is finished after transition",
        "steps": "1. Launch app\n2. Wait for splash screen transition\n3. Press back button",
        "expected": "Back button closes app (splash not in backstack)",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-006",
        "category": "Splash Screen",
        "feature": "Portrait Orientation",
        "description": "Verify splash screen displays correctly in portrait mode",
        "steps": "1. Ensure device is in portrait\n2. Launch app",
        "expected": "Splash screen elements are properly aligned in portrait",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-007",
        "category": "Splash Screen",
        "feature": "Landscape Orientation",
        "description": "Verify splash screen displays correctly in landscape mode",
        "steps": "1. Rotate device to landscape\n2. Launch app",
        "expected": "Splash screen elements are properly aligned in landscape",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-008",
        "category": "Splash Screen",
        "feature": "Screen Timeout",
        "description": "Verify splash screen timeout works even with screen off",
        "steps": "1. Launch app\n2. Immediately turn screen off",
        "expected": "App continues and shows login after screen is turned on",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-009",
        "category": "Splash Screen",
        "feature": "Network Status",
        "description": "Verify splash screen displays with no network connectivity",
        "steps": "1. Disable WiFi and Mobile data\n2. Launch app",
        "expected": "Splash screen displays and transitions normally",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "TC-010",
        "category": "Splash Screen",
        "feature": "App Version Display",
        "description": "Verify app version is displayed on splash screen",
        "steps": "1. Launch app\n2. Look for version text on splash",
        "expected": "Version number is visible on splash screen",
        "status": "PENDING",
        "priority": "LOW"
    },
    
    # ========== 2. LOGIN (TC-011 to TC-035) ==========
    {
        "id": "TC-011",
        "category": "Login",
        "feature": "Login Screen Load",
        "description": "Verify login screen loads successfully after splash",
        "steps": "1. Wait for splash transition\n2. Observe login screen",
        "expected": "Login activity displays with all UI elements",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-012",
        "category": "Login",
        "feature": "Email Field Presence",
        "description": "Verify email input field is present on login screen",
        "steps": "1. Go to login screen\n2. Look for email input field",
        "expected": "Email input field with placeholder is visible",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-013",
        "category": "Login",
        "feature": "Password Field Presence",
        "description": "Verify password input field is present on login screen",
        "steps": "1. Go to login screen\n2. Look for password input field",
        "expected": "Password input field with placeholder is visible",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-014",
        "category": "Login",
        "feature": "Login Button",
        "description": "Verify login button is present and clickable",
        "steps": "1. Go to login screen\n2. Look for login button",
        "expected": "Login button is visible and clickable",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-015",
        "category": "Login",
        "feature": "Valid Credentials",
        "description": "Verify login with valid email and password",
        "steps": "1. Enter valid email\n2. Enter valid password\n3. Click login",
        "expected": "User is logged in and navigated to dashboard",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-016",
        "category": "Login",
        "feature": "Invalid Email",
        "description": "Verify error message for invalid email format",
        "steps": "1. Enter invalid email format (e.g., 'notanemail')\n2. Click login",
        "expected": "Error message displays: 'Invalid email format'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-017",
        "category": "Login",
        "feature": "Empty Email",
        "description": "Verify error message when email field is empty",
        "steps": "1. Leave email empty\n2. Enter password\n3. Click login",
        "expected": "Error message displays: 'Email is required'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-018",
        "category": "Login",
        "feature": "Empty Password",
        "description": "Verify error message when password field is empty",
        "steps": "1. Enter email\n2. Leave password empty\n3. Click login",
        "expected": "Error message displays: 'Password is required'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-019",
        "category": "Login",
        "feature": "Wrong Password",
        "description": "Verify error message for incorrect password",
        "steps": "1. Enter valid email\n2. Enter wrong password\n3. Click login",
        "expected": "Error message displays: 'Invalid credentials'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-020",
        "category": "Login",
        "feature": "Non-existent User",
        "description": "Verify error message for non-existent user email",
        "steps": "1. Enter non-existent email\n2. Enter password\n3. Click login",
        "expected": "Error message displays: 'User not found'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-021",
        "category": "Login",
        "feature": "Password Visibility",
        "description": "Verify password visibility toggle button works",
        "steps": "1. Enter password\n2. Click visibility toggle",
        "expected": "Password characters become visible/hidden on toggle",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-022",
        "category": "Login",
        "feature": "Forget Password Link",
        "description": "Verify 'Forgot Password' link navigates to password reset",
        "steps": "1. Go to login screen\n2. Click 'Forgot Password' link",
        "expected": "Password reset screen is displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-023",
        "category": "Login",
        "feature": "Register Link",
        "description": "Verify 'Register' link navigates to registration screen",
        "steps": "1. Go to login screen\n2. Click 'Register' or 'Sign Up' link",
        "expected": "Registration screen is displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-024",
        "category": "Login",
        "feature": "Persistent Login",
        "description": "Verify remember me functionality persists login",
        "steps": "1. Check 'Remember me' checkbox\n2. Login successfully\n3. Restart app",
        "expected": "App remains logged in without re-entering credentials",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-025",
        "category": "Login",
        "feature": "Session Timeout",
        "description": "Verify session timeout after inactivity",
        "steps": "1. Login successfully\n2. Wait for 30 minutes of inactivity",
        "expected": "User is logged out and returned to login screen",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-026",
        "category": "Login",
        "feature": "Multiple Login Attempts",
        "description": "Verify account lock after 5 failed attempts",
        "steps": "1. Enter wrong password 5 times\n2. Attempt 6th login",
        "expected": "Account is temporarily locked with message",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-027",
        "category": "Login",
        "feature": "Email Case Insensitivity",
        "description": "Verify login works with different email cases",
        "steps": "1. Enter email in different cases (TEST@EMAIL.COM)\n2. Login",
        "expected": "Login succeeds regardless of email case",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-028",
        "category": "Login",
        "feature": "Whitespace Handling",
        "description": "Verify whitespace in email is trimmed",
        "steps": "1. Enter email with leading/trailing spaces\n2. Login",
        "expected": "Whitespace is trimmed and login succeeds",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-029",
        "category": "Login",
        "feature": "Network Error Handling",
        "description": "Verify error handling when network is unavailable",
        "steps": "1. Disable network\n2. Try to login",
        "expected": "Error message: 'Network connection failed'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-030",
        "category": "Login",
        "feature": "Server Timeout",
        "description": "Verify timeout error when server doesn't respond",
        "steps": "1. Try to login with slow network",
        "expected": "Timeout error after 30 seconds with retry option",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-031",
        "category": "Login",
        "feature": "MFA - OTP Display",
        "description": "Verify OTP input screen displays after valid login",
        "steps": "1. Login with valid credentials\n2. If MFA enabled, check OTP input",
        "expected": "OTP input field is displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-032",
        "category": "Login",
        "feature": "MFA - Valid OTP",
        "description": "Verify successful login with correct OTP",
        "steps": "1. Login and get OTP\n2. Enter valid OTP\n3. Click verify",
        "expected": "User is logged in and navigated to dashboard",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-033",
        "category": "Login",
        "feature": "MFA - Invalid OTP",
        "description": "Verify error for invalid OTP",
        "steps": "1. Login and get OTP\n2. Enter invalid OTP\n3. Click verify",
        "expected": "Error message: 'Invalid OTP' with retry option",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-034",
        "category": "Login",
        "feature": "MFA - OTP Resend",
        "description": "Verify OTP resend functionality",
        "steps": "1. Click 'Resend OTP' link\n2. Check if new OTP is sent",
        "expected": "New OTP is sent and confirmed with message",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-035",
        "category": "Login",
        "feature": "Biometric Login",
        "description": "Verify biometric authentication (fingerprint/face)",
        "steps": "1. Enable biometric on device\n2. Setup biometric login\n3. Use biometric to login",
        "expected": "User is logged in with biometric authentication",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    
    # ========== 3. REGISTRATION (TC-036 to TC-055) ==========
    {
        "id": "TC-036",
        "category": "Registration",
        "feature": "Registration Screen Load",
        "description": "Verify registration screen loads successfully",
        "steps": "1. Click register link from login\n2. Observe registration screen",
        "expected": "Registration form with all fields is displayed",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-037",
        "category": "Registration",
        "feature": "Required Fields",
        "description": "Verify all required fields are marked",
        "steps": "1. Go to registration screen\n2. Identify required fields",
        "expected": "Name, Email, Password, Confirm Password marked as required",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-038",
        "category": "Registration",
        "feature": "Valid Registration",
        "description": "Verify successful registration with valid data",
        "steps": "1. Enter valid name, email, password\n2. Click register",
        "expected": "User account is created and redirected to login/dashboard",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-039",
        "category": "Registration",
        "feature": "Duplicate Email",
        "description": "Verify error when registering with existing email",
        "steps": "1. Enter email already in database\n2. Click register",
        "expected": "Error message: 'Email already registered'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-040",
        "category": "Registration",
        "feature": "Password Requirements",
        "description": "Verify password must meet requirements (8+ chars, uppercase, number)",
        "steps": "1. Enter weak password (e.g., 'abc')\n2. Click register",
        "expected": "Error message with password requirements",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-041",
        "category": "Registration",
        "feature": "Password Mismatch",
        "description": "Verify error when passwords don't match",
        "steps": "1. Enter different password and confirm password\n2. Click register",
        "expected": "Error message: 'Passwords do not match'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-042",
        "category": "Registration",
        "feature": "Invalid Email Format",
        "description": "Verify error for invalid email format",
        "steps": "1. Enter invalid email\n2. Click register",
        "expected": "Error message: 'Invalid email format'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-043",
        "category": "Registration",
        "feature": "Empty Fields",
        "description": "Verify error when required fields are empty",
        "steps": "1. Leave required fields empty\n2. Click register",
        "expected": "Error messages for all empty required fields",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-044",
        "category": "Registration",
        "feature": "Name Validation",
        "description": "Verify name accepts only alphabetic characters",
        "steps": "1. Enter name with special characters\n2. Click register",
        "expected": "Error or special characters are not accepted",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-045",
        "category": "Registration",
        "feature": "Terms and Conditions",
        "description": "Verify terms and conditions acceptance",
        "steps": "1. Try to register without accepting T&C\n2. Then accept T&C and register",
        "expected": "Error without acceptance, success with acceptance",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-046",
        "category": "Registration",
        "feature": "Email Verification",
        "description": "Verify email verification link sent after registration",
        "steps": "1. Register with valid data\n2. Check email for verification link",
        "expected": "Email with verification link is received",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-047",
        "category": "Registration",
        "feature": "Email Verification Click",
        "description": "Verify account is activated after email verification",
        "steps": "1. Receive verification email\n2. Click verification link",
        "expected": "Account is activated and user can login",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-048",
        "category": "Registration",
        "feature": "Resend Verification Email",
        "description": "Verify resend verification email functionality",
        "steps": "1. Don't verify email\n2. Click 'Resend verification email'",
        "expected": "New verification email is sent",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-049",
        "category": "Registration",
        "feature": "Login Link on Registration",
        "description": "Verify 'Already have account?' link goes to login",
        "steps": "1. Click 'Already have account?' on registration",
        "expected": "Login screen is displayed",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "TC-050",
        "category": "Registration",
        "feature": "Password Strength Indicator",
        "description": "Verify password strength indicator displays",
        "steps": "1. Enter different strength passwords\n2. Observe strength indicator",
        "expected": "Color-coded strength indicator updates as password changes",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-051",
        "category": "Registration",
        "feature": "Role Selection",
        "description": "Verify role selection during registration (if applicable)",
        "steps": "1. On registration form, select user role\n2. Complete registration",
        "expected": "Role is saved with user account",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-052",
        "category": "Registration",
        "feature": "Phone Number Validation",
        "description": "Verify phone number validation if required",
        "steps": "1. Enter invalid phone number\n2. Enter valid phone number",
        "expected": "Invalid format rejected, valid format accepted",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-053",
        "category": "Registration",
        "feature": "OTP Verification",
        "description": "Verify OTP-based email verification if enabled",
        "steps": "1. Register and receive OTP\n2. Enter OTP",
        "expected": "Email is verified and account activated",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-054",
        "category": "Registration",
        "feature": "Duplicate Account Prevention",
        "description": "Verify system prevents creating duplicate accounts",
        "steps": "1. Try registering twice with same email",
        "expected": "Second attempt is rejected with appropriate message",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-055",
        "category": "Registration",
        "feature": "Data Privacy Acknowledgment",
        "description": "Verify data privacy policy acknowledgment during registration",
        "steps": "1. Complete registration form\n2. Check privacy policy checkbox",
        "expected": "Privacy acknowledgment is recorded",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    
    # ========== 4. DASHBOARD (TC-056 to TC-070) ==========
    {
        "id": "TC-056",
        "category": "Dashboard",
        "feature": "Dashboard Load",
        "description": "Verify dashboard loads successfully after login",
        "steps": "1. Login with valid credentials\n2. Wait for dashboard to load",
        "expected": "Dashboard screen with all components is displayed",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-057",
        "category": "Dashboard",
        "feature": "User Profile Display",
        "description": "Verify user profile information displays on dashboard",
        "steps": "1. Login and open dashboard\n2. Check profile section",
        "expected": "User name and profile picture are displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-058",
        "category": "Dashboard",
        "feature": "Navigation Menu",
        "description": "Verify all navigation menu items are visible",
        "steps": "1. Open dashboard\n2. Check navigation menu",
        "expected": "Menu items: Home, Patients, Analysis, Settings are visible",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-059",
        "category": "Dashboard",
        "feature": "Recent Patients",
        "description": "Verify recent patients list displays on dashboard",
        "steps": "1. Login and open dashboard\n2. Check recent patients section",
        "expected": "List of recent patients is displayed with names and dates",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-060",
        "category": "Dashboard",
        "feature": "Dashboard Statistics",
        "description": "Verify dashboard statistics cards (total patients, analysis, etc)",
        "steps": "1. Open dashboard\n2. Check statistics cards",
        "expected": "Statistics cards show accurate counts",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-061",
        "category": "Dashboard",
        "feature": "Logout Button",
        "description": "Verify logout button is present and functional",
        "steps": "1. Open dashboard\n2. Find logout button\n3. Click logout",
        "expected": "User is logged out and returned to login screen",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-062",
        "category": "Dashboard",
        "feature": "Quick Action Buttons",
        "description": "Verify quick action buttons (New Patient, Upload Image, etc)",
        "steps": "1. Open dashboard\n2. Check quick action buttons",
        "expected": "Quick action buttons are visible and clickable",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-063",
        "category": "Dashboard",
        "feature": "Search Patients",
        "description": "Verify search functionality for patients on dashboard",
        "steps": "1. Open dashboard\n2. Use search field to find patient",
        "expected": "Patient search returns matching results",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-064",
        "category": "Dashboard",
        "feature": "Notifications Badge",
        "description": "Verify notification badge displays unread notifications",
        "steps": "1. Open dashboard\n2. Check notification icon",
        "expected": "Notification badge shows unread count",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-065",
        "category": "Dashboard",
        "feature": "Refresh Dashboard",
        "description": "Verify pull-to-refresh functionality on dashboard",
        "steps": "1. Open dashboard\n2. Pull down to refresh",
        "expected": "Dashboard data is refreshed",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-066",
        "category": "Dashboard",
        "feature": "Empty State",
        "description": "Verify empty state message when no patients exist",
        "steps": "1. Login with new account\n2. Open dashboard",
        "expected": "Empty state message and suggestion to add first patient",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "TC-067",
        "category": "Dashboard",
        "feature": "Dark Mode",
        "description": "Verify dark mode displays on dashboard if enabled",
        "steps": "1. Enable dark mode in settings\n2. Open dashboard",
        "expected": "Dashboard displays in dark mode theme",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "TC-068",
        "category": "Dashboard",
        "feature": "Responsive Layout",
        "description": "Verify dashboard layout is responsive to screen size",
        "steps": "1. Open dashboard\n2. Rotate device orientation",
        "expected": "Layout adapts properly to portrait and landscape",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-069",
        "category": "Dashboard",
        "feature": "Loading State",
        "description": "Verify loading skeleton displays while data loads",
        "steps": "1. Open dashboard with slow network\n2. Observe loading state",
        "expected": "Loading skeleton is displayed until data loads",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "TC-070",
        "category": "Dashboard",
        "feature": "Error State",
        "description": "Verify error state displays when data fails to load",
        "steps": "1. Open dashboard\n2. Simulate network error\n3. Retry loading",
        "expected": "Error message displays with retry option",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    
    # ========== 5. IMAGE ANALYSIS (TC-071 to TC-085) ==========
    {
        "id": "TC-071",
        "category": "Image Analysis",
        "feature": "Upload Image",
        "description": "Verify image upload from device gallery",
        "steps": "1. Click upload image button\n2. Select image from gallery",
        "expected": "Image is uploaded and preview is displayed",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-072",
        "category": "Image Analysis",
        "feature": "Camera Capture",
        "description": "Verify image capture directly from camera",
        "steps": "1. Click camera button\n2. Take a photo\n3. Confirm capture",
        "expected": "Image is captured and preview is displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-073",
        "category": "Image Analysis",
        "feature": "Multiple Image Upload",
        "description": "Verify uploading multiple images for batch analysis",
        "steps": "1. Select multiple image upload option\n2. Choose multiple images",
        "expected": "Multiple images are uploaded and listed",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-074",
        "category": "Image Analysis",
        "feature": "Supported Formats",
        "description": "Verify only supported image formats are accepted",
        "steps": "1. Try to upload unsupported format (e.g., .pdf)\n2. Upload supported format (e.g., .jpg)",
        "expected": "Unsupported format rejected, supported format accepted",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-075",
        "category": "Image Analysis",
        "feature": "Image Size Validation",
        "description": "Verify image size limits are enforced",
        "steps": "1. Try uploading image > 10MB\n2. Upload image < 10MB",
        "expected": "Large image rejected with error, valid size accepted",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-076",
        "category": "Image Analysis",
        "feature": "Image Preview",
        "description": "Verify image preview displays correctly",
        "steps": "1. Upload image\n2. Check preview",
        "expected": "Image preview is displayed with correct aspect ratio",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-077",
        "category": "Image Analysis",
        "feature": "Image Cropping",
        "description": "Verify image cropping/editing functionality",
        "steps": "1. Upload image\n2. Click crop/edit button\n3. Adjust crop area",
        "expected": "Image can be cropped and edited",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-078",
        "category": "Image Analysis",
        "feature": "Rotation",
        "description": "Verify image rotation functionality",
        "steps": "1. Upload image\n2. Click rotate button",
        "expected": "Image is rotated by 90 degrees",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-079",
        "category": "Image Analysis",
        "feature": "Analysis Start",
        "description": "Verify analysis starts after submitting image",
        "steps": "1. Upload and prepare image\n2. Click 'Analyze' button",
        "expected": "Analysis begins with progress indicator",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-080",
        "category": "Image Analysis",
        "feature": "Analysis Progress",
        "description": "Verify analysis progress indicator displays",
        "steps": "1. Start image analysis\n2. Watch progress bar/indicator",
        "expected": "Progress bar shows analysis status (0-100%)",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-081",
        "category": "Image Analysis",
        "feature": "Analysis Results",
        "description": "Verify analysis results display correctly",
        "steps": "1. Complete image analysis\n2. Check results page",
        "expected": "Analysis results with predictions and confidence scores",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-082",
        "category": "Image Analysis",
        "feature": "Result Details",
        "description": "Verify detailed analysis results and recommendations",
        "steps": "1. View analysis results\n2. Check detailed information",
        "expected": "Detailed results with disease classification and recommendations",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-083",
        "category": "Image Analysis",
        "feature": "Result Export",
        "description": "Verify exporting analysis results as PDF/Image",
        "steps": "1. Get analysis results\n2. Click export button\n3. Choose format",
        "expected": "Results are exported in selected format",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-084",
        "category": "Image Analysis",
        "feature": "Result Share",
        "description": "Verify sharing analysis results with colleagues",
        "steps": "1. Get analysis results\n2. Click share button\n3. Select recipient",
        "expected": "Results are shared via email/link",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-085",
        "category": "Image Analysis",
        "feature": "Save to Patient",
        "description": "Verify saving analysis result to patient record",
        "steps": "1. Complete analysis\n2. Click 'Save to Patient' button",
        "expected": "Result is saved to patient's medical record",
        "status": "PENDING",
        "priority": "HIGH"
    },
    
    # ========== 6. PATIENT MANAGEMENT (TC-086 to TC-095) ==========
    {
        "id": "TC-086",
        "category": "Patient Management",
        "feature": "Add New Patient",
        "description": "Verify adding new patient record",
        "steps": "1. Click 'Add Patient' button\n2. Fill patient details\n3. Submit",
        "expected": "New patient is added to the system",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "TC-087",
        "category": "Patient Management",
        "feature": "Edit Patient",
        "description": "Verify editing existing patient information",
        "steps": "1. Select patient\n2. Click edit button\n3. Update details\n4. Save",
        "expected": "Patient information is updated",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-088",
        "category": "Patient Management",
        "feature": "Delete Patient",
        "description": "Verify deleting patient record",
        "steps": "1. Select patient\n2. Click delete button\n3. Confirm deletion",
        "expected": "Patient record is deleted",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-089",
        "category": "Patient Management",
        "feature": "Patient History",
        "description": "Verify viewing patient analysis history",
        "steps": "1. Open patient record\n2. Check history/results tab",
        "expected": "Patient's previous analysis results are displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-090",
        "category": "Patient Management",
        "feature": "Duplicate Prevention",
        "description": "Verify system prevents duplicate patient entries",
        "steps": "1. Create patient with ID\n2. Try creating patient with same ID",
        "expected": "Duplicate patient is prevented with error message",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-091",
        "category": "Patient Management",
        "feature": "Required Fields",
        "description": "Verify required fields for patient creation",
        "steps": "1. Try creating patient without required fields",
        "expected": "Error message for missing required fields",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-092",
        "category": "Patient Management",
        "feature": "Patient Search",
        "description": "Verify searching patients by name/ID",
        "steps": "1. Go to patient list\n2. Search for patient",
        "expected": "Search returns matching patient records",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "TC-093",
        "category": "Patient Management",
        "feature": "Patient Sorting",
        "description": "Verify sorting patients by name/date/ID",
        "steps": "1. Go to patient list\n2. Click sort option",
        "expected": "Patients are sorted by selected criteria",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-094",
        "category": "Patient Management",
        "feature": "Patient Filtering",
        "description": "Verify filtering patients by status/date",
        "steps": "1. Use filter options\n2. Select filter criteria",
        "expected": "Patient list is filtered by selected criteria",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-095",
        "category": "Patient Management",
        "feature": "Export Patient Data",
        "description": "Verify exporting patient data",
        "steps": "1. Go to patient list\n2. Click export button",
        "expected": "Patient data is exported as CSV/Excel",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    
    # ========== 7. SETTINGS (TC-096 to TC-100) ==========
    {
        "id": "TC-096",
        "category": "Settings",
        "feature": "Settings Screen",
        "description": "Verify settings screen loads successfully",
        "steps": "1. Go to dashboard\n2. Click settings",
        "expected": "Settings screen is displayed with all options",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-097",
        "category": "Settings",
        "feature": "Theme Settings",
        "description": "Verify dark/light theme toggle",
        "steps": "1. Go to settings\n2. Toggle theme setting",
        "expected": "App theme changes between light and dark",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "TC-098",
        "category": "Settings",
        "feature": "Notification Settings",
        "description": "Verify notification preferences can be configured",
        "steps": "1. Go to settings\n2. Configure notification options",
        "expected": "Notification preferences are saved",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-099",
        "category": "Settings",
        "feature": "Privacy Settings",
        "description": "Verify privacy settings and permissions",
        "steps": "1. Go to settings\n2. Check privacy options",
        "expected": "Privacy settings can be configured",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "TC-100",
        "category": "Settings",
        "feature": "About App",
        "description": "Verify app version and information",
        "steps": "1. Go to settings\n2. Click about",
        "expected": "App version and build info is displayed",
        "status": "PENDING",
        "priority": "LOW"
    }
]
