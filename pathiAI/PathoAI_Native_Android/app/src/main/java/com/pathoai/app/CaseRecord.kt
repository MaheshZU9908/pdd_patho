package com.pathoai.app

import java.io.Serializable

data class CaseRecord(
    val id: String,
    val patientId: String,
    val patientName: String,
    val disease: String,
    val tumorBudding: String,
    val stromalInflammation: String,
    val invasionDepth: Double,
    val metastasisRisk: Int,
    val confidence: Double,
    val interpretation: String,
    val dateAnalyzed: String,
    var doctorNotes: String,
    val imageUri: String?
) : Serializable
