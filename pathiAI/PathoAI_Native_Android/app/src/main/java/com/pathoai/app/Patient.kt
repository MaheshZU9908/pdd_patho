package com.pathoai.app

data class Patient(
    val id: String,
    val name: String,
    val age: Int,
    val gender: String,
    val contact: String,
    val dateRegistered: String,
    val diagnosis: String,
    val status: String,
    var notes: String
)
