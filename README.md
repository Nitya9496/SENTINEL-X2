# SENTINEL-X
### Supervisory Analytics Tool for SOC Assessment (SAT-SA)
> **Deterministic Operational Integrity & Forensic Workflow Reconstruction for National Critical Sector Entities**  
> *Developed for Regulatory Oversight under Information Technology Act, Section 70A | NCIIPC Cyber Command*

---

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Backend](https://img.shields.io/badge/Framework-FastAPI-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Architecture](https://img.shields.io/badge/Architecture-Air--Gapped%20%2F%20Zero--Cloud-critical?style=for-the-badge&logo=shield)](https://nciipc.gov.in/)
[![SIH Compliance](https://img.shields.io/badge/SIH-Evaluation--Ready-success.svg?style=for-the-badge&logo=github)](https://sih.gov.in/)
[![UI Console](https://img.shields.io/badge/UI-Executive%20Pure%20White%20SPA-informational?style=for-the-badge)](http://localhost:8080)

---

## 📌 1. The SIH Problem Statement & National Impact

### The Core Problem
In national cybersecurity governance, regulatory authorities such as **NCIIPC** do not operate internal Security Operations Centers (SOCs) for every Critical Sector Entity (CSE). Instead, they oversee and audit the **operational integrity** of independent SOCs across power grids, banking switches, defense backbones, nuclear facilities, and telecommunications.

Traditional SIEM/SOAR platforms (Splunk, Microsoft Sentinel, IBM QRadar) look **outward** to catch external adversaries.  
**SENTINEL-X solves the regulatory blind spot by looking INWARD at the SOC itself:**
* **Rubber-Stamped Closures:** Critical alerts marked "Resolved" in under 7 minutes without opening an investigation case or executing a forensic query.
* **Negative Space (Silent Assets):** Tier-1 critical assets declared "Active & Monitored" in CMDB registries that report zero telemetry for days.
* **Contradictory Remediation:** Alerts marked "Remediated" recurring on identical hosts hours later due to unverified ticket closures.
* **Metric-Outcome Divergence:** Executive dashboards showing 99% SLA compliance while true incident triage is bypassed.

```
       ========================================================================
                         THE "318" QUANTITATIVE PROOF STORY
       ========================================================================
       2,430 Critical SCADA Alerts Generated (NRLDC // CSE-07)
         └── 2,112 Legitimate Investigation Tickets Opened
               └──  318 UNINVESTIGATED CLOSURES (POTENTIAL EXECUTION GAPS)
       ========================================================================
```

---

## 💡 2. Proposed Solution & Architecture

SENTINEL-X is an **air-gapped, zero-cloud-dependent supervisory intelligence platform** that reconciles disparate SOC log streams (Alert Logs, Case Management, CMDB Assets, Telemetry Feeds) using **deterministic graph reconstruction**. It provides regulatory supervisors with unassailable, mathematically verifiable proof of operational failures.

### Reconstructed Operational Lifecycle
Every incident is mapped against the mandatory 10-stage regulatory lifecycle to detect bypassed stages:

```mermaid
flowchart LR
    A["Asset Active"] --> B["Telemetry Ingestion"]
    B --> C["Alert Fired"]
    C --> D["Analyst Ack"]
    D -.->|BYPASSED STAGE| E["❌ Investigation Ticket"]
    E -.->|MISSING EVIDENCE| F["❌ Forensic Capture"]
    F --> G["Decision / Triage"]
    G --> H["Remediation"]
    H --> I["Verified Closure"]

    classDef ok fill:#D1FAE5,stroke:#059669,stroke-width:2px,color:#065F46;
    classDef gap fill:#FEE2E2,stroke:#DC2626,stroke-width:2px,color:#991B1B,stroke-dasharray: 5 5;
    class A,B,C,D,G,H,I ok;
    class E,F gap;
```

---

## 🖥️ 3. The 5 Core Prototype Screens

| Screen | View Name | High-Value Supervisory Function |
|---|---|---|
| **Screen 1** | **Command Overview** | Real-time queue of 20 Critical Sector Entities ranked by additive Attention Scores, KPI metrics, and the 318 story container. |
| **Screen 2** | **CSE Assessment** | Deep dive into specific entities (e.g. NRLDC), transparent vector breakdowns, and prioritized gap lists. |
| **Screen 3** | **Findings & Gaps** | Multi-source disparity breakdown, "Why Flagged?" deterministic justification, and Human-in-the-Loop disposition triage. |
| **Screen 4** | **Supervisory Evidence Graph** | **Hero Feature:** Interactive lifecycle flow demonstrating exact broken links, missing foreign keys, and bypassed SOPs. |
| **Screen 5** | **Evidence Explorer** | Granular source record provenance verifying that every finding is linked to raw database telemetry. |
| **Screen 6** | **Directive Briefing Report** | Formal statutory notice generation under IT Act Section 70A ready for 1-click PDF dispatch. |

---

## 🔬 4. Deterministic Analytics Engine (Zero Hallucination)

Unlike generative AI wrappers that hallucinate risk ratings, SENTINEL-X computes deterministic metrics backed by strict regulatory logic:

1. **Rule 1: Execution Gap (Uninvestigated Closure)**
   $$\text{Gap} \iff (\text{Severity} = \text{'CRITICAL'}) \land (\text{Status} = \text{'CLOSED'}) \land (\text{Investigation\_ID} = \text{NULL})$$

2. **Rule 2: Negative Space (Monitoring Blind Spot)**
   $$\text{BlindSpot} \iff (\text{CMDB.Criticality} \ge \text{Tier-1}) \land (\text{CMDB.Monitored} = \text{True}) \land (\sum \text{Telemetry}_{72\text{h}} = 0)$$

3. **Rule 3: Cross-Source Contradiction**
   $$\text{Contradiction} \iff (\text{Case.Status} = \text{'Remediated'}) \land (\Delta t_{\text{re-alert}} \le 24\text{h}) \land (\text{Asset} = \text{Identical})$$

4. **Rule 4: Velocity Anomaly**
   $$\text{AnomalousClosure} \iff \text{ClosureTime} < 0.20 \times \text{PeerMedianClosureTime}$$
   *(NRLDC SCADA Closure: 7.08 mins vs National Peer Baseline: 46.0 mins)*

---

## 🛠️ 5. Technical Architecture & Tech Stack

```
SENTINEL-X System Architecture
├── Presentation Tier (Air-Gapped Vanilla SPA)
│   ├── Executive Pure White Theme (Light Mode Default) & Cyber Dark Mode
│   ├── Native Dynamic SVG Lifecycle Flow Engine
│   └── Zero External CDN Dependencies (100% Offline Self-Contained)
├── Supervisory Analytics Server (Python 3.10+ / FastAPI)
│   ├── Deterministic Rules Engine (SupervisoryAnalyticsEngine)
│   ├── Synthetic High-Fidelity SOC Generator (20 CSEs, SCADA/OT/IT logs)
│   └── Tamper-Evident Audit Ledger
└── Storage & Data Interchange
    ├── In-Memory High-Performance Vector Store
    └── Standardized JSON / CSV Telemetry Ingestion Schemas
```

### Categorized Stack
* **Backend:** Python 3.10+, FastAPI, Uvicorn, Pydantic v2
* **Frontend:** Modern Semantic HTML5, CSS3 Custom Properties (Design Tokens), Vanilla ES6+ SPA Router
* **Visualization:** Custom SVG Evidence Graph Engine (Zero bloated charting libraries)
* **Security & Compliance:** Air-gapped deployment, local assets only, tamper-evident audit logging

---

## 📂 6. Repository Structure

```
d:\SENTINEL-X\
├── backend/
│   ├── analytics_engine.py    # Deterministic rule evaluation logic
│   ├── data_generator.py      # High-fidelity multi-entity SOC simulation
│   ├── main.py                # FastAPI REST endpoints & static server
│   └── models.py              # Pydantic data schemas & telemetry models
├── sample_data/
│   ├── cse_07_alert_export.csv    # Offline SOC alert log sample
│   └── cse_07_telemetry_dump.json # Raw OT/SCADA sensor telemetry
├── static/
│   ├── css/
│   │   └── styles.css         # Executive White & Cyber Dark design system
│   ├── img/
│   │   └── sentinel-logo.svg  # Vector Shield Brand Identity
│   ├── js/
│   │   ├── app.js             # SPA Client Router & Supervisor Controls
│   │   └── evidence_graph.js  # Interactive Lifecycle Flow Renderer
│   └── index.html             # Single-Page Application Console
├── .env.example               # Safe environment configuration template
├── .gitignore                 # Production-grade git exclusion rules
├── README.md                  # Comprehensive project documentation
├── requirements.txt           # Minimal, reproducible dependencies
├── run.py                     # Python server launcher
└── start.bat                  # 1-Click Windows execution script
```

---

## 🚀 7. Step-by-Step "Plug & Play" Setup

### Prerequisites
* **Python 3.10 or higher** installed on the host system.
* Modern web browser (Chrome, Edge, Firefox).
* No internet connection required after dependency installation (Air-Gapped).

### Installation & Run

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-org/sentinel-x.git
   cd sentinel-x
   ```

2. **Set Up Python Virtual Environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux / macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Supervisory Console:**
   ```bash
   # Windows (1-Click)
   start.bat

   # Or via Python Launcher
   python run.py
   ```

5. **Access the Console:**
   Open your browser to:
   👉 **`http://localhost:8080/`** (or `http://localhost:8000/`)

---

## 🔮 8. Future Enhancements

* **STIX/TAXII 2.1 Native Gateway:** Standardized ingestion of national threat feeds.
* **Hardware Security Module (HSM) Signing:** Cryptographic digital signatures on all Section 70A regulatory directives.
* **Distributed Peer Federated Baselines:** Privacy-preserving cross-entity benchmark modeling without exposing raw tenant logs.
* **Live Kafka / Syslog Air-Gapped Tap:** Real-time ingestion engine for SCADA historian streaming.

---

## 👥 9. Contributors & Team Details

| Role | Name | Responsibilities |
|---|---|---|
| **Team Lead & System Architect** | *[Insert Name]* | Core architecture, Deterministic rules engine, SIH Coordination |
| **Backend & Analytics Engineer** | *[Insert Name]* | FastAPI REST server, SOC data normalization, Graph algorithms |
| **Frontend & UI/UX Specialist** | *[Insert Name]* | Executive SPA console, SVG evidence graph, Design tokens |
| **Cybersecurity & Compliance Lead** | *[Insert Name]* | Regulatory framework alignment, SOP validation, Audit trail |

---

*Developed for the Smart India Hackathon (SIH) | National Critical Information Infrastructure Protection Centre (NCIIPC) Supervisory Oversight Framework.*

