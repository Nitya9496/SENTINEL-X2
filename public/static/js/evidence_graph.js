/**
 * SENTINEL-X — Supervisory Evidence Graph Engine (Hero Feature)
 * Renders the reconstructed operational lifecycle:
 * Asset -> Telemetry -> Alert -> Ack -> Investigation -> Evidence -> Decision -> Escalation -> Remediation -> Closure
 * Highlights broken links, missing evidence, bypassed SOPs, and premature closures.
 */

window.EvidenceGraph = {
  currentCaseId: 'CASE-GRAPH-07-01',
  graphData: null,
  selectedNodeId: null,

  async init(caseId = 'CASE-GRAPH-07-01') {
    this.currentCaseId = caseId;
    await this.loadCase(caseId);
  },

  async loadCase(caseId) {
    this.currentCaseId = caseId;
    try {
      const resp = await fetch(`/api/evidence-graph/${caseId}`);
      if (!resp.ok) throw new Error('Failed to load graph data');
      this.graphData = await resp.json();
    } catch (e) {
      console.warn('Network fetch error, trying local fallback', e);
      if (window.MockData && window.MockData.graphs) {
        this.graphData = window.MockData.graphs[caseId] || window.MockData.graphs['CASE-GRAPH-07-01'];
      }
    }

    this.render();
    this.updateCaseSwitcherUI();
  },

  render() {
    const container = document.getElementById('graph-track-nodes') || document.getElementById('graph-track');
    const summaryEl = document.getElementById('graph-scenario-summary') || document.getElementById('graph-summary-text');
    if (!container || !this.graphData) return;

    if (summaryEl) {
      summaryEl.innerHTML = `
        <span style="color: var(--accent-theme-light); font-weight: 800; text-transform: uppercase;">${this.graphData.scenario_type || 'Reconstructed Lifecycle'}:</span>
        <span style="margin-left: 6px; color: var(--text-secondary);">${this.graphData.summary || ''}</span>
      `;
    }

    container.innerHTML = '';
    const nodes = this.graphData.nodes || [];
    const totalNodes = nodes.length;

    // Pick default selected node: first missing/bypassed node or first node
    const defaultNode = nodes.find(n => n.status === 'missing') || nodes.find(n => n.status === 'bypassed') || nodes[0];
    if (!this.selectedNodeId || !nodes.find(n => n.id === this.selectedNodeId)) {
      this.selectedNodeId = defaultNode ? defaultNode.id : null;
    }

    nodes.forEach((node, index) => {
      const nodeEl = document.createElement('div');
      const isSelected = this.selectedNodeId === node.id;
      nodeEl.className = `node-element node-${node.status} ${isSelected ? 'selected' : ''}`;
      nodeEl.id = `ui-${node.id}`;
      nodeEl.onclick = () => this.selectNode(node.id);

      let iconClass = 'verified';
      let iconSymbol = '✓';
      if (node.status === 'missing') {
        iconClass = 'missing';
        iconSymbol = '✕';
      } else if (node.status === 'bypassed') {
        iconClass = 'bypassed';
        iconSymbol = '⊘';
      }

      nodeEl.innerHTML = `
        <div style="display: flex; align-items: center; justify-content: space-between;">
          <span style="font-size: 10px; text-transform: uppercase; color: var(--text-muted); font-weight: 700; letter-spacing: 0.5px;">${node.stage}</span>
          <div class="node-icon-circle ${iconClass}">${iconSymbol}</div>
        </div>
        <div style="font-weight: 700; font-size: 13.5px; color: #FFFFFF; line-height: 1.3;" title="${node.label}">${node.label}</div>
        <div style="font-size: 11px; color: var(--text-secondary); margin-top: 2px;">${node.subtitle || ''}</div>
        <div style="font-size: 10.5px; font-family: var(--font-mono); color: var(--text-muted); margin-top: 4px;">${node.timestamp || ''}</div>
      `;

      container.appendChild(nodeEl);

      // Add connector between nodes
      if (index < totalNodes - 1) {
        const nextNode = nodes[index + 1];
        const isBroken = node.status === 'missing' || nextNode.status === 'missing' || nextNode.status === 'bypassed';

        const connector = document.createElement('div');
        connector.className = 'track-connector-arrow';
        connector.innerHTML = `
          <div class="track-line ${isBroken ? 'broken' : 'verified'}"></div>
        `;
        container.appendChild(connector);
      }
    });

    this.renderInspector();
  },

  selectNode(nodeId) {
    this.selectedNodeId = nodeId;
    document.querySelectorAll('.node-element').forEach(el => el.classList.remove('selected'));
    const targetEl = document.getElementById(`ui-${nodeId}`);
    if (targetEl) targetEl.classList.add('selected');
    this.renderInspector();
  },

  renderInspector() {
    const drawerContent = document.getElementById('inspector-drawer-content') || document.getElementById('node-inspector-content');
    if (!drawerContent || !this.graphData) return;

    const node = (this.graphData.nodes || []).find(n => n.id === this.selectedNodeId);
    if (!node) {
      drawerContent.innerHTML = `<p style="color: var(--text-muted); font-size: 13px;">Click any lifecycle node in the graph to inspect technical details and database foreign keys.</p>`;
      return;
    }

    let statusBadge = `<span class="badge badge-low">VERIFIED / RECORDED</span>`;
    if (node.status === 'missing') {
      statusBadge = `<span class="badge badge-high" style="background: rgba(239, 68, 68, 0.2); color: #EF4444; border: 1px solid rgba(239, 68, 68, 0.4);">MISSING / BROKEN WORKFLOW</span>`;
    } else if (node.status === 'bypassed') {
      statusBadge = `<span class="badge badge-medium" style="background: rgba(245, 158, 11, 0.2); color: #F59E0B; border: 1px solid rgba(245, 158, 11, 0.4);">BYPASSED / SKIPPED</span>`;
    }

    let detailsRows = '';
    if (node.details) {
      for (const [key, value] of Object.entries(node.details)) {
        detailsRows += `
          <tr style="border-bottom: 1px solid var(--border-subtle);">
            <td style="padding: 7px 0; font-size: 11.5px; font-weight: 700; color: var(--text-muted); text-transform: uppercase;">${key}</td>
            <td style="padding: 7px 0; font-size: 12.5px; color: #FFFFFF; font-family: var(--font-mono); text-align: right;">${value}</td>
          </tr>
        `;
      }
    }

    let flagSection = '';
    if (node.flag_reason) {
      flagSection = `
        <div style="background: rgba(239, 68, 68, 0.1); border-left: 3px solid var(--status-critical); padding: 12px 14px; border-radius: var(--radius-xs); margin: 10px 0;">
          <div style="font-size: 11px; font-weight: 800; text-transform: uppercase; color: var(--status-critical); letter-spacing: 0.5px;">
            ⚠️ SUPERVISORY GAP DETECTED
          </div>
          <div style="font-size: 12.5px; color: #F1F5F9; margin-top: 4px; line-height: 1.4;">
            ${node.flag_reason}
          </div>
        </div>
      `;
    }

    drawerContent.innerHTML = `
      <div style="display: flex; flex-direction: column; gap: 8px;">
        <div style="font-size: 11px; text-transform: uppercase; color: var(--text-muted); font-weight: 700;">WORKFLOW STAGE: ${node.stage}</div>
        <h3 style="font-size: 16px; font-weight: 800; color: #FFFFFF; line-height: 1.2;">${node.label}</h3>
        <div>${statusBadge}</div>
      </div>

      ${flagSection}

      <div style="margin-top: 10px;">
        <div style="font-size: 11px; text-transform: uppercase; color: var(--accent-theme-light); font-weight: 700; margin-bottom: 6px;">EVIDENTIARY ATTRIBUTES</div>
        <table style="width: 100%; border-collapse: collapse;">
          <tbody>${detailsRows}</tbody>
        </table>
      </div>

      <div style="margin-top: 18px;">
        <button class="btn btn-secondary btn-sm" style="width: 100%; justify-content: center;" onclick="window.App.navigateToScreen('evidence-explorer', { alert_id: '${this.graphData.alert_id || ''}', cse_id: '${this.graphData.cse_id || ''}' })">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
          Inspect Raw Database Record
        </button>
      </div>
    `;
  },

  updateCaseSwitcherUI() {
    document.querySelectorAll('.case-btn, .case-toggle-btn').forEach(btn => {
      const targetCase = btn.getAttribute('data-case');
      if (targetCase === this.currentCaseId) {
        btn.classList.add('active');
      } else {
        btn.classList.remove('active');
      }
    });
  }
};
