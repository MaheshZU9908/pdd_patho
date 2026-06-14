# test_cases_selenium_100.py
# Complete 100 test cases for PathoAI Web Application
# Categories: Splash Screen, Login, Registration, Dashboard, Image Analysis, Patient Management, Settings, API Integration, Security, Edge Cases

TEST_CASES_SELENIUM = [
    # ========== 1. SPLASH SCREEN (WEB-001 to WEB-010) ==========
    {
        "id": "WEB-001",
        "category": "Splash Screen",
        "feature": "Page Load",
        "description": "Verify web app loads and displays splash screen",
        "steps": "1. Open browser at web URL\n2. Observe splash screen",
        "expected": "Splash screen displays with logo and loading indicator",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-002",
        "category": "Splash Screen",
        "feature": "Logo Display",
        "description": "Verify logo/branding is visible on splash",
        "steps": "1. Load page\n2. Check for logo element",
        "expected": "Logo is visible and properly centered",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-003",
        "category": "Splash Screen",
        "feature": "Tagline Display",
        "description": "Verify tagline displays on splash",
        "steps": "1. Load page\n2. Check tagline text",
        "expected": "Tagline 'Precision Pathology & Deep MIL Intelligence' is visible",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-004",
        "category": "Splash Screen",
        "feature": "Loading Animation",
        "description": "Verify loading animation displays",
        "steps": "1. Load page\n2. Observe loading animation",
        "expected": "Animated loader is displayed during page load",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-005",
        "category": "Splash Screen",
        "feature": "Auto-Navigation",
        "description": "Verify splash auto-transitions to login after 3 seconds",
        "steps": "1. Load page\n2. Wait for navigation",
        "expected": "Page transitions to login view after 3 seconds",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-006",
        "category": "Splash Screen",
        "feature": "Responsive Design",
        "description": "Verify splash screen is responsive on different screen sizes",
        "steps": "1. Load page\n2. Resize browser window",
        "expected": "Splash screen remains centered on all screen sizes",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-007",
        "category": "Splash Screen",
        "feature": "Browser Compatibility",
        "description": "Verify splash works on different browsers (Chrome, Firefox, Safari)",
        "steps": "1. Load page on different browsers",
        "expected": "Splash screen displays correctly on all browsers",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-008",
        "category": "Splash Screen",
        "feature": "Mobile Viewport",
        "description": "Verify splash is optimized for mobile viewport",
        "steps": "1. Open page on mobile device/emulator",
        "expected": "Splash screen displays optimally on mobile screens",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-009",
        "category": "Splash Screen",
        "feature": "Network Error Handling",
        "description": "Verify splash handles network errors gracefully",
        "steps": "1. Simulate network error\n2. Load page",
        "expected": "Error message displays with retry option",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-010",
        "category": "Splash Screen",
        "feature": "Skip Splash Option",
        "description": "Verify skip button on splash (if available)",
        "steps": "1. Load page\n2. Click skip button",
        "expected": "Login page loads immediately",
        "status": "PENDING",
        "priority": "LOW"
    },
    
    # ========== 2. LOGIN (WEB-011 to WEB-040) ==========
    {
        "id": "WEB-011",
        "category": "Login",
        "feature": "Login Form Load",
        "description": "Verify login form loads successfully",
        "steps": "1. Navigate to login page\n2. Observe form elements",
        "expected": "Login form with email and password fields displays",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-012",
        "category": "Login",
        "feature": "Email Field",
        "description": "Verify email input field is present and functional",
        "steps": "1. Go to login\n2. Click email field",
        "expected": "Email field is focused and accepts input",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-013",
        "category": "Login",
        "feature": "Password Field",
        "description": "Verify password input field is present and functional",
        "steps": "1. Go to login\n2. Click password field",
        "expected": "Password field is focused and masks input",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-014",
        "category": "Login",
        "feature": "Login Button",
        "description": "Verify login button is present and clickable",
        "steps": "1. Go to login\n2. Observe login button",
        "expected": "Login button is visible and clickable",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-015",
        "category": "Login",
        "feature": "Valid Credentials",
        "description": "Verify successful login with valid credentials",
        "steps": "1. Enter valid email\n2. Enter valid password\n3. Click login",
        "expected": "User is logged in and dashboard displays",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-016",
        "category": "Login",
        "feature": "Invalid Email",
        "description": "Verify error for invalid email format",
        "steps": "1. Enter invalid email\n2. Click login",
        "expected": "Error: 'Please enter a valid email address'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-017",
        "category": "Login",
        "feature": "Empty Email",
        "description": "Verify error when email is empty",
        "steps": "1. Leave email empty\n2. Click login",
        "expected": "Error: 'Email is required'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-018",
        "category": "Login",
        "feature": "Empty Password",
        "description": "Verify error when password is empty",
        "steps": "1. Leave password empty\n2. Click login",
        "expected": "Error: 'Password is required'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-019",
        "category": "Login",
        "feature": "Wrong Password",
        "description": "Verify error for incorrect password",
        "steps": "1. Enter correct email and wrong password\n2. Click login",
        "expected": "Error: 'Invalid email or password'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-020",
        "category": "Login",
        "feature": "Non-existent User",
        "description": "Verify error for non-existent user",
        "steps": "1. Enter non-existent email\n2. Click login",
        "expected": "Error: 'Invalid email or password'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-021",
        "category": "Login",
        "feature": "Password Toggle Visibility",
        "description": "Verify password visibility toggle",
        "steps": "1. Enter password\n2. Click visibility toggle",
        "expected": "Password becomes visible/hidden on toggle",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-022",
        "category": "Login",
        "feature": "Forgot Password Link",
        "description": "Verify forgot password link navigates correctly",
        "steps": "1. Click 'Forgot Password' link",
        "expected": "Password reset page displays",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-023",
        "category": "Login",
        "feature": "Register Link",
        "description": "Verify register link navigates to registration",
        "steps": "1. Click 'Register' or 'Sign Up' link",
        "expected": "Registration page displays",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-024",
        "category": "Login",
        "feature": "Remember Me",
        "description": "Verify remember me checkbox functionality",
        "steps": "1. Check 'Remember me'\n2. Login\n3. Close and reopen browser",
        "expected": "User remains logged in after browser restart",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-025",
        "category": "Login",
        "feature": "Session Timeout",
        "description": "Verify user is logged out after inactivity",
        "steps": "1. Login\n2. Wait 30 minutes without activity",
        "expected": "User is logged out and returned to login",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-026",
        "category": "Login",
        "feature": "Failed Login Attempts",
        "description": "Verify account lock after 5 failed attempts",
        "steps": "1. Enter wrong password 5 times",
        "expected": "Account locked with message to try later",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-027",
        "category": "Login",
        "feature": "Email Case Insensitive",
        "description": "Verify login works with different email cases",
        "steps": "1. Enter email in uppercase\n2. Login",
        "expected": "Login succeeds regardless of case",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-028",
        "category": "Login",
        "feature": "Whitespace Trim",
        "description": "Verify whitespace in email is trimmed",
        "steps": "1. Enter email with spaces\n2. Login",
        "expected": "Whitespace is trimmed and login succeeds",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-029",
        "category": "Login",
        "feature": "Network Error",
        "description": "Verify error handling for network failure",
        "steps": "1. Disable network\n2. Try to login",
        "expected": "Error: 'Network connection failed'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-030",
        "category": "Login",
        "feature": "Server Timeout",
        "description": "Verify timeout error handling",
        "steps": "1. Try login with slow network",
        "expected": "Timeout error with retry option",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-031",
        "category": "Login",
        "feature": "SSL/HTTPS",
        "description": "Verify login works over HTTPS",
        "steps": "1. Load login page\n2. Check URL for HTTPS",
        "expected": "Page loads over HTTPS with valid certificate",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-032",
        "category": "Login",
        "feature": "SQL Injection Prevention",
        "description": "Verify SQL injection is prevented",
        "steps": "1. Enter SQL injection payload\n2. Try to login",
        "expected": "Input is sanitized and rejected or handled safely",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-033",
        "category": "Login",
        "feature": "XSS Prevention",
        "description": "Verify XSS attacks are prevented",
        "steps": "1. Enter XSS payload in email\n2. Try to login",
        "expected": "Payload is escaped and rendered as text",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-034",
        "category": "Login",
        "feature": "MFA - OTP",
        "description": "Verify OTP input after valid login",
        "steps": "1. Login with valid credentials\n2. Check for OTP input",
        "expected": "OTP input field displays if MFA is enabled",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-035",
        "category": "Login",
        "feature": "MFA - Valid OTP",
        "description": "Verify successful login with correct OTP",
        "steps": "1. Enter correct OTP",
        "expected": "User logged in and dashboard displays",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-036",
        "category": "Login",
        "feature": "MFA - Invalid OTP",
        "description": "Verify error for invalid OTP",
        "steps": "1. Enter invalid OTP",
        "expected": "Error: 'Invalid OTP' with retry option",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-037",
        "category": "Login",
        "feature": "MFA - Resend OTP",
        "description": "Verify OTP resend functionality",
        "steps": "1. Click 'Resend OTP'",
        "expected": "New OTP sent with confirmation message",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-038",
        "category": "Login",
        "feature": "Login Analytics",
        "description": "Verify login attempts are tracked",
        "steps": "1. Login\n2. Check admin analytics",
        "expected": "Login event is recorded in analytics",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "WEB-039",
        "category": "Login",
        "feature": "Social Login",
        "description": "Verify login via social accounts (Google/GitHub)",
        "steps": "1. Click social login button\n2. Authenticate",
        "expected": "User logged in with social account",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-040",
        "category": "Login",
        "feature": "Cookie Management",
        "description": "Verify session cookies are set correctly",
        "steps": "1. Login\n2. Check browser cookies",
        "expected": "Session cookie is set with HttpOnly and Secure flags",
        "status": "PENDING",
        "priority": "HIGH"
    },
    
    # ========== 3. REGISTRATION (WEB-041 to WEB-065) ==========
    {
        "id": "WEB-041",
        "category": "Registration",
        "feature": "Registration Form",
        "description": "Verify registration form loads successfully",
        "steps": "1. Navigate to registration page",
        "expected": "Registration form displays with all fields",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-042",
        "category": "Registration",
        "feature": "Form Fields",
        "description": "Verify all required fields are present",
        "steps": "1. Check registration form\n2. Identify all fields",
        "expected": "Name, Email, Password, Confirm Password fields present",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-043",
        "category": "Registration",
        "feature": "Valid Registration",
        "description": "Verify successful registration with valid data",
        "steps": "1. Fill all fields\n2. Click register",
        "expected": "Account created and confirmation message displays",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-044",
        "category": "Registration",
        "feature": "Duplicate Email",
        "description": "Verify error for duplicate email",
        "steps": "1. Register with existing email",
        "expected": "Error: 'Email already registered'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-045",
        "category": "Registration",
        "feature": "Password Requirements",
        "description": "Verify password meets requirements",
        "steps": "1. Enter weak password\n2. Try to register",
        "expected": "Error with password requirements",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-046",
        "category": "Registration",
        "feature": "Password Mismatch",
        "description": "Verify error for mismatched passwords",
        "steps": "1. Enter different passwords",
        "expected": "Error: 'Passwords do not match'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-047",
        "category": "Registration",
        "feature": "Invalid Email Format",
        "description": "Verify error for invalid email",
        "steps": "1. Enter invalid email",
        "expected": "Error: 'Invalid email format'",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-048",
        "category": "Registration",
        "feature": "Empty Fields",
        "description": "Verify error for empty required fields",
        "steps": "1. Leave required fields empty",
        "expected": "Error messages for all empty fields",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-049",
        "category": "Registration",
        "feature": "Name Validation",
        "description": "Verify name validation",
        "steps": "1. Enter name with special characters",
        "expected": "Special characters rejected or not accepted",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-050",
        "category": "Registration",
        "feature": "Terms & Conditions",
        "description": "Verify T&C acceptance requirement",
        "steps": "1. Try register without accepting T&C\n2. Then accept and register",
        "expected": "Error without acceptance, success with acceptance",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-051",
        "category": "Registration",
        "feature": "Email Verification",
        "description": "Verify email verification link sent",
        "steps": "1. Register\n2. Check email for verification link",
        "expected": "Verification email received",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-052",
        "category": "Registration",
        "feature": "Email Link Verification",
        "description": "Verify account activation via email link",
        "steps": "1. Click verification link",
        "expected": "Account activated with confirmation",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-053",
        "category": "Registration",
        "feature": "Resend Verification",
        "description": "Verify resend verification email",
        "steps": "1. Click 'Resend verification'",
        "expected": "New email sent",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-054",
        "category": "Registration",
        "feature": "Login Link",
        "description": "Verify login link from registration",
        "steps": "1. Click 'Already have account?'",
        "expected": "Login page displays",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "WEB-055",
        "category": "Registration",
        "feature": "Password Strength",
        "description": "Verify password strength indicator",
        "steps": "1. Type different passwords\n2. Observe indicator",
        "expected": "Indicator shows real-time strength",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-056",
        "category": "Registration",
        "feature": "Role Selection",
        "description": "Verify role selection during registration",
        "steps": "1. Select role (if applicable)",
        "expected": "Role is saved with account",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-057",
        "category": "Registration",
        "feature": "Phone Validation",
        "description": "Verify phone number validation",
        "steps": "1. Enter invalid phone\n2. Enter valid phone",
        "expected": "Invalid rejected, valid accepted",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-058",
        "category": "Registration",
        "feature": "OTP Verification",
        "description": "Verify OTP-based email verification",
        "steps": "1. Receive OTP\n2. Enter OTP",
        "expected": "Account verified",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-059",
        "category": "Registration",
        "feature": "Duplicate Prevention",
        "description": "Verify duplicate account prevention",
        "steps": "1. Register twice with same email",
        "expected": "Second attempt rejected",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-060",
        "category": "Registration",
        "feature": "Privacy Policy",
        "description": "Verify privacy policy acknowledgment",
        "steps": "1. Check privacy policy checkbox",
        "expected": "Privacy preference recorded",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-061",
        "category": "Registration",
        "feature": "CAPTCHA",
        "description": "Verify CAPTCHA verification",
        "steps": "1. Solve CAPTCHA\n2. Register",
        "expected": "CAPTCHA validation passes",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-062",
        "category": "Registration",
        "feature": "Form Validation",
        "description": "Verify client-side form validation",
        "steps": "1. Enter invalid data\n2. Check for errors",
        "expected": "Real-time validation errors display",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-063",
        "category": "Registration",
        "feature": "Success Message",
        "description": "Verify registration success message",
        "steps": "1. Complete registration",
        "expected": "Success message and next steps shown",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "WEB-064",
        "category": "Registration",
        "feature": "Account Recovery",
        "description": "Verify account recovery email sent",
        "steps": "1. Register\n2. Check for recovery email",
        "expected": "Recovery email with backup codes sent",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-065",
        "category": "Registration",
        "feature": "Data Privacy",
        "description": "Verify user data is encrypted",
        "steps": "1. Register\n2. Inspect network traffic",
        "expected": "Data transmitted over HTTPS",
        "status": "PENDING",
        "priority": "HIGH"
    },
    
    # ========== 4. DASHBOARD (WEB-066 to WEB-080) ==========
    {
        "id": "WEB-066",
        "category": "Dashboard",
        "feature": "Dashboard Load",
        "description": "Verify dashboard loads after login",
        "steps": "1. Login\n2. Wait for dashboard",
        "expected": "Dashboard displays with all components",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-067",
        "category": "Dashboard",
        "feature": "User Profile",
        "description": "Verify user profile displays",
        "steps": "1. Check profile section",
        "expected": "User name and photo displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-068",
        "category": "Dashboard",
        "feature": "Navigation Menu",
        "description": "Verify navigation menu items",
        "steps": "1. Check menu",
        "expected": "All menu items visible and clickable",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-069",
        "category": "Dashboard",
        "feature": "Recent Patients",
        "description": "Verify recent patients list",
        "steps": "1. Check recent patients\n2. Verify data",
        "expected": "Recent patients displayed with details",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-070",
        "category": "Dashboard",
        "feature": "Statistics Cards",
        "description": "Verify statistics cards display",
        "steps": "1. Check stats section",
        "expected": "Stats cards show accurate counts",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-071",
        "category": "Dashboard",
        "feature": "Logout",
        "description": "Verify logout functionality",
        "steps": "1. Click logout",
        "expected": "User logged out, redirected to login",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-072",
        "category": "Dashboard",
        "feature": "Quick Actions",
        "description": "Verify quick action buttons",
        "steps": "1. Check quick action buttons",
        "expected": "Buttons visible and clickable",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-073",
        "category": "Dashboard",
        "feature": "Search",
        "description": "Verify search functionality",
        "steps": "1. Use search\n2. Enter search term",
        "expected": "Results display for search term",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-074",
        "category": "Dashboard",
        "feature": "Notifications",
        "description": "Verify notifications badge",
        "steps": "1. Check notification badge",
        "expected": "Unread count displayed",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-075",
        "category": "Dashboard",
        "feature": "Responsive",
        "description": "Verify responsive design",
        "steps": "1. Resize window\n2. Check layout",
        "expected": "Layout adapts to screen size",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-076",
        "category": "Dashboard",
        "feature": "Dark Mode",
        "description": "Verify dark mode toggle",
        "steps": "1. Toggle dark mode",
        "expected": "Theme changes to dark",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "WEB-077",
        "category": "Dashboard",
        "feature": "Loading State",
        "description": "Verify loading skeleton",
        "steps": "1. Load dashboard slowly",
        "expected": "Skeleton loaders display",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "WEB-078",
        "category": "Dashboard",
        "feature": "Error State",
        "description": "Verify error handling",
        "steps": "1. Simulate network error",
        "expected": "Error message with retry shown",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-079",
        "category": "Dashboard",
        "feature": "Empty State",
        "description": "Verify empty state message",
        "steps": "1. New account, no data",
        "expected": "Empty state with suggestions",
        "status": "PENDING",
        "priority": "LOW"
    },
    {
        "id": "WEB-080",
        "category": "Dashboard",
        "feature": "Pagination",
        "description": "Verify pagination works",
        "steps": "1. Check pagination controls",
        "expected": "Page navigation works correctly",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    
    # ========== 5. IMAGE ANALYSIS (WEB-081 to WEB-095) ==========
    {
        "id": "WEB-081",
        "category": "Image Analysis",
        "feature": "Upload Image",
        "description": "Verify image upload functionality",
        "steps": "1. Click upload\n2. Select image",
        "expected": "Image uploaded and preview shown",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-082",
        "category": "Image Analysis",
        "feature": "Drag & Drop",
        "description": "Verify drag and drop upload",
        "steps": "1. Drag image to drop zone",
        "expected": "Image uploaded successfully",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-083",
        "category": "Image Analysis",
        "feature": "Multiple Upload",
        "description": "Verify multiple image upload",
        "steps": "1. Select multiple images",
        "expected": "All images uploaded",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-084",
        "category": "Image Analysis",
        "feature": "Supported Formats",
        "description": "Verify format validation",
        "steps": "1. Try unsupported format",
        "expected": "Unsupported format rejected",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-085",
        "category": "Image Analysis",
        "feature": "File Size",
        "description": "Verify file size limit",
        "steps": "1. Upload large file",
        "expected": "Large file rejected with error",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-086",
        "category": "Image Analysis",
        "feature": "Image Preview",
        "description": "Verify image preview",
        "steps": "1. Upload image\n2. Check preview",
        "expected": "Preview displays correctly",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-087",
        "category": "Image Analysis",
        "feature": "Image Crop",
        "description": "Verify image cropping",
        "steps": "1. Click crop\n2. Adjust crop",
        "expected": "Image cropped successfully",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-088",
        "category": "Image Analysis",
        "feature": "Analyze Button",
        "description": "Verify analyze button",
        "steps": "1. Click analyze",
        "expected": "Analysis starts",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-089",
        "category": "Image Analysis",
        "feature": "Progress Indicator",
        "description": "Verify progress bar",
        "steps": "1. Start analysis\n2. Watch progress",
        "expected": "Progress bar updates",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-090",
        "category": "Image Analysis",
        "feature": "Results Display",
        "description": "Verify results display",
        "steps": "1. Complete analysis\n2. Check results",
        "expected": "Results displayed with confidence scores",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-091",
        "category": "Image Analysis",
        "feature": "Export PDF",
        "description": "Verify export to PDF",
        "steps": "1. Click export\n2. Choose PDF",
        "expected": "PDF generated and downloaded",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-092",
        "category": "Image Analysis",
        "feature": "Share Results",
        "description": "Verify share functionality",
        "steps": "1. Click share\n2. Enter email",
        "expected": "Results shared via email",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-093",
        "category": "Image Analysis",
        "feature": "Save to Patient",
        "description": "Verify save to patient",
        "steps": "1. Click save\n2. Select patient",
        "expected": "Result saved to patient record",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-094",
        "category": "Image Analysis",
        "feature": "History",
        "description": "Verify analysis history",
        "steps": "1. Check history tab",
        "expected": "Previous analyses listed",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-095",
        "category": "Image Analysis",
        "feature": "Download Results",
        "description": "Verify download results",
        "steps": "1. Click download",
        "expected": "Results file downloaded",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    
    # ========== 6. PATIENT MANAGEMENT (WEB-096 to WEB-100) ==========
    {
        "id": "WEB-096",
        "category": "Patient Management",
        "feature": "Add Patient",
        "description": "Verify add patient functionality",
        "steps": "1. Click add patient\n2. Fill details\n3. Save",
        "expected": "Patient added successfully",
        "status": "PENDING",
        "priority": "CRITICAL"
    },
    {
        "id": "WEB-097",
        "category": "Patient Management",
        "feature": "Edit Patient",
        "description": "Verify edit patient functionality",
        "steps": "1. Select patient\n2. Click edit\n3. Update details",
        "expected": "Patient updated successfully",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-098",
        "category": "Patient Management",
        "feature": "Delete Patient",
        "description": "Verify delete patient functionality",
        "steps": "1. Select patient\n2. Click delete\n3. Confirm",
        "expected": "Patient deleted successfully",
        "status": "PENDING",
        "priority": "MEDIUM"
    },
    {
        "id": "WEB-099",
        "category": "Patient Management",
        "feature": "Search Patients",
        "description": "Verify patient search",
        "steps": "1. Use search\n2. Enter patient name",
        "expected": "Matching patients displayed",
        "status": "PENDING",
        "priority": "HIGH"
    },
    {
        "id": "WEB-100",
        "category": "Patient Management",
        "feature": "Export Patients",
        "description": "Verify export patient list",
        "steps": "1. Click export\n2. Choose format",
        "expected": "Patient list exported",
        "status": "PENDING",
        "priority": "MEDIUM"
    }
]
