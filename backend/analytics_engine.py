"""
SENTINEL-X — Deterministic Supervisory Analytics Engine
Implements core operational gap detection rules, transparent attention scoring,
and cross-source contradiction correlation.
"""

from typing import Dict, List, Any, Optional

class SupervisoryAnalyticsEngine:
    """
    Deterministic Supervisory Rules Engine for NCIIPC SOC Assessment.
    No opaque AI black boxes: all findings are deterministic, evidence-backed,
    and traceable to specific operational telemetry rows.
    """

    @staticmethod
    def evaluate_execution_gap(alert: Dict[str, Any], investigation: Optional[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Rule A: Execution Gap
        IF severity = Critical AND status = Closed AND investigation_id = NULL
        THEN Flag Execution Gap
        """
        severity = str(alert.get("severity", "")).lower()
        status = str(alert.get("status", "")).lower()
        investigation_id = alert.get("investigation_id") or (investigation.get("id") if investigation else None)

        if severity == "critical" and "closed" in status and not investigation_id:
            return {
                "rule": "RULE_EXECUTION_GAP_CRITICAL_UNINVESTIGATED",
                "severity": "Critical",
                "alert_id": alert.get("id"),
                "asset_id": alert.get("asset_id"),
                "reason": "Critical severity alert closed without mandatory investigation record.",
                "duration_minutes": alert.get("closure_minutes", 0),
                "sop_violation": "NCIIPC Category-A Mandate Section 4.2"
            }
        return None

    @staticmethod
    def evaluate_negative_space(asset: Dict[str, Any], telemetry_stats: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Rule B: Negative Space
        IF asset.criticality = HIGH AND monitoring = ENABLED AND telemetry_count ≈ 0
        THEN Flag Negative Space Blind Spot
        """
        criticality = str(asset.get("criticality", "")).upper()
        monitoring = str(asset.get("monitoring_status", "")).upper()
        event_count = telemetry_stats.get("event_count_7d", 0)

        if criticality in ["CRITICAL", "HIGH", "TIER-1"] and monitoring == "ENABLED" and event_count < 10:
            return {
                "rule": "RULE_NEGATIVE_SPACE_TELEMETRY_SILENCE",
                "severity": "Critical",
                "asset_id": asset.get("id"),
                "asset_name": asset.get("name"),
                "reason": f"Asset declared active in CMDB but recorded only {event_count} telemetry events over 7 days.",
                "expected_events": telemetry_stats.get("expected_events_7d", 100000),
                "actual_events": event_count,
                "gap_type": "Monitoring Blind Spot"
            }
        return None

    @staticmethod
    def evaluate_contradiction(remediation: Dict[str, Any], subsequent_alerts: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        Rule C: Cross-Source Contradiction
        IF remediation_status = COMPLETED AND same asset/category repeatedly generates alerts afterward
        THEN Flag Remediation Effectiveness Contradiction
        """
        status = str(remediation.get("status", "")).upper()
        asset_id = remediation.get("asset_id")
        
        matching_recurrences = [
            a for a in subsequent_alerts
            if a.get("asset_id") == asset_id and a.get("category") == remediation.get("category")
        ]

        if status == "COMPLETED" and len(matching_recurrences) > 0:
            return {
                "rule": "RULE_REMEDIATION_CONTRADICTION",
                "severity": "High",
                "case_id": remediation.get("case_id"),
                "asset_id": asset_id,
                "reason": f"Case marked 'Completed' yet {len(matching_recurrences)} identical alerts generated within recurrence window.",
                "recurrence_count": len(matching_recurrences),
                "subsequent_alerts": [a.get("id") for a in matching_recurrences[:3]]
            }
        return None

    @staticmethod
    def evaluate_metric_divergence(kpis: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Rule D: Metric–Outcome Divergence
        IF acknowledgement_SLA > 95% AND investigation_rate is low AND recurring_alert_rate is high
        THEN Flag Metric–Outcome Divergence
        """
        ack_sla = kpis.get("ack_sla_pct", 0)
        inv_rate = kpis.get("investigation_rate_pct", 0)
        recurrence_rate = kpis.get("recurring_alert_rate_pct", 0)

        if ack_sla >= 95.0 and inv_rate < 30.0 and recurrence_rate > 25.0:
            return {
                "rule": "RULE_METRIC_OUTCOME_DIVERGENCE",
                "severity": "High",
                "reason": f"Near-perfect ACK SLA ({ack_sla}%) diverged from poor downstream investigation rate ({inv_rate}%) and high recurrence ({recurrence_rate}%).",
                "divergence_delta": round(ack_sla - inv_rate, 1)
            }
        return None

    @staticmethod
    def calculate_attention_score(metrics: Dict[str, int]) -> Dict[str, Any]:
        """
        Transparent Supervisory Attention Score (0 - 100).
        No hidden coefficients. Clean additive vector:
        Execution Gap: up to 30
        Negative Space: up to 25
        Contradiction: up to 20
        Recurring Risk: up to 15
        Peer Deviation: up to 10
        """
        raw_gap = min(30, int(metrics.get("execution_gaps", 0) * 1.5))
        raw_neg = min(25, int(metrics.get("negative_space", 0) * 2.2))
        raw_con = min(20, int(metrics.get("contradictions", 0) * 2.5))
        raw_rec = min(15, int(metrics.get("recurring_risks", 0) * 1.6))
        raw_peer = min(10, int(metrics.get("peer_deviation", 8)))

        total = min(100, raw_gap + raw_neg + raw_con + raw_rec + raw_peer)

        if total >= 70:
            level = "High"
        elif total >= 40:
            level = "Medium"
        else:
            level = "Low"

        return {
            "score": total,
            "level": level,
            "breakdown": {
                "Execution Gap": raw_gap,
                "Negative Space": raw_neg,
                "Contradiction": raw_con,
                "Recurring Risk": raw_rec,
                "Peer Deviation": raw_peer
            },
            "formula_explanation": "Deterministic sum across 5 integrity vectors: Execution Gap (max 30) + Negative Space (max 25) + Contradictions (max 20) + Recurring Risk (max 15) + Peer Deviation (max 10)."
        }
