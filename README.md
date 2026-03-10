# taurgo-internship-assignment-sadique

# TaurgoVision — AI-Powered Visual Inspection System
A hybrid AI inspection tool that analyzes images for cracks, damp, and other visible anomalies using offline Computer Vision and optional cloud LLM vision models (Gemini Vision / OpenAI Vision).  
Designed for reliability, clarity, and professional reporting with overlays, structured summaries, and downloadable PDF reports.

---
STEPS TO RUN (MAKE SURE YOU HAVE PYTHON INSTALLED ON YOUR SYSTEM BEFORE YOU EXECUTE THE FOLLOWING STEPS):
If Python is not installed, please refer to these steps:

1. Download Python from the official website:  
   https://www.python.org/downloads/windows/
2. Run the installer.
3. IMPORTANT: On the first install screen, tick the box:  
   "Add Python to PATH"
4. Click “Install Now”.
5. After installation, restart PowerShell.

Now we can proceed with the demo:

First clone the code from github, then perform the following steps:

# Backend Setup (FastAPI)

### 1: Enter the backend folder:
Open powershell on windows and navigate to your backend folder as shown in the demo
Use cd backend (Note: backend stands for the backend path which will be differnt on different computers, make sure to check the demo to understand how to paste this path here)

### 2: Create a virtual environment:
python -m venv venv

### 3: Activate it:
venv\Scripts\activate

### 4: Install dependencies:
pip install -r requirements.txt

### SKIP THIS STEP. Go to step 5 directly after step 4. No need to run this but I am putting it here to show the system's higher level capabilities. (Optional) Enable ONLINE AI mode:
Rename .env.example - .env, then fill:
OPENAI_API_KEY=
GEMINI_API_KEY=

### 5: Run the backend:
python -m uvicorn app:app --reload

Backend runs at:
http://localhost:8000

---

# Fronend Setup (Next.js)

### 1: Open a new PowerShell window
Keep backend running.

### 2: Navigate to the frontend folder:
cd frontend (again check the demo for the path)

### 3: Install dependencies:
npm install

### 4: Run the development server:
npm run dev

Frontend now runs at:
http://localhost:3000 - Copy paste this link and run in your browser.

######### How to Use TaurgoVision #########

1. Open the frontend in your browser
2. Upload a JPG/PNG/HEIC file
3. Click Analyze
4. View:
	Original image
	Overlay with highlighted defects
	Structured defect report
	Recommendations

5. Click Download PDF Report to export a professional PDF


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
How The Analysis Works (Hybrid Pipeline)
1. Gemini/OpenAI (if API keys exist)
Used first for semantic understanding:

General defect detection
Summary generation
Confidence scoring

2. Offline CV (Always available)
Fallback when:

No API keys
No internet
Cloud models fail

Offline CV detects:

Cracks (Hough transform)
Damp patches (threshold & morphology)
Generates overlays
Produces structured output

This makes TaurgoVision extremely reliable.

Some important notes:

- The project runs 100% offline
- API keys are not required
- HEIC uploads work out‑of‑the‑box
- The UI is polished and intuitive
- Includes PDF exporting
- Designed to reflect real inspection workflows
- No external configuration needed

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Features ###
### Dual‑Mode Analysis (Offline + Online)
TaurgoVision can run in:
- **Offline Mode (Default)** - Pure OpenCV detection  
  - Crack detection (Hough transform)
  - Damp/moisture patch detection  
  - High‑contrast overlays  
  - Works without Internet

- **Online Mode (Optional)** → Gemini Vision or OpenAI Vision  
  - Auto‑detects keys from `.env`
  - If `GEMINI_API_KEY` exists - use Gemini Vision  
  - Else if `OPENAI_API_KEY` exists - use OpenAI Vision  
  - Else - fallback to offline CV  
  - Zero configuration needed

### HEIC Image Support (iPhone Photos) ###
Thanks to `pillow-heif`, TaurgoVision accepts:
- `.jpg`
- `.jpeg`
- `.png`
- `.heic`
- `.HEIC`

### Clear Before/After Overlays ###
- Thick, high‑contrast red crack lines (with black halo)
- Cyan damp boxes (with white border)
- Professional, survey-grade visualization

### Professional Report UI ###
- Summary section  
- Defect table with severity badges  
- Recommendations  
- Side‑by‑side image comparison  
- Dark outer theme + light report card

### PDF Report Export ###
- RICS‑style inspection summary  
- Defects & severity  
- Recommendations  
- Simple reliable layout


### Project Structure ###

taurgovision/
│
├── backend/
│   ├── app.py
│   ├── cv_engine.py
│   ├── ai_engine.py
│   ├── report_generator.py
│   ├── utils.py
│   ├── models.py
│   ├── requirements.txt
│   └── .env.example
│
└── frontend/
├── package.json
├── next.config.mjs
├── pages/
│     ├── _app.js
│     └── index.js
├── components/
│     ├── UploadBox.js
│     └── ResultPanel.js
└── styles/
└── globals.css


