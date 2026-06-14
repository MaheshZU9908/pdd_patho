import os
import sqlite3
import uuid
import datetime
from flask import Flask, request, jsonify, send_from_directory
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Directory setup
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
DB_PATH = os.path.join(BASE_DIR, 'database.db')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Create Patients Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            gender TEXT NOT NULL,
            contact TEXT NOT NULL,
            date_registered TEXT NOT NULL,
            diagnosis TEXT NOT NULL,
            status TEXT NOT NULL,
            notes TEXT
        )
    ''')
    
    # Create Cases Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cases (
            id TEXT PRIMARY KEY,
            patient_id TEXT NOT NULL,
            patient_name TEXT NOT NULL,
            disease TEXT NOT NULL,
            tumor_budding TEXT NOT NULL,
            stromal_inflammation TEXT NOT NULL,
            invasion_depth REAL NOT NULL,
            metastasis_risk INTEGER NOT NULL,
            confidence REAL NOT NULL,
            interpretation TEXT NOT NULL,
            date_analyzed TEXT NOT NULL,
            doctor_notes TEXT,
            image_url TEXT NOT NULL,
            FOREIGN KEY (patient_id) REFERENCES patients(id)
        )
    ''')
    
    # Prepopulate default patients if table is empty
    cursor.execute('SELECT COUNT(*) FROM patients')
    if cursor.fetchone()[0] == 0:
        default_patients = [
            ("PID-1021", "John Doe", 54, "Male", "+1-555-0192", "2026-05-10", "Invasive Carcinoma", "High Risk", "Advised surgical resection."),
            ("PID-1022", "Jane Smith", 42, "Female", "+1-555-0143", "2026-05-12", "Normal Tissue", "Clear", "No malignancy detected. Regular screening in 1 year."),
            ("PID-1023", "Robert Brown", 68, "Male", "+1-555-0185", "2026-05-14", "Adenocarcinoma", "Moderate Risk", "Follow-up endoscopy scheduled."),
            ("PID-1024", "Emily Davis", 31, "Female", "+1-555-0111", "2026-05-15", "Squamous Cell Carcinoma", "Critical", "Urgent oncological consultation recommended.")
        ]
        cursor.executemany(
            'INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            default_patients
        )
        
        # Prepopulate default cases if table is empty
        default_cases = [
            (
                "CASE-1001", "PID-1021", "John Doe", "Invasive Ductal Carcinoma", 
                "Grade 2 (Moderate)", "Moderate", 3.5, 72, 94.8, 
                "Section shows infiltration of cohesive nests of malignant epithelial cells. Moderate tumor budding (5 buds/HPF) observed at the invasive front. Moderate lymphoplasmacytic stromal response present.",
                "2026-05-10 14:30", "Scheduled for surgical consult.", "/api/images/default_case_1.png"
            ),
            (
                "CASE-1002", "PID-1023", "Robert Brown", "Adenocarcinoma", 
                "Grade 1 (Low)", "Mild", 1.8, 45, 91.2, 
                "Well-differentiated neoplastic glandular structures infiltrating the submucosal stroma. Low budding score (2 buds/HPF). Mild peritumoral inflammatory response.",
                "2026-05-14 11:15", "Prescribed initial therapy cycles.", "/api/images/default_case_2.png"
            ),
            (
                "CASE-1003", "PID-1024", "Emily Davis", "Oral Squamous Cell Carcinoma", 
                "Grade 3 (High)", "Severe", 5.6, 98, 98.7, 
                "Malignant squamous cells invading deeply into muscle and bone. High tumor budding (12 buds/HPF) at the peripheral boundary. Marked stromal inflammation and cellular atypia.",
                "2026-05-15 09:45", "CRITICAL: Patient notified. Urgent staging CT scheduled.", "/api/images/default_case_3.png"
            )
        ]
        cursor.executemany(
            'INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
            default_cases
        )
    
    conn.commit()
    conn.close()

# Initialize DB on start
init_db()

def process_and_annotate_biopsy(image_path, out_filename):
    """
    Simulates tissue segmentation and deep learning predictions using PIL.
    Analyzes H&E colors, detects high nuclear density, and draws annotations on the image.
    """
    img = Image.open(image_path).convert('RGB')
    width, height = img.size
    
    # Downsample to analyze colors efficiently
    small_img = img.resize((100, 100))
    nuclei_count = 0
    cytoplasm_count = 0
    
    for x in range(100):
        for y in range(100):
            r, g, b = small_img.getPixel((x, y))
            
            # Simple H&E color detection
            # Hematoxylin (purple/blue): High blue compared to red/green, low brightness
            if b > r and b > g and r < 180:
                nuclei_count += 1
            # Eosin (pink/red): High red compared to green/blue
            elif r > g and r > b and g < 200:
                cytoplasm_count += 1
                
    total_stained = nuclei_count + cytoplasm_count
    cellularity = (nuclei_count / total_stained) if total_stained > 0 else 0.35
    
    # Draw annotations on a copy of the original image
    annotated_img = img.copy()
    draw = ImageDraw.Draw(annotated_img)
    
    # Use built-in default font
    try:
        font = ImageFont.load_default()
    except Exception:
        font = None

    # Helper function to draw rectangles with thickness
    def draw_thick_rect(coords, color, width=4):
        for i in range(width):
            draw.rectangle([coords[0]-i, coords[1]-i, coords[2]+i, coords[3]+i], outline=color)
            
    is_normal = cellularity < 0.22
    
    if is_normal:
        # Draw a green box representing Normal Epithelium
        box_coords = [int(width * 0.15), int(height * 0.15), int(width * 0.85), int(height * 0.85)]
        draw_thick_rect(box_coords, (16, 185, 129), width=6) # Success Green
        draw.text((box_coords[0] + 15, box_coords[1] + 15), "Normal Epithelium / Intact Basement Membrane", fill=(16, 185, 129))
        
        disease = "Normal Biopsy Slide / No Malignancy"
        tumor_budding = "Grade 0 (0 buds/HPF)"
        stromal_inflammation = "Mild (Physiological limits)"
        invasion_depth = 0.0
        metastasis_risk = 2
        confidence = 99.4
        interpretation = "Multi-Instance Learning analysis maps high-confidence regular tissue architecture. The stratified squamous epithelium exhibits mature architectural layout. Basement membrane is fully continuous and intact with no stromal infiltration. Cellularity ratio lies well within normal physiological margins, showing no hyperchromasia or severe nuclear enlargement."
        doctor_notes = "Biopsy shows benign features with no pathological evidence of squamous or glandular malignancy. Recommend standard annual clinical follow-up."
    
    elif cellularity < 0.45:
        # Moderate cellularity -> Adenocarcinoma G2
        # Draw an amber box representing infiltrating glandular focus
        box_coords = [int(width * 0.2), int(height * 0.25), int(width * 0.8), int(height * 0.75)]
        draw_thick_rect(box_coords, (245, 158, 11), width=6) # Amber
        draw.text((box_coords[0] + 15, box_coords[1] + 15), "Infiltrating Glandular Focus (Adenocarcinoma G2)", fill=(245, 158, 11))
        
        # Draw some tumor budding points (small red dots)
        for dx, dy in [(0, 15), (20, 0), (-15, -20)]:
            cx, cy = int(width * 0.5) + dx, int(height * 0.5) + dy
            draw.ellipse([cx-5, cy-5, cx+5, cy+5], fill=(239, 68, 110))
            
        disease = "Infiltrating Adenocarcinoma (G2)"
        tumor_budding = "Grade 2 (Moderate, 6 buds/HPF)"
        stromal_inflammation = "Moderate (Focal inflammatory response)"
        invasion_depth = round(1.8 + cellularity * 3.8, 1)
        metastasis_risk = int(35 + (cellularity - 0.22) * 140)
        confidence = round(90.5 + cellularity * 12.0, 1)
        interpretation = f"Convolutional feature extraction mapped moderately differentiated atypical glandular structures infiltrating mucosal layers. Spatial attention weights clustered at tumor-stroma boundaries, indicating active mucosal invasion. Peripheral tumor budding tracked at Grade 2. Deepest invasive focus estimated at {invasion_depth} mm. Stromal tissue exhibits a moderate lymphocytic response."
        doctor_notes = "Advised comprehensive clinical staging including contrast-enhanced CT. Refer to clinical oncology team for treatment planning."
        
    else:
        # High cellularity -> Squamous Cell Carcinoma G3
        # Draw multiple red dashed boxes for tumor nests
        nest1 = [int(width * 0.15), int(height * 0.15), int(width * 0.55), int(height * 0.55)]
        nest2 = [int(width * 0.6), int(height * 0.45), int(width * 0.9), int(height * 0.8)]
        draw_thick_rect(nest1, (239, 68, 68), width=8) # Danger Red
        draw_thick_rect(nest2, (239, 68, 68), width=6)
        
        draw.text((nest1[0] + 15, nest1[1] + 15), "Tumor Nest (Pleomorphic SCC)", fill=(239, 68, 68))
        draw.text((nest2[0] + 10, nest2[1] + 10), "Infiltrating Stromal Focus", fill=(239, 68, 68))
        
        # Deep invasion line
        y_line = int(height * 0.85)
        draw.line([int(width * 0.1), y_line, int(width * 0.9), y_line], fill=(245, 158, 11), width=5)
        draw.text((int(width * 0.15), y_line - 20), "Deep Invasion Boundary", fill=(245, 158, 11))
        
        disease = "Oral Squamous Cell Carcinoma (High Grade)"
        tumor_budding = "Grade 3 (High, 14 buds/HPF)"
        stromal_inflammation = "Severe (Dense infiltration of tumor-infiltrating lymphocytes)"
        invasion_depth = round(4.8 + cellularity * 4.5, 1)
        metastasis_risk = int(82 + (cellularity - 0.45) * 35)
        confidence = round(95.2 + cellularity * 3.5, 1)
        interpretation = f"Multi-Instance Learning (MIL) neural network identified high-attention tiled patches corresponding to nests of highly pleomorphic squamous epithelial cells. High nuclear crowding and hyperchromasia indicate aggressive mitotic activity. Active tumor budding (Grade 3) noted at the peripheral stroma interface. Deep invasive front measured at {invasion_depth} mm with severe host peritumoral inflammatory infiltration."
        doctor_notes = "CRITICAL PATHOLOGY REPORT: Highly suspicious squamous malignancy with deep infiltration. Immediate surgical resection planning and oncological staging requested."

    # Clamp bounds
    metastasis_risk = max(0, min(99, metastasis_risk))
    confidence = max(0.0, min(99.9, confidence))
    
    annotated_img.save(os.path.join(UPLOAD_FOLDER, out_filename), format='PNG')
    
    return {
        "disease": disease,
        "tumor_budding": tumor_budding,
        "stromal_inflammation": stromal_inflammation,
        "invasion_depth": invasion_depth,
        "metastasis_risk": metastasis_risk,
        "confidence": confidence,
        "interpretation": interpretation,
        "doctor_notes": doctor_notes
    }

# ==========================================
# REST API ENDPOINTS
# ==========================================

@app.route('/api/patients', methods=['GET'])
def get_patients():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients ORDER BY id DESC')
    rows = cursor.fetchall()
    conn.close()
    
    patients = [dict(row) for row in rows]
    return jsonify(patients)

@app.route('/api/patients', methods=['POST'])
def add_patient():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
        
    conn = get_db()
    cursor = conn.cursor()
    
    # Generate ID
    cursor.execute('SELECT COUNT(*) FROM patients')
    count = cursor.fetchone()[0]
    patient_id = f"PID-{1000 + count + 1}"
    
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    
    cursor.execute(
        'INSERT INTO patients VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (
            patient_id,
            data.get('name'),
            int(data.get('age', 30)),
            data.get('gender', 'Other'),
            data.get('contact', '+1-555-0100'),
            date_str,
            data.get('diagnosis', 'Pending Biopsy'),
            data.get('status', 'Clear'),
            data.get('notes', '')
        )
    )
    
    conn.commit()
    
    cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
    row = cursor.fetchone()
    conn.close()
    
    return jsonify(dict(row)), 201

@app.route('/api/cases', methods=['GET'])
def get_cases():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cases ORDER BY date_analyzed DESC')
    rows = cursor.fetchall()
    conn.close()
    
    cases = [dict(row) for row in rows]
    return jsonify(cases)

@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image part in the request"}), 400
        
    file = request.files['image']
    patient_id = request.form.get('patient_id')
    
    if not file or not patient_id:
        return jsonify({"error": "Image file and patient_id are required"}), 400
        
    # Get patient record
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM patients WHERE id = ?', (patient_id,))
    patient = cursor.fetchone()
    if not patient:
        conn.close()
        return jsonify({"error": f"Patient with ID {patient_id} not found"}), 404
        
    # Generate unique filenames
    unique_id = str(uuid.uuid4())
    orig_filename = f"original_{unique_id}.png"
    seg_filename = f"segmented_{unique_id}.png"
    
    orig_path = os.path.join(app.config['UPLOAD_FOLDER'], orig_filename)
    file.save(orig_path)
    
    # Process image & run simulated deep learning overlay
    findings = process_and_annotate_biopsy(orig_path, seg_filename)
    
    # Save case in Database
    case_id = f"CASE-{1000 + len(unique_id) % 9000}" # Generate case ID
    cursor.execute('SELECT COUNT(*) FROM cases')
    case_count = cursor.fetchone()[0]
    case_id = f"CASE-{1000 + case_count + 1}"
    
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Return full image url pointing to the Flask server hosting the file
    host_url = request.host_url
    image_url = f"{host_url}api/images/{seg_filename}"
    
    cursor.execute(
        'INSERT INTO cases VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
        (
            case_id,
            patient_id,
            patient['name'],
            findings['disease'],
            findings['tumor_budding'],
            findings['stromal_inflammation'],
            findings['invasion_depth'],
            findings['metastasis_risk'],
            findings['confidence'],
            findings['interpretation'],
            date_str,
            findings['doctor_notes'],
            image_url
        )
    )
    
    # Update patient's status and diagnosis
    new_status = "Clear"
    if findings['metastasis_risk'] > 80:
        new_status = "Critical"
    elif findings['metastasis_risk'] > 50:
        new_status = "High Risk"
    elif findings['metastasis_risk'] > 20:
        new_status = "Moderate Risk"
        
    cursor.execute(
        'UPDATE patients SET status = ?, diagnosis = ? WHERE id = ?',
        (new_status, findings['disease'], patient_id)
    )
    
    conn.commit()
    
    # Retrieve the new case row
    cursor.execute('SELECT * FROM cases WHERE id = ?', (case_id,))
    case_row = dict(cursor.fetchone())
    conn.close()
    
    # Replace DB image_url with case_row JSON imageUri to match android client expectation
    # In kotlin, CaseRecord field is named imageUri
    case_row['imageUri'] = case_row.pop('image_url')
    
    return jsonify(case_row), 200

@app.route('/api/images/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
