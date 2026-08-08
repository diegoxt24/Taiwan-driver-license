# 🇹🇼 Taiwan Driving & Riding License Written Exam Prep Master App (2026 Edition)

An ultra-premium, high-yield web application designed to help candidates achieve a **100% score** on the official **Taiwan Highway Bureau (THB / 交通部公路局)** Written License Examinations for both **Automobile (汽車)** and **Motorcycle (機車)** licenses.

![Taiwan Driver Prep Preview](https://img.shields.io/badge/Taiwan%20THB%20Exam-2026%20Edition-emerald?style=for-the-badge&logo=taiwan)
![Question Bank](https://img.shields.io/badge/Total%20Questions-3%2C555%20Verified-blue?style=for-the-badge)
![Passing Score](https://img.shields.io/badge/Passing%20Threshold-85%25-orange?style=for-the-badge)

---

## 🌟 Key Features & Study Modes

The app incorporates **Sheppard Air Direct Recall methodology**, active recall learning, spatial sign graphic matching, streaming hazard perception video integration, and custom profile progress syncing.

### 🧠 Mode 0: Master Rule Grouping (75 Synthesized Cards)
Consolidates the massive 3,555 official question bank into **75 core Master Rule Cards** for 5x faster learning speed:
- **Title, Summary & Key Facts**: Clear high-yield legal synthesis.
- **Visual SVG Diagrams**: Custom visual diagrams for Speed Limits (50/40/15 km/h), Alcohol BAC thresholds, Crosswalk Yielding (3m / 4 stripes), 2-Stage Door Opening, and CPR Protocol (30:2).
- **Strict Canonical Questions**: Every card pairs with a 100% correlated canonical question from the official THB exam bank.

### ✨ Sheppard Air Mode 1: Direct Answer Recall
- Shows **ONLY the correct answer** with an emerald green checkmark (`✓`).
- Eliminates distractor options from memory to build rapid, subconscious correct-answer recognition.

### 🖍️ Sheppard Air Mode 2: Highlighted Options
- Renders all multiple-choice options with the **correct option highlighted in green**.
- Great for secondary review before taking mock exams.

### 🎯 Mode 3: Interactive Quiz with Instant Feedback
- Click any option for instant **Green (Correct)** or **Red (Incorrect)** feedback.
- Incorrectly answered questions are automatically saved to your personal **Failed Questions Retry Bank**.
- Reveals custom **Educational Explanations** detailing **Why the choice is Right** and **Why alternative options are Wrong**.

### ⏱️ Mode 4: 50-Question Practice Exam Simulation
- Generates a realistic **50-Question Mock Exam** drawn directly from the official THB question bank.
- 85% passing threshold requirement.
- Displays a final score breakdown and score card upon submission.

### ⭐ Starred Bookmarks & ⚠️ Failed Questions Retries
- Star key questions anytime to review under the **Bookmarked** tab.
- Track weak areas automatically in the **Failed Questions** bank.

### 📋 Complete NT$ Fine & Law Cram Sheet
Quick-reference cram guide covering exact numbers:
- **Running Red Light**: NT$1,800 to NT$5,400 fine + 3 demerit points.
- **Handheld Mobile Phone**: NT$3,000 fine (Car) / NT$1,000 fine (Motorcycle).
- **Drunk Driving BAC**: 0.15 mg/L administrative (NT$30k-120k Car / NT$15k-90k Moto) / 0.25 mg/L criminal prosecution / NT$180,000 BAC refusal fine.
- **Cargo Dimensions**: Motorcycle rear extension <= 50 cm / handlebar width extension <= 10 cm.
- **First Aid & CPR**: Priority = Airway (B) -> Bleeding (A) -> Fracture (C); CPR ratio = 30 compressions to 2 rescue breaths (30:2).

### 👥 Dual User Profile Syncing & Backup
- Independent progress tracking for **Diego** and **Johana** profiles.
- One-click **JSON Backup & Restore Sync** across desktop, tablet, and mobile devices.

---

## 📂 Official Question Bank Coverage (100% Verifiable)

Extracted directly from official Taiwan Highway Bureau (THB / 交通部公路局) PDFs announced for 2026:

| Module | Official PDF Source Files | Unique Questions |
| :--- | :--- | :---: |
| 🚗 **Automobile (汽車)** | `汽車筆試題庫_英文完整版_115年_含圖示_1090題.pdf`<br>`1150605-危險感知影片題(英文版).pdf` | **1,073 Questions** |
| 🛵 **Motorcycle (機車)** | `Motorcycle_License_Written_Test_Question_Bank_English0127.pdf`<br>`機車法規選擇題-英文1140516.pdf`<br>`機車法規是非題-英文1130110.pdf`<br>`機車標誌選擇題-英文-1131113.pdf`<br>`機車標誌是非題-英文-1131113.pdf`<br>`機車危險感知體驗板影片題目113.08.30.pdf` | **2,482 Questions** |
| 📊 **Total Bank** | **100% Coverage of All Official Exam PDFs** | **3,555 Unique Items** |

---

## 🛠️ Technology Stack & Architecture

- **Frontend**: Vanilla HTML5, Modern Responsive CSS3 (Glassmorphism, Dark/Light theme), Pure ES6+ JavaScript.
- **Offline PWA Support**: `standalone_app.html` bundles all 3,555 questions, 75 Master Rules, SVG diagrams, and CSS into a single self-contained file.
- **Media & Assets**: High-resolution cropped road sign graphics (`assets/car_signs/` & `assets/moto_signs/`) and direct THB streaming hazard perception video links.

---

## 🚀 How to Run Locally

### Option 1: Open Single Standalone File
Simply double click [`standalone_app.html`](standalone_app.html) in any browser (Chrome, Safari, Edge, Firefox) — **no web server required!**

### Option 2: Local Python HTTP Server
```bash
# Clone the repository
git clone https://github.com/diegoxt24/Taiwan-driver-license.git
cd Taiwan-driver-license

# Start local server
python -m http.server 8000
```
Open your browser at `http://localhost:8000`.

---

## 📄 License & Attribution

All exam questions, traffic signs, and hazard perception video streaming links are official public safety training assets published by the **Taiwan Ministry of Transportation and Communications (MOTC) Highway Bureau (交通部公路局)**.
