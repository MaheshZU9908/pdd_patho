# test_cases.py
# Contains 100 detailed test case definitions for the PathoAI mobile application.

TEST_CASES = [
    # 1. SPLASH SCREEN (TC-001 to TC-005)
    {
        "id": "TC-001",
        "category": "Splash Screen",
        "feature": "App Launch",
        "description": "Verify app launches successfully and displays the Splash screen.",
        "steps": "1. Launch PathoAI mobile application.\n2. Observe active activity name.",
        "expected": "SplashActivity is launched and visible.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-002",
        "category": "Splash Screen",
        "feature": "UI Elements",
        "description": "Verify the logo branding is displayed on the Splash screen.",
        "steps": "1. Launch app.\n2. Inspect content view elements on the Splash screen.",
        "expected": "App logo/branding drawable is visible and centered.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-003",
        "category": "Splash Screen",
        "feature": "Transition Delay",
        "description": "Verify splash screen stays active for exactly 2 seconds delay.",
        "steps": "1. Launch app and start timer.\n2. Stop timer when LoginActivity starts.",
        "expected": "Transition occurs post a 2000ms delay.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-004",
        "category": "Splash Screen",
        "feature": "Auto-Navigation",
        "description": "Verify auto-transition from Splash to LoginActivity.",
        "steps": "1. Launch app.\n2. Wait for 2.5 seconds without user interaction.",
        "expected": "LoginActivity automatically comes into foreground.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-005",
        "category": "Splash Screen",
        "feature": "Activity Stack",
        "description": "Verify SplashActivity is finished and cleared from the backstack after transition.",
        "steps": "1. Wait for auto-transition to LoginActivity.\n2. Press Android system back button.",
        "expected": "App closes instead of returning to the Splash screen.",
        "status": "PENDING",
        "comments": ""
    },

    # 2. LOGIN VIEW - UI & ELEMENTS (TC-006 to TC-015)
    {
        "id": "TC-006",
        "category": "Login View",
        "feature": "UI Layout",
        "description": "Verify Login screen header text 'Welcome Doctor,' is visible.",
        "steps": "1. Navigate to Login screen.\n2. Inspect the top heading TextView.",
        "expected": "Header matches text 'Welcome Doctor,' exactly.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-007",
        "category": "Login View",
        "feature": "UI Layout",
        "description": "Verify Login screen subtitle instruction is visible.",
        "steps": "1. Inspect subtitle element below heading.",
        "expected": "Subtitle displays 'Sign in to access AI clinical tools'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-008",
        "category": "Login View",
        "feature": "UI Elements",
        "description": "Verify Medical Email/ID input field is visible with proper hint.",
        "steps": "1. Locate email EditText field via ID 'et_email'.",
        "expected": "EditText is visible and placeholder hint matches 'Medical Email or ID'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-009",
        "category": "Login View",
        "feature": "UI Elements",
        "description": "Verify Password input field is visible with proper hint.",
        "steps": "1. Locate password EditText field via ID 'et_password'.",
        "expected": "EditText is visible and placeholder hint matches 'Password'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-010",
        "category": "Login View",
        "feature": "UI Elements",
        "description": "Verify 'Forgot Password?' navigation text link is visible.",
        "steps": "1. Locate TextView with ID 'tv_forgot_password'.",
        "expected": "Link text matches 'Forgot Password?' and is clickable.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-011",
        "category": "Login View",
        "feature": "UI Elements",
        "description": "Verify Login button is visible and properly styled.",
        "steps": "1. Locate Button with ID 'btn_login'.",
        "expected": "Button displays 'Login' text and is enabled.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-012",
        "category": "Login View",
        "feature": "UI Elements",
        "description": "Verify 'Don't have an account? Sign Up' link is visible.",
        "steps": "1. Locate TextView with ID 'tv_go_signup'.",
        "expected": "Link is visible and clickable.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-013",
        "category": "Login View",
        "feature": "Input Options",
        "description": "Verify Email field has type set to textEmailAddress.",
        "steps": "1. Check XML attributes or system input type for ID 'et_email'.",
        "expected": "Input type is restricted to valid email layout keyboards.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-014",
        "category": "Login View",
        "feature": "Input Options",
        "description": "Verify Password field hides characters (input type textPassword).",
        "steps": "1. Type characters in ID 'et_password'.\n2. Inspect visible text.",
        "expected": "Password characters are masked as dots/asterisks.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-015",
        "category": "Login View",
        "feature": "View Flipper State",
        "description": "Verify AuthViewFlipper defaults to index 0 on startup.",
        "steps": "1. Check current active view inside R.id.authViewFlipper.",
        "expected": "Active view is the Login layout container.",
        "status": "PENDING",
        "comments": ""
    },

    # 3. LOGIN FORM VALIDATION (TC-016 to TC-025)
    {
        "id": "TC-016",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify error feedback when Login is clicked with empty email.",
        "steps": "1. Clear email and password fields.\n2. Click Login button.",
        "expected": "Email input shows validation error 'Valid Email Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-017",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify error when email is missing '@' symbol.",
        "steps": "1. Enter 'doctor.example.com' in email field.\n2. Click Login button.",
        "expected": "Email input shows validation error 'Valid Email Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-018",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify error when email has no domain extension.",
        "steps": "1. Enter 'doctor@hospital' in email field.\n2. Click Login button.",
        "expected": "Email input shows validation error 'Valid Email Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-019",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify validation passes with clean standard medical email.",
        "steps": "1. Enter 'doctor@biopath.ai' in email field.\n2. Enter empty password.\n3. Click Login.",
        "expected": "Email validation passes; password input gets focus and reports error.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-020",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify error when password is empty.",
        "steps": "1. Enter 'doctor@biopath.ai' in email.\n2. Leave password empty.\n3. Click Login.",
        "expected": "Password input shows validation error 'Password must be at least 6 characters'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-021",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify error when password is under 6 characters.",
        "steps": "1. Enter 'doctor@biopath.ai' in email.\n2. Enter 'abc12' in password.\n3. Click Login.",
        "expected": "Password input shows validation error 'Password must be at least 6 characters'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-022",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify whitespace trimming on email fields.",
        "steps": "1. Enter '  doctor@biopath.ai  ' in email.\n2. Enter 'password123' in password.\n3. Click Login.",
        "expected": "Trimming occurs successfully and validates matching address format.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-023",
        "category": "Login View",
        "feature": "Form Validation",
        "description": "Verify password length validation on long strings.",
        "steps": "1. Enter valid email.\n2. Enter a 50-character string in password.\n3. Click Login.",
        "expected": "Password length criteria is met (>= 6) and allows authentication path.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-024",
        "category": "Login View",
        "feature": "Validation Priority",
        "description": "Verify email check precedes password length check.",
        "steps": "1. Leave both fields empty.\n2. Click Login.",
        "expected": "Validation stops at email error without marking password field.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-025",
        "category": "Login View",
        "feature": "Input Focus",
        "description": "Verify keyboard hides/shows properly on tapping input fields.",
        "steps": "1. Tap on Email edit text field.\n2. Tap outside on background space.",
        "expected": "Soft keyboard pops up on focus, closes on tap-out/dismiss.",
        "status": "PENDING",
        "comments": ""
    },

    # 4. LOGIN FLOW EXECUTION (TC-026 to TC-030)
    {
        "id": "TC-026",
        "category": "Login View",
        "feature": "Success Navigation",
        "description": "Verify successful login redirect with valid doctor credentials.",
        "steps": "1. Enter 'doctor@biopath.ai'.\n2. Enter 'password123'.\n3. Click Login.",
        "expected": "MainActivity is launched and transition is smooth.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-027",
        "category": "Login View",
        "feature": "Transition Animation",
        "description": "Verify custom fade transition animation on Login success.",
        "steps": "1. Click login with valid details.\n2. Watch screen switch.",
        "expected": "Transition shows smooth alpha cross-fade animation.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-028",
        "category": "Login View",
        "feature": "Session State",
        "description": "Verify Login finish logic destroys LoginActivity on success.",
        "steps": "1. Log in successfully to MainActivity.\n2. Click hardware/gesture Back button.",
        "expected": "App closes; backstack does not redirect back to LoginActivity.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-029",
        "category": "Login View",
        "feature": "Keyboard Action",
        "description": "Verify IME Actions (Done/Send) are handled on password input.",
        "steps": "1. Enter valid email.\n2. Enter password and press 'Done' key on virtual keyboard.",
        "expected": "Submits form trigger or closes keyboard.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-030",
        "category": "Login View",
        "feature": "State Isolation",
        "description": "Verify clearing email/password inputs works correctly.",
        "steps": "1. Enter dummy credentials.\n2. Tap back space or delete all characters.",
        "expected": "Fields remain completely empty with no hidden characters.",
        "status": "PENDING",
        "comments": ""
    },

    # 5. SIGNUP VIEW - UI & ELEMENTS (TC-031 to TC-035)
    {
        "id": "TC-031",
        "category": "Signup View",
        "feature": "UI Navigation",
        "description": "Verify navigating from Login to Signup via 'Sign Up' link.",
        "steps": "1. Click on 'Don't have an account? Sign Up' link.",
        "expected": "AuthViewFlipper changes display view child to index 1 (Signup View).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-032",
        "category": "Signup View",
        "feature": "UI Elements",
        "description": "Verify Full Name input field visibility in Signup View.",
        "steps": "1. Navigate to Signup screen.\n2. Locate ID 'et_signup_name'.",
        "expected": "Field is visible with hint text 'Full Name'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-033",
        "category": "Signup View",
        "feature": "UI Elements",
        "description": "Verify Medical Email input field visibility in Signup View.",
        "steps": "1. Locate ID 'et_signup_email'.",
        "expected": "Field is visible with hint text 'Medical Email'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-034",
        "category": "Signup View",
        "feature": "UI Elements",
        "description": "Verify Password input field visibility in Signup View.",
        "steps": "1. Locate ID 'et_signup_password'.",
        "expected": "Field is visible with hint text 'Password'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-035",
        "category": "Signup View",
        "feature": "UI Elements",
        "description": "Verify Sign Up button is visible and properly labeled.",
        "steps": "1. Locate ID 'btn_signup'.",
        "expected": "Button shows 'Sign Up' text and is enabled.",
        "status": "PENDING",
        "comments": ""
    },

    # 6. SIGNUP FORM VALIDATION & FLOW (TC-036 to TC-045)
    {
        "id": "TC-036",
        "category": "Signup View",
        "feature": "Form Validation",
        "description": "Verify error when Full Name is empty during signup.",
        "steps": "1. Leave Name field empty.\n2. Click Sign Up button.",
        "expected": "Name field shows validation error 'Name Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-037",
        "category": "Signup View",
        "feature": "Form Validation",
        "description": "Verify error when email is empty during signup.",
        "steps": "1. Enter name 'Dr. Miller'.\n2. Leave email empty.\n3. Click Sign Up.",
        "expected": "Email field shows validation error 'Valid Email Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-038",
        "category": "Signup View",
        "feature": "Form Validation",
        "description": "Verify error when email format is invalid during signup.",
        "steps": "1. Enter 'Dr. Miller' and 'miller_email.com'.\n2. Click Sign Up.",
        "expected": "Email field shows validation error 'Valid Email Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-039",
        "category": "Signup View",
        "feature": "Form Validation",
        "description": "Verify error when password is empty during signup.",
        "steps": "1. Enter name and valid email.\n2. Leave password empty.\n3. Click Sign Up.",
        "expected": "Password field shows validation error 'Password must be at least 6 characters'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-040",
        "category": "Signup View",
        "feature": "Form Validation",
        "description": "Verify error when password is less than 6 characters during signup.",
        "steps": "1. Enter name, email.\n2. Enter 'pass' in password.\n3. Click Sign Up.",
        "expected": "Password field shows validation error 'Password must be at least 6 characters'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-041",
        "category": "Signup View",
        "feature": "UI Navigation",
        "description": "Verify transition back to Login via 'Already have an account? Login' link.",
        "steps": "1. Click on 'Already have an account? Login' link (ID 'tv_go_login').",
        "expected": "AuthViewFlipper changes display view child back to index 0 (Login).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-042",
        "category": "Signup View",
        "feature": "Signup Success Flow",
        "description": "Verify successful registration with complete valid details.",
        "steps": "1. Enter name 'Sarah Miller', email 'sarah@biopath.ai', password 'secure123'.\n2. Click Sign Up.",
        "expected": "Shows toast 'Account Created Successfully' and redirects to Login.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-043",
        "category": "Signup View",
        "feature": "UI Toast Msg",
        "description": "Verify toast alert confirms account creation success.",
        "steps": "1. Fill valid signup fields.\n2. Press sign up.\n3. Verify Toast overlay content.",
        "expected": "Toast overlays with text 'Account Created Successfully'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-044",
        "category": "Signup View",
        "feature": "Form Reset",
        "description": "Verify signup form fields reset after transitioning to login and back.",
        "steps": "1. Enter data in signup fields.\n2. Click Login link.\n3. Click Signup link again.",
        "expected": "Fields in signup form do not retain previous inputs.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-045",
        "category": "Signup View",
        "feature": "Keyboard Actions",
        "description": "Verify password input action transitions focus to registration button.",
        "steps": "1. Click next on Email field.\n2. Check focus transition.",
        "expected": "Focus moves correctly to password field.",
        "status": "PENDING",
        "comments": ""
    },

    # 7. FORGOT PASSWORD & OTP VIEWS (TC-046 to TC-055)
    {
        "id": "TC-046",
        "category": "Reset & OTP View",
        "feature": "UI Navigation",
        "description": "Verify navigating from Login to Forgot Password screen.",
        "steps": "1. Click 'Forgot Password?' link (ID 'tv_forgot_password').",
        "expected": "AuthViewFlipper changes display view child to index 2 (Forgot Password).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-047",
        "category": "Reset & OTP View",
        "feature": "UI Layout",
        "description": "Verify reset screen instruction subtitle visibility.",
        "steps": "1. Inspect text under heading 'Reset Password'.",
        "expected": "Instructions read 'Enter your email to receive an OTP.'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-048",
        "category": "Reset & OTP View",
        "feature": "Form Validation",
        "description": "Verify error when Send OTP is clicked with empty email.",
        "steps": "1. Clear email field.\n2. Click Send OTP button (ID 'btn_send_otp').",
        "expected": "Reset email input shows error 'Valid Email Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-049",
        "category": "Reset & OTP View",
        "feature": "Form Validation",
        "description": "Verify error when Reset email format is invalid.",
        "steps": "1. Enter 'invalidmail' in Reset Email.\n2. Click Send OTP button.",
        "expected": "Reset email input shows error 'Valid Email Required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-050",
        "category": "Reset & OTP View",
        "feature": "OTP Dispatch Flow",
        "description": "Verify successful dispatch triggers OTP view and shows toast.",
        "steps": "1. Enter 'doctor@biopath.ai' in Reset Email.\n2. Click Send OTP.",
        "expected": "Toast shows 'OTP Sent to Email' and active view changes to index 3 (OTP).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-051",
        "category": "Reset & OTP View",
        "feature": "UI Elements",
        "description": "Verify 4-digit OTP input field properties (number type, length 4).",
        "steps": "1. Check XML or type values on ID 'et_otp'.",
        "expected": "Max length is 4, inputType is number, characters centered.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-052",
        "category": "Reset & OTP View",
        "feature": "Form Validation",
        "description": "Verify validation warning when OTP input is not exactly 4 digits.",
        "steps": "1. Enter '12' in OTP field.\n2. Click Verify & Login (ID 'btn_verify_otp').",
        "expected": "OTP input shows validation error 'Enter valid 4-digit OTP'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-053",
        "category": "Reset & OTP View",
        "feature": "OTP Verification Flow",
        "description": "Verify successful OTP validation redirects to MainActivity dashboard.",
        "steps": "1. Enter '1234' in OTP field.\n2. Click Verify & Login.",
        "expected": "Toast shows 'OTP Verified. Logging in...' and loads MainActivity.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-054",
        "category": "Reset & OTP View",
        "feature": "UI Navigation",
        "description": "Verify 'Back to Login' button on Forgot Password screen.",
        "steps": "1. Click link 'Back to Login' on Forgot Password screen (ID 'tv_back_to_login_from_reset').",
        "expected": "Returns to index 0 (Login View).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-055",
        "category": "Reset & OTP View",
        "feature": "UI Navigation",
        "description": "Verify 'Back to Login' button on OTP verification screen.",
        "steps": "1. Click link 'Back to Login' on OTP screen (ID 'tv_back_to_login_from_otp').",
        "expected": "Returns to index 0 (Login View).",
        "status": "PENDING",
        "comments": ""
    },

    # 8. MAIN DASHBOARD (TC-056 to TC-065)
    {
        "id": "TC-056",
        "category": "Main Dashboard",
        "feature": "Navigation Default",
        "description": "Verify app displays Home Dashboard by default on main activity start.",
        "steps": "1. Log in successfully.\n2. Verify the visible view child index in MainActivity's ViewFlipper.",
        "expected": "ViewFlipper shows child 0 (Home Dashboard layout).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-057",
        "category": "Main Dashboard",
        "feature": "UI Toolbar",
        "description": "Verify toolbar navigation icon opens the sidebar drawer navigation panel.",
        "steps": "1. Click on navigation menu icon in Toolbar.",
        "expected": "DrawerLayout opens side panel from GravityCompat.START.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-058",
        "category": "Main Dashboard",
        "feature": "UI Toolbar",
        "description": "Verify Toolbar displays correct app title 'PathoAI Dashboard'.",
        "steps": "1. Check text attribute of the Toolbar widget.",
        "expected": "Title text matches 'PathoAI Dashboard'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-059",
        "category": "Main Dashboard",
        "feature": "UI Statistics",
        "description": "Verify Total Cases counter displays correct case record counts.",
        "steps": "1. Inspect TextView ID 'tv_total_cases'.",
        "expected": "Displays current number of diagnostic records matching AppState.cases.size.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-060",
        "category": "Main Dashboard",
        "feature": "UI Statistics",
        "description": "Verify Critical Risk counter matches AppState critical patient counts.",
        "steps": "1. Inspect TextView ID 'tv_critical_risk'.",
        "expected": "Displays number of patients matching status 'Critical' in AppState.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-061",
        "category": "Main Dashboard",
        "feature": "UI Layout",
        "description": "Verify heading section title 'Recent Diagnosed Cases' is visible.",
        "steps": "1. Scroll down dashboard.\n2. Verify section header TextView.",
        "expected": "Displays section heading text 'Recent Diagnosed Cases'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-062",
        "category": "Main Dashboard",
        "feature": "UI Case Card",
        "description": "Verify empty message 'No cases diagnosed yet.' when case list is empty.",
        "steps": "1. Launch app under empty case state session.\n2. Observe recent cases container view.",
        "expected": "Displays placeholder text 'No cases diagnosed yet.'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-063",
        "category": "Main Dashboard",
        "feature": "UI Case Card",
        "description": "Verify dynamic generation of case cards when database records exist.",
        "steps": "1. Inject test records into AppState.cases.\n2. Refresh/Open Home tab.",
        "expected": "Recent cases list has child views mapped to corresponding records.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-064",
        "category": "Main Dashboard",
        "feature": "UI Case Card",
        "description": "Verify details shown on case card (Patient name, ID, Disease, Metastasis risk).",
        "steps": "1. Inspect recent case card items.",
        "expected": "Card labels contain patient name/ID, AI disease classification, and metastasis risk percentage.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-065",
        "category": "Main Dashboard",
        "feature": "UI Navigation",
        "description": "Verify clicking on a recent case card triggers redirect to results report.",
        "steps": "1. Click on first recent case card list item.",
        "expected": "Launches AnalysisResultActivity populated with matching case details.",
        "status": "PENDING",
        "comments": ""
    },

    # 9. PATIENT MANAGEMENT - UI & REGISTRATION (TC-066 to TC-075)
    {
        "id": "TC-066",
        "category": "Patient Management",
        "feature": "Bottom Nav Bar",
        "description": "Verify bottom navigation bar selection transitions to Patients View.",
        "steps": "1. Click on menu item ID 'nav_patients' on bottom bar.",
        "expected": "ViewFlipper displays child index 1 (Patient list UI).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-067",
        "category": "Patient Management",
        "feature": "UI Search Layout",
        "description": "Verify patient search input field is visible with proper hint.",
        "steps": "1. Navigate to Patients tab.\n2. Locate search input ID 'et_patient_search'.",
        "expected": "Input visible and hint displays 'Search Patients (ID or Name)'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-068",
        "category": "Patient Management",
        "feature": "UI Patients List",
        "description": "Verify RecyclerView displays patient items correctly.",
        "steps": "1. Inspect RecyclerView ID 'rv_patients'.",
        "expected": "RecyclerView is populated; items map to AppState.patients list.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-069",
        "category": "Patient Management",
        "feature": "UI Dialog Launch",
        "description": "Verify Floating Action Button (FAB) opens Register New Patient Dialog.",
        "steps": "1. Click FAB ID 'fab_add_patient'.",
        "expected": "AlertDialog opens and dialog layout dialog_patient.xml is inflated.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-070",
        "category": "Patient Management",
        "feature": "Registration Dialog",
        "description": "Verify dialog title is 'Register New Patient' on FAB click.",
        "steps": "1. Click FAB.\n2. Locate Dialog Title ID 'tv_dialog_title'.",
        "expected": "Title matches 'Register New Patient' exactly.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-071",
        "category": "Patient Management",
        "feature": "Registration Dialog",
        "description": "Verify spinners in Patient registration dialog are populated with options.",
        "steps": "1. Click gender spinner and risk spinner.",
        "expected": "Gender shows Male/Female/Other. Status shows Clear/Moderate Risk/High Risk/Critical.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-072",
        "category": "Patient Management",
        "feature": "Form Validation",
        "description": "Verify validation failure error on empty name input in dialog.",
        "steps": "1. Leave Name field empty.\n2. Click Register button (ID 'btn_dialog_save').",
        "expected": "Name field in dialog shows validation error 'Name is required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-073",
        "category": "Patient Management",
        "feature": "Form Validation",
        "description": "Verify validation error when age is invalid (empty/zero/negative).",
        "steps": "1. Enter name 'John'.\n2. Leave age empty or enter '-5'.\n3. Click Register.",
        "expected": "Age field shows validation error 'Enter valid age'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-074",
        "category": "Patient Management",
        "feature": "Form Validation",
        "description": "Verify validation error when contact number is empty.",
        "steps": "1. Fill name, valid age.\n2. Leave contact field empty.\n3. Click Register.",
        "expected": "Contact field shows validation error 'Contact is required'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-075",
        "category": "Patient Management",
        "feature": "Form Validation",
        "description": "Verify validation error when initial diagnosis is empty.",
        "steps": "1. Fill name, age, contact.\n2. Leave initial diagnosis field empty.\n3. Click Register.",
        "expected": "Diagnosis field shows validation error 'Initial diagnosis is required'.",
        "status": "PENDING",
        "comments": ""
    },

    # 10. PATIENT MANAGEMENT - ACTIONS & FILTERING (TC-076 to TC-085)
    {
        "id": "TC-076",
        "category": "Patient Management",
        "feature": "Registration Success",
        "description": "Verify successful registration updates patient list and displays Toast.",
        "steps": "1. Fill all valid details in dialog.\n2. Click Register button.",
        "expected": "Toast shows 'New patient registered', dialog closes, new item added to patient list.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-077",
        "category": "Patient Management",
        "feature": "Registration Dismiss",
        "description": "Verify dialog is dismissed without adding record on Cancel click.",
        "steps": "1. Open dialog, enter partial details.\n2. Click Cancel button.",
        "expected": "Dialog closes, patient list remains unmodified.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-078",
        "category": "Patient Management",
        "feature": "Patient List Search",
        "description": "Verify typing a substring in search bar filters list matching names.",
        "steps": "1. Enter 'Emily' in patient search bar.\n2. Observe matching list items.",
        "expected": "List updates to display only patients whose name matches 'Emily'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-079",
        "category": "Patient Management",
        "feature": "Patient List Search",
        "description": "Verify searching by ID matches exact patient ID code.",
        "steps": "1. Enter 'PID-1021' in patient search bar.\n2. Observe matching list items.",
        "expected": "Displays exact patient matching ID 'PID-1021'.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-080",
        "category": "Patient Management",
        "feature": "Patient List Search",
        "description": "Verify empty list state when search query matches no patient.",
        "steps": "1. Enter 'NonExistentPatientXYZ' in search bar.\n2. Observe list contents.",
        "expected": "RecyclerView displays no items.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-081",
        "category": "Patient Management",
        "feature": "Patient Edit Detail",
        "description": "Verify clicking edit icon on list item opens dialog pre-populated with current details.",
        "steps": "1. Find patient list item.\n2. Click edit button icon (ID 'btn_edit_patient').",
        "expected": "Dialog title is 'Edit Patient Details', fields show current records.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-082",
        "category": "Patient Management",
        "feature": "Patient Edit Detail",
        "description": "Verify saving edits updates details in list and shows Toast.",
        "steps": "1. Edit name to 'Emily Updated'.\n2. Click Save Updates button.",
        "expected": "Toast shows 'Patient details updated', list reflects updated name.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-083",
        "category": "Patient Management",
        "feature": "Patient Deletion Flow",
        "description": "Verify clicking delete icon prompts confirmation alert dialog.",
        "steps": "1. Locate patient list item.\n2. Click delete button icon (ID 'btn_delete_patient').",
        "expected": "Alert shows confirmation asking to delete profile and diagnostic scans history.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-084",
        "category": "Patient Management",
        "feature": "Patient Deletion Flow",
        "description": "Verify confirming deletion removes patient profile and associated scans.",
        "steps": "1. Click delete icon.\n2. Click confirmation dialog 'Delete' button.",
        "expected": "Toast shows 'Profile deleted', patient profile is permanently deleted.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-085",
        "category": "Patient Management",
        "feature": "Patient Detail Profile",
        "description": "Verify clicking patient item layout loads medical profile card overview.",
        "steps": "1. Tap on patient item body layout (ID 'patient_item_layout' or equivalent click listener).",
        "expected": "Alert dialog displays ID, demographics, clinical notes, and AI scan history timeline.",
        "status": "PENDING",
        "comments": ""
    },

    # 11. MIL SCANNER - ANALYZE TAB (TC-086 to TC-090)
    {
        "id": "TC-086",
        "category": "Analyze Scanner",
        "feature": "Bottom Nav Bar",
        "description": "Verify bottom navigation selection transitions to Analyze/Scan tab.",
        "steps": "1. Click menu item ID 'nav_upload' on bottom navigation bar.",
        "expected": "ViewFlipper displays child index 2 (Analyze Scanner interface).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-087",
        "category": "Analyze Scanner",
        "feature": "UI Elements",
        "description": "Verify patient dropdown list Spinner is visible and pre-populated.",
        "steps": "1. Locate spinner ID 'spinner_analyze_patient'.\n2. Click to open dropdown.",
        "expected": "Dropdown displays list of registered patients.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-088",
        "category": "Analyze Scanner",
        "feature": "UI Upload Layout",
        "description": "Verify slide upload preview frame contains placeholder overlay.",
        "steps": "1. Locate preview placeholder container ID 'layout_upload_placeholder'.",
        "expected": "Placeholder with upload graphic and helper text is visible.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-089",
        "category": "Analyze Scanner",
        "feature": "UI Upload Buttons",
        "description": "Verify capture/select buttons are visible and active.",
        "steps": "1. Locate camera selection button ID 'btn_upload_camera' and gallery ID 'btn_upload_gallery'.",
        "expected": "Both buttons are visible, enabled, and labeled correctly.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-090",
        "category": "Analyze Scanner",
        "feature": "UI Analyze Action",
        "description": "Verify Run AI Diagnosis button is disabled until slide is uploaded.",
        "steps": "1. Look at 'btn_run_analysis' state under default load.",
        "expected": "Run AI Diagnosis button is disabled and greyed out.",
        "status": "PENDING",
        "comments": ""
    },

    # 12. H&E VERIFICATION & SCANNING (TC-091 to TC-095)
    {
        "id": "TC-091",
        "category": "Analyze Scanner",
        "feature": "H&E Stain Check",
        "description": "Verify rejection of non-H&E stained images (non-pathology images).",
        "steps": "1. Trigger gallery selector mock returning standard nature/green image.\n2. Attempt loading.",
        "expected": "Rejection dialog shows warning that image is missing H&E stained pink/purple color profiles.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-092",
        "category": "Analyze Scanner",
        "feature": "H&E Stain Check",
        "description": "Verify successful load of pink/purple-dominated H&E microscopic slice.",
        "steps": "1. Trigger gallery picker mockup returning H&E microscopic crop.\n2. Load into app.",
        "expected": "Toast matches 'H&E microscopic slide detected and loaded.' and image previews.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-093",
        "category": "Analyze Scanner",
        "feature": "UI State Update",
        "description": "Verify Run AI Diagnosis button gets enabled upon loading valid slide.",
        "steps": "1. Successfully load a verified H&E biopsy image.",
        "expected": "Run AI Diagnosis button changes state to active (enabled).",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-094",
        "category": "Analyze Scanner",
        "feature": "Simulation Loading",
        "description": "Verify interface locking and progress state updates during simulation run.",
        "steps": "1. Click Run AI Diagnosis button.\n2. Inspect button visibility and inputs status.",
        "expected": "Spinner, buttons, and bottom navigation locks; progress card displays steps.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-095",
        "category": "Analyze Scanner",
        "feature": "Simulation Stages",
        "description": "Verify sequence of simulation messages during deep learning pipeline run.",
        "steps": "1. Click Run AI Diagnosis.\n2. Monitor simulation step TextView ID 'tv_simulation_step'.",
        "expected": "Step changes sequentially from Preprocessing to Feature Extraction to Report Parsing.",
        "status": "PENDING",
        "comments": ""
    },

    # 13. ANALYSIS RESULT VIEW (TC-096 to TC-100)
    {
        "id": "TC-096",
        "category": "Analysis Result",
        "feature": "UI Details",
        "description": "Verify diagnostic result screen pops up automatically post simulation.",
        "steps": "1. Run analysis flow and wait for completion.",
        "expected": "AnalysisResultActivity comes into foreground with detailed PDF export and saving buttons.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-097",
        "category": "Analysis Result",
        "feature": "Canvas Annotations",
        "description": "Verify canvas drawings highlight tumor nests or benign margins in biopsy image.",
        "steps": "1. Verify loaded bitmap overlay inside ID 'iv_result_biopsy_image'.",
        "expected": "Visual annotations (colored outlines/tumor budgeting fronts) drawn dynamically over raw sample.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-098",
        "category": "Analysis Result",
        "feature": "Doctor Clinical Notes",
        "description": "Verify updating clinical doctor notes saves successfully to state and patient record.",
        "steps": "1. Enter text in doctor notes input ID 'et_report_doctor_notes'.\n2. Click Save Findings.",
        "expected": "Toast shows 'Clinical findings updated successfully', notes persistent across session.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-099",
        "category": "Analysis Result",
        "feature": "PDF Generation",
        "description": "Verify PDF generation compiles details and launches share intent dialog.",
        "steps": "1. Click on Export PDF Report button (ID 'btn_download_report_pdf').",
        "expected": "Toast reports successful export, system share chooser overlay pops up.",
        "status": "PENDING",
        "comments": ""
    },
    {
        "id": "TC-100",
        "category": "Analysis Result",
        "feature": "Navigation Return",
        "description": "Verify returning from result screen redirects back to Main dashboard.",
        "steps": "1. Click on Back to Clinical Dashboard button (ID 'btn_report_back').",
        "expected": "Returns back to MainActivity, resetting scanning tab inputs.",
        "status": "PENDING",
        "comments": ""
    }
]
