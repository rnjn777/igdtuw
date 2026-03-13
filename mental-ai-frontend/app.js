// MindSentry Mock AI Engine & State Machine

// --- STATE ---
const state = {
    userName: "Student",
    sessionActive: false,
    messageCount: 0,
    history: [], // {role, content, emotion}
    burnoutScore: 20,
    stressPoints: 0
};

// --- DOM ELEMENTS ---
const els = {
    // Modals
    onboarding: document.getElementById('onboarding'),
    userNameInput: document.getElementById('user-name'),
    startBtn: document.getElementById('start-btn'),
    app: document.getElementById('app'),
    displayName: document.getElementById('display-name'),
    heroName: document.getElementById('hero-name'),

    // Chat
    chatBox: document.getElementById('chat-box'),
    heroSection: document.getElementById('hero-section'),
    chatInput: document.getElementById('chat-input'),
    sendBtn: document.getElementById('send-btn'),
    promptCards: document.querySelectorAll('.prompt-card'),
    orb: document.getElementById('main-orb'),
    crisisBanner: document.getElementById('crisis-banner'),
    closeCrisisBtn: document.getElementById('close-crisis'),

    // Insights
    emotionLabel: document.getElementById('insight-emotion'),
    emotionConf: document.getElementById('insight-conf'),
    emotionBar: document.getElementById('emotion-bar'),
    burnoutLabel: document.getElementById('insight-burnout'),
    burnoutTrend: document.getElementById('insight-burnout-trend'),
    stressLabel: document.getElementById('insight-stress'),
    stressTrend: document.getElementById('insight-stress-trend'),
    activityLabel: document.getElementById('insight-activity'),

    // Report
    genReportBtn: document.getElementById('generate-report-btn'),
    reportModal: document.getElementById('report-modal'),
    closeReportBtn: document.getElementById('close-report-btn'),
    copyReportBtn: document.getElementById('copy-report-btn'),
    reportContent: document.getElementById('report-content'),
    reportDate: document.getElementById('report-date')
};

// --- MOCK AI INTELLIGENCE ---

const keywords = {
    fear: ['anxious', 'scared', 'worry', 'worried', 'stress', 'panic', 'overwhelmed', 'exam', 'fail'],
    sadness: ['sad', 'tired', 'exhausted', 'burnout', 'depressed', 'cry', 'lonely', 'hopeless', 'down'],
    anger: ['angry', 'frustrated', 'mad', 'hate', 'annoyed', 'unfair', 'rage'],
    joy: ['happy', 'great', 'good', 'excited', 'proud', 'love', 'amazing', 'passed', 'joy']
};

const crisisKeywords = ['suicide', 'kill', 'end it', 'hopeless', 'give up', 'die'];

const responses = {
    fear: [
        "It sounds like you're carrying a lot of anxiety right now. Racing thoughts can feel overwhelming, especially with academic pressure. Try acknowledging the fear without fighting it. What is the specific scenario your mind keeps looping on?",
        "That overwhelmed feeling is your nervous system going into overdrive. It's completely valid. Let's try box breathing: inhale for 4, hold for 4, exhale for 4. Once you feel a bit grounded, what is one small thing you can control right now?"
    ],
    sadness: [
        "I hear you. Exhaustion and sadness often go hand-in-hand, and it sounds like you've been running on empty for a while. Your mind and body are asking for a pause. Have you been able to get any restful sleep lately?",
        "It takes courage to admit you're feeling this low. Burnout creeps up slowly. You don't have to fix everything today; sometimes just resting is the most productive thing you can do. Can you forgive yourself for taking a break tonight?"
    ],
    anger: [
        "I can feel the frustration in your words, and it makes complete sense that you're angry. Anger often means a boundary was crossed or something feels deeply unfair. Give yourself space to feel it. What triggered this specifically?",
        "It's okay to vent. Holding frustration in only makes it heavier. Before we try to solve anything, just take a deep breath to physically release some of that tension. Was it a specific person or situation that sparked this?"
    ],
    joy: [
        "That is wonderful to hear! Hold onto this feeling of energy and accomplishment. Recognizing positive moments builds resilience for the harder days. What specifically happened that made you feel this way?",
        "I love this energy! It's so important to celebrate the good days and the wins, no matter how small. Lean into this joy. Are you planning to celebrate or treat yourself today?"
    ],
    neutral: [
        "Thank you for checking in. Sometimes a quiet, neutral day is exactly what we need to recharge. How has your focus been today?",
        "I'm here with you. What's taking up the most space in your mind as you navigate through your day?"
    ]
};

const insightsMap = {
    fear: { color: 'var(--violet-glow)', barClass: 'bar-violet', conf: '88%', activity: "4-7-8 Breathing Technique to lower heart rate." },
    sadness: { color: '#475569', barClass: 'bar-gray', conf: '92%', activity: "Digital detox for 1 hour. Write 3 thoughts in a journal." },
    anger: { color: 'var(--red-glow)', barClass: 'bar-red', conf: '85%', activity: "Physical movement (brisk walk) to release cortisol." },
    joy: { color: 'var(--gold-glow)', barClass: 'bar-gold', conf: '95%', activity: "Reflect on this moment. Share your mood with a friend." },
    neutral: { color: 'var(--cyan-glow)', barClass: 'bar-cyan', conf: '80%', activity: "Maintain hydration and stick to your routine." }
};

// Chart.js Instance
let chartInstance = null;
const moodData = [5]; // Start neutral (1-10 scale)
const moodLabels = ['Start'];
const moodMapping = { 'sadness': 2, 'fear': 3, 'anger': 4, 'neutral': 5, 'joy': 8 };

// --- CORE FUNCTIONS ---

function initChart() {
    const ctx = document.getElementById('moodChart').getContext('2d');

    Chart.defaults.color = '#94A3B8';
    Chart.defaults.font.family = "'DM Sans', sans-serif";

    chartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: moodLabels,
            datasets: [{
                label: 'Mood Level',
                data: moodData,
                borderColor: '#00E5FF',
                backgroundColor: 'rgba(0, 229, 255, 0.1)',
                borderWidth: 2,
                pointBackgroundColor: '#C084FC',
                pointBorderColor: '#fff',
                pointRadius: 4,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { min: 0, max: 10, display: false },
                x: { grid: { color: 'rgba(255,255,255,0.05)' } }
            },
            plugins: {
                legend: { display: false },
                tooltip: { backgroundColor: 'rgba(0,0,0,0.8)', titleFont: { family: "'Sora'" } }
            }
        }
    });
}

// Global variable for large chart
let largeChartInstance = null;

function initLargeChart() {
    const ctx = document.getElementById('largeMoodChart').getContext('2d');

    if (largeChartInstance) {
        largeChartInstance.update();
        return;
    }

    largeChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: moodLabels, // Sharing the same array references!
            datasets: [{
                label: 'Mood Level',
                data: moodData,
                borderColor: '#00E5FF',
                backgroundColor: 'rgba(0, 229, 255, 0.1)',
                borderWidth: 3,
                pointBackgroundColor: '#C084FC',
                pointBorderColor: '#fff',
                pointRadius: 6,
                fill: true,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { min: 0, max: 10, display: false },
                x: { grid: { color: 'rgba(255,255,255,0.05)' } }
            },
            plugins: {
                legend: { display: false },
                tooltip: { backgroundColor: 'rgba(0,0,0,0.8)', titleFont: { family: "'Sora'" } }
            }
        }
    });
}

function updateChart(emotion) {
    const val = moodMapping[emotion] || 5;
    moodData.push(val);
    state.messageCount++;
    moodLabels.push(`Msg ${state.messageCount}`);

    if (moodData.length > 8) { moodData.shift(); moodLabels.shift(); }

    if (emotion === 'joy') chartInstance.data.datasets[0].borderColor = '#FBBF24';
    else if (emotion === 'fear') chartInstance.data.datasets[0].borderColor = '#C084FC';
    else if (emotion === 'anger') chartInstance.data.datasets[0].borderColor = '#FF4D4D';
    else chartInstance.data.datasets[0].borderColor = '#00E5FF';

    chartInstance.update();

    if (largeChartInstance) {
        if (emotion === 'joy') largeChartInstance.data.datasets[0].borderColor = '#FBBF24';
        else if (emotion === 'fear') largeChartInstance.data.datasets[0].borderColor = '#C084FC';
        else if (emotion === 'anger') largeChartInstance.data.datasets[0].borderColor = '#FF4D4D';
        else largeChartInstance.data.datasets[0].borderColor = '#00E5FF';
        largeChartInstance.update();
    }
}

function analyzeEmotion(text) {
    text = text.toLowerCase();

    // Crisis Check
    if (crisisKeywords.some(kw => text.includes(kw))) {
        els.crisisBanner.classList.remove('hidden');
    }

    for (const [emotion, words] of Object.entries(keywords)) {
        if (words.some(word => text.includes(word))) return emotion;
    }
    return 'neutral';
}

function updateInsights(emotion) {
    const data = insightsMap[emotion];

    // Update texts
    els.emotionLabel.textContent = emotion.charAt(0).toUpperCase() + emotion.slice(1);
    els.emotionLabel.style.color = data.color;
    els.emotionConf.textContent = data.conf;
    els.emotionConf.style.color = data.color;
    els.emotionConf.style.backgroundColor = `${data.color}22`; // Add transparency

    // Update bar
    els.emotionBar.className = `emotion-bar ${data.barClass}`;
    els.emotionBar.style.width = data.conf;

    // Update orb
    els.orb.className = `orb orb-${emotion === 'fear' ? 'anxious' : emotion === 'neutral' ? 'calm' : emotion} pulse-anim`;

    // Calculate Analytics
    if (['fear', 'sadness', 'anger'].includes(emotion)) {
        state.stressPoints += 2;
        state.burnoutScore = Math.min(100, state.burnoutScore + 10);
    } else if (emotion === 'joy') {
        state.stressPoints = Math.max(0, state.stressPoints - 2);
        state.burnoutScore = Math.max(0, state.burnoutScore - 5);
    }

    // Update UI Analytics
    els.burnoutLabel.textContent = state.burnoutScore > 60 ? 'High' : state.burnoutScore > 30 ? 'Moderate' : 'Low';

    if (state.stressPoints >= 4) {
        els.stressLabel.textContent = "Elevated";
        els.stressTrend.innerHTML = '<i class="ri-arrow-right-up-line"></i> Increasing';
        els.stressTrend.className = 'metric-trend trend-bad';
    } else if (state.stressPoints <= 1) {
        els.stressLabel.textContent = "Calm";
        els.stressTrend.innerHTML = '<i class="ri-arrow-right-down-line"></i> Decreasing';
        els.stressTrend.className = 'metric-trend trend-good';
    }

    els.activityLabel.textContent = data.activity;

    // Update Chart
    updateChart(emotion);
}

function appendMessage(role, text) {
    if (!state.sessionActive) {
        state.sessionActive = true;
        els.heroSection.classList.add('hidden');
    }

    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${role === 'user' ? 'msg-user' : 'msg-ai'}`;

    const avatar = role === 'user' ? '<i class="ri-user-smile-line"></i>' : '✦';

    let contentHtml = '';
    if (role === 'ai' && text === 'typing') {
        contentHtml = `<div class="typing-indicator"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>`;
        msgDiv.id = 'typing-indicator';
    } else {
        // Format paragraphs nicely
        contentHtml = `<div class="msg-content">${text.split('\n\n').map(p => `<p>${p}</p>`).join('')}</div>`;
    }

    msgDiv.innerHTML = `
        <div class="msg-avatar">${avatar}</div>
        ${contentHtml}
    `;

    els.chatBox.appendChild(msgDiv);
    els.chatBox.scrollTop = els.chatBox.scrollHeight;
}

async function handleInput(text) {
    if (!text.trim()) return;

    els.chatInput.value = '';

    // User message
    appendMessage('user', text);

    // Thinking delay
    appendMessage('ai', 'typing');

    try {
        const response = await fetch('http://localhost:5000/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                text: text,
                history: state.history
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Remove typing indicator
        const typingEl = document.getElementById('typing-indicator');
        if (typingEl) typingEl.remove();

        // 1. Update State History
        state.history.push({ role: 'user', content: text, emotion: data.emotion });
        state.history.push({ role: 'ai', content: data.response });

        // 2. Append Real ML Response
        appendMessage('ai', data.response);

        // 3. Update Visuals
        const emotion = data.emotion;
        updateChart(emotion);

        // Update UI Analytics with REAL DATA from backend
        // Use insights map for colors, but replace text/conf with real backend data
        const visualData = insightsMap[emotion] || insightsMap['neutral'];

        // Emotion Metric
        els.emotionLabel.textContent = emotion.charAt(0).toUpperCase() + emotion.slice(1);
        els.emotionLabel.style.color = visualData.color;
        els.emotionConf.textContent = data.confidence;
        els.emotionConf.style.color = visualData.color;
        els.emotionConf.style.backgroundColor = `${visualData.color}22`;

        // Emotion Bar
        els.emotionBar.className = `emotion-bar ${visualData.barClass}`;
        els.emotionBar.style.width = data.confidence;

        // Orb glow
        els.orb.className = `orb orb-${emotion === 'fear' ? 'anxious' : emotion === 'neutral' ? 'calm' : emotion} pulse-anim`;

        // Burnout & Stress (Calculated by insight_engine.py)
        els.burnoutLabel.textContent = data.insights.burnoutRisk;

        if (data.insights.stressTrend === "Elevated") {
            els.stressLabel.textContent = "Elevated";
            els.stressTrend.innerHTML = '<i class="ri-arrow-right-up-line"></i> Increasing';
            els.stressTrend.className = 'metric-trend trend-bad';
        } else {
            els.stressLabel.textContent = "Calm";
            els.stressTrend.innerHTML = '<i class="ri-arrow-right-down-line"></i> Decreasing';
            els.stressTrend.className = 'metric-trend trend-good';
        }

        // Activity
        els.activityLabel.textContent = data.insights.activity;

    } catch (error) {
        console.error("Failed to connect to ML backend:", error);
        const typingEl = document.getElementById('typing-indicator');
        if (typingEl) typingEl.remove();

        // Graceful fallback if backend is offline
        appendMessage('ai', "I'm having trouble connecting to my deeper neural networks right now (API Offline). Please make sure `api.py` is running on port 5000 in the `mental-ai` folder!");
    }
}

// --- EVENT LISTENERS ---

// Onboarding
els.userNameInput.addEventListener('input', (e) => {
    els.startBtn.disabled = e.target.value.trim().length === 0;
});

els.startBtn.addEventListener('click', () => {
    state.userName = els.userNameInput.value.trim();
    els.displayName.textContent = state.userName;
    els.heroName.textContent = state.userName;

    els.onboarding.classList.remove('active');
    setTimeout(() => {
        els.onboarding.classList.add('hidden');
        els.app.classList.remove('hidden');
        els.app.classList.add('fade-in');
        initChart();
    }, 500);
});

// Input
els.chatInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') handleInput(els.chatInput.value);
});
els.sendBtn.addEventListener('click', () => handleInput(els.chatInput.value));

// Prompt Cards
els.promptCards.forEach(card => {
    card.addEventListener('click', () => {
        handleInput(card.getAttribute('data-prompt'));
    });
});

// Crisis Banner
els.closeCrisisBtn.addEventListener('click', () => els.crisisBanner.classList.add('hidden'));

// Report Generation
els.genReportBtn.addEventListener('click', () => {
    const d = new Date();
    els.reportDate.textContent = d.toLocaleDateString() + ' at ' + d.toLocaleTimeString();

    const lastEmotion = state.history.length > 0 ? state.history[state.history.length - 2].emotion : 'Neutral';

    els.reportContent.innerHTML = `
        <ul>
            <li><span class="text-muted">Session Length:</span> <span>${state.messageCount} exchanges</span></li>
            <li><span class="text-muted">Primary State:</span> <span><strong class="text-cyan">${lastEmotion.toUpperCase()}</strong></span></li>
            <li><span class="text-muted">Burnout Risk:</span> <span>${state.burnoutScore}%</span></li>
            <li><span class="text-muted">Action Item:</span> <span>${els.activityLabel.textContent}</span></li>
        </ul>
        <p class="text-muted mt-md text-center" style="font-size:0.85rem">
           MindSentry AI Assistant logged this interaction safely and privately.
        </p>
    `;

    els.reportModal.classList.remove('hidden');
    setTimeout(() => els.reportModal.classList.add('active'), 10);
});

els.closeReportBtn.addEventListener('click', () => {
    els.reportModal.classList.remove('active');
    setTimeout(() => els.reportModal.classList.add('hidden'), 500);
});

els.copyReportBtn.addEventListener('click', () => {
    els.copyReportBtn.innerHTML = '<i class="ri-check-line"></i> Copied!';
    setTimeout(() => els.copyReportBtn.innerHTML = '<i class="ri-file-copy-line"></i> Copy to Clipboard', 2000);
});

// View Navigation Logic
document.querySelectorAll('.nav-item[data-view]').forEach(nav => {
    nav.addEventListener('click', (e) => {
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        e.currentTarget.classList.add('active');

        const viewId = e.currentTarget.getAttribute('data-view');

        // Hide all views
        document.querySelectorAll('.view-layer').forEach(v => v.classList.add('hidden'));

        // Show selected view
        document.getElementById(`view-${viewId}`).classList.remove('hidden');

        // Populate Data for Full Pages
        if (viewId === 'timeline') {
            document.getElementById('timeline-msgs').textContent = state.messageCount;
            document.getElementById('timeline-burnout').textContent = `${state.burnoutScore}%`;
            initLargeChart();
        } else if (viewId === 'report') {
            generateFullReport();
        }
    });
});

function generateFullReport() {
    const d = new Date();
    document.getElementById('page-report-date').textContent = d.toLocaleDateString() + ' at ' + d.toLocaleTimeString();

    const lastEmotion = state.history.length > 0 ? state.history[state.history.length - 2].emotion : 'Neutral';

    document.getElementById('page-report-content').innerHTML = `
        <ul>
            <li><span class="text-muted">Total Conversations:</span> <span>${state.messageCount} exchanges</span></li>
            <li><span class="text-muted">Current Primary State:</span> <span><strong class="text-cyan">${lastEmotion.toUpperCase()}</strong></span></li>
            <li><span class="text-muted">Calculated Burnout Risk:</span> <span>${state.burnoutScore}%</span></li>
            <li><span class="text-muted">Stress Trend:</span> <span>${els.stressLabel.textContent}</span></li>
            <li><span class="text-muted">Suggested Action Plan:</span> <span class="text-violet">${els.activityLabel.textContent}</span></li>
        </ul>
        <p class="text-muted mt-lg text-center" style="font-size:0.9rem; line-height: 1.6;">
           This report analyzes your interactions with MindSentry. 
           Your mental wellness journey is ongoing. Remember that taking breaks is productive, 
           and recognizing your emotions is the first step toward managing them.
        </p>
    `;
}

// Download Button for full report
document.getElementById('download-report-btn').addEventListener('click', (e) => {
    const btn = e.currentTarget;
    const oldHtml = btn.innerHTML;
    btn.innerHTML = '<i class="ri-loader-4-line pulse-anim"></i> Generating...';
    setTimeout(() => {
        btn.innerHTML = '<i class="ri-check-line"></i> Report Downloaded';
        setTimeout(() => btn.innerHTML = oldHtml, 3000);
    }, 1500);
});
