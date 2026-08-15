# 🇹🇼 Taiwan Driver & Motorcycle License Exam Prep (2026 Edition)

An ultra-modern, offline-first web application engineered for candidates preparing for the **Taiwan Ministry of Transportation and Communications (MOTC) Highway Bureau (交通部公路局 - THB)** written examinations for both **Automobile (汽車)** and **Motorcycle (機車)** licenses.

![Taiwan Driver Prep](https://img.shields.io/badge/Taiwan%20THB%20Exam-2026%20Official-emerald?style=for-the-badge&logo=taiwan)
![Car Bank](https://img.shields.io/badge/Car%20Bank-1%2C090%20Questions-blue?style=for-the-badge)
![Motorcycle Bank](https://img.shields.io/badge/Moto%20Bank-932%20Questions-indigo?style=for-the-badge)
![Passing Threshold](https://img.shields.io/badge/Passing%20Score-85%25-orange?style=for-the-badge)
![Cloud Sync](https://img.shields.io/badge/Cloud%20Sync-Active-brightgreen?style=for-the-badge)

---

## 🚀 Live Demo & Deployment

* **Live Web App**: [https://diegoxt24.github.io/Taiwan-driver-license/](https://diegoxt24.github.io/Taiwan-driver-license/)
* **Single-File Offline Version**: [`standalone_app.html`](standalone_app.html) (double-click to open in any browser, no internet or server required).

---

## 🌟 Key Features & Study Modes

The platform combines **Sheppard Air Direct Recall**, active testing, official spatial sign graphics, streaming hazard perception video integration, and automatic multi-device cloud synchronization.

### 🧠 Mode 0: Master Rules Synthesized Cards
Consolidates the official regulations into core **Master Rule Cards** for 5x faster learning:
* **Key Facts & Synthesis**: High-yield legal summaries and fines.
* **Visual SVG Diagrams**: Custom visual illustrations for speed limits, alcohol BAC thresholds, crosswalk rules, 2-stage door opening (Dooring law), and CPR protocols.
* **Correlated Canonical Questions**: Direct correlation with official THB test items.

### ✨ Mode 1: Sheppard Air Direct Recall
* Displays **ONLY the correct answer** with an emerald green checkmark (`✓`).
* Eliminates distractor options from memory to build instantaneous, subconscious correct-answer recognition.

### 👁️ Mode 2: Highlighted Options
* Renders all options with the **correct choice highlighted in green**.
* Ideal for rapid secondary review before simulated mock exams.

### 🎯 Mode 3: Interactive Quiz with Instant Feedback
* Immediate **Green (Correct)** or **Red (Incorrect)** feedback on click.
* Incorrectly answered questions are automatically recorded in your personal **Failed Questions Bank**.
* Comprehensive **Educational Explanations** detailing why the correct option is right and why distractors are wrong.

### 📝 Mode 4: 50-Question Practice Exam Simulation
* Generates a realistic **50-Question Mock Exam** mirroring the official test format.
* Official **85% passing threshold** with final score breakdown and review screen.

### ⭐ Starred Bookmarks & ⚠️ Failed Questions Retries
* Star difficult questions anytime for targeted revision under the **Bookmarked** tab.
* Automatically track and retry mistakes in the **Failed Items** bank.

### 📋 Complete NT$ Fine & Legal Cheat Sheets
Quick-reference cram tables covering exact numbers:
* **Running Red Light**: NT$1,800 to NT$5,400 + 3 demerit points.
* **Handheld Phone**: NT$3,000 (Car) / NT$1,000 (Motorcycle).
* **Alcohol BAC Limits**: 0.15 mg/L administrative / 0.25 mg/L criminal prosecution / NT$180,000 refusal fine.
* **Motorcycle Cargo Limits**: Rear extension ≤ 50 cm / Handlebar width extension ≤ 10 cm.
* **First Aid & CPR**: Airway (B) → Bleeding (A) → Fracture (C); CPR ratio = 30 compressions : 2 rescue breaths (30:2).

---

## ☁️ Zero-Config Cloud Sync & Universal Backup Hub

* **Automatic Background Cloud Sync**: Seamlessly synchronizes answered questions, bookmarks, and test history across **iPad, iPhone, Android, PC, and Mac**.
* **Smart Non-Destructive Merge**: Unions progress from different devices so questions studied offline are never overwritten or lost.
* **Universal iPad / Mobile Backup Hub**:
  * 📱 **AirDrop & iOS Files**: Native `navigator.share` integration to save `.json` backups directly to iCloud, Files, Notes, or AirDrop.
  * 📋 **One-Click Clipboard Copy**: Instantly copy raw JSON backup code to paste across devices.
  * 💾 **Direct JSON Download**: Downloadable timestamped backup files.
  * 📤 **Pasted Code & File Restore**: Restore progress on any device in seconds.
* **Offline-First PWA Support**: Full Service Worker caching (`sw.js`) ensures the application works seamlessly without an internet connection.

---

## 📊 Official Question Bank Coverage (100% Verifiable)

Extracted directly from official Taiwan Highway Bureau (THB / 交通部公路局) English exam regulations:

| Module | Official THB Source | Unique Questions |
| :--- | :--- | :---: |
| 🚗 **Automobile (汽車)** | Official 2026 Car Question Bank (Regulations, Signs & Hazard Perception) | **1,090 Questions** |
| 🏍️ **Motorcycle (機車)** | Official 2026 Motorcycle Question Bank (Regulations, Signs & Hazard Perception) | **932 Questions** |
| 👥 **User Profiles** | Multi-profile tracking for **Diego**, **Johana**, and **Alejandro** | **Independent Progress** |

---

## 📁 Repository Structure

```text
├── assets/                  # High-resolution traffic sign graphics & illustrations
├── Documentos oficiales/    # Official THB PDF regulation source files
├── index.html               # Main application entry point (PWA ready)
├── styles.css               # Modern glassmorphic responsive stylesheet (Dark/Light)
├── app.js                   # Application logic, study engines & cloud sync
├── sw.js                    # Service Worker for offline caching & network-first updates
├── manifest.json            # PWA manifest configuration
├── questions.json           # 932 verified official Motorcycle questions
├── car_questions.json       # 1,090 verified official Car questions
├── moto_master_rules.json   # Motorcycle Master Rule synthesized cards
├── car_master_rules.json    # Car Master Rule synthesized cards
├── cheat_sheet.json         # Motorcycle NT$ fine cram tables
├── car_cheat_sheet.json     # Car NT$ fine cram tables
├── user_sync_state.json     # Synced user state backup
├── standalone_app.html      # Fully self-contained, single-file offline application
├── build_standalone.py      # Build script to generate standalone_app.html
├── server.py                # Optional local development Python HTTP server
└── README.md                # Project documentation
```

---

## 🛠️ How to Run Locally

### Option 1: Open Standalone File (No Server Needed)
Double-click [`standalone_app.html`](standalone_app.html) to open directly in any browser.

### Option 2: Run with Python Local Server
```bash
# Clone the repository
git clone https://github.com/diegoxt24/Taiwan-driver-license.git
cd Taiwan-driver-license

# Start local server
python server.py
```
Open your browser at `http://localhost:8080` (or the local network IP displayed in console for mobile access).

---

## 📄 License & Attribution

All exam questions, traffic signs, and safety regulations are official public assets published by the **Taiwan Ministry of Transportation and Communications (MOTC) Highway Bureau (交通部公路局)**.
