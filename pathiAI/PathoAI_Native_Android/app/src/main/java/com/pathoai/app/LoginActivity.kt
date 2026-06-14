package com.pathoai.app

import android.content.Intent
import android.os.Bundle
import android.util.Patterns
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast
import android.widget.ViewFlipper
import androidx.appcompat.app.AppCompatActivity

class LoginActivity : AppCompatActivity() {

    private lateinit var authViewFlipper: ViewFlipper

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        authViewFlipper = findViewById(R.id.authViewFlipper)

        setupLoginView()
        setupSignupView()
        setupForgotPasswordView()
        setupOtpView()
    }

    private fun setupLoginView() {
        val btnLogin = findViewById<Button>(R.id.btn_login)
        val tvGoSignup = findViewById<TextView>(R.id.tv_go_signup)
        val tvForgotPassword = findViewById<TextView>(R.id.tv_forgot_password)
        val etEmail = findViewById<EditText>(R.id.et_email)
        val etPassword = findViewById<EditText>(R.id.et_password)

        btnLogin.setOnClickListener {
            val email = etEmail.text.toString().trim()
            val password = etPassword.text.toString().trim()

            if (email.isEmpty() || !Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
                etEmail.error = "Valid Email Required"
                return@setOnClickListener
            }
            if (password.length < 6) {
                etPassword.error = "Password must be at least 6 characters"
                return@setOnClickListener
            }

            // Simulate Login Success
            startActivity(Intent(this, MainActivity::class.java))
            overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out)
            finish()
        }

        tvGoSignup.setOnClickListener {
            authViewFlipper.displayedChild = 1 // Signup
        }

        tvForgotPassword.setOnClickListener {
            authViewFlipper.displayedChild = 2 // Forgot Password
        }
    }

    private fun setupSignupView() {
        val btnSignup = findViewById<Button>(R.id.btn_signup)
        val tvGoLogin = findViewById<TextView>(R.id.tv_go_login)
        
        val etName = findViewById<EditText>(R.id.et_signup_name)
        val etEmail = findViewById<EditText>(R.id.et_signup_email)
        val etPassword = findViewById<EditText>(R.id.et_signup_password)

        btnSignup.setOnClickListener {
            val name = etName.text.toString().trim()
            val email = etEmail.text.toString().trim()
            val password = etPassword.text.toString().trim()

            if (name.isEmpty()) {
                etName.error = "Name Required"
                return@setOnClickListener
            }
            if (email.isEmpty() || !Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
                etEmail.error = "Valid Email Required"
                return@setOnClickListener
            }
            if (password.length < 6) {
                etPassword.error = "Password must be at least 6 characters"
                return@setOnClickListener
            }

            Toast.makeText(this, "Account Created Successfully", Toast.LENGTH_SHORT).show()
            authViewFlipper.displayedChild = 0 // Back to Login
        }

        tvGoLogin.setOnClickListener {
            authViewFlipper.displayedChild = 0 // Login
        }
    }

    private fun setupForgotPasswordView() {
        val btnSendOtp = findViewById<Button>(R.id.btn_send_otp)
        val etEmail = findViewById<EditText>(R.id.et_reset_email)
        val tvBackToLogin = findViewById<TextView>(R.id.tv_back_to_login_from_reset)

        btnSendOtp.setOnClickListener {
            val email = etEmail.text.toString().trim()
            if (email.isEmpty() || !Patterns.EMAIL_ADDRESS.matcher(email).matches()) {
                etEmail.error = "Valid Email Required"
                return@setOnClickListener
            }
            Toast.makeText(this, "OTP Sent to Email", Toast.LENGTH_SHORT).show()
            authViewFlipper.displayedChild = 3 // Go to OTP
        }

        tvBackToLogin.setOnClickListener {
            authViewFlipper.displayedChild = 0
        }
    }

    private fun setupOtpView() {
        val btnVerifyOtp = findViewById<Button>(R.id.btn_verify_otp)
        val etOtp = findViewById<EditText>(R.id.et_otp)
        val tvBackToLogin = findViewById<TextView>(R.id.tv_back_to_login_from_otp)

        btnVerifyOtp.setOnClickListener {
            val otp = etOtp.text.toString().trim()
            if (otp.length != 4) {
                etOtp.error = "Enter valid 4-digit OTP"
                return@setOnClickListener
            }
            Toast.makeText(this, "OTP Verified. Logging in...", Toast.LENGTH_SHORT).show()
            startActivity(Intent(this, MainActivity::class.java))
            overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out)
            finish()
        }

        tvBackToLogin.setOnClickListener {
            authViewFlipper.displayedChild = 0
        }
    }
}
