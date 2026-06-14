// Minimal JavaScript for PathoAI UI
// This script provides stub implementations for UI functions referenced in index.html.
// It ensures the app loads without JS errors and enables basic prediction request.

// Utility to show a simple toast (optional)
function showToast(message) {
  console.log('Toast:', message);
}

// Navigation between main views
function switchView(viewId) {
  document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
  const el = document.getElementById(viewId);
  if (el) el.classList.add('active');
}

// Navigation between sub-views within main app
function switchSubView(viewId, elem) {
  // Update active nav item
  document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
  if (elem) elem.classList.add('active');
  // Show sub-view
  document.querySelectorAll('.sub-view').forEach(v => v.classList.remove('active'));
  const sv = document.getElementById(viewId);
  if (sv) sv.classList.add('active');
}

// Simple login handler (placeholder)
function handleLogin() {
  // In real app, validate credentials. Here we just switch to main app.
  switchView('app-main');
  showToast('Logged in (demo)');
}

// Placeholder for other UI actions
function filterPatientsList() { /* no-op */ }
function openPatientModal(mode) { /* no-op */ }
function closePatientModal() { /* no-op */ }
function savePatientRecord() { /* no-op */ }
function removeSelectedSlide() { /* no-op */ }
function handleImageSelection(event) { /* no-op */ }
function loadSampleSlide() { /* no-op */ }
function triggerPDFReportDownload() { /* no-op */ }
function saveCurrentCaseRecord() { /* no-op */ }
function openZoomMagnifier() { /* no-op */ }
function closeZoomMagnifier() { /* no-op */ }

// Initiate MIL analysis: send selected image to backend /predict endpoint
async function initiateMILAnalysis() {
  const fileInput = document.getElementById('fileInput');
  if (!fileInput || !fileInput.files.length) {
    showToast('Please select an image first');
    return;
  }
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append('file', file);
  try {
    const response = await fetch('/predict', {
      method: 'POST',
      body: formData,
    });
    if (!response.ok) throw new Error('Server error');
    const data = await response.json();
    console.log('Prediction result:', data);
    alert(`Result: ${data.label}\nConfidence: ${data.confidence}`);
  } catch (err) {
    console.error(err);
    alert('Prediction failed: ' + err.message);
  }
}

// Ensure the upload button is enabled when a file is selected
document.addEventListener('DOMContentLoaded', () => {
  const fileInput = document.getElementById('fileInput');
  if (fileInput) {
    fileInput.addEventListener('change', () => {
      const btn = document.getElementById('btn-run-analysis');
      if (btn) btn.disabled = false;
    });
  }
});
