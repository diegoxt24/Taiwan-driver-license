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
  },
  alejandro: {
    name: 'Alejandro (Study Profile)',
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

// CLOUD AUTO-SYNC ENGINE (OFFLINE FIRST + MULTI-DEVICE INSTANT SYNC)
const CLOUD_ENDPOINT = './user_sync_state.json'; 

async function syncWithCloud(forcePush = false) {
  const syncBadge = document.getElementById('cloudSyncStatus');
  const syncText = document.getElementById('cloudSyncText');

  if (!navigator.onLine) {
    if (syncBadge) {
      syncBadge.style.background = 'rgba(245,158,11,0.15)';
      syncBadge.style.color = '#fbbf24';
      syncBadge.style.borderColor = 'rgba(245,158,11,0.3)';
    }
    if (syncText) syncText.textContent = 'Offline Mode (Local Saved)';
    return;
  }

  try {
    // 1. Fetch and merge from server / cloud
    const res = await fetch(CLOUD_ENDPOINT + '?t=' + Date.now(), {
      headers: { 'Accept': 'application/json' }
    });

    if (res.ok) {
      const remoteRecord = await res.json();

      if (remoteRecord && remoteRecord.diego) {
        // Smart Merge Studied Questions & Last Indices across devices
        ['diego', 'johana', 'alejandro'].forEach(prof => {
          ['motorcycle', 'car'].forEach(mod => {
            if (remoteRecord[prof] && remoteRecord[prof][mod] && userState[prof] && userState[prof][mod]) {
              const rStudied = remoteRecord[prof][mod].studiedQuestions || [];
              const lStudied = userState[prof][mod].studiedQuestions || [];
              const mergedStudied = Array.from(new Set([...rStudied, ...lStudied]));
              
              userState[prof][mod].studiedQuestions = mergedStudied;

              const rFailed = remoteRecord[prof][mod].failedQuestions || [];
              const lFailed = userState[prof][mod].failedQuestions || [];
              userState[prof][mod].failedQuestions = Array.from(new Set([...rFailed, ...lFailed]));

              const rBook = remoteRecord[prof][mod].bookmarks || [];
              const lBook = userState[prof][mod].bookmarks || [];
              userState[prof][mod].bookmarks = Array.from(new Set([...rBook, ...lBook]));
            }
          });
        });

        localStorage.setItem('tw_driver_prep_state_v2', JSON.stringify(userState));
        localStorage.setItem('tw_driver_last_sync_time', Date.now().toString());
        updateDashboardStats();
        renderCurrentQuestion();
        if (syncBadge) {
          syncBadge.style.background = 'rgba(16, 185, 129, 0.15)';
          syncBadge.style.color = '#34d399';
          syncBadge.style.borderColor = 'rgba(16, 185, 129, 0.3)';
        }
        if (syncText) syncText.textContent = 'Auto-Synced ✓';
      }
    }
  } catch (e) {
    console.warn('Sync fetch info:', e);
  }

  // 2. If pushing updates or when studying, broadcast update to server
  if (forcePush) {
    try {
      userState.last_updated = Date.now();
      await fetch(CLOUD_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userState)
      });
    } catch (e) {
      // Offline fallback
    }
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
  
  // Trigger Background Cloud Sync
  syncWithCloud(false);
}

function saveStateToStorage() {
  localStorage.setItem('tw_driver_prep_state_v2', JSON.stringify(userState));
  localStorage.setItem('tw_driver_active_profile', activeProfile);
  updateDashboardStats();

  // Auto-sync to Cloud in background
  syncWithCloud(true);
}

function getModuleData() {
  const p = userState[activeProfile] || userState['diego'];
  if (!p[currentModule]) {
    p[currentModule] = { 
      bookmarks: [], 
      failedQuestions: [], 
      studiedQuestions: [], 
      examHistory: [],
      lastIndices: { sheppard1: 0, sheppard2: 0, interactive: 0, mode0: 0, bookmarks: 0, failed: 0 }
    };
  }
  if (!p[currentModule].lastIndices) {
    p[currentModule].lastIndices = { sheppard1: 0, sheppard2: 0, interactive: 0, mode0: 0, bookmarks: 0, failed: 0 };
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
          if (importedData.diego || importedData.johana || importedData.alejandro) {
            userState = importedData;
            saveStateToStorage();
            updateFilteredQuestions();
            renderCurrentQuestion();
            alert('🎉 Progress synced successfully across devices!');
          } else {
            alert('⚠️ Unrecognized backup structure.');
          }
        } catch (err) {
          alert('⚠️ Invalid JSON backup file format.');
        }
      };
      reader.readAsText(file);
    });
  }
  const modSelect = document.getElementById('moduleSelect');
  if (modSelect) {
    modSelect.addEventListener('change', async (e) => {
      currentIndex = 0;
      examQuestions = [];
      examSubmitted = false;
      examUserAnswers = {};
      await loadModuleData(e.target.value);
      if (currentTab === 'practice') {
        startPracticeExam();
      } else {
        switchTab(currentTab);
      }
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

  // Restart Current Mode Button
  const restartBtn = document.getElementById('restartModeBtn');
  if (restartBtn) {
    restartBtn.addEventListener('click', () => {
      if (confirm(`Reset current mode progress (${currentTab}) back to Question #1? Your overall studied progress and Exam Readiness will be preserved.`)) {
        currentIndex = 0;
        const m = getModuleData();
        if (m.lastIndices) m.lastIndices[currentTab] = 0;
        saveStateToStorage();
        renderCurrentQuestion();
      }
    });
  }

  // Jump-to-Question Input Listener
  const jumpInp = document.getElementById('jumpInput');
  if (jumpInp) {
    jumpInp.addEventListener('change', (e) => {
      const targetVal = parseInt(e.target.value);
      if (!isNaN(targetVal) && targetVal >= 1 && targetVal <= filteredQuestions.length) {
        currentIndex = targetVal - 1;
        const m = getModuleData();
        if (m.lastIndices) m.lastIndices[currentTab] = currentIndex;
        saveStateToStorage();
        renderCurrentQuestion();
      }
    });
  }

  // Tab Buttons
  document.querySelectorAll('.nav-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      const tab = btn.dataset.tab;
      switchTab(tab);
    });
  });



  // Keyboard Shortcuts for Rapid Evaluation (Arrow keys & 1/2/3 option selection)
  window.addEventListener('keydown', (e) => {
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT' || e.target.tagName === 'TEXTAREA') return;
    if (e.key === 'ArrowLeft') {
      document.getElementById('prevBtn')?.click();
    } else if (e.key === 'ArrowRight') {
      document.getElementById('nextBtn')?.click();
    } else if (['1', '2', '3'].includes(e.key)) {
      const optBtns = document.querySelectorAll('#optionsContainer button.opt-btn');
      const idx = parseInt(e.key) - 1;
      if (optBtns[idx]) {
        optBtns[idx].click();
      }
    }
  });

  // Theme Toggle
  document.getElementById('themeToggleBtn')?.addEventListener('click', () => {
    document.body.classList.toggle('light-theme');
  });

  // Mobile Bottom Navigation Bar Listeners
  document.getElementById('mobilePrevBtn')?.addEventListener('click', () => {
    document.getElementById('prevBtn')?.click();
  });
  document.getElementById('mobileNextBtn')?.addEventListener('click', () => {
    document.getElementById('nextBtn')?.click();
  });
  document.getElementById('mobileExplBtn')?.addEventListener('click', () => {
    document.getElementById('toggleExplBtn')?.click();
  });
  document.getElementById('mobileSubmitBtn')?.addEventListener('click', () => {
    document.getElementById('submitExamBtn')?.click();
  });

  // Filter Drawer Toggle on Mobile
  document.getElementById('filterToggleBtn')?.addEventListener('click', () => {
    const sidebar = document.getElementById('sidebarPanel');
    if (sidebar) {
      sidebar.classList.toggle('collapsed');
    }
  });

  // Navigation Buttons
  document.getElementById('prevBtn')?.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      const m = getModuleData();
      if (m.lastIndices) m.lastIndices[currentTab] = currentIndex;
      saveStateToStorage();
      renderCurrentQuestion();
    }
  });

  document.getElementById('nextBtn')?.addEventListener('click', () => {
    if (currentIndex < filteredQuestions.length - 1) {
      currentIndex++;
      const m = getModuleData();
      if (m.lastIndices) m.lastIndices[currentTab] = currentIndex;
      saveStateToStorage();
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

  const m = getModuleData();
  if (m.lastIndices && m.lastIndices[tab] !== undefined) {
    currentIndex = m.lastIndices[tab];
  } else {
    currentIndex = 0;
  }
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

  // Sign Image & Video Link Rendering
  if (q.sign_image || q.sign_svg || q.video_link) {
    let mediaHTML = '';
    if (q.sign_image) {
      mediaHTML += `<div style="text-align:center; padding:0.5rem;"><img src="${q.sign_image}" style="max-height:120px; max-width:100%; border-radius:8px; border:1px solid var(--border-color); background:#fff; padding:4px;" alt="Official Sign Image" /></div>`;
    } else if (q.sign_svg) {
      mediaHTML += q.sign_svg;
    }
    if (q.video_link) {
      mediaHTML += `<div style="text-align:center; margin-top:0.5rem;"><a href="${q.video_link}" target="_blank" rel="noopener" class="btn-primary" style="display:inline-flex; align-items:center; gap:0.4rem; padding:0.4rem 0.8rem; font-size:0.82rem; text-decoration:none; border-radius:6px; background:#ef4444; color:#fff;">🎬 Watch Official THB Hazard Video #${q.video_number || ''}</a></div>`;
    }
    signSvgDiv.innerHTML = mediaHTML;
    signBox.classList.remove('hidden');
  } else {
    signBox.classList.add('hidden');
  }

  // Badges & Jump Input Sync
  const isStudied = m.studiedQuestions && m.studiedQuestions.includes(q.id);
  const studiedBadgeHTML = isStudied ? `<span style="font-size:0.7rem; font-weight:800; background:rgba(16,185,129,0.2); color:#34d399; border:1px solid rgba(16,185,129,0.4); padding:0.15rem 0.45rem; border-radius:6px; margin-right:0.4rem;">✓ STUDIED</span>` : '';
  
  document.getElementById('questionCategoryBadge').innerHTML = studiedBadgeHTML + q.category;
  document.getElementById('questionTopicBadge').textContent = q.topic || 'General Law';
  document.getElementById('questionIndexText').textContent = `Question ${currentIndex + 1} of ${filteredQuestions.length}`;
  const jumpInpEl = document.getElementById('jumpInput');
  if (jumpInpEl) {
    jumpInpEl.value = currentIndex + 1;
    jumpInpEl.max = filteredQuestions.length;
  }

  // Bookmark Button State
  updateBookmarkUI(q.id);

  // Question Text
  document.getElementById('questionText').textContent = q.question;

  // Render Options By Tab Mode
  optionsDiv.innerHTML = '';
  explanationCard.classList.add('hidden');
  const explLabel = document.getElementById('explBtnLabel');
  if (explLabel) explLabel.textContent = 'Show Explanation';
  const explTextEl = document.getElementById('explanationText');

  // Prepare explanation HTML with visual diagram if available
  let diagramHTML = '';
  if (q.diagram) {
    diagramHTML = getDiagramHTML(q.diagram, currentModule);
  }

  const formattedExpl = (q.explanation || 'Official Taiwan Road Traffic Safety Rule.')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/\n\n/g, '<br/><br/>')
    .replace(/\n/g, '<br/>');

  explTextEl.innerHTML = `<div style="line-height:1.5; font-size:0.92rem;">${formattedExpl}</div>${diagramHTML}`;

  if (currentTab === 'sheppard1') {
    // Mode 1: SHOW ONLY CORRECT ANSWER (Clickable to mark studied)
    const optBtn = document.createElement('button');
    optBtn.className = 'opt-btn correct-highlight';
    optBtn.style.width = '100%';
    optBtn.style.cursor = 'pointer';
    optBtn.innerHTML = `
      <div>
        <div style="font-size:0.7rem; text-transform:uppercase; font-weight:800; color:#34d399; margin-bottom:0.2rem;">Sheppard Air Correct Recall Answer ${isStudied ? '(Marked Studied ✓)' : '(Click to Mark Studied)'}</div>
        <div style="font-size:0.95rem; font-weight:700;">${q.correct_answer}</div>
      </div>
      <span style="font-size:1.2rem;">${isStudied ? '✓' : '👉'}</span>
    `;
    optBtn.addEventListener('click', () => {
      recordQuestionStudied(q.id);
      renderCurrentQuestion();
    });
    optionsDiv.appendChild(optBtn);
  } else if (currentTab === 'sheppard2') {
    // Mode 2: HIGHLIGHT CORRECT ANSWER IN GREEN (Clickable to mark studied)
    q.options.forEach((optText, idx) => {
      const optBtn = document.createElement('button');
      optBtn.style.width = '100%';
      optBtn.style.cursor = 'pointer';
      const isCorrect = (idx === q.correct_index);
      if (isCorrect) {
        optBtn.className = 'opt-btn correct-highlight';
        optBtn.innerHTML = `<span>${optText}</span> <span style="font-weight:800; font-size:0.75rem; background:rgba(16,185,129,0.25); padding:0.2rem 0.5rem; border-radius:4px;">${isStudied ? '✓ STUDIED' : 'CORRECT (CLICK)'}</span>`;
      } else {
        optBtn.className = 'opt-btn';
        optBtn.style.opacity = '0.5';
        optBtn.innerHTML = `<span>${optText}</span>`;
      }
      optBtn.addEventListener('click', () => {
        recordQuestionStudied(q.id);
        renderCurrentQuestion();
      });
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
      if (explLabel) explLabel.textContent = 'Hide Explanation';
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
    if (explLabel) explLabel.textContent = 'Hide Explanation';
  }

  // Update Nav Buttons & Submit Exam Visibility
  const submitBtn = document.getElementById('submitExamBtn');
  const mobileSubmitBtn = document.getElementById('mobileSubmitBtn');
  const isPracticeActive = (currentTab === 'practice' && !examSubmitted);

  if (submitBtn) {
    if (isPracticeActive) submitBtn.classList.remove('hidden');
    else submitBtn.classList.add('hidden');
  }
  if (mobileSubmitBtn) {
    if (isPracticeActive) mobileSubmitBtn.classList.remove('hidden');
    else mobileSubmitBtn.classList.add('hidden');
  }

  const isFirst = (currentIndex === 0 || filteredQuestions.length === 0);
  const isLast = (currentIndex === filteredQuestions.length - 1 || filteredQuestions.length === 0);

  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const mobilePrevBtn = document.getElementById('mobilePrevBtn');
  const mobileNextBtn = document.getElementById('mobileNextBtn');

  if (prevBtn) prevBtn.disabled = isFirst;
  if (nextBtn) nextBtn.disabled = isLast;
  if (mobilePrevBtn) mobilePrevBtn.disabled = isFirst;
  if (mobileNextBtn) mobileNextBtn.disabled = isLast;
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
        <span class="cheat-badge">${item.value || item.val || ''}</span>
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

function getDiagramHTML(diagramKey, moduleType) {
  const isCar = moduleType === 'car';
  if (diagramKey === 'car_door') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="35" width="120" height="40" rx="8" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="55" cy="75" r="10" fill="#64748b"/>
        <circle cx="125" cy="75" r="10" fill="#64748b"/>
        <line x1="120" y1="35" x2="160" y2="10" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
        <circle cx="160" cy="10" r="4" fill="#ef4444"/>
        <text x="240" y="45" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Car Door Warning!</text>
        <text x="240" y="65" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Fine: NT$2,400–4,800</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'phone_fine') {
    const fineText = isCar ? "Fine: NT$3,000 (Car)" : "Fine: NT$1,000 (Moto)";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="60" y="20" width="35" height="60" rx="5" fill="#1e293b" stroke="#f59e0b" stroke-width="3"/>
        <rect x="67" y="27" width="21" height="40" rx="2" fill="#38bdf8"/>
        <circle cx="77" cy="73" r="2.5" fill="#f59e0b"/>
        <circle cx="77" cy="50" r="28" fill="none" stroke="#ef4444" stroke-width="4"/>
        <line x1="57" y1="30" x2="97" y2="70" stroke="#ef4444" stroke-width="4"/>
        <text x="220" y="45" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">No Handheld Phone</text>
        <text x="220" y="65" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">${fineText}</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'seatbelt_law') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="40" y="20" width="80" height="60" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <line x1="45" y1="25" x2="115" y2="75" stroke="#10b981" stroke-width="6"/>
        <text x="230" y="45" fill="#10b981" font-size="13" font-weight="800" text-anchor="middle">Seatbelt Mandatory</text>
        <text x="230" y="65" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">All Occupants (Front & Rear)</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'speed_limit_50') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <circle cx="80" cy="50" r="32" fill="#ffffff" stroke="#ef4444" stroke-width="7"/>
        <text x="80" y="60" fill="#0f172a" font-size="26" font-weight="900" text-anchor="middle">50</text>
        <text x="230" y="45" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Max Speed 50 km/h</text>
        <text x="230" y="65" fill="#94a3b8" font-size="11" text-anchor="middle">Unmarked Urban Roads</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'speed_limit_40') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <circle cx="80" cy="50" r="32" fill="#ffffff" stroke="#ef4444" stroke-width="7"/>
        <text x="80" y="60" fill="#0f172a" font-size="26" font-weight="900" text-anchor="middle">40</text>
        <text x="230" y="45" fill="#f59e0b" font-size="13" font-weight="800" text-anchor="middle">Max Speed 40 km/h</text>
        <text x="230" y="65" fill="#94a3b8" font-size="11" text-anchor="middle">Slow Lanes & Narrow Roads</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'railroad_crossing') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <line x1="30" y1="70" x2="130" y2="70" stroke="#94a3b8" stroke-width="6"/>
        <line x1="50" y1="55" x2="50" y2="85" stroke="#e2e8f0" stroke-width="4"/>
        <line x1="80" y1="55" x2="80" y2="85" stroke="#e2e8f0" stroke-width="4"/>
        <line x1="110" y1="55" x2="110" y2="85" stroke="#e2e8f0" stroke-width="4"/>
        <rect x="140" y="30" width="30" height="30" fill="#ef4444" rx="4"/>
        <text x="155" y="50" fill="#ffffff" font-size="10" font-weight="900" text-anchor="middle">SOS</text>
        <text x="250" y="40" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Railroad Crossing</text>
        <text x="250" y="60" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Max 15 km/h / Press SOS Button</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'braking_physics') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <text x="40" y="35" fill="#38bdf8" font-size="11" font-weight="800">1x Speed (40km/h) → 1x Distance</text>
        <rect x="40" y="42" width="40" height="8" rx="2" fill="#38bdf8"/>
        <text x="40" y="70" fill="#ef4444" font-size="11" font-weight="800">2x Speed (80km/h) → 4x Distance (Quadrupled!)</text>
        <rect x="40" y="77" width="160" height="8" rx="2" fill="#ef4444"/>
      </svg>
    </div>`;
  } else if (diagramKey === 'siren_yield') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="30" width="70" height="40" rx="6" fill="#dc2626"/>
        <path d="M 40 30 Q 65 10 90 30" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="3"/>
        <text x="65" y="55" fill="#ffffff" font-size="12" font-weight="900" text-anchor="middle">AMBULANCE</text>
        <text x="230" y="45" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Must Yield to Emergency Siren</text>
        <text x="230" y="65" fill="#f87171" font-size="11" font-weight="700" text-anchor="middle">Violation = License Revocation!</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'traffic_light') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="20" width="100" height="60" rx="10" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        <circle cx="50" cy="50" r="12" fill="#ef4444"/>
        <circle cx="80" cy="50" r="12" fill="#f59e0b"/>
        <circle cx="110" cy="50" r="12" fill="#10b981"/>
        <text x="240" y="40" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Solid Red: Stop Behind Line</text>
        <text x="240" y="60" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">Red Light Fine + 3 Demerit Points</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'demerit_points') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <circle cx="70" cy="50" r="28" fill="#7e22ce" stroke="#c084fc" stroke-width="3"/>
        <text x="70" y="58" fill="#ffffff" font-size="20" font-weight="900" text-anchor="middle">12pt</text>
        <text x="230" y="45" fill="#c084fc" font-size="13" font-weight="800" text-anchor="middle">12 Demerit Points in 1 Year</text>
        <text x="230" y="65" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">= 2-Month Driver License Suspension</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'cpr_protocol') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="30" width="90" height="40" rx="8" fill="#0284c7"/>
        <text x="75" y="55" fill="#ffffff" font-size="14" font-weight="900" text-anchor="middle">30 : 2</text>
        <text x="230" y="40" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">CPR Protocol (30 Compressions : 2 Breaths)</text>
        <text x="230" y="60" fill="#94a3b8" font-size="11" text-anchor="middle">Depth: 5-6 cm | Rate: 100-120/min</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'cargo_rear') {
    const extText = isCar ? "Max 30 cm Past Bumper" : "Max 50 cm Past Rear Axle";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="40" y="45" width="130" height="25" rx="4" fill="#3b82f6"/>
        <circle cx="65" cy="73" r="10" fill="#64748b"/>
        <circle cx="145" cy="73" r="10" fill="#64748b"/>
        <rect x="170" y="40" width="30" height="30" fill="#f59e0b" rx="3"/>
        <line x1="145" y1="80" x2="200" y2="80" stroke="#ef4444" stroke-width="2" stroke-dasharray="3"/>
        <text x="260" y="45" fill="#f59e0b" font-size="12" font-weight="800" text-anchor="middle">Cargo Extension Limit</text>
        <text x="260" y="65" fill="#ef4444" font-size="11" font-weight="700" text-anchor="middle">${extText}</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'right_of_way') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <line x1="30" y1="50" x2="150" y2="50" stroke="#10b981" stroke-width="4"/>
        <polygon points="150,45 160,50 150,55" fill="#10b981"/>
        <text x="240" y="45" fill="#10b981" font-size="12" font-weight="800" text-anchor="middle">Intersection Right-of-Way</text>
        <text x="240" y="65" fill="#38bdf8" font-size="11" font-weight="700" text-anchor="middle">Straight-Going Vehicle (Priority #1)</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'alcohol_limit') {
    const fineText = isCar ? "Fine: NT$30k–120k" : "Fine: NT$15k–90k";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="40" width="120" height="20" rx="4" fill="#334155"/>
        <rect x="30" y="40" width="40" height="20" rx="4" fill="#10b981"/>
        <line x1="70" y1="25" x2="70" y2="75" stroke="#ef4444" stroke-width="3"/>
        <text x="70" y="20" fill="#ef4444" font-size="10" font-weight="800" text-anchor="middle">BAC 0.15 mg/L</text>
        <text x="230" y="45" fill="#ef4444" font-size="12" font-weight="800" text-anchor="middle">Legal BAC Limit: 0.15 mg/L</text>
        <text x="230" y="65" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">${fineText} / Refusal: NT$180k</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'tire_tread') {
    const depthText = isCar ? "Min Tread: 1.6 mm (Car)" : "Min Tread: 1.0 mm (Moto)";
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="30" width="100" height="40" fill="#334155" rx="6"/>
        <line x1="60" y1="30" x2="60" y2="70" stroke="#f59e0b" stroke-width="4"/>
        <line x1="90" y1="30" x2="90" y2="70" stroke="#f59e0b" stroke-width="4"/>
        <text x="230" y="45" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Tire Inspection Standard</text>
        <text x="230" y="65" fill="#f59e0b" font-size="11" font-weight="700" text-anchor="middle">${depthText}</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'freeway_distance') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="40" width="45" height="20" rx="3" fill="#3b82f6"/>
        <rect x="120" y="40" width="45" height="20" rx="3" fill="#3b82f6"/>
        <line x1="75" y1="50" x2="120" y2="50" stroke="#10b981" stroke-width="2" stroke-dasharray="3"/>
        <text x="250" y="45" fill="#10b981" font-size="12" font-weight="800" text-anchor="middle">Safe Distance = Speed ÷ 2</text>
        <text x="250" y="65" fill="#38bdf8" font-size="11" text-anchor="middle">50m @ 100km/h (Double in rain)</text>
      </svg>
    </div>`;
  } else if (diagramKey === 'child_seat') {
    return `<div class="rule-diagram-box">
      <svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;">
        <rect x="30" y="25" width="100" height="50" rx="8" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
        <circle cx="80" cy="50" r="14" fill="#f59e0b"/>
        <text x="240" y="45" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Child Safety Seat Law</text>
        <text x="240" y="65" fill="#94a3b8" font-size="11" text-anchor="middle">Under 4 yrs / 18kg → Mandatory Rear Seat</text>
      </svg>
    </div>`;
  }
  return `<div class="rule-diagram-box"><svg viewBox="0 0 340 100" style="background:#0f172a; border-radius:8px; width:100%;"><circle cx="170" cy="50" r="30" fill="#ffffff" stroke="#ef4444" stroke-width="5"/><text x="170" y="60" fill="#0f172a" font-size="24" font-weight="900" text-anchor="middle">50</text></svg></div>`;
}

// RENDER MASTER RULES (MODE 0)
function renderMasterRules() {
  const container = document.getElementById('masterRulesContainer');
  if (!container) return;
  container.innerHTML = '';

  masterRulesData.forEach(rule => {
    const card = document.createElement('div');
    card.className = 'cheat-card';

    const diagramHTML = getDiagramHTML(rule.diagram, currentModule);

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
