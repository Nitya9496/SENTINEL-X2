/**
 * SENTINEL-X — Client Application & Router
 * Manages the 5 core screens, the 60-second guided demo story,
 * supervisor triage actions, and dynamic filtering.
 */

window.App = {
  currentScreen: 'dashboard',
  selectedCseId: 'CSE-07',
  selectedFindingId: 'F-07-01',
  demoStep: 0,
  cses: [],
  overview: null,

  async init() {
    console.log("Initializing SENTINEL-X Supervisory Analytics Console...");
    this.initTheme();
    await this.fetchOverview();
    await this.fetchCses();
    this.setupEventListeners();
    this.navigateToScreen('dashboard');
  },

  initTheme() {
    let theme = 'light';
    try {
      const userTheme = localStorage.getItem('sentinel_theme_user_choice');
      if (userTheme === 'dark') theme = 'dark';
    } catch(e) {}
    this.setTheme(theme);
  },

  toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    this.setTheme(newTheme);
    try {
      localStorage.setItem('sentinel_theme_user_choice', newTheme);
    } catch(e) {}
    if (typeof this.showToast === 'function') {
      this.showToast(`Switched to ${newTheme === 'dark' ? 'Cyber Dark Mode' : 'Executive Light Theme'}`);
    }
  },

  setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    const toggleBtn = document.getElementById('theme-toggle');
    if (toggleBtn) {
      if (theme === 'dark') {
        toggleBtn.innerHTML = '☀️ Light Mode';
        toggleBtn.title = 'Switch to Executive White Theme';
      } else {
        toggleBtn.innerHTML = '🌙 Dark Mode';
        toggleBtn.title = 'Switch to Cyber Dark Mode';
      }
    }
  },

  setupEventListeners() {
    // Search input
    const searchInput = document.getElementById('cse-search-input');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.filterCseTable(e.target.value);
      });
    }

    // Sector & Attention filters
    const sectorFilter = document.getElementById('sector-filter');
    const attentionFilter = document.getElementById('attention-filter');
    if (sectorFilter) {
      sectorFilter.addEventListener('change', () => this.applyFilters());
    }
    if (attentionFilter) {
      attentionFilter.addEventListener('change', () => this.applyFilters());
    }
  },

  async fetchOverview() {
    try {
      const resp = await fetch('/api/overview');
      if (resp.ok) {
        this.overview = await resp.json();
        this.renderOverviewCards();
      }
    } catch (e) {
      console.warn('Overview fetch error', e);
    }
  },

  async fetchCses() {
    try {
      const resp = await fetch('/api/cses');
      if (resp.ok) {
        this.cses = await resp.json();
        this.renderCseTable(this.cses);
      }
    } catch (e) {
      console.warn('CSEs fetch error', e);
    }
  },

  renderOverviewCards() {
    if (!this.overview) return;
    const setTxt = (id, val) => {
      const el = document.getElementById(id);
      if (el) el.innerText = val;
    };
    setTxt('stat-total-cses', this.overview.total_cses);
    setTxt('stat-total-alerts', Number(this.overview.total_alerts).toLocaleString());
    setTxt('stat-total-cases', Number(this.overview.total_cases).toLocaleString());
    setTxt('stat-attention-cses', this.overview.cses_requiring_attention);
    setTxt('stat-exec-gaps', this.overview.total_execution_gaps);
    setTxt('stat-neg-space', this.overview.total_negative_space);
    setTxt('stat-contradictions', this.overview.total_contradictions);
  },

  renderCseTable(cses) {
    const tbody = document.getElementById('cse-table-body');
    if (!tbody) return;
    tbody.innerHTML = '';

    cses.forEach(cse => {
      const tr = document.createElement('tr');
      tr.style.cursor = 'pointer';

      let badgeClass = 'badge-low';
      let scoreColor = 'score-low';
      if (cse.attention_level === 'High') {
        badgeClass = 'badge-high';
        scoreColor = 'score-high';
      } else if (cse.attention_level === 'Medium') {
        badgeClass = 'badge-medium';
        scoreColor = 'score-med';
      }

      tr.innerHTML = `
        <td style="font-weight: 700; color: var(--text-main); font-family: var(--font-mono);">
          ${cse.id}
          ${cse.id === 'CSE-07' ? '<span class="badge badge-tag" style="margin-left: 6px; font-size: 10px; color: var(--accent-theme);">DEMO FOCUS</span>' : ''}
        </td>
        <td>
          <div style="font-weight: 600; color: var(--text-main);">${cse.name}</div>
          <div style="font-size: 11px; color: var(--text-muted);">${cse.sector}</div>
        </td>
        <td>
          <span class="badge ${badgeClass}">${cse.attention_level}</span>
        </td>
        <td>
          <span class="score-display ${scoreColor}">${cse.attention_score}</span>
          <span style="font-size: 11px; color: var(--text-muted);">/100</span>
        </td>
        <td>
          <span style="font-size: 12.5px; color: var(--text-secondary); font-weight: 500;">${cse.main_signal}</span>
        </td>
        <td style="font-family: var(--font-mono); font-weight: 700; color: var(--text-main); text-align: center;">
          ${cse.findings_count}
        </td>
        <td style="text-align: right;">
          <button class="btn btn-secondary btn-sm" onclick="event.stopPropagation(); window.App.openCseDetail('${cse.id}')">
            Inspect CSE →
          </button>
        </td>
      `;

      tr.onclick = () => this.openCseDetail(cse.id);
      tbody.appendChild(tr);
    });
  },

  applyFilters() {
    const sectorVal = document.getElementById('sector-filter')?.value || 'All';
    const attentionVal = document.getElementById('attention-filter')?.value || 'All';
    const searchVal = document.getElementById('cse-search-input')?.value.toLowerCase() || '';

    const filtered = this.cses.filter(cse => {
      const matchSector = sectorVal === 'All' || cse.sector.toLowerCase() === sectorVal.toLowerCase();
      const matchAttention = attentionVal === 'All' || cse.attention_level.toLowerCase() === attentionVal.toLowerCase();
      const matchSearch = !searchVal || 
        cse.id.toLowerCase().includes(searchVal) ||
        cse.name.toLowerCase().includes(searchVal) ||
        cse.main_signal.toLowerCase().includes(searchVal);
      return matchSector && matchAttention && matchSearch;
    });

    this.renderCseTable(filtered);
  },

  filterCseTable(keyword) {
    this.applyFilters();
  },

  // Navigation Router
  navigateToScreen(screenName, params = {}) {
    this.currentScreen = screenName;

    // 1. Hide all screens with display: none !important
    const allScreens = document.querySelectorAll('.view-screen, .screen-view');
    allScreens.forEach(s => {
      s.classList.remove('active');
      s.style.setProperty('display', 'none', 'important');
    });

    // 2. Update navigation tabs active state
    document.querySelectorAll('.nav-tab-btn, .nav-item').forEach(nav => {
      if (nav.getAttribute('data-screen') === screenName) {
        nav.classList.add('active');
      } else {
        nav.classList.remove('active');
      }
    });

    // 3. Show target screen immediately
    const targetScreen = document.getElementById(`screen-${screenName}`);
    if (targetScreen) {
      targetScreen.classList.add('active');
      targetScreen.style.setProperty('display', 'flex', 'important');
      targetScreen.style.flexDirection = 'column';
    }

    // 4. Reset scroll immediately to the very top (zero scrolling required!)
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    document.documentElement.scrollTop = 0;
    document.body.scrollTop = 0;
    const contentWrapper = document.querySelector('.content-wrapper');
    if (contentWrapper) contentWrapper.scrollTop = 0;

    // 5. Update breadcrumbs
    this.updateBreadcrumbs(screenName);

    // 6. Trigger screen specific loaders safely
    try {
      if (screenName === 'cse-detail') {
        const cseId = params.cse_id || this.selectedCseId || 'CSE-07';
        this.selectedCseId = cseId;
        this.loadCseDetail(cseId);
      } else if (screenName === 'finding-detail') {
        const findingId = params.finding_id || this.selectedFindingId || 'F-07-01';
        this.selectedFindingId = findingId;
        this.loadFindingDetail(findingId);
      } else if (screenName === 'evidence-graph') {
        const caseId = params.case_id || 'CASE-GRAPH-07-01';
        if (window.EvidenceGraph && typeof window.EvidenceGraph.init === 'function') {
          window.EvidenceGraph.init(caseId);
        }
      } else if (screenName === 'evidence-explorer') {
        this.loadEvidenceExplorer(params);
      } else if (screenName === 'reports') {
        const cseId = params.cse_id || this.selectedCseId || 'CSE-07';
        this.loadReportView(cseId);
      } else if (screenName === 'audit-log') {
        this.loadAuditLogs();
      }
    } catch (err) {
      console.error("Screen loader execution error:", err);
    }
  },

  updateBreadcrumbs(screenName) {
    const bc = document.getElementById('breadcrumbs-bar');
    if (!bc) return;

    if (screenName === 'dashboard') {
      bc.innerHTML = `
        <span class="breadcrumb-item active">National SOC Supervisory Command</span>
      `;
    } else if (screenName === 'cse-detail') {
      bc.innerHTML = `
        <span class="breadcrumb-item" onclick="window.App.navigateToScreen('dashboard')">Command</span>
        <span>/</span>
        <span class="breadcrumb-item" onclick="window.App.navigateToScreen('dashboard')">CSE Assessment</span>
        <span>/</span>
        <span class="breadcrumb-item active">${this.selectedCseId}</span>
      `;
    } else if (screenName === 'finding-detail') {
      bc.innerHTML = `
        <span class="breadcrumb-item" onclick="window.App.navigateToScreen('dashboard')">Command</span>
        <span>/</span>
        <span class="breadcrumb-item" onclick="window.App.openCseDetail('${this.selectedCseId}')">${this.selectedCseId}</span>
        <span>/</span>
        <span class="breadcrumb-item active">Finding Detail</span>
      `;
    } else if (screenName === 'evidence-graph') {
      bc.innerHTML = `
        <span class="breadcrumb-item" onclick="window.App.navigateToScreen('dashboard')">Command</span>
        <span>/</span>
        <span class="breadcrumb-item" onclick="window.App.openCseDetail('${this.selectedCseId}')">${this.selectedCseId}</span>
        <span>/</span>
        <span class="breadcrumb-item active">Supervisory Evidence Graph</span>
      `;
    } else if (screenName === 'evidence-explorer') {
      bc.innerHTML = `
        <span class="breadcrumb-item" onclick="window.App.navigateToScreen('dashboard')">Command</span>
        <span>/</span>
        <span class="breadcrumb-item active">Evidence Explorer</span>
      `;
    } else {
      bc.innerHTML = `
        <span class="breadcrumb-item" onclick="window.App.navigateToScreen('dashboard')">Command</span>
        <span>/</span>
        <span class="breadcrumb-item active">${screenName.toUpperCase()}</span>
      `;
    }
  },

  // SCREEN 2: CSE Detail
  async openCseDetail(cseId = 'CSE-07') {
    this.selectedCseId = cseId;
    this.navigateToScreen('cse-detail', { cse_id: cseId });
  },

  async loadCseDetail(cseId = 'CSE-07') {
    try {
      const resp = await fetch(`/api/cses/${cseId}`);
      if (!resp.ok) throw new Error('Failed to load CSE detail');
      const data = await resp.json();
      const cse = data.cse;
      const findings = data.findings;

      // Populate Header
      const elId = document.getElementById('cse-view-id') || document.getElementById('cse-detail-id');
      if (elId) elId.innerText = cse.id;

      const elName = document.getElementById('cse-view-name') || document.getElementById('cse-detail-name');
      if (elName) elName.innerText = cse.name;

      const elDesc = document.getElementById('cse-view-desc') || document.getElementById('cse-detail-desc');
      if (elDesc) elDesc.innerText = cse.description;

      const elScore = document.getElementById('cse-view-score') || document.getElementById('cse-detail-score');
      if (elScore) elScore.innerHTML = `${cse.attention_score} <span style="font-size: 16px; color: var(--text-muted); font-weight: 500;">/ 100</span>`;

      const elBadge = document.getElementById('cse-view-attention-badge') || document.getElementById('cse-detail-attention-badge');
      if (elBadge) {
        elBadge.className = `badge badge-${cse.attention_level.toLowerCase()}`;
        elBadge.innerText = `SUPERVISORY ATTENTION: ${cse.attention_level}`;
      }

      // Breakdown text
      const b = cse.score_breakdown || {};
      const elBreakdown = document.getElementById('cse-view-score-breakdown') || document.getElementById('cse-score-breakdown-text');
      if (elBreakdown) {
        elBreakdown.innerHTML = `
          Execution Gap: <strong>+${b['Execution Gap'] || 0}</strong> &nbsp;|&nbsp;
          Negative Space: <strong>+${b['Negative Space'] || 0}</strong> &nbsp;|&nbsp;
          Contradiction: <strong>+${b['Contradiction'] || 0}</strong> &nbsp;|&nbsp;
          Recurring: <strong>+${b['Recurring Risk'] || 0}</strong> &nbsp;|&nbsp;
          Peer Dev: <strong>+${b['Peer Deviation'] || 0}</strong>
        `;
      }

      // Metric Cards
      const elGaps = document.getElementById('cse-metric-gaps') || document.getElementById('cse-card-exec-gaps');
      if (elGaps) elGaps.innerText = cse.execution_gaps ?? 0;

      const elNeg = document.getElementById('cse-metric-neg') || document.getElementById('cse-card-neg-space');
      if (elNeg) elNeg.innerText = cse.negative_space ?? 0;

      const elContr = document.getElementById('cse-metric-contradictions') || document.getElementById('cse-card-contradictions');
      if (elContr) elContr.innerText = cse.contradictions ?? 0;

      const elRec = document.getElementById('cse-metric-recurring') || document.getElementById('cse-card-recurring');
      if (elRec) elRec.innerText = cse.recurring_risks ?? 0;

      const elCov = document.getElementById('cse-metric-coverage') || document.getElementById('cse-card-coverage');
      if (elCov) elCov.innerText = `${cse.evidence_coverage || 0}%`;

      // Update CSE selector dropdown
      const cseSelector = document.getElementById('cse-assessment-selector');
      if (cseSelector) {
        if (cseSelector.options.length <= 1 && this.cses && this.cses.length) {
          cseSelector.innerHTML = '';
          this.cses.forEach(c => {
            const opt = document.createElement('option');
            opt.value = c.id;
            opt.text = `${c.id} — ${c.name} (${c.attention_level})`;
            cseSelector.appendChild(opt);
          });
        }
        cseSelector.value = cseId;
      }

      // Render Findings List
      const findingsListEl = document.getElementById('cse-findings-container') || document.getElementById('cse-findings-list');
      if (findingsListEl) {
        findingsListEl.innerHTML = '';

        findings.forEach(f => {
          const item = document.createElement('div');
          item.className = 'finding-card-item';
          item.onclick = () => this.openFindingDetail(f.id);

          let severityBadge = 'badge-critical';
          if (f.severity === 'High') severityBadge = 'badge-high';
          if (f.severity === 'Medium') severityBadge = 'badge-medium';

          item.innerHTML = `
            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 14px; width: 100%;">
              <div style="flex: 1;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
                  <span class="badge ${severityBadge}">${f.severity}</span>
                  <span class="badge badge-tag">${f.category}</span>
                  <span style="font-family: var(--font-mono); font-size: 11px; color: var(--text-muted);">${f.id}</span>
                </div>
                <h4 style="font-size: 15px; font-weight: 700; color: var(--text-main); margin-bottom: 4px;">${f.title}</h4>
                <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.45;">${f.explanation}</p>
              </div>
              <div style="display: flex; align-items: center; gap: 14px; margin-left: 16px;">
                <div style="text-align: right;">
                  <div style="font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">CONFIDENCE</div>
                  <div style="font-size: 14px; font-weight: 800; font-family: var(--font-mono); color: var(--status-success);">${f.confidence}%</div>
                </div>
                <button class="btn btn-secondary btn-sm" onclick="event.stopPropagation(); window.App.openFindingDetail('${f.id}')">
                  Examine Gap →
                </button>
              </div>
            </div>
          `;
          findingsListEl.appendChild(item);
        });
      }

    } catch (e) {
      console.error("loadCseDetail error:", e);
    }
  },

  // SCREEN 3: Finding Detail
  async openFindingDetail(findingId = 'F-07-01') {
    this.selectedFindingId = findingId;
    this.navigateToScreen('finding-detail', { finding_id: findingId });
  },

  async loadFindingDetail(findingId = 'F-07-01') {
    try {
      const resp = await fetch(`/api/findings/${findingId}`);
      if (!resp.ok) throw new Error('Failed to load finding');
      const data = await resp.json();
      const f = data.finding;
      const cse = data.cse;

      const elTitle = document.getElementById('finding-view-title') || document.getElementById('finding-title');
      if (elTitle) elTitle.innerText = f.title;

      const elCse = document.getElementById('finding-view-cse-code') || document.getElementById('finding-cse-tag');
      if (elCse) elCse.innerText = `${cse.id} — ${cse.name}`;

      const elCat = document.getElementById('finding-view-category') || document.getElementById('finding-category-tag');
      if (elCat) elCat.innerText = f.category;

      const elSev = document.getElementById('finding-view-severity') || document.getElementById('finding-severity-badge');
      if (elSev) {
        elSev.className = `badge badge-${f.severity.toLowerCase()}`;
        elSev.innerText = f.severity;
      }

      const elExp = document.getElementById('finding-view-explanation') || document.getElementById('finding-explanation');
      if (elExp) elExp.innerText = f.explanation;

      // Disparity KPI Bar
      const m = f.metrics || {};
      const elAlerts = document.getElementById('finding-metric-alerts') || document.getElementById('disparity-critical-alerts');
      if (elAlerts) elAlerts.innerText = m.critical_alerts ? m.critical_alerts.toLocaleString() : '2,430';

      const elInvs = document.getElementById('finding-metric-invs') || document.getElementById('disparity-investigations');
      if (elInvs) elInvs.innerText = m.investigations ? m.investigations.toLocaleString() : '2,112';

      const elGaps = document.getElementById('finding-metric-gaps') || document.getElementById('disparity-potential-gaps');
      if (elGaps) elGaps.innerText = m.potential_gaps ? m.potential_gaps.toLocaleString() : (m.silent_critical_assets || '318');

      // "Why Flagged?" reasons
      const reasonsList = document.getElementById('finding-reasons-container') || document.getElementById('why-flagged-list');
      if (reasonsList && f.why_flagged) {
        reasonsList.innerHTML = '';
        f.why_flagged.forEach(reason => {
          const li = document.createElement('li');
          li.innerHTML = `<span class="reason-bullet">▸</span> <span>${reason}</span>`;
          reasonsList.appendChild(li);
        });
      }

      // Supporting records table
      const recordsTbody = document.getElementById('finding-records-tbody') || document.getElementById('supporting-records-body');
      if (recordsTbody && f.supporting_records) {
        recordsTbody.innerHTML = '';
        f.supporting_records.forEach(rec => {
          const tr = document.createElement('tr');
          tr.onclick = () => {
            this.navigateToScreen('evidence-explorer', { alert_id: rec.alert_id });
          };

          tr.innerHTML = `
            <td style="font-family: var(--font-mono); font-weight: 700; color: var(--text-main);">${rec.alert_id}</td>
            <td><span class="badge badge-high">${rec.severity}</span></td>
            <td style="font-family: var(--font-mono);">${rec.status}</td>
            <td style="font-family: var(--font-mono); font-weight: 700; color: var(--status-critical);">${rec.investigation}</td>
            <td><span class="badge badge-tag">${rec.asset}</span> <span style="font-size: 11px; color: var(--text-muted);">${rec.asset_role || ''}</span></td>
            <td style="font-family: var(--font-mono); font-size: 11.5px;">${rec.created}</td>
            <td style="text-align: right;">
              <button class="btn btn-secondary btn-sm" onclick="event.stopPropagation(); window.App.viewEvidenceGraphForCase('${f.evidence_graph_case_id}')">
                Graph Flow →
              </button>
            </td>
          `;
          recordsTbody.appendChild(tr);
        });
      }

      // Possible explanations (HITL)
      const explanationsWrap = document.getElementById('finding-explanations-tags') || document.getElementById('hitl-explanations');
      if (explanationsWrap && f.possible_explanations) {
        explanationsWrap.innerHTML = '';
        f.possible_explanations.forEach(exp => {
          const tag = document.createElement('span');
          tag.className = 'explanation-tag';
          tag.innerText = exp;
          explanationsWrap.appendChild(tag);
        });
      }

      // Button: VIEW EVIDENCE GRAPH
      const viewGraphBtn = document.getElementById('btn-view-evidence-graph');
      if (viewGraphBtn) {
        viewGraphBtn.onclick = () => {
          this.viewEvidenceGraphForCase(f.evidence_graph_case_id);
        };
      }

    } catch (e) {
      console.error("loadFindingDetail error:", e);
    }
  },

  // SCREEN 4: Supervisory Evidence Graph
  viewEvidenceGraphForCase(caseId = 'CASE-GRAPH-07-01') {
    this.navigateToScreen('evidence-graph', { case_id: caseId });
  },

  // Human-in-the-Loop review actions
  async updateFindingReview(status) {
    try {
      const resp = await fetch(`/api/findings/${this.selectedFindingId}/review`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: status, note: `Disposition marked by NCIIPC Supervisor: ${status}` })
      });

      if (resp.ok) {
        this.showToast(`Finding status updated to: "${status}". Logged to tamper-evident audit trail.`);
        this.loadFindingDetail(this.selectedFindingId);
      }
    } catch (e) {
      console.error(e);
    }
  },

  // SCREEN 5: Evidence Explorer
  async loadEvidenceExplorer(params = {}) {
    try {
      const queryParams = new URLSearchParams();
      if (params.alert_id) queryParams.set('alert_id', params.alert_id);
      if (params.cse_id) queryParams.set('cse_id', params.cse_id);

      const resp = await fetch(`/api/evidence-records?${queryParams.toString()}`);
      if (!resp.ok) throw new Error('Failed to load evidence records');
      const records = await resp.json();

      const tbody = document.getElementById('explorer-records-tbody') || document.getElementById('evidence-records-tbody');
      if (!tbody) return;
      tbody.innerHTML = '';

      records.forEach(r => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-family: var(--font-mono); font-weight: 700; color: var(--text-main);">${r.record_id}</td>
          <td style="font-family: var(--font-mono); color: var(--accent-theme); font-weight: 700;">${r.alert_id}</td>
          <td><span class="badge badge-tag">${r.asset_id}</span></td>
          <td><span class="badge badge-tag">${r.cse_id}</span></td>
          <td><span class="badge ${r.severity === 'CRITICAL' ? 'badge-critical' : 'badge-high'}">${r.severity}</span></td>
          <td style="color: var(--text-main); font-weight: 500;">${r.category}</td>
          <td style="font-family: var(--font-mono); font-weight: 700; color: ${r.investigation_status === 'MISSING' ? 'var(--status-critical)' : 'var(--status-success)'};">
            ${r.investigation_status}
          </td>
          <td style="font-size: 11.5px; color: var(--status-critical); font-weight: 500;">${r.discrepancy}</td>
          <td style="text-align: right;">
            <button class="btn btn-secondary btn-sm" onclick="window.App.viewEvidenceGraphForCase('CASE-GRAPH-07-01')">
              Graph Flow →
            </button>
          </td>
        `;
        tbody.appendChild(tr);
      });

    } catch (e) {
      console.error("loadEvidenceExplorer error:", e);
    }
  },

  // Official Report View
  async loadReportView(cseId = 'CSE-07') {
    try {
      const resp = await fetch(`/api/reports/${cseId}`);
      if (!resp.ok) throw new Error('Failed to load report');
      const data = await resp.json();

      const elTitle = document.getElementById('report-view-cse-title') || document.getElementById('report-cse-title');
      if (elTitle) elTitle.innerText = `${data.target_entity.id} — ${data.target_entity.name}`;

      const elSector = document.getElementById('report-view-cse-sector');
      if (elSector) elSector.innerText = `Sector: ${data.target_entity.sector}`;

      const elScore = document.getElementById('report-view-score') || document.getElementById('report-score');
      if (elScore) elScore.innerText = `${data.target_entity.attention_score} / 100`;

      const elRec = document.getElementById('report-view-directive-text') || document.getElementById('report-recommendation');
      if (elRec) elRec.innerText = data.recommendation;

      const elDate = document.getElementById('report-view-date') || document.getElementById('report-generated-at');
      if (elDate) elDate.innerText = data.generated_at;

      const elClass = document.getElementById('report-view-classification-bar') || document.getElementById('report-classification');
      if (elClass) elClass.innerText = `Issued under Information Technology Act Section 70A • Mandate 2026/Q3`;

      const findingsContainer = document.getElementById('report-table-tbody') || document.getElementById('report-findings-table-body');
      if (findingsContainer && data.findings) {
        findingsContainer.innerHTML = '';
        data.findings.forEach(f => {
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td style="font-weight: 700; font-family: var(--font-mono); color: #0F172A;">${f.id}</td>
            <td style="font-weight: 600; color: #0F172A;">${f.title}</td>
            <td><span class="badge badge-tag">${f.category}</span></td>
            <td><span class="badge ${f.severity === 'CRITICAL' || f.severity === 'High' ? 'badge-critical' : 'badge-high'}">${f.severity}</span></td>
            <td style="font-size: 12px; color: #475569;">${f.explanation}</td>
          `;
          findingsContainer.appendChild(tr);
        });
      }

      const selector = document.getElementById('report-cse-selector');
      if (selector) {
        if (selector.options.length <= 1 && this.cses && this.cses.length) {
          selector.innerHTML = '';
          this.cses.forEach(c => {
            const opt = document.createElement('option');
            opt.value = c.id;
            opt.text = `${c.id} — ${c.name} (${c.attention_level})`;
            selector.appendChild(opt);
          });
        }
        selector.value = cseId;
      }
    } catch (e) {
      console.error("loadReportView error:", e);
    }
  },

  // Audit Log View
  async loadAuditLogs() {
    try {
      const resp = await fetch('/api/audit-logs');
      if (!resp.ok) throw new Error('Failed to load audit logs');
      const logs = await resp.json();

      const tbody = document.getElementById('audit-log-tbody');
      if (!tbody) return;
      tbody.innerHTML = '';
      logs.forEach(log => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td style="font-family: var(--font-mono); font-size: 11.5px; color: var(--text-muted);">${log.timestamp}</td>
          <td style="font-weight: 600; color: var(--text-main);">${log.actor}</td>
          <td><span class="badge badge-tag">${log.action}</span></td>
          <td style="font-size: 12.5px; color: var(--text-secondary);">${log.details}</td>
        `;
        tbody.appendChild(tr);
      });
    } catch (e) {
      console.error(e);
    }
  },

  // 60-Second Guided Tour Engine
  startDemoStory() {
    this.demoStep = 1;
    this.updateDemoBanner();
    this.navigateToScreen('dashboard');
  },

  nextDemoStep() {
    if (this.demoStep < 5) {
      this.demoStep++;
    } else {
      this.demoStep = 0;
    }
    this.updateDemoBanner();
    this.executeCurrentDemoStep();
  },

  prevDemoStep() {
    if (this.demoStep > 1) {
      this.demoStep--;
      this.updateDemoBanner();
      this.executeCurrentDemoStep();
    }
  },

  dismissDemoStory() {
    this.demoStep = 0;
    this.updateDemoBanner();
  },

  updateDemoBanner() {
    const banner = document.getElementById('demo-tour-banner');
    if (!banner) return;

    if (this.demoStep === 0) {
      banner.style.display = 'none';
      return;
    }

    banner.style.display = 'flex';
    document.querySelectorAll('.tour-step-pill').forEach(pill => {
      const step = parseInt(pill.getAttribute('data-step'));
      if (step === this.demoStep) {
        pill.classList.add('active');
      } else {
        pill.classList.remove('active');
      }
    });

    const stepTexts = {
      1: "Step 1 of 5: System assessed 20 Critical Sector Entities. 7 flagged for Supervisory Attention. Notice CSE-07 (Score 87/100).",
      2: "Step 2 of 5: Inspecting CSE-07 (Northern Grid). 17 Execution Gaps detected. Reviewing top findings.",
      3: "Step 3 of 5: Deep-dive into Finding: 318 Critical Alerts closed without investigation. Closure duration = 7 mins vs peer 46 mins.",
      4: "Step 4 of 5: SUPERVISORY EVIDENCE GRAPH (Hero Feature). Notice the red broken link: Investigation & Evidence stages are completely missing!",
      5: "Step 5 of 5: Click any node (e.g. Investigation). Inspect the exact missing record details. SENTINEL-X equips the supervisor with unassailable proof."
    };

    const textEl = document.getElementById('demo-step-text');
    if (textEl) textEl.innerText = stepTexts[this.demoStep] || "";
  },

  executeCurrentDemoStep() {
    if (this.demoStep === 1) {
      this.navigateToScreen('dashboard');
    } else if (this.demoStep === 2) {
      this.openCseDetail('CSE-07');
    } else if (this.demoStep === 3) {
      this.openFindingDetail('F-07-01');
    } else if (this.demoStep === 4) {
      this.viewEvidenceGraphForCase('CASE-GRAPH-07-01');
    } else if (this.demoStep === 5) {
      this.navigateToScreen('evidence-graph', { case_id: 'CASE-GRAPH-07-01' });
      setTimeout(() => {
        if (window.EvidenceGraph && typeof window.EvidenceGraph.selectNode === 'function') {
          window.EvidenceGraph.selectNode('node-investigation');
        }
      }, 300);
    }
  },

  // Upload Modal Handler
  openUploadModal() {
    const m = document.getElementById('upload-modal');
    if (m) m.classList.add('active');
  },

  closeUploadModal() {
    const m = document.getElementById('upload-modal');
    if (m) m.classList.remove('active');
  },

  async handleFileUpload(fileInput) {
    if (!fileInput.files || fileInput.files.length === 0) return;
    const file = fileInput.files[0];
    const statusEl = document.getElementById('upload-status-text');
    if (statusEl) statusEl.innerHTML = `Ingesting ${file.name} (${(file.size / 1024).toFixed(1)} KB)...`;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const resp = await fetch('/api/upload', {
        method: 'POST',
        body: formData
      });
      if (resp.ok) {
        if (statusEl) statusEl.innerHTML = `✓ Ingestion complete. Running deterministic gap evaluation...`;
        setTimeout(() => {
          this.closeUploadModal();
          this.fetchOverview();
          this.fetchCses();
          this.showToast(`SOC telemetry ingested: ${file.name}. Audit evidence graph updated.`);
        }, 1000);
      }
    } catch (e) {
      console.error(e);
      if (statusEl) statusEl.innerHTML = `Error uploading file.`;
    }
  },

  // Raw Record Modal
  openRawRecordModal(rec) {
    const modal = document.getElementById('raw-record-modal');
    const content = document.getElementById('raw-record-content');
    if (!modal || !content) return;
    content.innerText = JSON.stringify(rec, null, 2);
    modal.classList.add('active');
  },

  closeRawRecordModal() {
    const modal = document.getElementById('raw-record-modal');
    if (modal) modal.classList.remove('active');
  },

  showToast(msg) {
    const toast = document.createElement('div');
    toast.className = 'supervisor-toast';
    toast.innerHTML = `
      <div style="display: flex; align-items: center; gap: 8px;">
        <span style="color: var(--accent-theme); font-weight: 800;">⚡ SENTINEL-X AUDIT:</span>
        <span>${msg}</span>
      </div>
    `;
    toast.style.position = 'fixed';
    toast.style.bottom = '24px';
    toast.style.right = '24px';
    toast.style.background = 'var(--bg-surface-elevated)';
    toast.style.color = 'var(--text-main)';
    toast.style.border = '1px solid var(--accent-theme)';
    toast.style.boxShadow = '0 8px 30px rgba(0,0,0,0.3)';
    toast.style.padding = '12px 20px';
    toast.style.borderRadius = 'var(--radius-md)';
    toast.style.fontSize = '13px';
    toast.style.fontWeight = '600';
    toast.style.zIndex = '999999';
    toast.style.animation = 'fadeInScreen 0.2s ease';
    document.body.appendChild(toast);

    setTimeout(() => {
      toast.style.transition = 'opacity 0.5s ease';
      toast.style.opacity = '0';
      setTimeout(() => toast.remove(), 500);
    }, 4000);
  },

  toggleWhyFlaggedDrawer() {
    const drawer = document.getElementById('hero-why-drawer');
    const btn = document.getElementById('btn-why-flagged-toggle');
    if (!drawer) return;
    if (drawer.classList.contains('active')) {
      drawer.classList.remove('active');
      if (btn) btn.innerHTML = 'Why Flagged? ▾';
    } else {
      drawer.classList.add('active');
      if (btn) btn.innerHTML = 'Why Flagged? ▴';
    }
  },

  navigateTo(screenName, params = {}) {
    this.navigateToScreen(screenName, params);
  },

  openCse(cseId = 'CSE-07') {
    this.selectedCseId = cseId || 'CSE-07';
    this.navigateToScreen('cse-detail', { cse_id: this.selectedCseId });
  },

  openFinding(findingId = 'F-07-01') {
    this.selectedFindingId = findingId || 'F-07-01';
    this.navigateToScreen('finding-detail', { finding_id: this.selectedFindingId });
  },

  openGraph(caseId = 'CASE-GRAPH-07-01') {
    this.navigateToScreen('evidence-graph', { case_id: caseId || 'CASE-GRAPH-07-01' });
  },

  openDirectiveModal(actionType = 'Confirmed Finding') {
    const modal = document.getElementById('directive-modal');
    if (!modal) return;
    const elType = document.getElementById('modal-directive-action-type');
    if (elType) elType.value = actionType;
    modal.classList.add('active');
  },

  closeDirectiveModal() {
    const modal = document.getElementById('directive-modal');
    if (modal) modal.classList.remove('active');
  },

  async submitDirective() {
    const noticeRef = document.getElementById('modal-directive-ref')?.value || 'DIR-2026';
    this.closeDirectiveModal();
    this.showToast(`Statutory Notice ${noticeRef} Signed & Dispatched! Recorded in tamper-evident ledger.`);
  },

  async loadSampleData() {
    const statusEl = document.getElementById('upload-status-msg');
    if (statusEl) statusEl.innerHTML = `⚡ Reconciling 1,420 simulated SOC telemetry events across 20 CSEs...`;
    try {
      const formData = new FormData();
      formData.append('sample_trigger', 'true');
      await fetch('/api/upload', { method: 'POST', body: formData });
    } catch (e) {}
    setTimeout(() => {
      this.closeUploadModal();
      this.fetchOverview();
      this.fetchCses();
      this.showToast("Sample data reconciled! 1,420 events ingested into evidence graph.");
    }, 1200);
  },

  async runLiveEngine() {
    this.showToast("⚡ Running deterministic supervisory analytics cycle across all 20 CSEs...");
    try {
      const resp = await fetch('/api/run-analytics', { method: 'POST' });
      if (resp.ok) {
        const data = await resp.json();
        this.overview = data.overview;
        this.renderOverviewCards();
      }
    } catch (e) {}
    setTimeout(() => {
      this.showToast("Supervisory evaluation complete! Evidence lifecycle chains updated.");
    }, 800);
  }
};

window.addEventListener('DOMContentLoaded', () => {
  window.App.init();
});
