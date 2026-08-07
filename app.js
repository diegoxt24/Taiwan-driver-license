/**
 * Taiwan Driver & Rider Prep Web App - Dual Module Engine
 * Sheppard Air Style Accelerated Learning System + Interactive Practice
 */

// STATE MANAGEMENT
let allQuestions = [];
let filteredQuestions = [];
let cheatSheetData = [];

let currentModule = 'motorcycle'; // 'motorcycle' or 'car'
let currentIndex = 0;
let currentTab = 'mode0'; // mode0, sheppard1, sheppard2, interactive, practice, bookmarks, failed, cheatsheet
let selectedCategory = 'ALL';
let selectedTopic = 'ALL_TOPICS';
let searchQuery = '';

// Interactive Quiz state per question
let interactiveAnswered = {}; // qId -> selectedIndex

// User Profile Data structure stored in localStorage
let activeProfile = 'diego';
let userState = {
  diego: {
    name: 'Diego (Pilot Mode)',
    motorcycle: { bookmarks: [], failedQuestions: [], studiedQuestions: [], examHistory: [] },
    car: { bookmarks: [], failedQuestions: [], studiedQuestions: [], examHistory: [] }
  },
  johana: {
    name: 'Johana (Study Profile)',
    motorcycle: { bookmarks: [], failedQuestions: [], studiedQuestions: [], examHistory: [] },
    car: { bookmarks: [], failedQuestions: [], studiedQuestions: [], examHistory: [] }
  }
};

// Practice Exam State
let examQuestions = [];
let examUserAnswers = {}; // qId -> optionIndex
let examSubmitted = false;

// INITIALIZATION
document.addEventListener('DOMContentLoaded', async () => {
  loadProfileFromStorage();
  await loadModuleData(currentModule);
  setupEventListeners();
  switchTab(currentTab);
});

let masterRulesData = [];

// LOAD MODULE DATA (Motorcycle vs. Car)
async function loadModuleData(mod) {
  currentModule = mod;
  try {
    const qFile = (mod === 'car') ? 'car_questions.json' : 'questions.json';
    const cFile = (mod === 'car') ? 'car_cheat_sheet.json' : 'cheat_sheet.json';
    const mFile = (mod === 'car') ? 'car_master_rules.json' : 'moto_master_rules.json';

    const qResp = await fetch(qFile);
    allQuestions = await qResp.json();

    const cResp = await fetch(cFile);
    cheatSheetData = await cResp.json();

    const mResp = await fetch(mFile);
    masterRulesData = await mResp.json();

    updateModuleHeaderUI();
    updateCategoryAndTopicDropdowns();
    updateFilteredQuestions();
  } catch (err) {
    console.error('Error loading module question bank:', err);
  }
}

function updateModuleHeaderUI() {
  const totalCountEl = document.getElementById('dbTotalCountText');
  if (totalCountEl) {
    totalCountEl.textContent = `${allQuestions.length.toLocaleString()} Questions`;
  }
  const brandIcon = document.getElementById('brandIcon');
  if (brandIcon) {
    if (currentModule === 'car') {
      brandIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A2 2 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>`;
    } else {
      brandIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A2 2 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="3"/><circle cx="17" cy="17" r="3"/></svg>`;
    }
  }
}

function updateCategoryAndTopicDropdowns() {
  const catSelect = document.getElementById('categorySelect');
  const topicSelect = document.getElementById('topicSelect');

  if (catSelect) {
    const cats = Array.from(new Set(allQuestions.map(q => q.category))).filter(Boolean);
    catSelect.innerHTML = `<option value="ALL">All Categories (${allQuestions.length} Questions)</option>` +
      cats.map(c => `<option value="${c}">${c}</option>`).join('');
  }

  if (topicSelect) {
    const topics = Array.from(new Set(allQuestions.map(q => q.topic))).filter(Boolean);
    topicSelect.innerHTML = `<option value="ALL_TOPICS">All Subjects / Topics</option>` +
      topics.map(t => `<option value="${t}">${t}</option>`).join('');
  }
}

// STORAGE PERSISTENCE
function loadProfileFromStorage() {
  const savedState = localStorage.getItem('tw_driver_prep_state_v2');
  if (savedState) {
    try {
      const parsed = JSON.parse(savedState);
      if (parsed.diego) userState = parsed;
    } catch (e) {}
  }
  const savedProfile = localStorage.getItem('tw_driver_active_profile');
  if (savedProfile && userState[savedProfile]) {
    activeProfile = savedProfile;
  }
  updateProfileUI();
}

function saveStateToStorage() {
  localStorage.setItem('tw_driver_prep_state_v2', JSON.stringify(userState));
  localStorage.setItem('tw_driver_active_profile', activeProfile);
  updateDashboardStats();
}

function getModuleData() {
  const p = userState[activeProfile] || userState['diego'];
  if (!p[currentModule]) {
    p[currentModule] = { bookmarks: [], failedQuestions: [], studiedQuestions: [], examHistory: [] };
  }
  return p[currentModule];
}

function updateProfileUI() {
  const profSelect = document.getElementById('profileSelect');
  if (profSelect) profSelect.value = activeProfile;
}

// EVENT LISTENERS SETUP
function setupEventListeners() {
  const profSelect = document.getElementById('profileSelect');
  if (profSelect) {
    profSelect.addEventListener('change', (e) => {
      activeProfile = e.target.value;
      saveStateToStorage();
      updateFilteredQuestions();
      renderCurrentQuestion();
    });
  }

  const expBtn = document.getElementById('exportSyncBtn');
  if (expBtn) {
    expBtn.addEventListener('click', () => {
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(userState, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `taiwan_driver_prep_backup_${activeProfile}.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    });
  }

  const impBtn = document.getElementById('importSyncBtn');
  const impFile = document.getElementById('importFileInput');
  if (impBtn && impFile) {
    impBtn.addEventListener('click', () => impFile.click());
    impFile.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (event) => {
        try {
          const importedData = JSON.parse(event.target.result);
          if (importedData.diego || importedData.johana) {
            userState = importedData;
            saveStateToStorage();
            alert('🎉 Progress synced successfully across devices!');
          }
        } catch (err) {
          alert('⚠️ Invalid backup file format.');
        }
      };
      reader.readAsText(file);
    });
  }
  const modSelect = document.getElementById('moduleSelect');
  if (modSelect) {
    modSelect.addEventListener('change', async (e) => {
      currentIndex = 0;
      await loadModuleData(e.target.value);
      switchTab(currentTab);
    });
  }

  const topicSelect = document.getElementById('topicSelect');
  if (topicSelect) {
    topicSelect.addEventListener('change', (e) => {
      selectedTopic = e.target.value;
      currentIndex = 0;
      updateFilteredQuestions();
      renderCurrentQuestion();
    });
  }

  const catSelect = document.getElementById('categorySelect');
  if (catSelect) {
    catSelect.addEventListener('change', (e) => {
      selectedCategory = e.target.value;
      currentIndex = 0;
      updateFilteredQuestions();
      renderCurrentQuestion();
    });
  }

  const searchInp = document.getElementById('searchInput');
  if (searchInp) {
    searchInp.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim().toLowerCase();
      currentIndex = 0;
      updateFilteredQuestions();
      renderCurrentQuestion();
    });
  }

  // Tab Buttons
  document.querySelectorAll('.nav-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = btn.dataset.tab;
      switchTab(tab);
    });
  });

  // Profile Toggle
  document.getElementById('profileBtn')?.addEventListener('click', () => {
    activeProfile = (activeProfile === 'diego') ? 'student' : 'diego';
    saveStateToStorage();
    updateProfileUI();
    updateFilteredQuestions();
    renderCurrentQuestion();
  });

  // Theme Toggle
  document.getElementById('themeToggleBtn')?.addEventListener('click', () => {
    document.body.classList.toggle('light-theme');
  });

  // Navigation Buttons
  document.getElementById('prevBtn')?.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      renderCurrentQuestion();
    }
  });

  document.getElementById('nextBtn')?.addEventListener('click', () => {
    if (currentIndex < filteredQuestions.length - 1) {
      currentIndex++;
      recordQuestionStudied(filteredQuestions[currentIndex - 1]?.id);
      renderCurrentQuestion();
    }
  });

  // Bookmark Button
  document.getElementById('bookmarkBtn')?.addEventListener('click', () => {
    if (!filteredQuestions[currentIndex]) return;
    const qId = filteredQuestions[currentIndex].id;
    const m = getModuleData();
    const idx = m.bookmarks.indexOf(qId);
    if (idx >= 0) {
      m.bookmarks.splice(idx, 1);
    } else {
      m.bookmarks.push(qId);
    }
    saveStateToStorage();
    updateBookmarkUI(qId);
    if (currentTab === 'bookmarks') {
      updateFilteredQuestions();
      renderCurrentQuestion();
    }
  });

  // Explanation Toggle
  document.getElementById('toggleExplBtn')?.addEventListener('click', () => {
    const card = document.getElementById('explanationCard');
    const label = document.getElementById('explBtnLabel');
    if (card.classList.contains('hidden')) {
      card.classList.remove('hidden');
      label.textContent = 'Hide Explanation';
    } else {
      card.classList.add('hidden');
      label.textContent = 'Show Explanation';
    }
  });

  // Retake / Review / Submit Exam
  document.getElementById('restartExamBtn')?.addEventListener('click', () => {
    startPracticeExam();
  });
  document.getElementById('reviewFailedExamBtn')?.addEventListener('click', () => {
    switchTab('failed');
  });
  document.getElementById('submitExamBtn')?.addEventListener('click', () => {
    submitPracticeExam();
  });

  // Keyboard Shortcuts for Rapid Pilot Study
  document.addEventListener('keydown', (e) => {
    if (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'SELECT') return;
    if (e.key === 'ArrowRight' || e.key === ' ') {
      e.preventDefault();
      document.getElementById('nextBtn')?.click();
    } else if (e.key === 'ArrowLeft') {
      e.preventDefault();
      document.getElementById('prevBtn')?.click();
    } else if (e.key === 'e' || e.key === 'E') {
      document.getElementById('toggleExplBtn')?.click();
    } else if (e.key === 'b' || e.key === 'B') {
      document.getElementById('bookmarkBtn')?.click();
    }
  });
}

// FILTERING LOGIC
function updateFilteredQuestions() {
  const m = getModuleData();

  if (currentTab === 'bookmarks') {
    filteredQuestions = allQuestions.filter(q => m.bookmarks.includes(q.id));
  } else if (currentTab === 'failed') {
    filteredQuestions = allQuestions.filter(q => m.failedQuestions.includes(q.id));
  } else if (currentTab === 'practice') {
    filteredQuestions = examQuestions;
  } else {
    // Sheppard 1, 2, Interactive
    filteredQuestions = allQuestions.filter(q => {
      const matchCat = (selectedCategory === 'ALL' || q.category === selectedCategory);
      const matchTopic = (selectedTopic === 'ALL_TOPICS' || q.topic === selectedTopic);
      const matchSearch = !searchQuery || (
        q.question.toLowerCase().includes(searchQuery) ||
        q.options.some(o => o.toLowerCase().includes(searchQuery))
      );
      return matchCat && matchTopic && matchSearch;
    });
  }

  if (currentIndex >= filteredQuestions.length) {
    currentIndex = Math.max(0, filteredQuestions.length - 1);
  }

  updateDashboardStats();
}

// TAB SWITCHING
function switchTab(tab) {
  currentTab = tab;

  document.querySelectorAll('.nav-tab').forEach(btn => {
    if (btn.dataset.tab === tab) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  const questionCard = document.getElementById('questionContainer');
  const resultCard = document.getElementById('examResultCard');
  const cheatCard = document.getElementById('cheatSheetContainer');
  const masterCardContainer = document.getElementById('masterRulesContainer');

  questionCard.classList.add('hidden');
  resultCard.classList.add('hidden');
  cheatCard.classList.add('hidden');
  if (masterCardContainer) masterCardContainer.classList.add('hidden');

  const modeTitle = document.getElementById('modeTitle');
  const modeDesc = document.getElementById('modeDesc');

  if (tab === 'mode0') {
    const modLabel = (currentModule === 'car') ? 'Car License (汽車)' : 'Motorcycle License (機車)';
    modeTitle.innerHTML = `🧠 Mode 0: Master Rule Grouping (${modLabel})`;
    modeDesc.textContent = 'High-level synthesis: Consolidates 3,000+ questions into 9 core Master Rule Cards for 5x faster learning.';
    if (masterCardContainer) {
      masterCardContainer.classList.remove('hidden');
      renderMasterRules();
    }
  } else if (tab === 'sheppard1') {
    modeTitle.innerHTML = '✨ Sheppard Air Mode 1: Direct Answer Recall';
    modeDesc.textContent = 'Shows ONLY the correct answer for rapid, distraction-free neural memorization.';
    questionCard.classList.remove('hidden');
  } else if (tab === 'sheppard2') {
    modeTitle.innerHTML = '🖍️ Sheppard Air Mode 2: Highlighted Options';
    modeDesc.textContent = 'Displays all options with the correct answer explicitly highlighted in green.';
    questionCard.classList.remove('hidden');
  } else if (tab === 'interactive') {
    modeTitle.innerHTML = '🎯 Interactive Quiz + Instant Feedback';
    modeDesc.textContent = 'Click options for instant Green (Correct) / Red (Incorrect) feedback & law context.';
    questionCard.classList.remove('hidden');
  } else if (tab === 'practice') {
    modeTitle.innerHTML = '⏱️ 50-Question Practice Exam Simulation';
    modeDesc.textContent = 'Simulated test environment with 85% passing score threshold.';
    if (examQuestions.length === 0 || examSubmitted) {
      startPracticeExam();
    } else {
      questionCard.classList.remove('hidden');
    }
  } else if (tab === 'bookmarks') {
    modeTitle.innerHTML = '⭐ Bookmarked Starred Questions';
    modeDesc.textContent = 'Targeted review for your starred key items.';
    questionCard.classList.remove('hidden');
  } else if (tab === 'failed') {
    modeTitle.innerHTML = '⚠️ Failed Questions Retry Bank';
    modeDesc.textContent = 'Automatically review questions missed in previous quizzes/exams.';
    questionCard.classList.remove('hidden');
  } else if (tab === 'cheatsheet') {
    const modLabel = (currentModule === 'car') ? 'Car License (汽車)' : 'Motorcycle License (機車)';
    modeTitle.innerHTML = `📋 ${modLabel} Cram Sheet & Key Facts`;
    modeDesc.textContent = 'Quick reference guide covering numbers, cargo, speeds, BAC limits, fines, and CPR.';
    cheatCard.classList.remove('hidden');
    renderCheatSheet();
  }

  currentIndex = 0;
  updateFilteredQuestions();
  renderCurrentQuestion();
}

// RENDER CURRENT QUESTION
function renderCurrentQuestion() {
  if (currentTab === 'cheatsheet') return;

  const optionsDiv = document.getElementById('optionsContainer');
  const explanationCard = document.getElementById('explanationCard');
  const signBox = document.getElementById('signIllustrationBox');
  const signSvgDiv = document.getElementById('signSvgContainer');

  if (filteredQuestions.length === 0) {
    document.getElementById('questionCategoryBadge').textContent = 'No Items';
    document.getElementById('questionTopicBadge').textContent = 'Empty Bank';
    document.getElementById('questionIndexText').textContent = '0 of 0';
    document.getElementById('questionText').textContent = getEmptyMessage();
    optionsDiv.innerHTML = '';
    signBox.classList.add('hidden');
    explanationCard.classList.add('hidden');
    document.getElementById('prevBtn').disabled = true;
    document.getElementById('nextBtn').disabled = true;
    return;
  }

  const q = filteredQuestions[currentIndex];
  const m = getModuleData();

  // Sign SVG Rendering
  if (q.sign_svg) {
    signSvgDiv.innerHTML = q.sign_svg;
    signBox.classList.remove('hidden');
  } else {
    signBox.classList.add('hidden');
  }

  // Badges
  document.getElementById('questionCategoryBadge').textContent = q.category;
  document.getElementById('questionTopicBadge').textContent = q.topic || 'General Law';
  document.getElementById('questionIndexText').textContent = `Question ${currentIndex + 1} of ${filteredQuestions.length}`;

  // Bookmark Button State
  updateBookmarkUI(q.id);

  // Question Text
  document.getElementById('questionText').textContent = q.question;

  // Render Options By Tab Mode
  optionsDiv.innerHTML = '';
  explanationCard.classList.add('hidden');
  const explTextEl = document.getElementById('explanationText');

  // Prepare explanation HTML with visual diagram if available
  let diagramHTML = '';
  if (q.diagram === 'cargo_rear') {
    diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 400 120" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="50" y="50" width="160" height="30" rx="6" fill="#3b82f6"/><circle cx="80" cy="85" r="14" fill="#64748b"/><circle cx="180" cy="85" r="14" fill="#64748b"/><rect x="210" y="45" width="40" height="35" fill="#f59e0b" rx="4"/><line x1="180" y1="95" x2="260" y2="95" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/><text x="220" y="112" fill="#ef4444" font-size="12" font-weight="bold">Cargo Extension</text></svg></div>`;
  } else if (q.diagram === 'right_of_way') {
    diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 120" style="background:#0f172a; border-radius:8px; width:100%;"><line x1="20" y1="60" x2="280" y2="60" stroke="#10b981" stroke-width="4"/><text x="100" y="45" fill="#10b981" font-size="12" font-weight="bold">Straight-Going Vehicle (Priority #1)</text></svg></div>`;
  } else if (q.diagram === 'alcohol_limit') {
    diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 100" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="30" y="40" width="240" height="20" rx="4" fill="#334155"/><rect x="30" y="40" width="80" height="20" rx="4" fill="#10b981"/><line x1="110" y1="25" x2="110" y2="75" stroke="#ef4444" stroke-width="3"/><text x="110" y="20" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">Legal Limit: 0.15 mg/L</text></svg></div>`;
  } else if (q.diagram === 'tire_tread') {
    diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 100" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="50" y="30" width="200" height="40" fill="#334155" rx="6"/><line x1="100" y1="30" x2="100" y2="70" stroke="#f59e0b" stroke-width="4"/><text x="150" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Min Tread Depth (1.0mm Moto / 1.6mm Car)</text></svg></div>`;
  } else if (q.diagram === 'freeway_distance') {
    diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 350 100" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="30" y="40" width="60" height="25" rx="4" fill="#3b82f6"/><rect x="250" y="40" width="60" height="25" rx="4" fill="#3b82f6"/><line x1="90" y1="52" x2="250" y2="52" stroke="#10b981" stroke-width="2" stroke-dasharray="4"/><text x="170" y="45" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Safe Distance = Speed ÷ 2 (50m @ 100km/h)</text></svg></div>`;
  } else if (q.diagram === 'child_seat') {
    diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 100" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="40" y="25" width="220" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/><text x="150" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Under 4 yrs / 18kg → Mandatory Rear Child Seat</text></svg></div>`;
  } else if (q.diagram === 'speed_limit') {
    diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 100" style="background:#0f172a; border-radius:8px; width:100%;"><circle cx="150" cy="50" r="35" fill="#ffffff" stroke="#ef4444" stroke-width="6"/><text x="150" y="60" fill="#0f172a" font-size="28" font-weight="900" text-anchor="middle">50</text></svg></div>`;
  }

  explTextEl.innerHTML = `<div>${q.explanation || 'Official Taiwan Road Traffic Safety Rule.'}</div>${diagramHTML}`;

  if (currentTab === 'sheppard1') {
    // Mode 1: SHOW ONLY CORRECT ANSWER
    const optBtn = document.createElement('div');
    optBtn.className = 'opt-btn correct-highlight';
    optBtn.innerHTML = `
      <div>
        <div style="font-size:0.7rem; text-transform:uppercase; font-weight:800; color:#34d399; margin-bottom:0.2rem;">Sheppard Air Correct Recall Answer</div>
        <div>${q.correct_answer}</div>
      </div>
      <span style="font-size:1.2rem;">✓</span>
    `;
    optionsDiv.appendChild(optBtn);
  } else if (currentTab === 'sheppard2') {
    // Mode 2: HIGHLIGHT CORRECT ANSWER IN GREEN
    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('div');
      const isCorrect = (idx === q.correct_index);
      if (isCorrect) {
        optBtn.className = 'opt-btn correct-highlight';
        optBtn.innerHTML = `<span>${optText}</span> <span style="font-weight:800; font-size:0.75rem; background:rgba(16,185,129,0.25); padding:0.2rem 0.5rem; border-radius:4px;">CORRECT</span>`;
      } else {
        optBtn.className = 'opt-btn';
        optBtn.style.opacity = '0.5';
        optBtn.innerHTML = `<span>${optText}</span>`;
      }
      optionsDiv.appendChild(optBtn);
    });
  } else if (currentTab === 'interactive') {
    // Mode 3: INTERACTIVE INSTANT RED/GREEN FEEDBACK
    const userSel = interactiveAnswered[q.id];

    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('button');
      optBtn.className = 'opt-btn';

      if (userSel !== undefined) {
        if (idx === q.correct_index) {
          optBtn.classList.add('correct-highlight');
          optBtn.innerHTML = `<span>${optText}</span> <span>✓ Correct</span>`;
        } else if (userSel === idx) {
          optBtn.classList.add('incorrect-highlight');
          optBtn.innerHTML = `<span>${optText}</span> <span>✗ Incorrect</span>`;
        } else {
          optBtn.style.opacity = '0.4';
          optBtn.innerHTML = `<span>${optText}</span>`;
        }
      } else {
        optBtn.innerHTML = `<span>${optText}</span>`;
        optBtn.addEventListener('click', () => {
          interactiveAnswered[q.id] = idx;
          if (idx !== q.correct_index) {
            if (!m.failedQuestions.includes(q.id)) {
              m.failedQuestions.push(q.id);
              saveStateToStorage();
            }
          }
          renderCurrentQuestion();
        });
      }
      optionsDiv.appendChild(optBtn);
    });

    if (userSel !== undefined) {
      explanationCard.classList.remove('hidden');
    }
  } else if (currentTab === 'practice') {
    // Mode 4: PRACTICE EXAM CHOICES
    const userSel = examUserAnswers[q.id];

    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('button');
      optBtn.className = 'opt-btn';

      if (userSel === idx) {
        optBtn.style.borderColor = 'var(--accent-indigo)';
        optBtn.style.backgroundColor = 'rgba(99,102,241,0.2)';
        optBtn.innerHTML = `<span>${optText}</span> <span>Selected</span>`;
      } else {
        optBtn.innerHTML = `<span>${optText}</span>`;
      }

      optBtn.addEventListener('click', () => {
        if (!examSubmitted) {
          examUserAnswers[q.id] = idx;
          renderCurrentQuestion();
        }
      });
      optionsDiv.appendChild(optBtn);
    });
  } else {
    // Bookmarks / Failed Mode -> Full interactivity
    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('div');
      const isCorrect = (idx === q.correct_index);
      if (isCorrect) {
        optBtn.className = 'opt-btn correct-highlight';
        optBtn.innerHTML = `<span>${optText}</span> <span>Correct Choice</span>`;
      } else {
        optBtn.className = 'opt-btn';
        optBtn.style.opacity = '0.6';
        optBtn.innerHTML = `<span>${optText}</span>`;
      }
      optionsDiv.appendChild(optBtn);
    });
    explanationCard.classList.remove('hidden');
  }

  // Update Nav Buttons & Submit Exam Visibility
  const submitBtn = document.getElementById('submitExamBtn');
  if (submitBtn) {
    if (currentTab === 'practice' && !examSubmitted) {
      submitBtn.classList.remove('hidden');
    } else {
      submitBtn.classList.add('hidden');
    }
  }

  document.getElementById('prevBtn').disabled = (currentIndex === 0);
  document.getElementById('nextBtn').disabled = (currentIndex === filteredQuestions.length - 1);
}

function updateBookmarkUI(qId) {
  const m = getModuleData();
  const isBookmarked = m.bookmarks.includes(qId);
  const btn = document.getElementById('bookmarkBtn');
  if (btn) {
    if (isBookmarked) {
      btn.classList.add('bookmarked');
      btn.textContent = '★';
    } else {
      btn.classList.remove('bookmarked');
      btn.textContent = '☆';
    }
  }
}

function recordQuestionStudied(qId) {
  if (!qId) return;
  const m = getModuleData();
  if (!m.studiedQuestions.includes(qId)) {
    m.studiedQuestions.push(qId);
    saveStateToStorage();
  }
}

// PRACTICE EXAM LOGIC
function startPracticeExam() {
  examSubmitted = false;
  examUserAnswers = {};

  const shuffled = [...allQuestions].sort(() => 0.5 - Math.random());
  examQuestions = shuffled.slice(0, Math.min(50, allQuestions.length));

  document.getElementById('questionContainer').classList.remove('hidden');
  document.getElementById('examResultCard').classList.add('hidden');

  updateFilteredQuestions();
  renderCurrentQuestion();
}

function submitPracticeExam() {
  examSubmitted = true;
  let correctCount = 0;
  const m = getModuleData();

  examQuestions.forEach(q => {
    const userSel = examUserAnswers[q.id];
    if (userSel === q.correct_index) {
      correctCount++;
    } else {
      if (!m.failedQuestions.includes(q.id)) {
        m.failedQuestions.push(q.id);
      }
    }
  });

  const total = examQuestions.length || 1;
  const scorePercent = Math.round((correctCount / total) * 100);
  const passed = scorePercent >= 85;

  m.examHistory.push({
    date: new Date().toISOString(),
    score: scorePercent,
    passed: passed,
    totalCount: total,
    correctCount: correctCount
  });

  saveStateToStorage();

  const questionCard = document.getElementById('questionContainer');
  const resultCard = document.getElementById('examResultCard');

  questionCard.classList.add('hidden');
  resultCard.classList.remove('hidden');

  document.getElementById('examResultTitle').textContent = passed ? '🎉 Exam Passed!' : '⚠️ Exam Not Passed';
  document.getElementById('examResultScore').textContent = `${scorePercent}% (${correctCount} / ${total} Correct)`;
  document.getElementById('examResultScore').style.color = passed ? 'var(--accent-emerald)' : 'var(--accent-rose)';
  document.getElementById('examResultStatus').textContent = passed
    ? `Congratulations! You scored ${scorePercent}%. Taiwan Highway Bureau requires 85% to pass.`
    : `You scored ${scorePercent}%. Passing score is 85%. Review failed questions and retake when ready!`;
}

// RENDER CHEAT SHEET
function renderCheatSheet() {
  const container = document.getElementById('cheatSheetContainer');
  container.innerHTML = '';

  cheatSheetData.forEach(sec => {
    const secCard = document.createElement('div');
    secCard.className = 'cheat-card';

    let itemsHTML = sec.items.map(item => `
      <div class="cheat-row">
        <span class="cheat-label">${item.label}</span>
        <span class="cheat-badge">${item.val}</span>
      </div>
    `).join('');

    secCard.innerHTML = `
      <div class="cheat-head">
        <span>${sec.category}</span>
      </div>
      <div>${itemsHTML}</div>
    `;
    container.appendChild(secCard);
  });
}

// RENDER MASTER RULES (MODE 0)
function renderMasterRules() {
  const container = document.getElementById('masterRulesContainer');
  if (!container) return;
  container.innerHTML = '';

  masterRulesData.forEach(rule => {
    const card = document.createElement('div');
    card.className = 'cheat-card';

    let diagramHTML = '';
    if (rule.diagram === 'cargo_rear') {
      diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 400 120" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="50" y="50" width="160" height="30" rx="6" fill="#3b82f6"/><circle cx="80" cy="85" r="14" fill="#64748b"/><circle cx="180" cy="85" r="14" fill="#64748b"/><rect x="210" y="45" width="40" height="35" fill="#f59e0b" rx="4"/><line x1="180" y1="95" x2="260" y2="95" stroke="#ef4444" stroke-width="2" stroke-dasharray="4"/><text x="220" y="112" fill="#ef4444" font-size="12" font-weight="bold">Cargo Extension</text></svg></div>`;
    } else if (rule.diagram === 'right_of_way') {
      diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 120" style="background:#0f172a; border-radius:8px; width:100%;"><line x1="20" y1="60" x2="280" y2="60" stroke="#10b981" stroke-width="4"/><text x="100" y="45" fill="#10b981" font-size="12" font-weight="bold">Straight-Going Vehicle (Priority #1)</text></svg></div>`;
    } else if (rule.diagram === 'alcohol_limit') {
      diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 100" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="30" y="40" width="240" height="20" rx="4" fill="#334155"/><rect x="30" y="40" width="80" height="20" rx="4" fill="#10b981"/><line x1="110" y1="25" x2="110" y2="75" stroke="#ef4444" stroke-width="3"/><text x="110" y="20" fill="#ef4444" font-size="11" font-weight="bold" text-anchor="middle">Legal Limit: 0.15 mg/L</text></svg></div>`;
    } else if (rule.diagram === 'tire_tread') {
      diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 100" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="50" y="30" width="200" height="40" fill="#334155" rx="6"/><line x1="100" y1="30" x2="100" y2="70" stroke="#f59e0b" stroke-width="4"/><text x="150" y="55" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">Min Tread Depth (1.0mm Moto / 1.6mm Car)</text></svg></div>`;
    } else if (rule.diagram === 'freeway_distance') {
      diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 350 100" style="background:#0f172a; border-radius:8px; width:100%;"><rect x="30" y="40" width="60" height="25" rx="4" fill="#3b82f6"/><rect x="250" y="40" width="60" height="25" rx="4" fill="#3b82f6"/><line x1="90" y1="52" x2="250" y2="52" stroke="#10b981" stroke-width="2" stroke-dasharray="4"/><text x="170" y="45" fill="#10b981" font-size="12" font-weight="bold" text-anchor="middle">Safe Distance = Speed ÷ 2 (50m @ 100km/h)</text></svg></div>`;
    } else if (rule.diagram === 'speed_limit') {
      diagramHTML = `<div class="rule-diagram-box"><svg viewBox="0 0 300 100" style="background:#0f172a; border-radius:8px; width:100%;"><circle cx="150" cy="50" r="35" fill="#ffffff" stroke="#ef4444" stroke-width="6"/><text x="150" y="60" fill="#0f172a" font-size="28" font-weight="900" text-anchor="middle">50</text></svg></div>`;
    }

    let optionsHTML = rule.canonical_options.map((opt, i) => `
      <div style="padding:0.4rem 0.6rem; border-radius:6px; margin-top:0.3rem; font-size:0.85rem; ${i === rule.canonical_correct_index ? 'background:rgba(16,185,129,0.2); color:#34d399; font-weight:700;' : 'opacity:0.6;'}">
        ${opt}
      </div>
    `).join('');

    card.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid var(--border-color); padding-bottom:0.5rem; margin-bottom:0.75rem;">
        <span style="font-size:1.1rem; font-weight:800; color:var(--text-main);">${rule.title}</span>
        <span class="cheat-badge" style="background:rgba(168,85,247,0.2); color:#c084fc; border-color:rgba(168,85,247,0.4);">Covers ${rule.matched_question_count} Questions</span>
      </div>

      <div style="font-size:0.88rem; color:var(--text-main); line-height:1.6; margin-bottom:0.75rem; white-space:pre-line;">
        ${rule.summary}
      </div>

      ${diagramHTML}

      <div style="margin-top:1rem; padding:0.75rem; background:var(--bg-input); border-radius:10px; border:1px solid var(--border-color);">
        <div style="font-size:0.72rem; font-weight:800; text-transform:uppercase; color:var(--accent-indigo); margin-bottom:0.3rem;">Canonical Representative Question</div>
        <div style="font-weight:700; font-size:0.9rem; margin-bottom:0.4rem;">${rule.canonical_question}</div>
        <div>${optionsHTML}</div>
      </div>
    `;

    container.appendChild(card);
  });
}

// DASHBOARD STATS
function updateDashboardStats() {
  const m = getModuleData();

  const bmBadge = document.getElementById('navBookmarkBadge');
  const failBadge = document.getElementById('navFailedBadge');
  if (bmBadge) bmBadge.textContent = m.bookmarks.length;
  if (failBadge) failBadge.textContent = m.failedQuestions.length;

  const statMastered = document.getElementById('statMastered');
  const statFailed = document.getElementById('statFailed');
  if (statMastered) statMastered.textContent = m.studiedQuestions.length;
  if (statFailed) statFailed.textContent = m.failedQuestions.length;

  const total = allQuestions.length || 1;
  const studiedRatio = Math.min(1, m.studiedQuestions.length / total);
  const readiness = Math.round(studiedRatio * 100);

  const scoreEl = document.getElementById('readinessScore');
  const barEl = document.getElementById('readinessBar');
  if (scoreEl) scoreEl.textContent = `${readiness}%`;
  if (barEl) barEl.style.width = `${readiness}%`;
}

function getEmptyMessage() {
  if (currentTab === 'bookmarks') {
    return 'No bookmarked questions in this module yet. Click star (☆) on any question to add it here!';
  } else if (currentTab === 'failed') {
    return 'No failed questions! Try the Interactive Quiz or 50-Q Practice Exam to test your skills.';
  } else {
    return 'No questions match your current search/filter criteria.';
  }
}
