package com.pathoai.app

import android.graphics.Color
import android.graphics.drawable.GradientDrawable
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class PatientAdapter(
    private var allPatients: List<Patient>,
    private val listener: OnPatientActionListener
) : RecyclerView.Adapter<PatientAdapter.PatientViewHolder>() {

    private var filteredList = ArrayList<Patient>()

    interface OnPatientActionListener {
        fun onItemClick(patient: Patient)
        fun onEditClick(patient: Patient)
        fun onDeleteClick(patient: Patient)
    }

    init {
        filteredList.addAll(allPatients)
    }

    fun updateData(newList: List<Patient>) {
        allPatients = newList
        filter("") // Reset filter
    }

    fun filter(query: String) {
        filteredList.clear()
        if (query.trim().isEmpty()) {
            filteredList.addAll(allPatients)
        } else {
            val lowerCaseQuery = query.trim().lowercase()
            for (p in allPatients) {
                if (p.name.lowercase().contains(lowerCaseQuery) || p.id.lowercase().contains(lowerCaseQuery)) {
                    filteredList.add(p)
                }
            }
        }
        notifyDataSetChanged()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): PatientViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.patient_item, parent, false)
        return PatientViewHolder(view)
    }

    override fun onBindViewHolder(holder: PatientViewHolder, position: Int) {
        val patient = filteredList[position]
        holder.bind(patient)
    }

    override fun getItemCount(): Int {
        return filteredList.size
    }

    inner class PatientViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        private val tvName: TextView = itemView.findViewById(R.id.tv_patient_name)
        private val tvId: TextView = itemView.findViewById(R.id.tv_patient_id)
        private val tvAgeGender: TextView = itemView.findViewById(R.id.tv_patient_age_gender)
        private val tvDiagnosis: TextView = itemView.findViewById(R.id.tv_patient_diagnosis)
        private val tvContact: TextView = itemView.findViewById(R.id.tv_patient_contact)
        private val tvStatusBadge: TextView = itemView.findViewById(R.id.tv_patient_status_badge)
        private val btnEdit: ImageView = itemView.findViewById(R.id.btn_edit_patient)
        private val btnDelete: ImageView = itemView.findViewById(R.id.btn_delete_patient)

        fun bind(patient: Patient) {
            tvName.text = patient.name
            tvId.text = patient.id
            tvAgeGender.text = "${patient.age} yrs / ${patient.gender}"
            tvDiagnosis.text = patient.diagnosis
            tvContact.text = "Contact: ${patient.contact}"
            tvStatusBadge.text = patient.status

            // Style the risk badge background and text color dynamically
            val badgeDrawable = GradientDrawable().apply {
                cornerRadius = 12f // in pixels
                shape = GradientDrawable.RECTANGLE
            }

            when (patient.status.lowercase()) {
                "critical" -> {
                    badgeDrawable.setColor(Color.parseColor("#EF4444")) // Red
                    tvStatusBadge.setTextColor(Color.WHITE)
                }
                "high risk" -> {
                    badgeDrawable.setColor(Color.parseColor("#F97316")) // Orange
                    tvStatusBadge.setTextColor(Color.WHITE)
                }
                "moderate risk" -> {
                    badgeDrawable.setColor(Color.parseColor("#F59E0B")) // Amber
                    tvStatusBadge.setTextColor(Color.WHITE)
                }
                else -> { // Clear / Normal
                    badgeDrawable.setColor(Color.parseColor("#10B981")) // Green
                    tvStatusBadge.setTextColor(Color.WHITE)
                }
            }
            tvStatusBadge.background = badgeDrawable

            itemView.setOnClickListener { listener.onItemClick(patient) }
            btnEdit.setOnClickListener { listener.onEditClick(patient) }
            btnDelete.setOnClickListener { listener.onDeleteClick(patient) }
        }
    }
}
