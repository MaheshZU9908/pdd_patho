package com.pathoai.app

object AppState {
    
    val patients = mutableListOf<Patient>()
    val cases = mutableListOf<CaseRecord>()
    val notifications = mutableListOf<String>()

    init {
        // Prepopulate default patients
        patients.add(Patient("PID-1021", "John Doe", 54, "Male", "+1-555-0192", "2026-05-10", "Invasive Carcinoma", "High Risk", "Advised surgical resection."))
        patients.add(Patient("PID-1022", "Jane Smith", 42, "Female", "+1-555-0143", "2026-05-12", "Normal Tissue", "Clear", "No malignancy detected. Regular screening in 1 year."))
        patients.add(Patient("PID-1023", "Robert Brown", 68, "Male", "+1-555-0185", "2026-05-14", "Adenocarcinoma", "Moderate Risk", "Follow-up endoscopy scheduled."))
        patients.add(Patient("PID-1024", "Emily Davis", 31, "Female", "+1-555-0111", "2026-05-15", "Squamous Cell Carcinoma", "Critical", "Urgent oncological consultation recommended."))

        // Prepopulate default cases
        cases.add(CaseRecord(
            id = "CASE-1001",
            patientId = "PID-1021",
            patientName = "John Doe",
            disease = "Invasive Ductal Carcinoma",
            tumorBudding = "Grade 2 (Moderate)",
            stromalInflammation = "Moderate",
            invasionDepth = 3.5,
            metastasisRisk = 72,
            confidence = 94.8,
            interpretation = "Section shows infiltration of cohesive nests of malignant epithelial cells. Moderate tumor budding (5 buds/HPF) observed at the invasive front. Moderate lymphoplasmacytic stromal response present.",
            dateAnalyzed = "2026-05-10 14:30",
            doctorNotes = "Scheduled for surgical consult.",
            imageUri = null
        ))

        cases.add(CaseRecord(
            id = "CASE-1002",
            patientId = "PID-1023",
            patientName = "Robert Brown",
            disease = "Adenocarcinoma",
            tumorBudding = "Grade 1 (Low)",
            stromalInflammation = "Mild",
            invasionDepth = 1.8,
            metastasisRisk = 45,
            confidence = 91.2,
            interpretation = "Well-differentiated neoplastic glandular structures infiltrating the submucosal stroma. Low budding score (2 buds/HPF). Mild peritumoral inflammatory response.",
            dateAnalyzed = "2026-05-14 11:15",
            doctorNotes = "Prescribed initial therapy cycles.",
            imageUri = null
        ))

        cases.add(CaseRecord(
            id = "CASE-1003",
            patientId = "PID-1024",
            patientName = "Emily Davis",
            disease = "Oral Squamous Cell Carcinoma",
            tumorBudding = "Grade 3 (High)",
            stromalInflammation = "Severe",
            invasionDepth = 5.6,
            metastasisRisk = 98,
            confidence = 98.7,
            interpretation = "Malignant squamous cells invading deeply into muscle and bone. High tumor budding (12 buds/HPF) at the peripheral boundary. Marked stromal inflammation and cellular atypia.",
            dateAnalyzed = "2026-05-15 09:45",
            doctorNotes = "CRITICAL: Patient notified. Urgent staging CT scheduled.",
            imageUri = null
        ))

        // Prepopulate default alerts
        notifications.add("CRITICAL ALERT: PID-1024 requires urgent review (98% Metastasis Risk)")
        notifications.add("System Notification: AI ResNet-MIL pathology model v3.0 deployed successfully.")
        notifications.add("Worklist Update: Dr. Sarah, 3 clinical pathology reports are pending signature.")
        notifications.add("QC Alert: Slight illumination artifact detected in slide upload PID-1029.")
    }

    fun addPatient(patient: Patient) {
        patients.add(0, patient)
    }

    fun removePatient(patientId: String) {
        patients.removeAll { it.id == patientId }
        cases.removeAll { it.patientId == patientId }
    }

    fun addCase(caseRecord: CaseRecord) {
        cases.add(0, caseRecord)
        // Also update patient's diagnosis and status
        val patient = patients.find { it.id == caseRecord.patientId }
        if (patient != null) {
            val updated = patient.copy(
                diagnosis = caseRecord.disease,
                status = if (caseRecord.metastasisRisk > 80) "Critical" 
                         else if (caseRecord.metastasisRisk > 50) "High Risk" 
                         else if (caseRecord.metastasisRisk > 20) "Moderate Risk" 
                         else "Clear"
            )
            val index = patients.indexOf(patient)
            if (index != -1) {
                patients[index] = updated
            }
        }
    }
}
