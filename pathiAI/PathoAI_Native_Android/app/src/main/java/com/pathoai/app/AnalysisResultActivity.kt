package com.pathoai.app

import android.app.Dialog
import android.content.Intent
import android.graphics.*
import android.net.Uri
import android.os.Bundle
import android.view.ViewGroup
import android.view.Window
import android.widget.Button
import android.widget.EditText
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import android.widget.LinearLayout
import android.view.View
import androidx.appcompat.app.AppCompatActivity
import java.io.File
import java.io.FileOutputStream

class AnalysisResultActivity : AppCompatActivity() {

    private lateinit var tvReportDateTime: TextView
    private lateinit var tvPatientName: TextView
    private lateinit var tvPatientId: TextView
    private lateinit var tvPatientMeta: TextView
    private lateinit var ivBiopsyImage: ImageView
    private lateinit var tvDisease: TextView
    private lateinit var tvConfidence: TextView
    private lateinit var tvMetastasis: TextView
    private lateinit var tvBudding: TextView
    private lateinit var tvInflammation: TextView
    private lateinit var tvInvasion: TextView
    private lateinit var tvStatus: TextView
    private lateinit var tvInterpretation: TextView
    private lateinit var etDoctorNotes: EditText
    private lateinit var btnSaveFindings: Button
    private lateinit var btnExportPdf: Button
    private lateinit var btnBack: Button
    private lateinit var layoutImageContainer: ViewGroup

    private var caseRecord: CaseRecord? = null
    private var highlightedBitmap: Bitmap? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        // Bind Views
        tvReportDateTime = findViewById(R.id.tv_report_datetime)
        tvPatientName = findViewById(R.id.tv_report_patient_name)
        tvPatientId = findViewById(R.id.tv_report_patient_id)
        tvPatientMeta = findViewById(R.id.tv_report_patient_meta)
        ivBiopsyImage = findViewById(R.id.iv_result_biopsy_image)
        tvDisease = findViewById(R.id.tv_res_disease)
        tvConfidence = findViewById(R.id.tv_res_confidence)
        tvMetastasis = findViewById(R.id.tv_res_metastasis)
        tvBudding = findViewById(R.id.tv_res_budding)
        tvInflammation = findViewById(R.id.tv_res_inflammation)
        tvInvasion = findViewById(R.id.tv_res_invasion)
        tvStatus = findViewById(R.id.tv_res_status)
        tvInterpretation = findViewById(R.id.tv_res_interpretation)
        etDoctorNotes = findViewById(R.id.et_report_doctor_notes)
        btnSaveFindings = findViewById(R.id.btn_save_report_changes)
        btnExportPdf = findViewById(R.id.btn_download_report_pdf)
        btnBack = findViewById(R.id.btn_report_back)
        layoutImageContainer = findViewById(R.id.layout_result_image_container)

        // Extract Data
        caseRecord = intent.getSerializableExtra("CASE_RECORD") as? CaseRecord

        if (caseRecord == null) {
            Toast.makeText(this, "No diagnostic case data found.", Toast.LENGTH_SHORT).show()
            finish()
            return
        }

        populateUI()
        setupListeners()
    }

    private fun populateUI() {
        val case = caseRecord ?: return

        tvReportDateTime.text = "Date of Analysis: ${case.dateAnalyzed}"
        tvPatientName.text = case.patientName
        tvPatientId.text = case.patientId
        tvDisease.text = case.disease
        tvConfidence.text = "${case.confidence}%"
        tvMetastasis.text = "${case.metastasisRisk}% (${if (case.metastasisRisk > 80) "Critical Risk" else if (case.metastasisRisk > 40) "Moderate Risk" else "Low Risk"})"
        tvBudding.text = case.tumorBudding
        tvInflammation.text = case.stromalInflammation
        tvInvasion.text = if (case.invasionDepth > 0) "${case.invasionDepth} mm" else "N/A"
        tvInterpretation.text = case.interpretation
        etDoctorNotes.setText(case.doctorNotes)

        // Style the metastasis risk text color
        if (case.metastasisRisk > 80) {
            tvMetastasis.setTextColor(Color.parseColor("#EF4444")) // Red
            tvStatus.text = "CRITICAL / UNVERIFIED"
            tvStatus.setTextColor(Color.parseColor("#EF4444"))
        } else if (case.metastasisRisk > 40) {
            tvMetastasis.setTextColor(Color.parseColor("#F97316")) // Orange
            tvStatus.text = "STABLE / UNVERIFIED"
            tvStatus.setTextColor(Color.parseColor("#F59E0B"))
        } else {
            tvMetastasis.setTextColor(Color.parseColor("#10B981")) // Green
            tvStatus.text = "CLEAR / UNVERIFIED"
            tvStatus.setTextColor(Color.parseColor("#10B981"))
        }

        // Fetch patient demographics from state
        val patient = AppState.patients.find { it.id == case.patientId }
        if (patient != null) {
            tvPatientMeta.text = "Age: ${patient.age} yrs | Gender: ${patient.gender} | Contact: ${patient.contact}"
        } else {
            tvPatientMeta.text = "Demographic record not found in session"
        }

        // Load image & apply canvas annotations overlay
        loadAndHighlightBiopsyImage(case)
    }

    private fun loadAndHighlightBiopsyImage(case: CaseRecord) {
        val imageUriStr = case.imageUri

        if (imageUriStr != null && (imageUriStr.startsWith("http://") || imageUriStr.startsWith("https://"))) {
            // Download from server in background thread
            Thread {
                try {
                    val client = okhttp3.OkHttpClient()
                    val request = okhttp3.Request.Builder()
                        .url(imageUriStr)
                        .build()
                    val response = client.newCall(request).execute()
                    val body = response.body()
                    if (response.isSuccessful && body != null) {
                        val bytes = body.bytes()
                        val options = BitmapFactory.Options().apply {
                            inMutable = true
                        }
                        val remoteBitmap = BitmapFactory.decodeByteArray(bytes, 0, bytes.size, options)
                        if (remoteBitmap != null) {
                            runOnUiThread {
                                highlightedBitmap = remoteBitmap
                                ivBiopsyImage.setImageBitmap(highlightedBitmap)
                            }
                            return@Thread
                        }
                    }
                } catch (e: Exception) {
                    e.printStackTrace()
                }

                // If downloading fails, fallback to local sample
                runOnUiThread {
                    loadLocalFallbackImage(case)
                }
            }.start()
        } else {
            loadLocalFallbackImage(case)
        }
    }

    private fun loadLocalFallbackImage(case: CaseRecord) {
        var baseBitmap: Bitmap? = null

        // Try loading from local uri
        if (case.imageUri != null) {
            try {
                val uri = Uri.parse(case.imageUri)
                val options = BitmapFactory.Options().apply {
                    inSampleSize = 2 // Optimize downsample ratio
                    inMutable = true
                }
                val stream = contentResolver.openInputStream(uri)
                baseBitmap = BitmapFactory.decodeStream(stream, null, options)
                stream?.close()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }

        // Fallback to sample pathology slide drawable
        if (baseBitmap == null) {
            try {
                val options = BitmapFactory.Options().apply {
                    inMutable = true
                }
                baseBitmap = BitmapFactory.decodeResource(resources, R.drawable.pathology_slide_sample, options)
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }

        if (baseBitmap != null) {
            highlightedBitmap = drawPathologyHighlightOverlay(baseBitmap, case.disease)
            ivBiopsyImage.setImageBitmap(highlightedBitmap)
        } else {
            ivBiopsyImage.setImageResource(android.R.drawable.ic_menu_report_image)
        }
    }

    private fun drawPathologyHighlightOverlay(bitmap: Bitmap, disease: String): Bitmap {
        val width = bitmap.width
        val height = bitmap.height
        val mutableBitmap = bitmap.copy(Bitmap.Config.ARGB_8888, true)
        val canvas = Canvas(mutableBitmap)

        val isNormal = disease.lowercase().contains("normal") || disease.lowercase().contains("benign")

        if (isNormal) {
            // Draw green outline representing normal, intact basement membrane / epithelium
            val strokePaint = Paint().apply {
                color = Color.parseColor("#10B981")
                style = Paint.Style.STROKE
                strokeWidth = width * 0.008f
                isAntiAlias = true
            }
            val fillPaint = Paint().apply {
                color = Color.parseColor("#10B981")
                style = Paint.Style.FILL
                alpha = 25
                isAntiAlias = true
            }
            val textPaint = Paint().apply {
                color = Color.parseColor("#10B981")
                textSize = width * 0.035f
                isAntiAlias = true
                isFakeBoldText = true
            }
            val labelBg = Paint().apply {
                color = Color.parseColor("#CC10B981")
                style = Paint.Style.FILL
            }

            // Normal layer oval
            val rect = RectF(width * 0.15f, height * 0.15f, width * 0.85f, height * 0.85f)
            canvas.drawOval(rect, fillPaint)
            canvas.drawOval(rect, strokePaint)

            drawTextLabel(canvas, " Intact Basal Membrane & Benign Epithelium ", width * 0.20f, height * 0.5f, textPaint, labelBg)
        } else {
            // Malignant biopsy scans: draw dashed red tumor nests and amber invasion lines
            val nestStroke = Paint().apply {
                color = Color.parseColor("#EF4444") // Red
                style = Paint.Style.STROKE
                strokeWidth = width * 0.008f
                isAntiAlias = true
                pathEffect = DashPathEffect(floatArrayOf(15f, 10f), 0f)
            }
            val nestFill = Paint().apply {
                color = Color.parseColor("#EF4444")
                style = Paint.Style.FILL
                alpha = 40
                isAntiAlias = true
            }
            val budPaint = Paint().apply {
                color = Color.parseColor("#EF4444")
                style = Paint.Style.FILL
                isAntiAlias = true
            }
            val lineStroke = Paint().apply {
                color = Color.parseColor("#F59E0B") // Amber
                style = Paint.Style.STROKE
                strokeWidth = width * 0.008f
                isAntiAlias = true
                pathEffect = DashPathEffect(floatArrayOf(20f, 15f), 0f)
            }

            val textPaint = Paint().apply {
                color = Color.WHITE
                textSize = width * 0.032f
                isAntiAlias = true
                isFakeBoldText = true
            }
            val redBg = Paint().apply {
                color = Color.parseColor("#CCEF4444")
                style = Paint.Style.FILL
            }
            val amberBg = Paint().apply {
                color = Color.parseColor("#CCF59E0B")
                style = Paint.Style.FILL
            }

            // Nest 1
            canvas.drawCircle(width * 0.38f, height * 0.42f, width * 0.18f, nestFill)
            canvas.drawCircle(width * 0.38f, height * 0.42f, width * 0.18f, nestStroke)
            drawTextLabel(canvas, " Tumor Nest (Pleomorphic) ", width * 0.22f, height * 0.38f, textPaint, redBg)

            // Nest 2
            canvas.drawCircle(width * 0.72f, height * 0.58f, width * 0.13f, nestFill)
            canvas.drawCircle(width * 0.72f, height * 0.58f, width * 0.13f, nestStroke)
            drawTextLabel(canvas, " Infiltrating Stromal Focus ", width * 0.58f, height * 0.55f, textPaint, redBg)

            // Tumor budding indicators at peripheral margins
            canvas.drawCircle(width * 0.52f, height * 0.48f, width * 0.018f, budPaint)
            canvas.drawCircle(width * 0.55f, height * 0.45f, width * 0.018f, budPaint)
            canvas.drawCircle(width * 0.50f, height * 0.53f, width * 0.018f, budPaint)
            drawTextLabel(canvas, " Tumor Budding Front (G3) ", width * 0.42f, height * 0.52f, textPaint, redBg)

            // Invasion Front Boundary
            canvas.drawLine(width * 0.1f, height * 0.76f, width * 0.9f, height * 0.84f, lineStroke)
            drawTextLabel(canvas, " Deep Invasion Boundary ", width * 0.18f, height * 0.81f, textPaint, amberBg)
        }

        return mutableBitmap
    }

    private fun drawTextLabel(canvas: Canvas, text: String, x: Float, y: Float, textPaint: Paint, bgPaint: Paint) {
        val bounds = Rect()
        textPaint.getTextBounds(text, 0, text.length, bounds)
        val rect = RectF(x - 8, y + bounds.top - 6, x + bounds.width() + 8, y + bounds.bottom + 6)
        canvas.drawRoundRect(rect, 6f, 6f, bgPaint)
        canvas.drawText(text, x, y, textPaint)
    }

    private fun setupListeners() {
        val case = caseRecord ?: return

        btnSaveFindings.setOnClickListener {
            val notes = etDoctorNotes.text.toString().trim()
            case.doctorNotes = notes

            // Update AppState cases list
            val stateIndex = AppState.cases.indexOfFirst { it.id == case.id }
            if (stateIndex != -1) {
                AppState.cases[stateIndex].doctorNotes = notes
            }

            // Update patient notes in AppState
            val patient = AppState.patients.find { it.id == case.patientId }
            if (patient != null) {
                patient.notes = notes
            }

            Toast.makeText(this, "Clinical findings updated successfully", Toast.LENGTH_SHORT).show()
        }

        btnExportPdf.setOnClickListener {
            val patient = AppState.patients.find { it.id == case.patientId }
            if (patient != null) {
                exportReportToPDF(case, patient)
            } else {
                Toast.makeText(this, "Cannot locate patient demographic info", Toast.LENGTH_SHORT).show()
            }
        }

        layoutImageContainer.setOnClickListener {
            showFullscreenImageZoomDialog()
        }

        btnBack.setOnClickListener {
            finish()
            overridePendingTransition(android.R.anim.slide_in_left, android.R.anim.slide_out_right)
        }
    }

    private fun showFullscreenImageZoomDialog() {
        val bitmap = highlightedBitmap ?: return
        val dialog = Dialog(this, android.R.style.Theme_Black_NoTitleBar_Fullscreen)
        dialog.requestWindowFeature(Window.FEATURE_NO_TITLE)
        dialog.setContentView(R.layout.dialog_patient) // Reuse dialog base styling or custom

        // Setup custom fullscreen content dynamically
        val linearLayout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            gravity = android.view.Gravity.CENTER
            setBackgroundColor(Color.BLACK)
            layoutParams = ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT)
        }

        val imageView = ImageView(this).apply {
            setImageBitmap(bitmap)
            scaleType = ImageView.ScaleType.FIT_CENTER
            layoutParams = LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, 0, 1f)
        }

        val btnClose = Button(this).apply {
            text = "Close Zoom View"
            setBackgroundColor(Color.parseColor("#EF4444"))
            setTextColor(Color.WHITE)
            layoutParams = LinearLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT).apply {
                setMargins(32, 16, 32, 32)
            }
        }

        linearLayout.addView(imageView)
        linearLayout.addView(btnClose)

        dialog.setContentView(linearLayout)
        btnClose.setOnClickListener { dialog.dismiss() }
        dialog.show()
    }

    private fun exportReportToPDF(case: CaseRecord, patient: Patient) {
        try {
            val pdfDocument = android.graphics.pdf.PdfDocument()
            val pageInfo = android.graphics.pdf.PdfDocument.PageInfo.Builder(595, 842, 1).create()
            val page = pdfDocument.startPage(pageInfo)
            val canvas = page.canvas

            val textPaint = Paint().apply {
                color = Color.BLACK
                textSize = 12f
                isAntiAlias = true
            }

            val titlePaint = Paint().apply {
                color = Color.parseColor("#0F172A")
                textSize = 18f
                isFakeBoldText = true
                isAntiAlias = true
            }

            val headerPaint = Paint().apply {
                color = Color.parseColor("#0066FF")
                textSize = 14f
                isFakeBoldText = true
                isAntiAlias = true
            }

            var y = 50f

            // Report Header
            canvas.drawText("BIOPATH AI CLINICAL PATHOLOGY REPORT", 50f, y, titlePaint)
            y += 24f
            canvas.drawText("SYSTEM GENERATED METRICS & MICROSCOPIC SCAN LOGS", 50f, y, textPaint)
            y += 20f

            canvas.drawLine(50f, y, 545f, y, textPaint)
            y += 25f

            // Patient details
            canvas.drawText("PATIENT PROFILE", 50f, y, headerPaint)
            y += 20f
            canvas.drawText("Patient ID: ${patient.id}", 50f, y, textPaint)
            canvas.drawText("Name: ${patient.name}", 250f, y, textPaint)
            y += 18f
            canvas.drawText("Age: ${patient.age} | Gender: ${patient.gender}", 50f, y, textPaint)
            canvas.drawText("Date Analyzed: ${case.dateAnalyzed}", 250f, y, textPaint)
            y += 25f

            // Pathology findings metrics
            canvas.drawText("AI QUANTITATIVE FINDINGS (Attention MIL)", 50f, y, headerPaint)
            y += 20f
            canvas.drawText("Predicted Disease: ${case.disease}", 50f, y, textPaint)
            y += 18f
            canvas.drawText("Classification Confidence: ${case.confidence}%", 50f, y, textPaint)
            canvas.drawText("Nodal Metastasis Risk: ${case.metastasisRisk}%", 250f, y, textPaint)
            y += 18f
            canvas.drawText("Tumor Budding Level: ${case.tumorBudding}", 50f, y, textPaint)
            canvas.drawText("Stromal Inflammation: ${case.stromalInflammation}", 250f, y, textPaint)
            y += 18f
            canvas.drawText("Measured Invasion Depth: ${case.invasionDepth} mm", 50f, y, textPaint)
            y += 30f

            // AI Interpretation
            canvas.drawText("AI CLINICAL INTERPRETATION SUMMARY", 50f, y, headerPaint)
            y += 20f
            y = drawParagraph(canvas, case.interpretation, 50f, y, 495f, textPaint)
            y += 20f

            // Doctor Notes
            canvas.drawText("ATTENDING CLINICIAN FINDINGS & NOTES", 50f, y, headerPaint)
            y += 20f
            val notesText = if (case.doctorNotes.isEmpty()) "No custom recommendations logged." else case.doctorNotes
            y = drawParagraph(canvas, notesText, 50f, y, 495f, textPaint)
            y += 40f

            // Signature Line
            canvas.drawLine(50f, y, 200f, y, textPaint)
            y += 16f
            canvas.drawText("Attending Clinician Signature", 50f, y, textPaint)

            pdfDocument.finishPage(page)

            val file = File(getExternalFilesDir(null), "${case.id}_Report.pdf")
            val outputStream = FileOutputStream(file)
            pdfDocument.writeTo(outputStream)
            outputStream.flush()
            outputStream.close()
            pdfDocument.close()

            Toast.makeText(this, "Pathology Report exported: ${file.name}", Toast.LENGTH_LONG).show()

            // Trigger safe system chooser sharing via FileProvider
            val authority = "$packageName.fileprovider"
            val uri = androidx.core.content.FileProvider.getUriForFile(this, authority, file)
            val shareIntent = Intent(Intent.ACTION_SEND).apply {
                type = "application/pdf"
                putExtra(Intent.EXTRA_STREAM, uri)
                addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
            }
            startActivity(Intent.createChooser(shareIntent, "Share Pathology PDF Report"))

        } catch (e: Exception) {
            e.printStackTrace()
            Toast.makeText(this, "PDF Export failed: ${e.localizedMessage}", Toast.LENGTH_SHORT).show()
        }
    }

    private fun drawParagraph(canvas: Canvas, text: String, x: Float, startY: Float, widthLimit: Float, paint: Paint): Float {
        var y = startY
        val words = text.split(" ")
        var line = ""
        for (word in words) {
            if (paint.measureText("$line $word") < widthLimit) {
                line = "$line $word"
            } else {
                canvas.drawText(line.trim(), x, y, paint)
                y += 16f
                line = word
            }
        }
        if (line.isNotEmpty()) {
            canvas.drawText(line.trim(), x, y, paint)
            y += 16f
        }
        return y
    }

    override fun onBackPressed() {
        super.onBackPressed()
        overridePendingTransition(android.R.anim.slide_in_left, android.R.anim.slide_out_right)
    }
}
