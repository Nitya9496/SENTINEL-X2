"""
SENTINEL-X — Data Models
Pydantic schemas for entities, findings, evidence graph nodes, and supervisory assessments.
"""
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class CSE(BaseModel):
    id: str
    name: str
    sector: str
    criticality: str  # Critical, Tier-1, Tier-2
    attention_level: str  # High, Medium, Low
    attention_score: int  # 0 - 100
    main_signal: str
    findings_count: int
    execution_gaps: int
    raw_alert_gaps: Optional[int] = 0
    negative_space: int
    contradictions: int
    recurring_risks: int
    evidence_coverage: int  # percentage e.g. 71%
    score_breakdown: Dict[str, int]
    description: str
    total_alerts: int
    total_cases: int
    total_assets: int


class Finding(BaseModel):
    id: str
    cse_id: str
    title: str
    category: str  # Execution Gap, Negative Space, Contradiction, Metric Divergence, Repetition
    severity: str  # Critical, High, Medium, Low
    confidence: int  # percentage
    explanation: str
    metrics: Dict[str, Any]
    why_flagged: List[str]
    supporting_records: List[Dict[str, Any]]
    possible_explanations: List[str]
    evidence_graph_case_id: str
    status: str = "Active"  # Active, Confirmed, False Positive, Under Clarification


class GraphNode(BaseModel):
    id: str
    stage: str  # Asset, Telemetry, Alert, Ack, Investigation, Evidence, Decision, Escalation, Remediation, Closure
    label: str
    status: str  # verified, missing, bypassed, anomalous
    subtitle: Optional[str] = None
    icon: Optional[str] = None
    timestamp: Optional[str] = None
    details: Dict[str, Any] = Field(default_factory=dict)
    flag_reason: Optional[str] = None


class GraphEdge(BaseModel):
    source: str
    target: str
    status: str  # normal, broken, skipped
    label: Optional[str] = None


class EvidenceGraphData(BaseModel):
    case_id: str
    alert_id: str
    cse_id: str
    cse_name: str
    finding_title: str
    scenario_type: str
    nodes: List[GraphNode]
    edges: List[GraphEdge]
    summary: str


class EvidenceRecord(BaseModel):
    record_id: str
    cse_id: str
    alert_id: Optional[str] = None
    asset_id: Optional[str] = None
    record_type: str  # Alert, Asset, Telemetry, Case, Investigation, Remediation
    timestamp: str
    attributes: Dict[str, Any]
    discrepancy: Optional[str] = None


class SystemOverview(BaseModel):
    total_cses: int
    total_alerts: int
    total_cases: int
    cses_requiring_attention: int
    total_execution_gaps: int
    total_raw_alert_gaps: Optional[int] = 1420
    total_negative_space: int
    total_contradictions: int
    attention_distribution: Dict[str, int]
    sector_breakdown: Dict[str, int]
