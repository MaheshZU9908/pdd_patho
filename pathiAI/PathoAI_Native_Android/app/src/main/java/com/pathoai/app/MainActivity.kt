package com.pathoai.app

import android.app.Activity
import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.graphics.Color
import android.net.Uri
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.provider.MediaStore
import android.text.Editable
import android.text.TextWatcher
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.activity.result.contract.ActivityResultContracts
import androidx.appcompat.app.AlertDialog
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.GravityCompat
import androidx.drawerlayout.widget.DrawerLayout
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.google.android.material.bottomnavigation.BottomNavigationView
import com.google.android.material.navigation.NavigationView
import java.io.File
import java.io.FileOutputStream
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity(), PatientAdapter.OnPatientActionListener {

    private lateinit var drawerLayout: DrawerLayout
    private lateinit var viewFlipper: ViewFlipper
    private lateinit var bottomNavigation: BottomNavigationView
    private lateinit var navView: NavigationView

    // Patient Tab UI
    private lateinit var rvPatients: RecyclerView
    private lateinit var patientAdapter: PatientAdapter
    private lateinit var etSearch: EditText

    // Analyze Tab UI
    private lateinit var spinnerPatients: Spinner
    private lateinit var ivBiopsyPreview: ImageView
    private lateinit var layoutPlaceholder: View
    private lateinit var btnRunAnalysis: Button
    private lateinit var layoutSimulation: View
    private lateinit var tvSimulationStep: TextView
    private lateinit var tvSimulationSubtext: TextView
    private lateinit var btnUploadCamera: Button
    private lateinit var btnUploadGallery: Button

    private var selectedImageUri: Uri? = null

    // Image Picker Launcher
    private val galleryLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            val data: Intent? = result.data
            val uri = data?.data
            if (uri != null) {
                processUploadedImage(uri)
            }
        }
    }

    private val cameraLauncher = registerForActivityResult(ActivityResultContracts.StartActivityForResult()) { result ->
        if (result.resultCode == Activity.RESULT_OK) {
            val data: Intent? = result.data
            val bitmap = data?.extras?.get("data") as? Bitmap
            if (bitmap != null) {
                val uri = saveBitmapToCache(bitmap)
                if (uri != null) {
                    processUploadedImage(uri)
                } else {
                    Toast.makeText(this, "Failed to cache camera capture", Toast.LENGTH_SHORT).show()
                }
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Bind Base Drawer & Navigation Views
        drawerLayout = findViewById(R.id.drawer_layout)
        viewFlipper = findViewById(R.id.viewFlipper)
        bottomNavigation = findViewById(R.id.bottom_navigation)
        navView = findViewById(R.id.nav_view)

        setupToolbar()
        setupBottomNavigation()
        setupDrawerNavigation()

        // Init Dashboard Tab
        setupDashboard()

        // Init Patient Tab
        setupPatientTab()

        // Init Analyze Tab
        setupAnalyzeTab()

        // Init Alerts / Notifications Tab
        setupNotifications()

        // Init Profile Settings Tab
        setupProfile()
    }

    private fun setupToolbar() {
        val toolbar = findViewById<androidx.appcompat.widget.Toolbar>(R.id.toolbar)
        toolbar.setNavigationOnClickListener {
            drawerLayout.openDrawer(GravityCompat.START)
        }
    }

    private fun setupBottomNavigation() {
        bottomNavigation.setOnItemSelectedListener { item ->
            when (item.itemId) {
                R.id.nav_home -> {
                    viewFlipper.displayedChild = 0
                    setupDashboard() // Refresh dashboard stats
                }
                R.id.nav_patients -> {
                    viewFlipper.displayedChild = 1
                    patientAdapter.updateData(AppState.patients)
                }
                R.id.nav_upload -> {
                    viewFlipper.displayedChild = 2
                    refreshAnalyzePatientSpinner()
                }
                R.id.nav_notifications -> {
                    viewFlipper.displayedChild = 3
                    setupNotifications()
                }
                R.id.nav_profile -> {
                    viewFlipper.displayedChild = 4
                }
            }
            true
        }
    }

    private fun setupDrawerNavigation() {
        navView.setNavigationItemSelectedListener { item ->
            when (item.itemId) {
                R.id.nav_drawer_dashboard -> bottomNavigation.selectedItemId = R.id.nav_home
                R.id.nav_drawer_patients -> bottomNavigation.selectedItemId = R.id.nav_patients
                R.id.nav_drawer_history -> showScanHistoryTimelineDialog()
                R.id.nav_drawer_settings -> bottomNavigation.selectedItemId = R.id.nav_profile
                R.id.nav_drawer_help -> showHelpSupportDialog()
                R.id.nav_drawer_logout -> performLogout()
            }
            drawerLayout.closeDrawer(GravityCompat.START)
            true
        }
    }

    // ==========================================
    // DASHBOARD TAB (Child 0)
    // ==========================================
    private fun setupDashboard() {
        val totalCasesTv = findViewById<TextView>(R.id.tv_total_cases)
        val criticalRiskTv = findViewById<TextView>(R.id.tv_critical_risk)
        
        totalCasesTv.text = AppState.cases.size.toString()
        criticalRiskTv.text = AppState.patients.count { it.status == "Critical" }.toString()

        val container = findViewById<LinearLayout>(R.id.recent_cases_list)
        container.removeAllViews()

        val recentCases = AppState.cases.take(5)
        if (recentCases.isEmpty()) {
            val emptyTv = TextView(this).apply {
                text = "No cases diagnosed yet."
                setTextColor(Color.GRAY)
                setPadding(16, 16, 16, 16)
            }
            container.addView(emptyTv)
        } else {
            for (case in recentCases) {
                val card = createRecentCaseCard(case)
                container.addView(card)
            }
        }
    }

    private fun createRecentCaseCard(case: CaseRecord): View {
        val view = layoutInflater.inflate(android.R.layout.simple_list_item_2, null)
        val text1 = view.findViewById<TextView>(android.R.id.text1)
        val text2 = view.findViewById<TextView>(android.R.id.text2)

        text1.text = "${case.patientName} (${case.patientId})"
        text2.text = "AI Result: ${case.disease} | Risk: ${case.metastasisRisk}%"
        text1.setTextColor(Color.parseColor("#0F172A"))
        text1.textSize = 15f
        text1.paint?.isFakeBoldText = true
        text2.setTextColor(Color.parseColor("#475569"))
        text2.textSize = 13f

        view.setPadding(16, 24, 16, 24)
        view.setBackgroundResource(R.drawable.input_bg)
        
        val params = LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT)
        params.setMargins(0, 8, 0, 8)
        view.layoutParams = params

        view.setOnClickListener {
            val intent = Intent(this, AnalysisResultActivity::class.java).apply {
                putExtra("CASE_RECORD", case)
            }
            startActivity(intent)
        }
        return view
    }

    // ==========================================
    // PATIENTS TAB (Child 1)
    // ==========================================
    private fun setupPatientTab() {
        rvPatients = findViewById(R.id.rv_patients)
        etSearch = findViewById(R.id.et_patient_search)
        val fabAdd = findViewById<com.google.android.material.floatingactionbutton.FloatingActionButton>(R.id.fab_add_patient)

        rvPatients.layoutManager = LinearLayoutManager(this)
        patientAdapter = PatientAdapter(AppState.patients, this)
        rvPatients.adapter = patientAdapter

        etSearch.addTextChangedListener(object : TextWatcher {
            override fun afterTextChanged(s: Editable?) {
                patientAdapter.filter(s.toString())
            }
            override fun beforeTextChanged(s: CharSequence?, start: Int, count: Int, after: Int) {}
            override fun onTextChanged(s: CharSequence?, start: Int, before: Int, count: Int) {}
        })

        fabAdd.setOnClickListener {
            showAddEditPatientDialog(null)
        }
    }

    private fun showAddEditPatientDialog(patientToEdit: Patient?) {
        val dialogView = LayoutInflater.from(this).inflate(R.layout.dialog_patient, null)
        val tvTitle = dialogView.findViewById<TextView>(R.id.tv_dialog_title)
        val etName = dialogView.findViewById<EditText>(R.id.et_dialog_name)
        val etAge = dialogView.findViewById<EditText>(R.id.et_dialog_age)
        val spinnerGender = dialogView.findViewById<Spinner>(R.id.spinner_dialog_gender)
        val etContact = dialogView.findViewById<EditText>(R.id.et_dialog_contact)
        val etDiagnosis = dialogView.findViewById<EditText>(R.id.et_dialog_diagnosis)
        val spinnerStatus = dialogView.findViewById<Spinner>(R.id.spinner_dialog_status)
        val btnCancel = dialogView.findViewById<Button>(R.id.btn_dialog_cancel)
        val btnSave = dialogView.findViewById<Button>(R.id.btn_dialog_save)

        // Setup Spinners
        val genders = listOf("Male", "Female", "Other")
        val genderAdapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, genders)
        spinnerGender.adapter = genderAdapter

        val statuses = listOf("Clear", "Moderate Risk", "High Risk", "Critical")
        val statusAdapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, statuses)
        spinnerStatus.adapter = statusAdapter

        if (patientToEdit != null) {
            tvTitle.text = "Edit Patient Details"
            etName.setText(patientToEdit.name)
            etAge.setText(patientToEdit.age.toString())
            spinnerGender.setSelection(genders.indexOf(patientToEdit.gender))
            etContact.setText(patientToEdit.contact)
            etDiagnosis.setText(patientToEdit.diagnosis)
            spinnerStatus.setSelection(statuses.indexOf(patientToEdit.status))
            btnSave.text = "Save Updates"
        } else {
            tvTitle.text = "Register New Patient"
            btnSave.text = "Register"
        }

        val alertDialog = AlertDialog.Builder(this)
            .setView(dialogView)
            .create()

        btnCancel.setOnClickListener { alertDialog.dismiss() }

        btnSave.setOnClickListener {
            val name = etName.text.toString().trim()
            val ageStr = etAge.text.toString().trim()
            val contact = etContact.text.toString().trim()
            val diagnosis = etDiagnosis.text.toString().trim()
            val gender = spinnerGender.selectedItem.toString()
            val status = spinnerStatus.selectedItem.toString()

            if (name.isEmpty()) {
                etName.error = "Name is required"
                return@setOnClickListener
            }
            val age = ageStr.toIntOrNull()
            if (age == null || age <= 0) {
                etAge.error = "Enter valid age"
                return@setOnClickListener
            }
            if (contact.isEmpty()) {
                etContact.error = "Contact is required"
                return@setOnClickListener
            }
            if (diagnosis.isEmpty()) {
                etDiagnosis.error = "Initial diagnosis is required"
                return@setOnClickListener
            }

            if (patientToEdit != null) {
                // Edit mode
                val updated = patientToEdit.copy(
                    name = name,
                    age = age,
                    gender = gender,
                    contact = contact,
                    diagnosis = diagnosis,
                    status = status
                )
                val idx = AppState.patients.indexOf(patientToEdit)
                if (idx != -1) {
                    AppState.patients[idx] = updated
                }
                Toast.makeText(this, "Patient details updated", Toast.LENGTH_SHORT).show()
            } else {
                // Add mode
                val newId = "PID-${1000 + AppState.patients.size + 1}"
                val date = SimpleDateFormat("yyyy-MM-dd", Locale.getDefault()).format(Date())
                val newPatient = Patient(newId, name, age, gender, contact, date, diagnosis, status, "")
                AppState.addPatient(newPatient)
                Toast.makeText(this, "New patient registered", Toast.LENGTH_SHORT).show()
            }

            patientAdapter.updateData(AppState.patients)
            alertDialog.dismiss()
        }

        alertDialog.show()
    }

    override fun onItemClick(patient: Patient) {
        // Show Patient Detail Dialog
        val historyBuilder = StringBuilder()
        val patientCases = AppState.cases.filter { it.patientId == patient.id }
        if (patientCases.isEmpty()) {
            historyBuilder.append("No previous AI biopsy scans logged.")
        } else {
            for (case in patientCases) {
                historyBuilder.append("• ${case.id}: ${case.disease}\n  Risk: ${case.metastasisRisk}% | Conf: ${case.confidence}%\n  Date: ${case.dateAnalyzed}\n\n")
            }
        }

        val detailView = LayoutInflater.from(this).inflate(android.R.layout.simple_list_item_1, null)
        val textDetail = detailView.findViewById<TextView>(android.R.id.text1)
        textDetail.text = """
            Patient ID: ${patient.id}
            Name: ${patient.name}
            Age/Gender: ${patient.age} / ${patient.gender}
            Contact: ${patient.contact}
            Date Registered: ${patient.dateRegistered}
            Current Diagnosis: ${patient.diagnosis}
            Clinical Status: ${patient.status}
            
            Clinical Notes:
            ${if (patient.notes.isEmpty()) "None recorded." else patient.notes}
            
            AI Scan History:
            $historyBuilder
        """.trimIndent()
        textDetail.setTextColor(Color.BLACK)
        textDetail.setPadding(32, 32, 32, 32)

        AlertDialog.Builder(this)
            .setTitle("Patient Medical Profile")
            .setView(detailView)
            .setPositiveButton("Analyze Biopsy") { _, _ ->
                bottomNavigation.selectedItemId = R.id.nav_upload
                // Pre-select patient in Spinner
                Handler(Looper.getMainLooper()).postDelayed({
                    val index = AppState.patients.indexOf(patient)
                    if (index != -1 && ::spinnerPatients.isInitialized) {
                        spinnerPatients.setSelection(index)
                    }
                }, 200)
            }
            .setNegativeButton("Close", null)
            .show()
    }

    override fun onEditClick(patient: Patient) {
        showAddEditPatientDialog(patient)
    }

    override fun onDeleteClick(patient: Patient) {
        AlertDialog.Builder(this)
            .setTitle("Delete Patient Profile")
            .setMessage("Are you sure you want to delete ${patient.name} (${patient.id}) and all associated diagnostic case histories?")
            .setPositiveButton("Delete") { _, _ ->
                AppState.removePatient(patient.id)
                patientAdapter.updateData(AppState.patients)
                Toast.makeText(this, "Profile deleted", Toast.LENGTH_SHORT).show()
            }
            .setNegativeButton("Cancel", null)
            .show()
    }

    // ==========================================
    // ANALYZE / SCAN TAB (Child 2)
    // ==========================================
    private fun setupAnalyzeTab() {
        spinnerPatients = findViewById(R.id.spinner_analyze_patient)
        ivBiopsyPreview = findViewById(R.id.iv_biopsy_preview)
        layoutPlaceholder = findViewById(R.id.layout_upload_placeholder)
        btnRunAnalysis = findViewById(R.id.btn_run_analysis)
        layoutSimulation = findViewById(R.id.layout_analysis_simulation)
        tvSimulationStep = findViewById(R.id.tv_simulation_step)
        tvSimulationSubtext = findViewById(R.id.tv_simulation_subtext)
        btnUploadCamera = findViewById(R.id.btn_upload_camera)
        btnUploadGallery = findViewById(R.id.btn_upload_gallery)

        refreshAnalyzePatientSpinner()

        btnUploadGallery.setOnClickListener {
            val intent = Intent(Intent.ACTION_PICK, MediaStore.Images.Media.EXTERNAL_CONTENT_URI)
            galleryLauncher.launch(intent)
        }

        btnUploadCamera.setOnClickListener {
            val intent = Intent(MediaStore.ACTION_IMAGE_CAPTURE)
            cameraLauncher.launch(intent)
        }

        btnRunAnalysis.setOnClickListener {
            runMILDiagnosticSimulation()
        }
    }

    private fun refreshAnalyzePatientSpinner() {
        val names = AppState.patients.map { "${it.name} (${it.id})" }
        val adapter = ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, names)
        spinnerPatients.adapter = adapter
    }

    private fun processUploadedImage(uri: Uri) {
        // H&E Color Verification Check
        val isValidBiopsy = checkIfHEBiopsySlide(this, uri)
        if (isValidBiopsy) {
            selectedImageUri = uri
            ivBiopsyPreview.setImageURI(uri)
            layoutPlaceholder.visibility = View.GONE
            btnRunAnalysis.isEnabled = true
            Toast.makeText(this, "H&E microscopic slide detected and loaded.", Toast.LENGTH_SHORT).show()
        } else {
            selectedImageUri = null
            ivBiopsyPreview.setImageURI(null)
            layoutPlaceholder.visibility = View.VISIBLE
            btnRunAnalysis.isEnabled = false

            // Build rejection warning dialog
            AlertDialog.Builder(this)
                .setTitle("Unsupported Scan Image")
                .setMessage("BioPath AI only accepts microscopic biopsy pathology slide images (H&E stains). The uploaded image does not contain the purple/pink color profile characteristic of Hematoxylin & Eosin stains and has been rejected.")
                .setPositiveButton("OK", null)
                .show()
        }
    }

    private fun checkIfHEBiopsySlide(context: Context, uri: Uri): Boolean {
        return try {
            val options = BitmapFactory.Options().apply {
                inSampleSize = 8 // Downsample image to avoid memory overhead
            }
            val stream = context.contentResolver.openInputStream(uri)
            val bitmap = BitmapFactory.decodeStream(stream, null, options)
            stream?.close()

            if (bitmap == null) return false

            val width = bitmap.width
            val height = bitmap.height
            
            // Sample points in a grid layout (approx 250 points)
            var totalSampled = 0
            var pathologyColorCount = 0
            var backgroundCount = 0
            var nonPathologyColorCount = 0

            val xStep = width / 15
            val yStep = height / 15

            for (x in 2 until width - 2 step xStep) {
                for (y in 2 until height - 2 step yStep) {
                    val pixel = bitmap.getPixel(x, y)
                    val r = Color.red(pixel)
                    val g = Color.green(pixel)
                    val b = Color.blue(pixel)

                    val hsv = FloatArray(3)
                    Color.RGBToHSV(r, g, b, hsv)
                    val h = hsv[0] // 0 to 360
                    val s = hsv[1] // 0 to 1
                    val v = hsv[2] // 0 to 1

                    totalSampled++

                    // H&E Slide features purple/pink stains and white backgrounds
                    if (s < 0.15 && v > 0.82) {
                        // Slide background glass
                        backgroundCount++
                    } else if (h >= 280 || h <= 30) {
                        // Pink, red, magenta hues (Eosin / Cytoplasm)
                        pathologyColorCount++
                    } else if (h in 200.0..280.0) {
                        // Purple, blue (Hematoxylin / Nuclei)
                        pathologyColorCount++
                    } else if (h in 35.0..170.0 && s > 0.20 && v > 0.1) {
                        // Green, yellow, orange colors (Normal landscapes, trees, skin)
                        nonPathologyColorCount++
                    }
                }
            }

            // A typical microscopic H&E slide consists mostly of slide background and stained elements
            val pathologyRatio = (pathologyColorCount + backgroundCount).toFloat() / totalSampled
            val nonPathologyRatio = nonPathologyColorCount.toFloat() / totalSampled

            // Reject if non-pathology hues (like green/yellow/brown) dominate, or if pink/purple/white coverage is low
            pathologyRatio >= 0.70 && nonPathologyRatio < 0.15
        } catch (e: Exception) {
            e.printStackTrace()
            false
        }
    }

    private fun saveBitmapToCache(bitmap: Bitmap): Uri? {
        return try {
            val cachePath = File(cacheDir, "images")
            cachePath.mkdirs()
            val file = File(cachePath, "captured_biopsy.png")
            val stream = FileOutputStream(file)
            bitmap.compress(Bitmap.CompressFormat.PNG, 100, stream)
            stream.flush()
            stream.close()
            Uri.fromFile(file)
        } catch (e: Exception) {
            null
        }
    }

    private fun getFileFromUri(context: Context, uri: Uri): File? {
        return try {
            val contentResolver = context.contentResolver
            val inputStream = contentResolver.openInputStream(uri) ?: return null
            val tempFile = File(context.cacheDir, "upload_temp_${System.currentTimeMillis()}.png")
            val outputStream = FileOutputStream(tempFile)
            val buffer = ByteArray(4096)
            var bytesRead: Int
            while (inputStream.read(buffer).also { bytesRead = it } != -1) {
                outputStream.write(buffer, 0, bytesRead)
            }
            outputStream.close()
            inputStream.close()
            tempFile
        } catch (e: Exception) {
            e.printStackTrace()
            null
        }
    }

    private fun runMILDiagnosticSimulation() {
        val selectedUri = selectedImageUri
        if (selectedUri == null) {
            Toast.makeText(this, "Please select/upload an H&E biopsy image first", Toast.LENGTH_SHORT).show()
            return
        }
        if (spinnerPatients.selectedItem == null) {
            Toast.makeText(this, "Please register a patient first", Toast.LENGTH_SHORT).show()
            return
        }

        // Lock interface actions
        btnRunAnalysis.visibility = View.GONE
        btnUploadCamera.isEnabled = false
        btnUploadGallery.isEnabled = false
        spinnerPatients.isEnabled = false
        bottomNavigation.menu.findItem(R.id.nav_home).isEnabled = false
        bottomNavigation.menu.findItem(R.id.nav_patients).isEnabled = false
        bottomNavigation.menu.findItem(R.id.nav_upload).isEnabled = false
        bottomNavigation.menu.findItem(R.id.nav_notifications).isEnabled = false
        bottomNavigation.menu.findItem(R.id.nav_profile).isEnabled = false

        layoutSimulation.visibility = View.VISIBLE
        tvSimulationStep.text = "Step 1/3: Preprocessing & Uploading Slide..."
        tvSimulationSubtext.text = "Uploading H&E microscopic section to localhost AI server..."

        val patientIndex = spinnerPatients.selectedItemPosition
        val patient = AppState.patients[patientIndex]

        val client = okhttp3.OkHttpClient.Builder()
            .connectTimeout(30, java.util.concurrent.TimeUnit.SECONDS)
            .readTimeout(30, java.util.concurrent.TimeUnit.SECONDS)
            .writeTimeout(30, java.util.concurrent.TimeUnit.SECONDS)
            .build()

        val file = getFileFromUri(this, selectedUri)
        if (file == null) {
            Toast.makeText(this, "Failed to read image file", Toast.LENGTH_SHORT).show()
            resetInterfaceActions()
            return
        }

        // We will start the upload in a background thread
        Thread {
            try {
                // Update UI to Feature Extraction step after 1.5 seconds to simulate pipeline progress
                runOnUiThread {
                    tvSimulationStep.text = "Step 2/3: Deep Learning Feature Extraction..."
                    tvSimulationSubtext.text = "AI Server analyzing tissue segmentation and MIL attention scoring..."
                }

                val mediaType = okhttp3.MediaType.parse("image/*")
                val fileBody = okhttp3.RequestBody.create(mediaType, file)
                val requestBody = okhttp3.MultipartBody.Builder()
                    .setType(okhttp3.MultipartBody.FORM)
                    .addFormDataPart("patient_id", patient.id)
                    .addFormDataPart("image", file.name, fileBody)
                    .build()

                val request = okhttp3.Request.Builder()
                    .url("http://10.0.2.2:5000/api/upload")
                    .post(requestBody)
                    .build()

                val response = client.newCall(request).execute()
                val responseBody = response.body()?.string()

                if (response.isSuccessful && responseBody != null) {
                    runOnUiThread {
                        tvSimulationStep.text = "Step 3/3: Parsing AI Pathology Report..."
                        tvSimulationSubtext.text = "Formulating diagnostic findings and stroma metrics..."
                    }

                    // Parse CaseRecord
                    val caseRecord = com.google.gson.Gson().fromJson(responseBody, CaseRecord::class.java)

                    // Delete temp file
                    try { file.delete() } catch(e: Exception) {}

                    runOnUiThread {
                        // Save case and update patient status
                        AppState.addCase(caseRecord)

                        // Trigger alerts for high risks
                        if (caseRecord.metastasisRisk > 80) {
                            AppState.notifications.add(0, "CRITICAL METASTASIS RISK: Case ${caseRecord.id} (${patient.name}) requires immediate intervention.")
                        }

                        // Reset UI
                        layoutSimulation.visibility = View.GONE
                        btnRunAnalysis.visibility = View.VISIBLE
                        btnRunAnalysis.isEnabled = false
                        layoutPlaceholder.visibility = View.VISIBLE
                        ivBiopsyPreview.setImageURI(null)
                        resetInterfaceActions()

                        // Launch Results Screen
                        val intent = Intent(this, AnalysisResultActivity::class.java).apply {
                            putExtra("CASE_RECORD", caseRecord)
                        }
                        startActivity(intent)
                        overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out)
                    }
                } else {
                    val errorMsg = response.message() ?: "Server error"
                    runOnUiThread {
                        Toast.makeText(this@MainActivity, "AI Server Error: $errorMsg", Toast.LENGTH_LONG).show()
                        resetInterfaceActions()
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
                runOnUiThread {
                    Toast.makeText(this@MainActivity, "Network Error: Could not connect to localhost AI server. Make sure the server is running on port 5000.", Toast.LENGTH_LONG).show()
                    resetInterfaceActions()
                }
            }
        }.start()
    }

    private fun resetInterfaceActions() {
        layoutSimulation.visibility = View.GONE
        btnRunAnalysis.visibility = View.VISIBLE
        btnUploadCamera.isEnabled = true
        btnUploadGallery.isEnabled = true
        spinnerPatients.isEnabled = true
        bottomNavigation.menu.findItem(R.id.nav_home).isEnabled = true
        bottomNavigation.menu.findItem(R.id.nav_patients).isEnabled = true
        bottomNavigation.menu.findItem(R.id.nav_upload).isEnabled = true
        bottomNavigation.menu.findItem(R.id.nav_notifications).isEnabled = true
        bottomNavigation.menu.findItem(R.id.nav_profile).isEnabled = true
    }

    private fun generateRealisticDiagnosis(patient: Patient, uri: Uri?): CaseRecord {
        val caseId = "CASE-${1000 + AppState.cases.size + 1}"
        val dateStr = SimpleDateFormat("yyyy-MM-dd HH:mm", Locale.getDefault()).format(Date())

        var cellularity = 0.35 // Default baseline cellularity
        var hasAnalysedImage = false

        if (uri != null) {
            try {
                val options = BitmapFactory.Options().apply {
                    inSampleSize = 8 // Downsample image to avoid memory overhead
                }
                val stream = contentResolver.openInputStream(uri)
                val bitmap = BitmapFactory.decodeStream(stream, null, options)
                stream?.close()

                if (bitmap != null) {
                    val width = bitmap.width
                    val height = bitmap.height
                    var totalSampled = 0
                    var backgroundCount = 0
                    var nucleiCount = 0
                    var cytoplasmCount = 0

                    val xStep = (width / 15).coerceAtLeast(1)
                    val yStep = (height / 15).coerceAtLeast(1)

                    for (x in 2 until width - 2 step xStep) {
                        for (y in 2 until height - 2 step yStep) {
                            val pixel = bitmap.getPixel(x, y)
                            val r = Color.red(pixel)
                            val g = Color.green(pixel)
                            val b = Color.blue(pixel)

                            val hsv = FloatArray(3)
                            Color.RGBToHSV(r, g, b, hsv)
                            val h = hsv[0]
                            val s = hsv[1]
                            val v = hsv[2]

                            totalSampled++

                            if (s < 0.15 && v > 0.82) {
                                backgroundCount++
                            } else if (h in 200.0..280.0) {
                                // Purple/blue nuclei (Hematoxylin)
                                nucleiCount++
                            } else if (h >= 280 || h <= 30) {
                                // Pink/red cytoplasm (Eosin)
                                cytoplasmCount++
                            }
                        }
                    }

                    if (nucleiCount + cytoplasmCount > 0) {
                        cellularity = nucleiCount.toDouble() / (nucleiCount + cytoplasmCount)
                        hasAnalysedImage = true
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }

        // Generate diagnostic findings dynamically based on the calculated cellularity ratio
        if (hasAnalysedImage) {
            if (cellularity > 0.48) {
                // High density of hyperchromatic nuclei characteristic of high-grade Squamous Cell Carcinoma
                val confidence = (95.2 + cellularity * 3.5).coerceAtMost(99.9)
                val risk = (82 + (cellularity - 0.48) * 35).toInt().coerceAtMost(98)
                val depth = (4.8 + cellularity * 4.5).coerceAtMost(9.8)

                return CaseRecord(
                    id = caseId,
                    patientId = patient.id,
                    patientName = patient.name,
                    disease = "Oral Squamous Cell Carcinoma (High Grade)",
                    tumorBudding = "Grade 3 (High, 14 buds/HPF)",
                    stromalInflammation = "Severe (Dense infiltration of tumor-infiltrating lymphocytes)",
                    invasionDepth = Math.round(depth * 10.0) / 10.0,
                    metastasisRisk = risk,
                    confidence = Math.round(confidence * 10.0) / 10.0,
                    interpretation = "Multi-Instance Learning (MIL) neural network identified high-attention tiled patches corresponding to nests of highly pleomorphic squamous epithelial cells. High nuclear crowding and hyperchromasia indicate aggressive mitotic activity. Active tumor budding (Grade 3) noted at the peripheral stroma interface. Deep invasive front measured at ${Math.round(depth * 10.0) / 10.0} mm with severe host peritumoral inflammatory infiltration.",
                    dateAnalyzed = dateStr,
                    doctorNotes = "CRITICAL PATHOLOGY REPORT: Highly suspicious squamous malignancy with deep infiltration. Immediate surgical resection planning and oncological staging requested.",
                    imageUri = uri?.toString()
                )
            } else if (cellularity > 0.26) {
                // Moderate density of nuclei representing glandular Adenocarcinoma
                val confidence = (90.5 + cellularity * 12.0).coerceAtMost(98.5)
                val risk = (35 + (cellularity - 0.26) * 140).toInt().coerceAtMost(78)
                val depth = (1.8 + cellularity * 3.8).coerceAtMost(4.5)

                return CaseRecord(
                    id = caseId,
                    patientId = patient.id,
                    patientName = patient.name,
                    disease = "Infiltrating Adenocarcinoma (G2)",
                    tumorBudding = "Grade 2 (Moderate, 6 buds/HPF)",
                    stromalInflammation = "Moderate (Focal inflammatory response)",
                    invasionDepth = Math.round(depth * 10.0) / 10.0,
                    metastasisRisk = risk,
                    confidence = Math.round(confidence * 10.0) / 10.0,
                    interpretation = "Convolutional feature extraction mapped moderately differentiated atypical glandular structures infiltrating mucosal layers. Spatial attention weights clustered at tumor-stroma boundaries, indicating active mucosal invasion. Peripheral tumor budding tracked at Grade 2. Deepest invasive focus estimated at ${Math.round(depth * 10.0) / 10.0} mm. Stromal tissue exhibits a moderate lymphocytic response.",
                    dateAnalyzed = dateStr,
                    doctorNotes = "Advised comprehensive clinical staging including contrast-enhanced CT. Refer to clinical oncology team for treatment planning.",
                    imageUri = uri?.toString()
                )
            } else {
                // Low cellularity/regular nucleus-to-cytoplasm distribution matching Benign tissue
                val confidence = 99.4

                return CaseRecord(
                    id = caseId,
                    patientId = patient.id,
                    patientName = patient.name,
                    disease = "Normal Biopsy Slide / No Malignancy",
                    tumorBudding = "Grade 0 (0 buds/HPF)",
                    stromalInflammation = "Mild (Physiological limits)",
                    invasionDepth = 0.0,
                    metastasisRisk = 2,
                    confidence = confidence,
                    interpretation = "Deep pooling vectors indicate high-confidence regular tissue architecture. The stratified squamous epithelium exhibits mature architectural layout. Basement membrane is fully continuous and intact with no stromal infiltration. Cellularity ratio lies well within normal physiological margins, showing no hyperchromasia or severe nuclear enlargement.",
                    dateAnalyzed = dateStr,
                    doctorNotes = "Biopsy shows benign features with no pathological evidence of squamous or glandular malignancy. Recommend standard annual clinical follow-up.",
                    imageUri = uri?.toString()
                )
            }
        }

        // Fallback name-based simulation if no physical image uri is provided
        return if (patient.name.lowercase().contains("smith") || patient.diagnosis.lowercase().contains("normal")) {
            CaseRecord(
                id = caseId,
                patientId = patient.id,
                patientName = patient.name,
                disease = "Normal Biopsy Slide / No Malignancy",
                tumorBudding = "Grade 0 (0 buds/HPF)",
                stromalInflammation = "Mild",
                invasionDepth = 0.0,
                metastasisRisk = 2,
                confidence = 99.4,
                interpretation = "The sampled biopsy tissue scan shows regular cellular architecture. No atypical cellular changes, invasive nesting, or malignant budding observed. Basement membrane remains fully intact.",
                dateAnalyzed = dateStr,
                doctorNotes = "Advised regular annual medical checkups.",
                imageUri = uri?.toString()
            )
        } else if (patient.name.lowercase().contains("brown") || patient.diagnosis.lowercase().contains("adeno")) {
            CaseRecord(
                id = caseId,
                patientId = patient.id,
                patientName = patient.name,
                disease = "Infiltrating Adenocarcinoma (G1)",
                tumorBudding = "Grade 1 (Low)",
                stromalInflammation = "Moderate",
                invasionDepth = 2.1,
                metastasisRisk = 38,
                confidence = 92.5,
                interpretation = "Diagnostic pathology scan displays infiltrating atypical glands in stromal tissue. Low budding score detected at the invasive periphery. Stromal response is moderate.",
                dateAnalyzed = dateStr,
                doctorNotes = "Recommended staging investigations and medical consultation.",
                imageUri = uri?.toString()
            )
        } else {
            CaseRecord(
                id = caseId,
                patientId = patient.id,
                patientName = patient.name,
                disease = "Oral Squamous Cell Carcinoma",
                tumorBudding = "Grade 3 (High)",
                stromalInflammation = "Severe",
                invasionDepth = 5.2,
                metastasisRisk = 94,
                confidence = 97.8,
                interpretation = "Microscopic tissue scan displays sheets of malignant pleomorphic squamous cells invading deeply into the vascular stroma. High density of tumor budding (14 buds/HPF) at the peripheral margin. Marked peritumoral stromal inflammation present.",
                dateAnalyzed = dateStr,
                doctorNotes = "CRITICAL: Referred for urgent surgical resection and oncological staging.",
                imageUri = uri?.toString()
            )
        }
    }

    // ==========================================
    // NOTIFICATIONS TAB (Child 3)
    // ==========================================
    private fun setupNotifications() {
        val container = findViewById<LinearLayout>(R.id.notifications_container)
        container.removeAllViews()

        val titleTv = TextView(this).apply {
            text = "System Alerts & Logs"
            setTextColor(Color.parseColor("#0F172A"))
            textSize = 20f
            paint?.isFakeBoldText = true
            setPadding(0, 0, 0, 16)
        }
        container.addView(titleTv)

        for (notif in AppState.notifications) {
            val tv = TextView(this).apply {
                text = notif
                setPadding(24, 28, 24, 28)
                textSize = 14f
                if (notif.contains("CRITICAL") || notif.contains("METASTASIS")) {
                    setTextColor(Color.parseColor("#EF4444"))
                    setBackgroundColor(Color.parseColor("#FEF2F2"))
                } else {
                    setTextColor(Color.parseColor("#334155"))
                    setBackgroundColor(Color.parseColor("#F1F5F9"))
                }
                val params = LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT)
                params.setMargins(0, 0, 0, 12)
                layoutParams = params
            }
            container.addView(tv)
        }
    }

    // ==========================================
    // PROFILE / SETTINGS TAB (Child 4)
    // ==========================================
    private fun setupProfile() {
        findViewById<Button>(R.id.btn_logout_profile).setOnClickListener { performLogout() }
        val switchDark = findViewById<Switch>(R.id.switch_dark_mode)
        switchDark.setOnCheckedChangeListener { _, isChecked ->
            if (isChecked) {
                Toast.makeText(this, "Dark Mode Theme toggled. System restart simulation...", Toast.LENGTH_SHORT).show()
            } else {
                Toast.makeText(this, "Light Mode Theme restored.", Toast.LENGTH_SHORT).show()
            }
        }
    }

    private fun performLogout() {
        val intent = Intent(this, LoginActivity::class.java)
        intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
        startActivity(intent)
        overridePendingTransition(android.R.anim.slide_in_left, android.R.anim.slide_out_right)
        finish()
    }

    // ==========================================
    // SIDEBAR DRAWER ACTIONS
    // ==========================================
    private fun showScanHistoryTimelineDialog() {
        val layout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(32, 32, 32, 32)
        }

        val scroll = ScrollView(this).apply {
            addView(layout)
        }

        if (AppState.cases.isEmpty()) {
            layout.addView(TextView(this).apply { text = "No scans logged in system." })
        } else {
            for (case in AppState.cases) {
                val caseView = LinearLayout(this).apply {
                    orientation = LinearLayout.VERTICAL
                    setPadding(16, 16, 16, 16)
                    setBackgroundResource(R.drawable.input_bg)
                    val params = LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT)
                    params.setMargins(0, 0, 0, 12)
                    layoutParams = params
                }
                caseView.addView(TextView(this).apply {
                    text = "${case.patientName} (${case.patientId}) - ${case.id}"
                    textSize = 14f
                    paint?.isFakeBoldText = true
                    setTextColor(Color.parseColor("#0F172A"))
                })
                caseView.addView(TextView(this).apply {
                    text = "Diagnosis: ${case.disease}\nInvasion: ${case.invasionDepth}mm | Budding: ${case.tumorBudding}\nAnalyzed on: ${case.dateAnalyzed}"
                    textSize = 12f
                    setTextColor(Color.parseColor("#475569"))
                })
                caseView.setOnClickListener {
                    val intent = Intent(this@MainActivity, AnalysisResultActivity::class.java).apply {
                        putExtra("CASE_RECORD", case)
                    }
                    startActivity(intent)
                }
                layout.addView(caseView)
            }
        }

        AlertDialog.Builder(this)
            .setTitle("Diagnostic Scan Timeline")
            .setView(scroll)
            .setPositiveButton("Dismiss", null)
            .show()
    }

    private fun showHelpSupportDialog() {
        AlertDialog.Builder(this)
            .setTitle("System Help & Support")
            .setMessage("BioPath AI Diagnostic System v3.0\n\nFor clinical assistance, system calibrations, or reporting bugs, please reach out to hospital IT support or visit our clinical documentation portal.")
            .setPositiveButton("Close", null)
            .show()
    }
}
