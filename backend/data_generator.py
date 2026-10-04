"""
SENTINEL-X — Synthetic SOC & Supervisory Data Generator
Generates realistic, deterministic SOC assessment data across 20 Critical Sector Entities (CSEs)
specifically tailored for NCIIPC supervisory oversight.
"""

from typing import Dict, List, Any
import random

def generate_cse_dataset() -> Dict[str, Any]:
    cses: List[Dict[str, Any]] = [
        {
            "id": "CSE-07",
            "name": "Northern Regional Load Despatch Centre (NRLDC)",
            "sector": "Power & Energy Grid",
            "criticality": "Critical",
            "attention_level": "High",
            "attention_score": 87,
            "main_signal": "Execution Gap & Negative Space",
            "findings_count": 17,
            "execution_gaps": 17,
            "negative_space": 9,
            "contradictions": 6,
            "recurring_risks": 8,
            "evidence_coverage": 71,
            "score_breakdown": {
                "Execution Gap": 25,
                "Negative Space": 20,
                "Contradiction": 18,
                "Recurring Risk": 14,
                "Peer Deviation": 10
            },
            "description": "Critical power grid management telemetry exhibits extensive critical alert closure without investigation, alongside RTU/SCADA assets reporting zero telemetry despite active monitoring flags.",
            "total_alerts": 14250,
            "total_cases": 1240,
            "total_assets": 320
        },
        {
            "id": "CSE-12",
            "name": "National Interbank Settlement & Clearing System",
            "sector": "Financial Services & Banking",
            "criticality": "Critical",
            "attention_level": "High",
            "attention_score": 82,
            "main_signal": "Negative Space",
            "findings_count": 9,
            "execution_gaps": 11,
            "negative_space": 9,
            "contradictions": 5,
            "recurring_risks": 6,
            "evidence_coverage": 68,
            "score_breakdown": {
                "Execution Gap": 18,
                "Negative Space": 24,
                "Contradiction": 16,
                "Recurring Risk": 12,
                "Peer Deviation": 12
            },
            "description": "Core SWIFT gateway and high-value payment switches flagged for severe negative space: monitoring marked active while ingress telemetry logs show 0 events over 72h window.",
            "total_alerts": 18420,
            "total_cases": 1580,
            "total_assets": 280
        },
        {
            "id": "CSE-02",
            "name": "State Transmission Utility Substation Operations",
            "sector": "Power & Energy Grid",
            "criticality": "Critical",
            "attention_level": "High",
            "attention_score": 78,
            "main_signal": "Fast Closure (Execution Gap)",
            "findings_count": 14,
            "execution_gaps": 15,
            "negative_space": 4,
            "contradictions": 7,
            "recurring_risks": 5,
            "evidence_coverage": 74,
            "score_breakdown": {
                "Execution Gap": 26,
                "Negative Space": 12,
                "Contradiction": 15,
                "Recurring Risk": 11,
                "Peer Deviation": 14
            },
            "description": "Abnormal triage velocity: 74% of critical OT alerts marked closed in under 4 minutes with null investigation tickets.",
            "total_alerts": 8940,
            "total_cases": 720,
            "total_assets": 190
        },
        {
            "id": "CSE-03",
            "name": "Strategic Defense Telecommunications Backbone",
            "sector": "Telecommunications & Defense",
            "criticality": "Critical",
            "attention_level": "Medium",
            "attention_score": 64,
            "main_signal": "Metric Divergence",
            "findings_count": 6,
            "execution_gaps": 6,
            "negative_space": 8,
            "contradictions": 3,
            "recurring_risks": 4,
            "evidence_coverage": 81,
            "score_breakdown": {
                "Execution Gap": 12,
                "Negative Space": 18,
                "Contradiction": 10,
                "Recurring Risk": 12,
                "Peer Deviation": 12
            },
            "description": "Discrepancy between optical core telemetry and SIEM ingestion rate; edge multiplexers have 0 syslog reception despite audit status marked Enabled.",
            "total_alerts": 6320,
            "total_cases": 610,
            "total_assets": 145
        },
        {
            "id": "CSE-06",
            "name": "Central Railway Signalling & Traffic Control",
            "sector": "Transportation & Rail",
            "criticality": "Critical",
            "attention_level": "Medium",
            "attention_score": 69,
            "main_signal": "Recurring Risk",
            "findings_count": 8,
            "execution_gaps": 8,
            "negative_space": 5,
            "contradictions": 8,
            "recurring_risks": 9,
            "evidence_coverage": 77,
            "score_breakdown": {
                "Execution Gap": 14,
                "Negative Space": 10,
                "Contradiction": 20,
                "Recurring Risk": 18,
                "Peer Deviation": 7
            },
            "description": "Electronic Interlocking sub-systems repeatedly alert on unauthorized configuration changes 12-48 hours after remediation status is logged as Completed.",
            "total_alerts": 7110,
            "total_cases": 580,
            "total_assets": 210
        },
        {
            "id": "CSE-05",
            "name": "Integrated Petrochemical Refinery Pipeline SCADA",
            "sector": "Petroleum & Natural Gas",
            "criticality": "Critical",
            "attention_level": "Medium",
            "attention_score": 62,
            "main_signal": "Metric Divergence",
            "findings_count": 7,
            "execution_gaps": 7,
            "negative_space": 6,
            "contradictions": 4,
            "recurring_risks": 7,
            "evidence_coverage": 79,
            "score_breakdown": {
                "Execution Gap": 10,
                "Negative Space": 12,
                "Contradiction": 14,
                "Recurring Risk": 16,
                "Peer Deviation": 10
            },
            "description": "Displays 99.4% Alert Ack SLA compliance, yet downstream case resolution rate is only 14%, resulting in severe unmitigated exposure.",
            "total_alerts": 9450,
            "total_cases": 780,
            "total_assets": 310
        },
        {
            "id": "CSE-04",
            "name": "Civil Aviation Air Traffic Management SOC",
            "sector": "Civil Aviation",
            "criticality": "Critical",
            "attention_level": "Medium",
            "attention_score": 58,
            "main_signal": "Investigation Repetition",
            "findings_count": 5,
            "execution_gaps": 5,
            "negative_space": 4,
            "contradictions": 3,
            "recurring_risks": 5,
            "evidence_coverage": 84,
            "score_breakdown": {
                "Execution Gap": 8,
                "Negative Space": 10,
                "Contradiction": 10,
                "Recurring Risk": 10,
                "Peer Deviation": 20
            },
            "description": "83% of radar data stream investigation records follow an identical boilerplate fingerprint: identical closing note, 180-second duration, zero triage artifacts.",
            "total_alerts": 5210,
            "total_cases": 490,
            "total_assets": 175
        },
        {
            "id": "CSE-01",
            "name": "Unified Payments Interface (UPI) Core Switch",
            "sector": "Financial Services & Banking",
            "criticality": "Critical",
            "attention_level": "Low",
            "attention_score": 14,
            "main_signal": "Baseline Normal",
            "findings_count": 1,
            "execution_gaps": 1,
            "negative_space": 0,
            "contradictions": 0,
            "recurring_risks": 1,
            "evidence_coverage": 97,
            "score_breakdown": {
                "Execution Gap": 4,
                "Negative Space": 2,
                "Contradiction": 2,
                "Recurring Risk": 3,
                "Peer Deviation": 3
            },
            "description": "Demonstrates robust operational integrity. Full evidence chains recorded across 97% of incident lifecycles with verified artifact attachments.",
            "total_alerts": 22100,
            "total_cases": 2180,
            "total_assets": 410
        },
        {
            "id": "CSE-08",
            "name": "Nuclear Power Generation Cyber Command",
            "sector": "Atomic Energy & Nuclear",
            "criticality": "Critical",
            "attention_level": "Low",
            "attention_score": 18,
            "main_signal": "Baseline Normal",
            "findings_count": 2,
            "execution_gaps": 2,
            "negative_space": 1,
            "contradictions": 0,
            "recurring_risks": 1,
            "evidence_coverage": 95,
            "score_breakdown": {
                "Execution Gap": 5,
                "Negative Space": 3,
                "Contradiction": 2,
                "Recurring Risk": 4,
                "Peer Deviation": 4
            },
            "description": "Strict air-gapped forensic logging and verified multi-analyst review protocols adhere to NCIIPC Category-A mandates.",
            "total_alerts": 3890,
            "total_cases": 410,
            "total_assets": 110
        },
        {
            "id": "CSE-09",
            "name": "National Satellite Telemetry & Tracking Ground Station",
            "sector": "Space & Defense",
            "criticality": "Critical",
            "attention_level": "Low",
            "attention_score": 22,
            "main_signal": "Baseline Normal",
            "findings_count": 2,
            "execution_gaps": 2,
            "negative_space": 1,
            "contradictions": 1,
            "recurring_risks": 2,
            "evidence_coverage": 93,
            "score_breakdown": {
                "Execution Gap": 6,
                "Negative Space": 4,
                "Contradiction": 3,
                "Recurring Risk": 5,
                "Peer Deviation": 4
            },
            "description": "Minor delay in Tier-3 escalation reporting, otherwise solid evidence chain traceability.",
            "total_alerts": 4410,
            "total_cases": 390,
            "total_assets": 95
        },
        {
            "id": "CSE-10",
            "name": "Major Seaport Container Terminal Operating System",
            "sector": "Maritime & Ports",
            "criticality": "Tier-1",
            "attention_level": "Medium",
            "attention_score": 52,
            "main_signal": "Recurring Risk",
            "findings_count": 6,
            "execution_gaps": 5,
            "negative_space": 4,
            "contradictions": 6,
            "recurring_risks": 7,
            "evidence_coverage": 80,
            "score_breakdown": {
                "Execution Gap": 11,
                "Negative Space": 9,
                "Contradiction": 14,
                "Recurring Risk": 12,
                "Peer Deviation": 6
            },
            "description": "Automated stacking crane gateway recurrently alerts on unauthorized protocol deviations.",
            "total_alerts": 5600,
            "total_cases": 470,
            "total_assets": 160
        },
        {
            "id": "CSE-11",
            "name": "State Health Record Exchange & Hospital Information Network",
            "sector": "Healthcare & Public Health",
            "criticality": "Tier-1",
            "attention_level": "Medium",
            "attention_score": 55,
            "main_signal": "Investigation Repetition",
            "findings_count": 5,
            "execution_gaps": 6,
            "negative_space": 5,
            "contradictions": 3,
            "recurring_risks": 5,
            "evidence_coverage": 78,
            "score_breakdown": {
                "Execution Gap": 12,
                "Negative Space": 10,
                "Contradiction": 9,
                "Recurring Risk": 11,
                "Peer Deviation": 13
            },
            "description": "Repeated fast-closure triage for ransomware precursor alerts without secondary IOC validation.",
            "total_alerts": 4820,
            "total_cases": 390,
            "total_assets": 210
        },
        {
            "id": "CSE-13",
            "name": "National Stock Exchange Core Trading Engine",
            "sector": "Financial Services & Banking",
            "criticality": "Critical",
            "attention_level": "Low",
            "attention_score": 19,
            "main_signal": "Baseline Normal",
            "findings_count": 2,
            "execution_gaps": 1,
            "negative_space": 1,
            "contradictions": 1,
            "recurring_risks": 1,
            "evidence_coverage": 96,
            "score_breakdown": {
                "Execution Gap": 4,
                "Negative Space": 3,
                "Contradiction": 3,
                "Recurring Risk": 4,
                "Peer Deviation": 5
            },
            "description": "Ultra low-latency matching engine maintains full forensic capture with automated case linking.",
            "total_alerts": 29800,
            "total_cases": 2840,
            "total_assets": 520
        },
        {
            "id": "CSE-14",
            "name": "Urban Metro Rail Automated Train Supervision (ATS)",
            "sector": "Transportation & Rail",
            "criticality": "Tier-1",
            "attention_level": "Medium",
            "attention_score": 48,
            "main_signal": "Negative Space",
            "findings_count": 4,
            "execution_gaps": 4,
            "negative_space": 7,
            "contradictions": 2,
            "recurring_risks": 3,
            "evidence_coverage": 83,
            "score_breakdown": {
                "Execution Gap": 9,
                "Negative Space": 16,
                "Contradiction": 6,
                "Recurring Risk": 8,
                "Peer Deviation": 9
            },
            "description": "Wayside track controller telemetry drops out during peak operation hours without triggering SOC health alarms.",
            "total_alerts": 3610,
            "total_cases": 310,
            "total_assets": 140
        },
        {
            "id": "CSE-15",
            "name": "National Emergency Response 112 Dispatch Network",
            "sector": "Public Safety & Emergency",
            "criticality": "Tier-1",
            "attention_level": "Low",
            "attention_score": 28,
            "main_signal": "Peer Deviation",
            "findings_count": 3,
            "execution_gaps": 3,
            "negative_space": 2,
            "contradictions": 1,
            "recurring_risks": 2,
            "evidence_coverage": 91,
            "score_breakdown": {
                "Execution Gap": 6,
                "Negative Space": 4,
                "Contradiction": 3,
                "Recurring Risk": 5,
                "Peer Deviation": 10
            },
            "description": "Slight variance in acknowledgement latency compared to regional peer dispatch centers.",
            "total_alerts": 4120,
            "total_cases": 360,
            "total_assets": 115
        },
        {
            "id": "CSE-16",
            "name": "National Identity Authentication Gateway",
            "sector": "Government & E-Governance",
            "criticality": "Critical",
            "attention_level": "Low",
            "attention_score": 21,
            "main_signal": "Baseline Normal",
            "findings_count": 2,
            "execution_gaps": 2,
            "negative_space": 1,
            "contradictions": 1,
            "recurring_risks": 2,
            "evidence_coverage": 94,
            "score_breakdown": {
                "Execution Gap": 5,
                "Negative Space": 3,
                "Contradiction": 3,
                "Recurring Risk": 4,
                "Peer Deviation": 6
            },
            "description": "Robust compliance with mandatory tamper-evident investigation audit logging.",
            "total_alerts": 17800,
            "total_cases": 1620,
            "total_assets": 390
        },
        {
            "id": "CSE-17",
            "name": "Strategic Oil Reserve Storage Control Hub",
            "sector": "Petroleum & Natural Gas",
            "criticality": "Critical",
            "attention_level": "High",
            "attention_score": 75,
            "main_signal": "Contradiction & Execution Gap",
            "findings_count": 12,
            "execution_gaps": 13,
            "negative_space": 6,
            "contradictions": 9,
            "recurring_risks": 7,
            "evidence_coverage": 72,
            "score_breakdown": {
                "Execution Gap": 22,
                "Negative Space": 14,
                "Contradiction": 20,
                "Recurring Risk": 12,
                "Peer Deviation": 7
            },
            "description": "High contradiction rate: valve actuator anomalies marked 'False Positive' repeatedly reappear with increased frequency.",
            "total_alerts": 6890,
            "total_cases": 540,
            "total_assets": 195
        },
        {
            "id": "CSE-18",
            "name": "Inland Waterways Traffic Management System",
            "sector": "Maritime & Ports",
            "criticality": "Tier-2",
            "attention_level": "Low",
            "attention_score": 25,
            "main_signal": "Baseline Normal",
            "findings_count": 2,
            "execution_gaps": 2,
            "negative_space": 2,
            "contradictions": 1,
            "recurring_risks": 2,
            "evidence_coverage": 90,
            "score_breakdown": {
                "Execution Gap": 5,
                "Negative Space": 5,
                "Contradiction": 3,
                "Recurring Risk": 5,
                "Peer Deviation": 7
            },
            "description": "Normal operational baseline with standard incident handling cycles.",
            "total_alerts": 2980,
            "total_cases": 240,
            "total_assets": 88
        },
        {
            "id": "CSE-19",
            "name": "National Power Grid Southern Hub (SRLDC)",
            "sector": "Power & Energy Grid",
            "criticality": "Critical",
            "attention_level": "Medium",
            "attention_score": 46,
            "main_signal": "Negative Space",
            "findings_count": 4,
            "execution_gaps": 4,
            "negative_space": 6,
            "contradictions": 2,
            "recurring_risks": 3,
            "evidence_coverage": 85,
            "score_breakdown": {
                "Execution Gap": 9,
                "Negative Space": 15,
                "Contradiction": 6,
                "Recurring Risk": 8,
                "Peer Deviation": 8
            },
            "description": "Substation RTU gateway logs show intermittent 15-minute telemetry blind spots during shift rotations.",
            "total_alerts": 8400,
            "total_cases": 710,
            "total_assets": 270
        },
        {
            "id": "CSE-20",
            "name": "State Broadband Infrastructure Corporation",
            "sector": "Telecommunications & Defense",
            "criticality": "Tier-1",
            "attention_level": "Low",
            "attention_score": 26,
            "main_signal": "Peer Deviation",
            "findings_count": 3,
            "execution_gaps": 2,
            "negative_space": 2,
            "contradictions": 1,
            "recurring_risks": 3,
            "evidence_coverage": 92,
            "score_breakdown": {
                "Execution Gap": 5,
                "Negative Space": 4,
                "Contradiction": 3,
                "Recurring Risk": 6,
                "Peer Deviation": 8
            },
            "description": "Minor deviation in alert triage turnaround during off-peak weekend windows.",
            "total_alerts": 5120,
            "total_cases": 460,
            "total_assets": 190
        }
    ]

    # Detailed findings for CSE-07 (Main Demo Hero) and others
    findings: List[Dict[str, Any]] = [
        {
            "id": "F-07-01",
            "cse_id": "CSE-07",
            "title": "Critical alerts frequently closed without investigation",
            "category": "Execution Gap",
            "severity": "Critical",
            "confidence": 94,
            "explanation": "318 critical alerts have no corresponding investigation evidence in SOC case records.",
            "metrics": {
                "critical_alerts": 2430,
                "investigations": 2112,
                "potential_gaps": 318,
                "avg_closure_minutes": 7.2,
                "peer_median_minutes": 46.0,
                "gap_ratio": "13.1%"
            },
            "why_flagged": [
                "Alert severity = Critical but investigation_id = NULL in case management index.",
                "Alert lifecycle transitioned directly from 'Acknowledged' to 'Closed - Resolved'.",
                "Average closure time is 7 minutes vs Peer median closure time of 46 minutes.",
                "No linked forensic memory dump, PCAP, or triage attachment found."
            ],
            "supporting_records": [
                {
                    "alert_id": "A-10231",
                    "severity": "Critical",
                    "status": "Closed (7m)",
                    "investigation": "Missing",
                    "asset": "SERVER-17",
                    "asset_role": "SCADA Gateway",
                    "created": "14:32:10",
                    "closed": "14:39:15",
                    "rule": "Malware C2 Communication Beacon"
                },
                {
                    "alert_id": "A-10248",
                    "severity": "Critical",
                    "status": "Closed (4m)",
                    "investigation": "Missing",
                    "asset": "RTU-09",
                    "asset_role": "Feeder Controller Substation 4",
                    "created": "15:10:04",
                    "closed": "15:14:22",
                    "rule": "Unauthorized Modbus Function Code Write"
                },
                {
                    "alert_id": "A-10312",
                    "severity": "Critical",
                    "status": "Closed (6m)",
                    "investigation": "Missing",
                    "asset": "HMI-02",
                    "asset_role": "Transmission Operations Console",
                    "created": "16:44:19",
                    "closed": "16:50:30",
                    "rule": "Privilege Escalation via Service Execution"
                },
                {
                    "alert_id": "A-10317",
                    "severity": "Critical",
                    "status": "Closed (5m)",
                    "investigation": "Missing",
                    "asset": "SERVER-17",
                    "asset_role": "SCADA Gateway",
                    "created": "17:02:11",
                    "closed": "17:07:44",
                    "rule": "Repeated Outbound Port 4444 Connection"
                },
                {
                    "alert_id": "A-10405",
                    "severity": "Critical",
                    "status": "Closed (8m)",
                    "investigation": "Missing",
                    "asset": "PLC-CORE-01",
                    "asset_role": "Busbar Protection Controller",
                    "created": "18:15:33",
                    "closed": "18:23:51",
                    "rule": "Firmware Verification Signature Mismatch"
                }
            ],
            "possible_explanations": [
                "Automated SOAR playbook closed alert without logging child case ID.",
                "Known maintenance window test traffic suppressed by tier-1 operator.",
                "Duplicate alert collapsed into parent ticket without foreign key reference.",
                "Incomplete SOC data export batch submitted to NCIIPC supervisory portal."
            ],
            "evidence_graph_case_id": "CASE-GRAPH-07-01",
            "status": "Active"
        },
        {
            "id": "F-07-02",
            "cse_id": "CSE-07",
            "title": "Critical assets with insufficient telemetry",
            "category": "Negative Space",
            "severity": "Critical",
            "confidence": 91,
            "explanation": "High-criticality assets registered as 'Monitoring Enabled' in asset inventory report less than 5 events over 7 days.",
            "metrics": {
                "critical_assets_monitored": 320,
                "silent_critical_assets": 28,
                "expected_daily_events_per_asset": 15000,
                "observed_daily_events": 3,
                "blind_spot_percentage": "8.75%"
            },
            "why_flagged": [
                "Asset Criticality = HIGH in CMDB asset inventory.",
                "Monitoring Status = ENABLED (Syslog, NetFlow, EDR flagged active).",
                "Actual Telemetry Event Count ≈ 0 over 7 consecutive reporting days.",
                "Direct contradiction between regulatory asset declaration and actual SIEM ingestion."
            ],
            "supporting_records": [
                {
                    "alert_id": "TEL-8812",
                    "severity": "High",
                    "status": "Telemetry Deficit",
                    "investigation": "N/A",
                    "asset": "GRID-EMS-SRV04",
                    "asset_role": "Energy Management Primary Database",
                    "created": "00:00:00",
                    "closed": "Present",
                    "rule": "Zero Telemetry Ingestion Over 72h"
                },
                {
                    "alert_id": "TEL-8819",
                    "severity": "High",
                    "status": "Telemetry Deficit",
                    "investigation": "N/A",
                    "asset": "SUBSTATION-RTU-11",
                    "asset_role": "400kV Switchyard Remote Terminal Unit",
                    "created": "00:00:00",
                    "closed": "Present",
                    "rule": "Network Heartbeat Missing Since Oct 01"
                },
                {
                    "alert_id": "TEL-8834",
                    "severity": "High",
                    "status": "Telemetry Deficit",
                    "investigation": "N/A",
                    "asset": "FW-PERIMETER-NORTH",
                    "asset_role": "Perimeter Next-Gen Firewall",
                    "created": "00:00:00",
                    "closed": "Present",
                    "rule": "Syslog Forwarding Forwarder Broken"
                }
            ],
            "possible_explanations": [
                "Log forwarding agent crashed after recent OS kernel update.",
                "Network Access Control (NAC) policy blocked Syslog UDP port 514.",
                "Asset decommissioned in substation without updating CMDB.",
                "Air-gap diode buffer queue overflow dropped uncommitted packets."
            ],
            "evidence_graph_case_id": "CASE-GRAPH-07-02",
            "status": "Active"
        },
        {
            "id": "F-07-03",
            "cse_id": "CSE-07",
            "title": "Repeated alerts without demonstrated remediation",
            "category": "Contradiction",
            "severity": "High",
            "confidence": 88,
            "explanation": "Case marked 'Remediation Completed' yet identical C2 and brute-force alerts recurred on the same host within 24 hours.",
            "metrics": {
                "closed_remediated_cases": 182,
                "recurring_within_48h": 54,
                "recurrence_rate": "29.7%",
                "repeat_assets_count": 12
            },
            "why_flagged": [
                "Case record logs remediation status as 'COMPLETED' (Host Isolated & Remediated).",
                "Telemetric signature for identical malware hash generated new alert 11h later.",
                "No root cause verification or secondary validation scan attached to case.",
                "Contradiction between declared remediation outcome and ongoing telemetry."
            ],
            "supporting_records": [
                {
                    "alert_id": "A-10891",
                    "severity": "High",
                    "status": "Recurred",
                    "investigation": "CASE-9021",
                    "asset": "SERVER-17",
                    "asset_role": "SCADA Gateway",
                    "created": "09:12:00",
                    "closed": "11:00:00",
                    "rule": "Beaconing Recurrence Post-Remediation"
                },
                {
                    "alert_id": "A-10905",
                    "severity": "High",
                    "status": "Recurred",
                    "investigation": "CASE-9021",
                    "asset": "SERVER-17",
                    "asset_role": "SCADA Gateway",
                    "created": "20:45:00",
                    "closed": "21:10:00",
                    "rule": "Persistent Scheduled Task Trigger"
                }
            ],
            "possible_explanations": [
                "Incomplete remediation; persistent malware rootkit not purged.",
                "Remediation was performed on wrong replica VM instance.",
                "Ticketing status manually toggled to 'Completed' to meet monthly SLA target."
            ],
            "evidence_graph_case_id": "CASE-GRAPH-07-03",
            "status": "Active"
        },
        {
            "id": "F-07-04",
            "cse_id": "CSE-07",
            "title": "Investigation patterns show high repetition",
            "category": "Repetition",
            "severity": "Medium",
            "confidence": 89,
            "explanation": "86% of analyst investigations follow an identical 3-step canned script with 0 unique forensic queries.",
            "metrics": {
                "total_investigations_reviewed": 840,
                "canned_pattern_count": 722,
                "fingerprint_dominant_pct": "86.0%",
                "avg_actions_per_case": 3.0
            },
            "why_flagged": [
                "Action sequence fingerprint: [View Alert -> Close Alert -> Standard Note 'Checked no impact'].",
                "Zero telemetry queries executed in EDR/SIEM backend for 86% of cases.",
                "Investigation duration strictly clusters around 90-120 seconds.",
                "Supervisory indicator of rubber-stamping rather than genuine threat triage."
            ],
            "supporting_records": [
                {
                    "alert_id": "INV-701",
                    "severity": "Medium",
                    "status": "Pattern-A",
                    "investigation": "CASE-9104",
                    "asset": "RTU-04",
                    "asset_role": "Feeder Controller",
                    "created": "11:20:00",
                    "closed": "11:21:40",
                    "rule": "Cookie-Cutter Closure Script"
                },
                {
                    "alert_id": "INV-702",
                    "severity": "Medium",
                    "status": "Pattern-A",
                    "investigation": "CASE-9105",
                    "asset": "RTU-05",
                    "asset_role": "Feeder Controller",
                    "created": "11:25:00",
                    "closed": "11:26:35",
                    "rule": "Cookie-Cutter Closure Script"
                }
            ],
            "possible_explanations": [
                "Understaffed analyst shift relying on macro hotkeys.",
                "Poor triage playbooks encouraging superficial inspection.",
                "Lack of access rights for tier-1 operators to query deep forensic databases."
            ],
            "evidence_graph_case_id": "CASE-GRAPH-07-04",
            "status": "Active"
        },
        {
            "id": "F-07-05",
            "cse_id": "CSE-07",
            "title": "Metric-Outcome Divergence: 99.2% ACK SLA vs 12% Downstream Remediation",
            "category": "Metric Divergence",
            "severity": "High",
            "confidence": 92,
            "explanation": "Near-perfect initial acknowledgement KPI masks severe breakdown in investigation and escalation pipelines.",
            "metrics": {
                "ack_sla_compliance": "99.2%",
                "investigation_rate": "23.4%",
                "escalation_rate": "4.1%",
                "true_remediation_rate": "12.0%",
                "kpi_divergence_delta": "+87.2%"
            },
            "why_flagged": [
                "Tier-1 SLA: 99.2% of alerts acknowledged in < 5 minutes (Executive dashboard looks green).",
                "Actual investigation rate for high/critical alerts is only 23.4%.",
                "Recurring alert rate on identical infrastructure remains elevated at 34%.",
                "Classic Metric-Outcome Divergence: compliance metrics optimized at the expense of real defensive posture."
            ],
            "supporting_records": [
                {
                    "alert_id": "MET-401",
                    "severity": "High",
                    "status": "Divergent",
                    "investigation": "N/A",
                    "asset": "SUBSTATION-HUB-01",
                    "asset_role": "Regional Substation Gateway",
                    "created": "08:00:00",
                    "closed": "08:03:00",
                    "rule": "Immediate Ack with Bypassed Escalation"
                }
            ],
            "possible_explanations": [
                "Contractual penalties pegged exclusively to Initial Acknowledgement Time.",
                "Automated ACK script configured in SIEM console to artificially inflate SLA.",
                "No Tier-2/Tier-3 forensic personnel assigned to the shift."
            ],
            "evidence_graph_case_id": "CASE-GRAPH-07-01",
            "status": "Active"
        }
    ]

    # Pre-built Evidence Graphs for Hero Scenarios
    graphs: Dict[str, Dict[str, Any]] = {
        "CASE-GRAPH-07-01": {
            "case_id": "CASE-GRAPH-07-01",
            "alert_id": "A-10231",
            "cse_id": "CSE-07",
            "cse_name": "Northern Regional Load Despatch Centre (NRLDC)",
            "finding_title": "Critical Alert Investigation Gap",
            "scenario_type": "Execution Gap",
            "summary": "Critical malware beaconing alert acknowledged within 3 minutes but closed in 7 minutes with complete absence of linked investigation, forensic evidence, or remediation.",
            "nodes": [
                {
                    "id": "node-asset",
                    "stage": "Asset",
                    "label": "SERVER-17",
                    "status": "verified",
                    "subtitle": "SCADA Gateway (Zone 1)",
                    "timestamp": "Pre-existing",
                    "details": {
                        "Asset ID": "SERVER-17",
                        "Role": "SCADA Gateway & Protocol Translator",
                        "Criticality Level": "CRITICAL (NCIIPC Category A)",
                        "Substation": "400kV Main Transmission Hub",
                        "IP Address": "10.240.12.17",
                        "OS": "Red Hat Enterprise Linux 8.8 (Hardened)",
                        "Monitoring Config": "Syslog UDP 514 + NetFlow + EDR Agent v4.2"
                    },
                    "flag_reason": None
                },
                {
                    "id": "node-telemetry",
                    "stage": "Telemetry",
                    "label": "NetFlow Anomaly",
                    "status": "verified",
                    "subtitle": "Port 4444 Outbound (540 KB)",
                    "timestamp": "14:32:05",
                    "details": {
                        "Telemetry Stream": "Core Switch Mirror NetFlow v9",
                        "Observed Traffic": "Repeated beaconing to external IP 198.51.100.42:4444",
                        "Bytes Transferred": "540 KB across 14 syn-ack sessions",
                        "Significance": "Known Cobalt Strike default listener port",
                        "Event ID": "EVT-894102"
                    },
                    "flag_reason": None
                },
                {
                    "id": "node-alert",
                    "stage": "Alert",
                    "label": "Alert A-10231",
                    "status": "verified",
                    "subtitle": "Critical: Malware C2 Beacon",
                    "timestamp": "14:32:10",
                    "details": {
                        "Alert ID": "A-10231",
                        "Severity": "CRITICAL",
                        "Rule Name": "Malware C2 Communication Beacon Detected",
                        "Category": "Command & Control / Exfiltration",
                        "Trigger Condition": "Threshold > 10 outbound unencrypted sessions to untrusted external IP",
                        "Raw Payload": "src=10.240.12.17:51220 dst=198.51.100.42:4444 proto=TCP"
                    },
                    "flag_reason": None
                },
                {
                    "id": "node-ack",
                    "stage": "Acknowledgement",
                    "label": "Acknowledged",
                    "status": "verified",
                    "subtitle": "Analyst-04 (Within 3 mins)",
                    "timestamp": "14:35:12",
                    "details": {
                        "Acknowledged By": "Analyst-04 (SOC Tier-1 Operator)",
                        "Ack Delay": "3 minutes 2 seconds (Within 5m SLA)",
                        "Session ID": "SESS-OP-4412",
                        "Initial Comment": "Alert queued for standard review"
                    },
                    "flag_reason": None
                },
                {
                    "id": "node-investigation",
                    "stage": "Investigation",
                    "label": "Investigation Record",
                    "status": "missing",
                    "subtitle": "MISSING — Broken Workflow",
                    "timestamp": "Expected 14:36",
                    "details": {
                        "Status": "NO LINKED INVESTIGATION FOUND",
                        "Case Ticket ID": "NULL / Missing",
                        "Expected Action": "Forensic host check, process tree inspection, netstat verification",
                        "Actual Action": "No query executed against SIEM/EDR backend",
                        "Deviation": "Violation of NCIIPC Standard Operating Procedure Section 4.2: Mandatory Deep Triage for Critical Assets"
                    },
                    "flag_reason": "Execution Gap: Critical alert transitioned to closure without opening investigation case ticket."
                },
                {
                    "id": "node-evidence",
                    "stage": "Evidence",
                    "label": "Forensic Artifacts",
                    "status": "missing",
                    "subtitle": "MISSING — Zero Proof Captured",
                    "timestamp": "Expected 14:38",
                    "details": {
                        "Status": "ZERO EVIDENCE ATTACHED",
                        "PCAP Attached": "No (Missing)",
                        "Memory Dump": "No (Missing)",
                        "Process List": "No (Missing)",
                        "Threat Intel Corroboration": "Not verified",
                        "Impact": "Inability for NCIIPC supervisor or CSE incident commander to evaluate actual compromise scope"
                    },
                    "flag_reason": "Negative Evidence: Expected forensic artifacts completely absent."
                },
                {
                    "id": "node-decision",
                    "stage": "Decision",
                    "label": "Triage Decision",
                    "status": "anomalous",
                    "subtitle": "Premature Disposition",
                    "timestamp": "14:40:02",
                    "details": {
                        "Disposition": "Closed - False Positive / Suppressed",
                        "Analyst Justification": "'Routine routine maintenance beaconing' (Generic boiler-plate text)",
                        "Supervisor Signoff": "None",
                        "Contradiction": "No scheduled maintenance window existed on NRLDC calendar for 14:00-15:00"
                    },
                    "flag_reason": "Decision made without supporting technical evidence."
                },
                {
                    "id": "node-escalation",
                    "stage": "Escalation",
                    "label": "Escalation to Tier-2/CERT",
                    "status": "bypassed",
                    "subtitle": "BYPASSED — SOP Violation",
                    "timestamp": "Skipped",
                    "details": {
                        "Escalation Status": "NOT TRIGGERED",
                        "Expected Escalation": "NCIIPC Alert Desk & National CERT Notification within 15 minutes",
                        "Actual Outcome": "Suppressed inside local SOC console without notification"
                    },
                    "flag_reason": "Mandatory regulatory escalation bypassed."
                },
                {
                    "id": "node-remediation",
                    "stage": "Remediation",
                    "label": "Host Isolation / IOC Block",
                    "status": "bypassed",
                    "subtitle": "SKIPPED — Exposure Active",
                    "timestamp": "Skipped",
                    "details": {
                        "Remediation Action": "NONE EXECUTED",
                        "Firewall Blacklist": "External IP 198.51.100.42 remains unblocked",
                        "Host Isolation": "SERVER-17 remains connected to SCADA LAN",
                        "Ongoing Risk": "Asset continued to transmit beacon packets at 17:02"
                    },
                    "flag_reason": "No containment or mitigation enacted."
                },
                {
                    "id": "node-closure",
                    "stage": "Closure",
                    "label": "Premature Closure",
                    "status": "verified",
                    "subtitle": "Closed at 14:39:15 (Total 7m)",
                    "timestamp": "14:39:15",
                    "details": {
                        "Final Status": "Closed - Resolved",
                        "Total Handling Time": "7 minutes 5 seconds",
                        "Peer Average Time": "46 minutes",
                        "Supervisor Verdict": "HIGH SUPERVISORY ATTENTION: Unsubstantiated closure of critical infrastructure alert."
                    },
                    "flag_reason": "Closed without fulfilling lifecycle prerequisites."
                }
            ],
            "edges": [
                {"source": "node-asset", "target": "node-telemetry", "status": "normal", "label": "Telemetry Egress"},
                {"source": "node-telemetry", "target": "node-alert", "status": "normal", "label": "Rule Match"},
                {"source": "node-alert", "target": "node-ack", "status": "normal", "label": "Ack (3m)"},
                {"source": "node-ack", "target": "node-investigation", "status": "broken", "label": "✗ Gap: Missing Inv"},
                {"source": "node-investigation", "target": "node-evidence", "status": "broken", "label": "✗ Gap: Missing Evid"},
                {"source": "node-evidence", "target": "node-decision", "status": "broken", "label": "Unsubstantiated"},
                {"source": "node-decision", "target": "node-escalation", "status": "skipped", "label": "Bypassed SOP"},
                {"source": "node-escalation", "target": "node-remediation", "status": "skipped", "label": "No Action"},
                {"source": "node-ack", "target": "node-closure", "status": "broken", "label": "Direct Premature Close"}
            ]
        },
        "CASE-GRAPH-07-02": {
            "case_id": "CASE-GRAPH-07-02",
            "alert_id": "TEL-8812",
            "cse_id": "CSE-07",
            "cse_name": "Northern Regional Load Despatch Centre (NRLDC)",
            "finding_title": "Critical assets with insufficient telemetry (Negative Space)",
            "scenario_type": "Negative Space",
            "summary": "High-criticality Energy Management Server GRID-EMS-SRV04 configured as actively monitored in CMDB, but telemetry flow has been flatlined at 0 events for over 72 hours.",
            "nodes": [
                {
                    "id": "node-asset",
                    "stage": "Asset",
                    "label": "GRID-EMS-SRV04",
                    "status": "verified",
                    "subtitle": "Critical EMS Database Server",
                    "timestamp": "Registered",
                    "details": {
                        "Asset ID": "GRID-EMS-SRV04",
                        "Criticality": "CRITICAL TIER-1",
                        "Function": "Master Energy Management & AGC System",
                        "Expected Telemetry Rate": "12,000 to 20,000 events/hr",
                        "Regulatory Requirement": "NCIIPC Mandatory Continuous Auditing"
                    },
                    "flag_reason": None
                },
                {
                    "id": "node-telemetry",
                    "stage": "Telemetry",
                    "label": "Telemetry Ingestion",
                    "status": "missing",
                    "subtitle": "NEGATIVE SPACE — Zero Logs",
                    "timestamp": "Last 72 Hours",
                    "details": {
                        "Observed Ingestion": "0 events/hour",
                        "Expected Ingestion": "15,000 events/hour",
                        "Status": "TELEMETRY SILENCE (Blind Spot)",
                        "Last Seen Packet": "72 hours ago"
                    },
                    "flag_reason": "Negative Space: Critical asset is invisible in SOC monitoring stream."
                },
                {
                    "id": "node-alert",
                    "stage": "Alert",
                    "label": "Health Check Alert",
                    "status": "missing",
                    "subtitle": "MISSING — Silence Undetected",
                    "timestamp": "Expected",
                    "details": {
                        "Heartbeat Alert": "Not Generated (SIEM log-drop detection rule disabled)",
                        "SOC Awareness": "SOC unaware of blind spot until supervisory audit"
                    },
                    "flag_reason": "Secondary Gap: No alert generated for log-forwarder failure."
                },
                {
                    "id": "node-ack",
                    "stage": "Acknowledgement",
                    "label": "Supervisor Detection",
                    "status": "anomalous",
                    "subtitle": "Flagged by SENTINEL-X",
                    "timestamp": "Audit Cycle",
                    "details": {
                        "Detected By": "SENTINEL-X Negative-Space Correlator",
                        "Delta": "Asset marked ACTIVE in CMDB vs 0 rows in Elastic/Splunk indices"
                    },
                    "flag_reason": "Discovered only via Supervisory Cross-Source Analytics."
                },
                {
                    "id": "node-investigation",
                    "stage": "Investigation",
                    "label": "Supervisory Audit Case",
                    "status": "verified",
                    "subtitle": "Audit Ticket SUP-882",
                    "timestamp": "Active",
                    "details": {
                        "Supervisory Ticket": "SUP-882",
                        "Action Required": "Immediate physical verification of forwarder daemon and router ACLs"
                    },
                    "flag_reason": None
                },
                {
                    "id": "node-closure",
                    "stage": "Closure",
                    "label": "Open Supervisory Directive",
                    "status": "anomalous",
                    "subtitle": "Pending CSE Remediation",
                    "timestamp": "Active",
                    "details": {
                        "Notice Issued": "Notice 4B issued to NRLDC Chief Information Security Officer"
                    },
                    "flag_reason": "Non-compliance directive issued."
                }
            ],
            "edges": [
                {"source": "node-asset", "target": "node-telemetry", "status": "broken", "label": "✗ 0 Events (Negative Space)"},
                {"source": "node-telemetry", "target": "node-alert", "status": "broken", "label": "No Heartbeat Alert"},
                {"source": "node-asset", "target": "node-ack", "status": "normal", "label": "SENTINEL-X Detection"},
                {"source": "node-ack", "target": "node-investigation", "status": "normal", "label": "Audit Opened"},
                {"source": "node-investigation", "target": "node-closure", "status": "normal", "label": "Supervisory Directive"}
            ]
        },
        "CASE-GRAPH-07-03": {
            "case_id": "CASE-GRAPH-07-03",
            "alert_id": "A-10891",
            "cse_id": "CSE-07",
            "cse_name": "Northern Regional Load Despatch Centre (NRLDC)",
            "finding_title": "Repeated alerts without demonstrated remediation (Contradiction)",
            "scenario_type": "Contradiction",
            "summary": "Case CASE-9021 logged as 'Remediated & Verified' on SERVER-17, but identical attack pattern repeated 11 hours later on the same asset.",
            "nodes": [
                {
                    "id": "node-asset",
                    "stage": "Asset",
                    "label": "SERVER-17",
                    "status": "verified",
                    "subtitle": "SCADA Gateway",
                    "timestamp": "Day 1",
                    "details": {"Asset": "SERVER-17", "Zone": "Substation OT Network"}
                },
                {
                    "id": "node-alert1",
                    "stage": "Alert",
                    "label": "Initial Alert A-10114",
                    "status": "verified",
                    "subtitle": "Malware C2 Communication",
                    "timestamp": "Day 1, 09:12",
                    "details": {"Alert ID": "A-10114", "Signature": "Win32/CobaltBeacon.Gen"}
                },
                {
                    "id": "node-case1",
                    "stage": "Remediation",
                    "label": "Case CASE-9021",
                    "status": "anomalous",
                    "subtitle": "Marked 'Remediated'",
                    "timestamp": "Day 1, 11:00",
                    "details": {
                        "Reported Action": "Host scanned, malicious service removed, port blocked",
                        "Remediation Status": "COMPLETED",
                        "Signoff Analyst": "Analyst-02"
                    },
                    "flag_reason": "Contradiction: Remediated state declared without technical efficacy."
                },
                {
                    "id": "node-alert2",
                    "stage": "Alert",
                    "label": "Recurring Alert A-10891",
                    "status": "anomalous",
                    "subtitle": "Identical C2 Reappeared (11h later)",
                    "timestamp": "Day 1, 22:15",
                    "details": {
                        "Alert ID": "A-10891",
                        "Signature": "Win32/CobaltBeacon.Gen",
                        "Asset": "SERVER-17",
                        "Interval": "11 hours 15 minutes post-remediation"
                    },
                    "flag_reason": "Contradiction: Declared remediation failed to eliminate threat."
                },
                {
                    "id": "node-closure",
                    "stage": "Closure",
                    "label": "Effectiveness Deficit",
                    "status": "missing",
                    "subtitle": "Recurring Threat Exposure",
                    "timestamp": "Ongoing",
                    "details": {
                        "Diagnosis": "Remediation was superficial; malicious scheduled task remained active",
                        "Supervisory Impact": "High risk of persistent adversary presence in critical OT subnet"
                    },
                    "flag_reason": "Persistent vulnerability despite closed ticket."
                }
            ],
            "edges": [
                {"source": "node-asset", "target": "node-alert1", "status": "normal", "label": "Initial Detection"},
                {"source": "node-alert1", "target": "node-case1", "status": "normal", "label": "Logged 'Remediated'"},
                {"source": "node-case1", "target": "node-alert2", "status": "broken", "label": "✗ Recurred in 11h (Contradiction)"},
                {"source": "node-alert2", "target": "node-closure", "status": "broken", "label": "Unresolved Exposure"}
            ]
        },
        "CASE-GRAPH-01-01": {
            "case_id": "CASE-GRAPH-01-01",
            "alert_id": "A-99014",
            "cse_id": "CSE-01",
            "cse_name": "Unified Payments Interface (UPI) Core Switch",
            "finding_title": "Baseline Normal Operation (Reference Model)",
            "scenario_type": "Baseline Normal",
            "summary": "Gold standard execution chain: Critical payment API anomaly investigated, forensic artifacts attached, escalated to L2, patched, verified, and closed with complete audit trail.",
            "nodes": [
                {
                    "id": "node-asset",
                    "stage": "Asset",
                    "label": "UPI-SWITCH-GW-01",
                    "status": "verified",
                    "subtitle": "Core Payment API Switch",
                    "timestamp": "Verified",
                    "details": {"Asset": "UPI-SWITCH-GW-01", "Criticality": "CRITICAL", "Zone": "Payment DMZ"}
                },
                {
                    "id": "node-telemetry",
                    "stage": "Telemetry",
                    "label": "API WAF Telemetry",
                    "status": "verified",
                    "subtitle": "Volumetric SQL Injection",
                    "timestamp": "10:14:02",
                    "details": {"Events": "1,420 malformed payloads", "Protocol": "HTTPS POST /api/v2/pay"}
                },
                {
                    "id": "node-alert",
                    "stage": "Alert",
                    "label": "Alert A-99014",
                    "status": "verified",
                    "subtitle": "Critical: SQLi Attack",
                    "timestamp": "10:14:08",
                    "details": {"Alert ID": "A-99014", "Severity": "Critical", "Rule": "Signature SQLi OWASP-01"}
                },
                {
                    "id": "node-ack",
                    "stage": "Acknowledgement",
                    "label": "Acknowledged",
                    "status": "verified",
                    "subtitle": "Analyst-11 (1m 40s)",
                    "timestamp": "10:15:48",
                    "details": {"Ack By": "Analyst-11", "Response Time": "1m 40s"}
                },
                {
                    "id": "node-investigation",
                    "stage": "Investigation",
                    "label": "Investigation Case",
                    "status": "verified",
                    "subtitle": "CASE-UPI-4402 Opened",
                    "timestamp": "10:17:10",
                    "details": {"Case ID": "CASE-UPI-4402", "Investigator": "Senior Analyst S. Nair"}
                },
                {
                    "id": "node-evidence",
                    "stage": "Evidence",
                    "label": "Forensic Evidence",
                    "status": "verified",
                    "subtitle": "PCAP + WAF Payload Dumps",
                    "timestamp": "10:22:40",
                    "details": {"Evidence Attached": "Full PCAP capture (3.8 MB) + IP origin correlation report"}
                },
                {
                    "id": "node-decision",
                    "stage": "Decision",
                    "label": "Confirmed True Positive",
                    "status": "verified",
                    "subtitle": "Malicious Automated Scanner",
                    "timestamp": "10:30:15",
                    "details": {"Verdict": "True Positive Attacker Probe"}
                },
                {
                    "id": "node-escalation",
                    "stage": "Escalation",
                    "label": "Escalation to CERT & NOC",
                    "status": "verified",
                    "subtitle": "Incident Ticket INC-981",
                    "timestamp": "10:35:00",
                    "details": {"Escalated To": "National CERT + Core Security Ops"}
                },
                {
                    "id": "node-remediation",
                    "stage": "Remediation",
                    "label": "IP Blacklist & WAF Rule Patch",
                    "status": "verified",
                    "subtitle": "Remediated in 42m",
                    "timestamp": "10:56:00",
                    "details": {"Actions": "Attacker CIDR blocked at border BGP; WAF virtual patch applied"}
                },
                {
                    "id": "node-closure",
                    "stage": "Closure",
                    "label": "Audit-Verified Closure",
                    "status": "verified",
                    "subtitle": "Complete Lifecycle Verified",
                    "timestamp": "11:20:00",
                    "details": {"Total Time": "1h 6m", "Evidence Coverage": "100%", "Status": "Resolved & Audited"}
                }
            ],
            "edges": [
                {"source": "node-asset", "target": "node-telemetry", "status": "normal", "label": "Egress Log"},
                {"source": "node-telemetry", "target": "node-alert", "status": "normal", "label": "Matched Rule"},
                {"source": "node-alert", "target": "node-ack", "status": "normal", "label": "Ack (1m 40s)"},
                {"source": "node-ack", "target": "node-investigation", "status": "normal", "label": "Case Opened"},
                {"source": "node-investigation", "target": "node-evidence", "status": "normal", "label": "Evidence Attached"},
                {"source": "node-evidence", "target": "node-decision", "status": "normal", "label": "Triage Confirmed"},
                {"source": "node-decision", "target": "node-escalation", "status": "normal", "label": "Escalation SOP"},
                {"source": "node-escalation", "target": "node-remediation", "status": "normal", "label": "Patched & Contained"},
                {"source": "node-remediation", "target": "node-closure", "status": "normal", "label": "Verified Audit"}
            ]
        }
    }

    # Aggregate stats for top dashboard cards
    total_alerts = sum(c["total_alerts"] for c in cses)
    total_cases = sum(c["total_cases"] for c in cses)
    cses_requiring_attention = sum(1 for c in cses if c["attention_level"] in ["High", "Medium"])
    total_execution_gaps = sum(c["execution_gaps"] for c in cses)
    total_negative_space = sum(c["negative_space"] for c in cses)
    total_contradictions = sum(c["contradictions"] for c in cses)

    overview = {
        "total_cses": len(cses),
        "total_alerts": total_alerts,
        "total_cases": total_cases,
        "cses_requiring_attention": cses_requiring_attention,
        "total_execution_gaps": total_execution_gaps,
        "total_negative_space": total_negative_space,
        "total_contradictions": total_contradictions,
        "attention_distribution": {
            "High": sum(1 for c in cses if c["attention_level"] == "High"),
            "Medium": sum(1 for c in cses if c["attention_level"] == "Medium"),
            "Low": sum(1 for c in cses if c["attention_level"] == "Low")
        },
        "sector_breakdown": {
            "Power & Energy Grid": 4,
            "Financial Services & Banking": 3,
            "Telecommunications & Defense": 3,
            "Transportation & Rail": 2,
            "Petroleum & Natural Gas": 2,
            "Civil Aviation": 1,
            "Atomic Energy & Nuclear": 1,
            "Space & Defense": 1,
            "Maritime & Ports": 2,
            "Healthcare & Public Health": 1,
            "Government & E-Governance": 1,
            "Public Safety & Emergency": 1
        }
    }

    return {
        "overview": overview,
        "cses": cses,
        "findings": findings,
        "graphs": graphs
    }
