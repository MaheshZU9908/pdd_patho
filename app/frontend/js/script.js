// PathoAI Clinical Suite Controller
document.addEventListener('DOMContentLoaded', () => {
    
    // --- 1. GLOBAL CLINICAL DATA STATE ---
    let patients = [
        {
            id: "PID-8821",
            name: "Sarah Jenkins",
            age: 54,
            gender: "Female",
            dateRegistered: "2026-05-12",
            diagnosis: "Breast Tissue",
            status: "High Risk",
            notes: "Referral due to suspicious dense mass in upper outer quadrant of left breast. Core biopsy obtained under ultrasound guidance."
        },
        {
            id: "PID-7742",
            name: "Marcus Vance",
            age: 62,
            gender: "Male",
            dateRegistered: "2026-05-18",
            diagnosis: "Colon Polyps",
            status: "Low Risk",
            notes: "History of adenomatous polyps. Surveillance colonoscopy identified a 15mm sessile polyp in descending colon."
        },
        {
            id: "PID-1029",
            name: "Clara Oswald",
            age: 48,
            gender: "Female",
            dateRegistered: "2026-05-25",
            diagnosis: "Breast Tissue",
            status: "High Risk",
            notes: "Screening mammogram revealed suspicious microcalcifications. Core needle biopsy requested."
        }
    ];

    let caseRecords = [
        {
            id: "SCAN-1092-23",
            patientId: "PID-8821",
            patientName: "Sarah Jenkins",
            disease: "Invasive Ductal Carcinoma (NST)",
            tumorBudding: "Grade 3 (High)",
            stromalInflammation: "34%",
            invasionDepth: "4.2 mm",
            metastasisRisk: 84,
            confidence: "98.4%",
            interpretation: "Histopathology shows infiltrating nests and cords of neoplastic ductal epithelial cells exhibiting marked cytological atypia and mitotic activity. Tumor budding is active at the invasive front (Grade 3), accompanied by a desmoplastic stromal response and moderate lymphocytic inflammation (34%). Microscopic invasion depth is estimated at 4.2 mm, indicating a high probability (84%) of regional nodal metastasis. Advise prompt clinical staging and surgical intervention.",
            dateAnalyzed: "2026-05-13",
            doctorNotes: "Primary tumor nests show severe nuclear pleomorphism. Invasion front appears infiltrative. Discussed at tumor board; surgical resection scheduled.",
            imageUri: "pathology_slide_sample.png",
            annotations: {
                nests: [{x: 120, y: 110, rx: 70, ry: 50}, {x: 280, y: 190, rx: 80, ry: 60}],
                buds: [{x: 200, y: 150}, {x: 215, y: 155}, {x: 195, y: 165}, {x: 370, y: 220}, {x: 380, y: 235}],
                front: [{x: 80, y: 80}, {x: 200, y: 140}, {x: 360, y: 210}, {x: 430, y: 260}],
                stroma: [{x: 60, y: 200, r: 25}, {x: 320, y: 80, r: 35}]
            }
        },
        {
            id: "SCAN-4401-23",
            patientId: "PID-7742",
            patientName: "Marcus Vance",
            disease: "Tubular Adenoma (Benign)",
            tumorBudding: "Grade 1 (Low)",
            stromalInflammation: "12%",
            invasionDepth: "0.8 mm",
            metastasisRisk: 15,
            confidence: "99.1%",
            interpretation: "Microscopic evaluation reveals colonic mucosal fragments exhibiting glandular crowding and epithelial cell elongation with hyperchromatic nuclei. Glandular architecture is relatively preserved. There is no evidence of high-grade dysplasia or stromal invasion (invasion depth is superficial at 0.8 mm). Active tumor budding is absent (Grade 1). Findings are consistent with a benign tubular adenoma. Complete local excision is curative; routine follow-up recommended.",
            dateAnalyzed: "2026-05-19",
            doctorNotes: "Sessile polyp margins appear clear. Benign presentation. Patient advised to reschedule colonoscopy in 3 years.",
            imageUri: "pathology_slide_sample.png",
            annotations: {
                nests: [{x: 200, y: 180, rx: 120, ry: 80}],
                buds: [],
                front: [{x: 50, y: 250}, {x: 450, y: 250}],
                stroma: [{x: 240, y: 100, r: 15}]
            }
        }
    ];

    let selectedSlideImage = null;
    let selectedSlideFileName = "";
    let activePatientId = "";
    let activeCaseRecordId = "";

    // --- 2. BOOTSTRAP INITIALIZATION ---
    setTimeout(() => {
        const splash = document.getElementById('view-splash');
        const login = document.getElementById('view-login');
        if (splash && login) {
            splash.classList.remove('active');
            login.classList.add('active');
        }
    }, 700);

    // Synchronize current date in greeting
    const updateHeaderGreeting = () => {
        const hour = new Date().getHours();
        const greetingEl = document.getElementById('header-greeting');
        if (greetingEl) {
            if (hour < 12) greetingEl.innerText = "Good Morning,";
            else if (hour < 17) greetingEl.innerText = "Good Afternoon,";
            else greetingEl.innerText = "Good Evening,";
        }
    };
    updateHeaderGreeting();

    // Global switch subviews to set navigation titles
    window.switchView = (viewId) => {
        document.querySelectorAll('.view').forEach(view => {
            view.classList.remove('active');
        });
        const targetView = document.getElementById(viewId);
        if (viewId === 'view-dashboard') {
            document.getElementById('app-main').classList.add('active');
            switchSubView('view-dashboard', document.querySelector('.nav-item'));
        } else {
            if (targetView) targetView.classList.add('active');
        }
    };

    window.switchSubView = (subViewId, navEl) => {
        const subViewTitles = {
            'view-dashboard': { title: 'Dashboard', sub: 'Clinical Overview' },
            'view-records': { title: 'Patient Directory', sub: 'Clinical Records' },
            'view-upload': { title: 'Clinical Workspace', sub: 'Upload Biopsy Slide' },
            'view-results': { title: 'Pathology Report', sub: 'MIL Staging Metrics' },
            'view-pipeline': { title: 'MIL Diagnostics', sub: 'Processing Tissue Slide' },
            'view-notifications': { title: 'Notifications Panel', sub: 'Recent Activity' },
            'view-settings': { title: 'Settings', sub: 'App Preferences' },
            'view-profile': { title: 'Doctor Profile', sub: 'Clinical Credentials' }
        };

        if (navEl) {
            document.querySelectorAll('.nav-item').forEach(item => item.classList.remove('active'));
            navEl.classList.add('active');
        }

        // Handle FAB button visibility
        const fab = document.getElementById('fab-add-patient');
        if (subViewId === 'view-records') {
            if (fab) fab.style.display = 'flex';
        } else {
            if (fab) fab.style.display = 'none';
        }

        document.querySelectorAll('.sub-view').forEach(view => view.classList.remove('active'));
        const target = document.getElementById(subViewId);
        if (target) {
            target.classList.add('active');
            const hTitle = document.getElementById('header-title');
            const hSub = document.getElementById('header-greeting');
            if (hTitle && subViewTitles[subViewId]) {
                hTitle.innerText = subViewTitles[subViewId].title;
                hSub.innerText = subViewTitles[subViewId].sub;
            }
        }
    };

    // --- 3. TOAST NOTIFICATION ---
    window.showToast = (message, type = "info") => {
        const toast = document.getElementById('toast-notification');
        const icon = document.getElementById('toast-icon');
        const text = document.getElementById('toast-message');
        if (toast && icon && text) {
            toast.className = `toast show ${type}`;
            text.innerText = message;
            
            // Set icons
            if (type === "success") icon.className = "fas fa-check-circle";
            else if (type === "danger") icon.className = "fas fa-times-circle";
            else if (type === "warning") icon.className = "fas fa-exclamation-circle";
            else icon.className = "fas fa-info-circle";

            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }
    };

    // --- 4. AUTHENTICATION ---
    window.handleLogin = () => {
        showToast("Pathology session authenticated.", "success");
        switchView('view-dashboard');
        renderDashboard();
        renderPatients();
        populatePatientDropdown();
    };

    window.handleLogout = () => {
        showToast("Clinical session closed.", "info");
        switchView('view-login');
    };

    // --- 5. DASHBOARD SUMMARY RENDER ---
    const renderDashboard = () => {
        // KPI metrics counters
        document.getElementById('kpi-total-patients').innerText = patients.length.toString().padStart(2, '0');
        document.getElementById('kpi-scanned-slides').innerText = caseRecords.length.toString().padStart(2, '0');
        
        const highRiskCount = caseRecords.filter(c => c.metastasisRisk >= 50).length;
        document.getElementById('kpi-high-risk').innerText = highRiskCount.toString().padStart(2, '0');

        // Recent cases list
        const caseListContainer = document.getElementById('dashboard-case-list');
        if (caseListContainer) {
            caseListContainer.innerHTML = '';
            
            if (caseRecords.length === 0) {
                caseListContainer.innerHTML = '<div style="text-align:center; padding: 2rem; color: var(--text-muted);">No scans recorded yet.</div>';
                return;
            }

            caseRecords.forEach(c => {
                const card = document.createElement('div');
                card.className = 'case-card';
                card.onclick = () => viewCaseResults(c.id);

                let badgeClass = 'low';
                if (c.metastasisRisk >= 70) badgeClass = 'high';
                else if (c.metastasisRisk >= 35) badgeClass = 'medium';

                card.innerHTML = `
                    <div class="case-info">
                        <strong>${c.patientName} (${c.patientId})</strong>
                        <span>Specimen: ${c.disease} | Date: ${c.dateAnalyzed}</span>
                    </div>
                    <div class="case-badge ${badgeClass}">${c.metastasisRisk}% Risk</div>
                `;
                caseListContainer.appendChild(card);
            });
        }
    };

    // --- 6. PATIENT CRUD MANAGER ---
    window.renderPatients = () => {
        const listContainer = document.getElementById('patient-directory-list');
        if (listContainer) {
            listContainer.innerHTML = '';
            
            if (patients.length === 0) {
                listContainer.innerHTML = '<div style="text-align:center; padding: 2rem; color: var(--text-muted);">No patients registered in database.</div>';
                return;
            }

            patients.forEach(p => {
                const card = document.createElement('div');
                card.className = 'patient-card';
                card.innerHTML = `
                    <div class="patient-info">
                        <strong>${p.name}</strong>
                        <span>ID: ${p.id} | Age/Sex: ${p.age} / ${p.gender}</span>
                        <span style="font-style: italic; font-size: 0.72rem; color: var(--primary-light); margin-top: 0.2rem;">Diagnosis: ${p.diagnosis}</span>
                    </div>
                    <div class="card-actions">
                        <button class="btn-card-action edit" onclick="event.stopPropagation(); openPatientModal('edit', '${p.id}')" title="Edit Profile"><i class="fas fa-edit"></i></button>
                        <button class="btn-card-action delete" onclick="event.stopPropagation(); handleDeletePatient('${p.id}')" title="Delete Profile"><i class="fas fa-trash-alt"></i></button>
                        <button class="btn-card-action analyze" onclick="event.stopPropagation(); selectPatientForAnalysis('${p.id}')" title="Scan Slide"><i class="fas fa-stethoscope"></i></button>
                    </div>
                `;
                listContainer.appendChild(card);
            });
        }
    };

    window.filterPatientsList = () => {
        const query = document.getElementById('patient-search').value.toLowerCase();
        const cards = document.querySelectorAll('#patient-directory-list .patient-card');
        
        cards.forEach(card => {
            const name = card.querySelector('strong').innerText.toLowerCase();
            const id = card.querySelector('span').innerText.toLowerCase();
            if (name.includes(query) || id.includes(query)) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    };

    window.openPatientModal = (mode, patientId = '') => {
        const modal = document.getElementById('patient-modal');
        const title = document.getElementById('patient-modal-title');
        
        // Reset fields
        document.getElementById('modal-patient-id').value = '';
        document.getElementById('modal-patient-name').value = '';
        document.getElementById('modal-patient-age').value = '';
        document.getElementById('modal-patient-gender').value = 'Male';
        document.getElementById('modal-patient-diagnosis').value = 'Breast Tissue';
        document.getElementById('modal-patient-notes').value = '';

        if (mode === 'edit' && patientId) {
            title.innerText = "Modify Patient Record";
            const patient = patients.find(p => p.id === patientId);
            if (patient) {
                document.getElementById('modal-patient-id').value = patient.id;
                document.getElementById('modal-patient-name').value = patient.name;
                document.getElementById('modal-patient-age').value = patient.age;
                document.getElementById('modal-patient-gender').value = patient.gender;
                document.getElementById('modal-patient-diagnosis').value = patient.diagnosis;
                document.getElementById('modal-patient-notes').value = patient.notes;
            }
        } else {
            title.innerText = "Register New Patient";
        }

        if (modal) modal.style.display = 'flex';
    };

    window.closePatientModal = () => {
        const modal = document.getElementById('patient-modal');
        if (modal) modal.style.display = 'none';
    };

    window.savePatientRecord = () => {
        const id = document.getElementById('modal-patient-id').value;
        const name = document.getElementById('modal-patient-name').value.trim();
        const age = parseInt(document.getElementById('modal-patient-age').value);
        const gender = document.getElementById('modal-patient-gender').value;
        const diagnosis = document.getElementById('modal-patient-diagnosis').value;
        const notes = document.getElementById('modal-patient-notes').value.trim();

        if (!name || isNaN(age) || age <= 0) {
            showToast("Please enter valid name and age.", "warning");
            return;
        }

        if (id) {
            // Update existing patient
            const index = patients.findIndex(p => p.id === id);
            if (index !== -1) {
                patients[index].name = name;
                patients[index].age = age;
                patients[index].gender = gender;
                patients[index].diagnosis = diagnosis;
                patients[index].notes = notes;
                showToast("Patient record updated.", "success");
            }
        } else {
            // Create new patient
            const newId = "PID-" + Math.floor(1000 + Math.random() * 9000);
            const today = new Date().toISOString().split('T')[0];
            patients.push({
                id: newId,
                name: name,
                age: age,
                gender: gender,
                dateRegistered: today,
                diagnosis: diagnosis,
                status: "Pending Scan",
                notes: notes
            });
            showToast("Patient record registered successfully.", "success");
        }

        closePatientModal();
        renderPatients();
        renderDashboard();
        populatePatientDropdown();
    };

    window.handleDeletePatient = (patientId) => {
        if (confirm(`Are you sure you want to permanently delete patient ${patientId}?`)) {
            patients = patients.filter(p => p.id !== patientId);
            // Also filter linked cases
            caseRecords = caseRecords.filter(c => c.patientId !== patientId);
            showToast("Patient record deleted.", "success");
            renderPatients();
            renderDashboard();
            populatePatientDropdown();
        }
    };

    window.selectPatientForAnalysis = (patientId) => {
        activePatientId = patientId;
        switchSubView('view-upload');
        populatePatientDropdown();
        const dropdown = document.getElementById('analysis-patient-select');
        if (dropdown) dropdown.value = patientId;
    };

    const populatePatientDropdown = () => {
        const dropdown = document.getElementById('analysis-patient-select');
        if (dropdown) {
            dropdown.innerHTML = '';
            
            if (patients.length === 0) {
                dropdown.innerHTML = '<option value="">No patients registered</option>';
                return;
            }

            patients.forEach(p => {
                const opt = document.createElement('option');
                opt.value = p.id;
                opt.innerText = `${p.name} (${p.id}) - Specimen: ${p.diagnosis}`;
                dropdown.appendChild(opt);
            });
            
            if (activePatientId) dropdown.value = activePatientId;
            else activePatientId = dropdown.value;
        }
    };

    // --- 7. SLIDE UPLOAD & H&E PIXEL VALIDATION ---
    window.handleImageSelection = (event) => {
        const file = event.target.files[0];
        if (file) {
            processBiopsyFile(file);
        }
    };

    const processBiopsyFile = (file) => {
        selectedSlideFileName = file.name;
        const reader = new FileReader();
        reader.onload = (e) => {
            selectedSlideImage = e.target.result;
            
            // Set thumbnail preview
            const previewContainer = document.getElementById('slide-preview-container');
            const previewImg = document.getElementById('selected-slide-preview');
            const dropZone = document.getElementById('drop-zone');
            
            if (previewContainer && previewImg && dropZone) {
                previewImg.src = selectedSlideImage;
                previewContainer.style.display = 'block';
                dropZone.style.display = 'none';
            }

            // Run pixel sampling color validation
            runSlideColorStainValidation(selectedSlideImage);
        };
        reader.readAsDataURL(file);
    };

    window.removeSelectedSlide = () => {
        selectedSlideImage = null;
        selectedSlideFileName = "";
        
        const previewContainer = document.getElementById('slide-preview-container');
        const dropZone = document.getElementById('drop-zone');
        const fileInput = document.getElementById('fileInput');
        const btnRun = document.getElementById('btn-run-analysis');
        
        if (previewContainer && dropZone && fileInput && btnRun) {
            previewContainer.style.display = 'none';
            dropZone.style.display = 'flex';
            fileInput.value = '';
            btnRun.disabled = true;
            btnRun.style.opacity = '0.6';
            btnRun.style.cursor = 'not-allowed';
        }
    };

    window.loadSampleSlide = () => {
        selectedSlideImage = "pathology_slide_sample.png";
        selectedSlideFileName = "pathology_slide_sample.png";
        
        const previewContainer = document.getElementById('slide-preview-container');
        const previewImg = document.getElementById('selected-slide-preview');
        const dropZone = document.getElementById('drop-zone');
        const btnRun = document.getElementById('btn-run-analysis');
        
        if (previewContainer && previewImg && dropZone && btnRun) {
            previewImg.src = selectedSlideImage;
            previewContainer.style.display = 'block';
            dropZone.style.display = 'none';
            
            btnRun.disabled = false;
            btnRun.style.opacity = '1';
            btnRun.style.cursor = 'pointer';
            
            showToast("Sample microscopic biopsy slide loaded.", "success");
        }
    };

    const runSlideColorStainValidation = (imageSrc) => {
        const img = new Image();
        img.src = imageSrc;
        img.onload = () => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            
            // Scaled down sampling for speed
            canvas.width = 100;
            canvas.height = 100;
            ctx.drawImage(img, 0, 0, 100, 100);
            
            const imgData = ctx.getImageData(0, 0, 100, 100).data;
            let heStainPixelCount = 0;
            let totalPixels = 100 * 100;
            
            for (let i = 0; i < imgData.length; i += 4) {
                const r = imgData[i];
                const g = imgData[i+1];
                const b = imgData[i+2];
                
                // Convert RGB to HSL for precise biological stain sampling
                const hsl = rgbToHsl(r, g, b);
                const h = hsl.h * 360;
                const s = hsl.s * 100;
                const l = hsl.l * 100;
                
                // H&E Stains contain deep pink, purple, magenta, and dark blue nuclei
                // Purple/Pink: Hue 280 to 355
                // Blue Nuclei: Hue 210 to 279
                // High saturation and mild luminosity
                const isPurplePink = (h >= 280 && h <= 355) && (s > 15) && (l > 15 && l < 92);
                const isBlueNuclei = (h >= 210 && h < 280) && (s > 15) && (l > 10 && l < 85);
                const isGlassBackground = (r > 240 && g > 240 && b > 240); // Transparent slide glass is white
                
                if (isPurplePink || isBlueNuclei || isGlassBackground) {
                    heStainPixelCount++;
                }
            }

            const heStainPercentage = (heStainPixelCount / totalPixels) * 100;
            const btnRun = document.getElementById('btn-run-analysis');
            
            if (heStainPercentage < 22) {
                // Not an H&E histological slide image
                showToast("Slide color validation failed. Not a valid H&E stained microscopic slide.", "danger");
                btnRun.disabled = true;
                btnRun.style.opacity = '0.6';
                btnRun.style.cursor = 'not-allowed';
            } else {
                showToast(`H&E Stain Density: ${heStainPercentage.toFixed(1)}%. Slide validated.`, "success");
                btnRun.disabled = false;
                btnRun.style.opacity = '1';
                btnRun.style.cursor = 'pointer';
            }
        };
        
        img.onerror = () => {
            showToast("Unable to sample uploaded image file.", "danger");
        };
    };

    // RGB to HSL helper
    const rgbToHsl = (r, g, b) => {
        r /= 255; g /= 255; b /= 255;
        const max = Math.max(r, g, b), min = Math.min(r, g, b);
        let h, s, l = (max + min) / 2;

        if (max === min) {
            h = s = 0; // achromatic
        } else {
            const d = max - min;
            s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
            switch (max) {
                case r: h = (g - b) / d + (g < b ? 6 : 0); break;
                case g: h = (b - r) / d + 2; break;
                case b: h = (r - g) / d + 4; break;
            }
            h /= 6;
        }
        return { h, s, l };
    };

    // --- 8. ANTIMATED MIL PIPELINE ENGINE ---
    window.initiateMILAnalysis = () => {
        const dropdown = document.getElementById('analysis-patient-select');
        if (dropdown) activePatientId = dropdown.value;
        
        if (!activePatientId) {
            showToast("Please register and select a patient first.", "warning");
            return;
        }

        switchSubView('view-pipeline');
        runNeuralPipelineStepper();
    };

    const runNeuralPipelineStepper = () => {
        const steps = [
            { id: "step-validation", desc: "Verifying H&E stain profile coordinates...", duration: 1200 },
            { id: "step-patches", desc: "Dividing WSI into 512x512 neural patches...", duration: 1500 },
            { id: "step-resnet", desc: "Extracting deep CNN feature vectors...", duration: 1800 },
            { id: "step-mil", desc: "Aggregating focus attention vectors...", duration: 2000 },
            { id: "step-report", desc: "Generating clinical reports & boundary overlays...", duration: 1200 }
        ];

        let currentStepIndex = 0;
        const progressFill = document.getElementById('pipeline-progress-fill');
        
        // Setup interactive grid canvas
        const pCanvas = document.getElementById('pipeline-canvas');
        const pCtx = pCanvas.getContext('2d');
        const previewImg = new Image();
        previewImg.src = selectedSlideImage || "pathology_slide_sample.png";
        
        previewImg.onload = () => {
            pCanvas.width = 400;
            pCanvas.height = 180;
            pCtx.drawImage(previewImg, 0, 0, 400, 180);
        };

        const processStep = () => {
            if (currentStepIndex >= steps.length) {
                // Done! Generate and open results
                finalizeDiagnosticReport();
                return;
            }

            const step = steps[currentStepIndex];
            const row = document.getElementById(step.id);
            const descEl = document.getElementById(`${step.id}-desc`);
            
            // Set active class
            document.querySelectorAll('.step-row').forEach(r => r.classList.remove('active'));
            if (row) {
                row.classList.add('active');
                if (descEl) descEl.innerText = step.desc;
            }

            // Animate canvas based on current step
            animatePipelineCanvas(pCtx, currentStepIndex, previewImg);

            // Update global progress bar
            const percent = ((currentStepIndex) / steps.length) * 100;
            if (progressFill) progressFill.style.width = `${percent}%`;

            setTimeout(() => {
                if (row) {
                    row.classList.remove('active');
                    row.classList.add('completed');
                }
                currentStepIndex++;
                processStep();
            }, step.duration);
        };

        // Reset all rows
        document.querySelectorAll('.step-row').forEach(r => {
            r.className = 'step-row';
        });
        if (progressFill) progressFill.style.width = '0%';

        processStep();
    };

    const animatePipelineCanvas = (ctx, stepIndex, img) => {
        if (!ctx) return;
        ctx.clearRect(0,0,400,180);
        ctx.drawImage(img, 0, 0, 400, 180);

        ctx.strokeStyle = "rgba(0,102,255,0.4)";
        ctx.lineWidth = 1;

        if (stepIndex === 1) {
            // Draw patch grid overlay
            for (let x = 0; x < 400; x += 20) {
                ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 180); ctx.stroke();
            }
            for (let y = 0; y < 180; y += 20) {
                ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(400, y); ctx.stroke();
            }
        } else if (stepIndex === 2) {
            // Feature scanning tiles highlight
            for (let x = 0; x < 400; x += 20) {
                for (let y = 0; y < 180; y += 20) {
                    if (Math.random() > 0.8) {
                        ctx.fillStyle = "rgba(0,102,255,0.25)";
                        ctx.fillRect(x, y, 20, 20);
                    }
                }
            }
        } else if (stepIndex === 3) {
            // MIL attention weights map drawing
            for (let x = 0; x < 400; x += 20) {
                for (let y = 0; y < 180; y += 20) {
                    const rand = Math.random();
                    if (rand > 0.85) {
                        ctx.fillStyle = "rgba(239, 68, 68, 0.4)"; // High tumor attention
                        ctx.fillRect(x, y, 20, 20);
                    } else if (rand > 0.7) {
                        ctx.fillStyle = "rgba(245, 158, 11, 0.25)"; // Border
                        ctx.fillRect(x, y, 20, 20);
                    }
                }
            }
        }
    };

    // --- 9. COMPILE DIAGNOSTIC RESULTS CASE ---
    const finalizeDiagnosticReport = () => {
        const patient = patients.find(p => p.id === activePatientId);
        if (!patient) return;

        // Create clinical findings parameters based on Patient Diagnosis Category
        let metastasisRisk = 84;
        let buddingGrade = "Grade 3 (High)";
        let stromalInflammation = "34%";
        let invasionDepth = "4.2 mm";
        let diseaseName = "Invasive Ductal Carcinoma (NST)";
        let confidence = "98.4%";
        let interpretationText = "";
        let annotations = {
            nests: [{x: 120, y: 110, rx: 70, ry: 50}, {x: 280, y: 190, rx: 80, ry: 60}],
            buds: [{x: 200, y: 150}, {x: 215, y: 155}, {x: 195, y: 165}, {x: 370, y: 220}, {x: 380, y: 235}],
            front: [{x: 80, y: 80}, {x: 200, y: 140}, {x: 360, y: 210}, {x: 430, y: 260}],
            stroma: [{x: 60, y: 200, r: 25}, {x: 320, y: 80, r: 35}]
        };

        if (patient.diagnosis === "Colon Polyps") {
            metastasisRisk = 18;
            buddingGrade = "Grade 1 (Low)";
            stromalInflammation = "14%";
            invasionDepth = "0.9 mm";
            diseaseName = "Tubular Adenoma (Benign mucosal changes)";
            confidence = "99.2%";
            interpretationText = "Mucosal biopsy sections display glandular crowding with mild nuclear enlargement and hyperchromasia. Architectural outlines remain intact. There is no evidence of aggressive infiltrative invasion front lines (Invasion depth superficial at 0.9 mm). Active budding clusters are not observed. Infiltration of inflammatory cells is focal and limited (14%). Pathology findings are typical of a benign tubular adenoma.";
            annotations = {
                nests: [{x: 180, y: 130, rx: 110, ry: 70}],
                buds: [],
                front: [{x: 40, y: 220}, {x: 440, y: 220}],
                stroma: [{x: 150, y: 80, r: 18}]
            };
        } else if (patient.diagnosis === "Prostate Core") {
            metastasisRisk = 68;
            buddingGrade = "Grade 2 (Moderate)";
            stromalInflammation = "26%";
            invasionDepth = "3.1 mm";
            diseaseName = "Prostatic Adenocarcinoma (Gleason 4+3)";
            confidence = "97.8%";
            interpretationText = "Prostate needle core biopsy specimens demonstrate infiltrating malignant prostatic acini with fused glandular configurations (Gleason pattern 4). Cellular morphology shows enlarged nuclei with prominent nucleoli. Moderate active budding points are identified along the infiltrative stromal boundaries. Local tumor penetration into peri-prostatic fat measures 3.1 mm. Metastasis risk is moderate-high (68%).";
            annotations = {
                nests: [{x: 130, y: 140, rx: 60, ry: 40}, {x: 250, y: 100, rx: 50, ry: 35}, {x: 310, y: 200, rx: 55, ry: 45}],
                buds: [{x: 195, y: 120}, {x: 200, y: 100}, {x: 290, y: 160}],
                front: [{x: 100, y: 160}, {x: 200, y: 130}, {x: 260, y: 140}, {x: 380, y: 220}],
                stroma: [{x: 80, y: 80, r: 20}, {x: 350, y: 90, r: 22}]
            };
        } else if (patient.diagnosis === "Lung Lesion") {
            metastasisRisk = 91;
            buddingGrade = "Grade 3 (High)";
            stromalInflammation = "42%";
            invasionDepth = "5.8 mm";
            diseaseName = "Pulmonary Adenocarcinoma (Infiltrative)";
            confidence = "98.9%";
            interpretationText = "Lung core biopsy shows solid sheets and acinar arrangements of malignant epithelial cells. Neoplastic glands display marked cytological atypia, irregular borders, and cellular necrosis. Extensive micro-budding is noted at the leading tumor front (Grade 3). The destructive invasion depth into surrounding alveolar structures is significant (5.8 mm). Severe inflammatory host response with lymphocytic infiltration is widespread (42%). Metastasis risk is critically high (91%).";
            annotations = {
                nests: [{x: 100, y: 80, rx: 80, ry: 50}, {x: 260, y: 130, rx: 90, ry: 65}],
                buds: [{x: 190, y: 110}, {x: 200, y: 120}, {x: 185, y: 130}, {x: 360, y: 180}, {x: 375, y: 195}, {x: 380, y: 210}],
                front: [{x: 60, y: 60}, {x: 180, y: 120}, {x: 350, y: 180}],
                stroma: [{x: 80, y: 220, r: 35}, {x: 300, y: 60, r: 25}]
            };
        } else {
            // General / Breast Tissue Default
            interpretationText = "Infiltrating ducts and cords of atypical epithelial structures are noted penetrating local fibrous stroma. Distinct severe cytological pleomorphism, enlarged vesicular nuclei, and prominent nucleoli are prominent. The leading biological front shows marked active tumor budding (Grade 3), coupled with extensive desmoplastic stromal response and lymphocytic infiltration (34%). Microscopic invasion depth is estimated at 4.2 mm. Staging is highly suggestive of nodal metastasis risk (84%).";
        }

        // Generate case ID
        const caseId = "SCAN-" + Math.floor(1000 + Math.random() * 9000) + "-26";
        const today = new Date().toISOString().split('T')[0];
        
        const newCase = {
            id: caseId,
            patientId: patient.id,
            patientName: patient.name,
            disease: diseaseName,
            tumorBudding: buddingGrade,
            stromalInflammation: stromalInflammation,
            invasionDepth: invasionDepth,
            metastasisRisk: metastasisRisk,
            confidence: confidence,
            interpretation: interpretationText,
            dateAnalyzed: today,
            doctorNotes: "",
            imageUri: selectedSlideImage || "pathology_slide_sample.png",
            annotations: annotations
        };

        caseRecords.unshift(newCase);
        activeCaseRecordId = caseId;

        // Update patient status in main database
        patient.status = metastasisRisk >= 50 ? "High Risk" : "Low Risk";

        showToast("Pathology diagnosis compiled.", "success");
        renderDashboard();
        renderPatients();
        
        viewCaseResults(caseId);
    };

    // --- 10. DISPLAY PATHOLOGY RESULTS CASE ---
    window.viewCaseResults = (caseId) => {
        const record = caseRecords.find(c => c.id === caseId);
        if (!record) return;

        activeCaseRecordId = caseId;
        switchSubView('view-results');

        // Demographics
        const patient = patients.find(p => p.id === record.patientId);
        document.getElementById('results-patient-meta').innerHTML = `
            <strong>Patient:</strong> ${record.patientName} (${record.patientId})<br>
            <strong>Specimen:</strong> ${patient ? patient.diagnosis : 'Biopsy Slide'}<br>
            <strong>Date Analyzed:</strong> ${record.dateAnalyzed}
        `;

        // Circular risk ring gauge
        document.getElementById('results-risk-percent').innerText = `${record.metastasisRisk}%`;
        const circleFill = document.getElementById('results-risk-fill');
        if (circleFill) {
            // Stroke dasharray 220
            const offset = 220 - (220 * record.metastasisRisk) / 100;
            circleFill.style.strokeDashoffset = offset;
            
            // Set alert colors
            circleFill.className.baseVal = "score-circle-fill";
            if (record.metastasisRisk >= 70) circleFill.classList.add('high');
            else if (record.metastasisRisk >= 35) circleFill.classList.add('medium');
            else circleFill.classList.add('low');
        }

        document.getElementById('results-diagnosis-title').innerText = record.disease;

        // Metrics
        document.getElementById('results-bud-grade').innerText = record.tumorBudding;
        document.getElementById('results-invasion-depth').innerText = record.invasionDepth;
        document.getElementById('results-inflammation').innerText = record.stromalInflammation;
        document.getElementById('results-confidence').innerText = `${record.confidence} Accuracy`;

        // Narrative clinical assessment text
        document.getElementById('results-interpretation-text').innerText = record.interpretation;

        // Pathologist notes inputs
        document.getElementById('results-doctor-notes').value = record.doctorNotes || '';

        // Draw histology vector contour canvas overlays
        setTimeout(() => {
            drawPathologyResults('result-canvas', record.imageUri, record.annotations);
        }, 150);
    };

    const drawPathologyResults = (canvasId, imageSrc, annotations) => {
        const canvas = document.getElementById(canvasId);
        if (!canvas) return;
        const ctx = canvas.getContext('2d');
        const img = new Image();
        img.src = imageSrc || "pathology_slide_sample.png";

        img.onload = () => {
            // High DPI scaling
            const width = 500;
            const height = 300;
            canvas.width = width;
            canvas.height = height;

            ctx.clearRect(0,0,width,height);
            ctx.drawImage(img, 0, 0, width, height);

            // 1. Draw Stromal Inflammation lymphocytic nodes (Translucent violet circles)
            if (annotations.stroma) {
                annotations.stroma.forEach(node => {
                    ctx.beginPath();
                    ctx.arc(node.x, node.y, node.r, 0, 2 * Math.PI);
                    ctx.fillStyle = "rgba(100, 0, 255, 0.15)";
                    ctx.fill();
                    ctx.strokeStyle = "rgba(100, 0, 255, 0.3)";
                    ctx.lineWidth = 1;
                    ctx.stroke();
                });
            }

            // 2. Draw Simulated Tumor Nests (Translucent red contours with dashed lines)
            if (annotations.nests) {
                annotations.nests.forEach(nest => {
                    ctx.beginPath();
                    ctx.ellipse(nest.x, nest.y, nest.rx, nest.ry, 0, 0, 2 * Math.PI);
                    ctx.fillStyle = "rgba(239, 68, 68, 0.18)";
                    ctx.fill();
                    ctx.strokeStyle = "rgba(239, 68, 68, 0.6)";
                    ctx.lineWidth = 2;
                    ctx.setLineDash([5, 5]);
                    ctx.stroke();
                    ctx.setLineDash([]);
                });
            }

            // 3. Draw Simulated Invasion Front (Amber dash-dotted border boundaries)
            if (annotations.front && annotations.front.length > 1) {
                ctx.beginPath();
                ctx.moveTo(annotations.front[0].x, annotations.front[0].y);
                for (let i = 1; i < annotations.front.length; i++) {
                    ctx.lineTo(annotations.front[i].x, annotations.front[i].y);
                }
                ctx.strokeStyle = "rgba(245, 158, 11, 0.8)";
                ctx.lineWidth = 3;
                ctx.setLineDash([8, 4, 2, 4]);
                ctx.stroke();
                ctx.setLineDash([]);
            }

            // 4. Draw Tumor Budding (Bright red dots identifying focal tumor cells groups)
            if (annotations.buds) {
                annotations.buds.forEach(bud => {
                    // Outer glow
                    ctx.beginPath();
                    ctx.arc(bud.x, bud.y, 6, 0, 2 * Math.PI);
                    ctx.fillStyle = "rgba(239, 68, 68, 0.4)";
                    ctx.fill();
                    
                    // Core point
                    ctx.beginPath();
                    ctx.arc(bud.x, bud.y, 3, 0, 2 * Math.PI);
                    ctx.fillStyle = "#EF4444";
                    ctx.fill();
                });
            }
        };
    };

    // --- 11. PATHOLOGIST NOTES SAVE ---
    window.saveCurrentCaseRecord = () => {
        const record = caseRecords.find(c => c.id === activeCaseRecordId);
        if (record) {
            const notes = document.getElementById('results-doctor-notes').value.trim();
            record.doctorNotes = notes;
            showToast("Clinical notes successfully appended to case log.", "success");
            renderDashboard();
        }
    };

    // --- 12. FULL SCREEN ZOOM MAGNIFIER OVERLAY ---
    window.openZoomMagnifier = () => {
        const modal = document.getElementById('zoom-modal');
        if (modal) {
            modal.style.display = 'flex';
            
            const record = caseRecords.find(c => c.id === activeCaseRecordId);
            if (record) {
                document.getElementById('zoom-title').innerText = `High-Resolution Inspection: ${record.patientName} (${record.id})`;
                drawPathologyResults('zoom-canvas', record.imageUri, record.annotations);
            }
        }
    };

    window.closeZoomMagnifier = () => {
        const modal = document.getElementById('zoom-modal');
        if (modal) modal.style.display = 'none';
    };

    // --- 13. PRINT HIGH-FIDELITY A4 PATHOLOGY REPORT ---
    window.triggerPDFReportDownload = () => {
        const record = caseRecords.find(c => c.id === activeCaseRecordId);
        if (!record) return;

        // Save current doctor's notes first
        const notes = document.getElementById('results-doctor-notes').value.trim();
        record.doctorNotes = notes;

        const patient = patients.find(p => p.id === record.patientId);

        // Populate print report DOM containers
        document.getElementById('print-patient-id').innerText = record.patientId;
        document.getElementById('print-case-id').innerText = record.id;
        document.getElementById('print-patient-name').innerText = record.patientName;
        document.getElementById('print-case-date').innerText = record.dateAnalyzed;
        document.getElementById('print-patient-age-gender').innerText = `${patient ? patient.age : 'N/A'} / ${patient ? patient.gender : 'N/A'}`;
        document.getElementById('print-patient-tissue').innerText = patient ? patient.diagnosis : 'Biopsy Tissue';
        
        document.getElementById('print-risk-index').innerText = `${record.metastasisRisk}% (${record.metastasisRisk >= 50 ? 'High Risk' : 'Low Risk'})`;
        document.getElementById('print-budding-grade').innerText = record.tumorBudding;
        document.getElementById('print-invasion').innerText = record.invasionDepth;
        document.getElementById('print-inflammation-pct').innerText = record.stromalInflammation;
        
        document.getElementById('print-narrative').innerText = record.interpretation;
        document.getElementById('print-doctor-notes').innerText = record.doctorNotes || 'No custom clinician notes appended.';

        // Invoke browser system print dialogue. CSS media queries print rules will format the layout automatically.
        window.print();
    };

});
