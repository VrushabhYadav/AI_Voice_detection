from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from enum import Enum
from datetime import datetime

class Verdict(str, Enum):
    HUMAN = "HUMAN"
    AI = "AI"
    UNCERTAIN = "UNCERTAIN"

class SessionStatus(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"

class WindowResultDB(BaseModel):
    session_id: str
    window_index: int
    timestamp: datetime
    verdict: Verdict
    risk_score: float
    confidence: float
    features_summary: List[float] = Field(description="1D array summary of MFCC/Mel features")
    evidence: Dict[str, Any]

class SessionDB(BaseModel):
    session_id: str
    source_type: str 
    original_filename: Optional[str] = None
    start_time: datetime
    end_time: Optional[datetime] = None
    status: SessionStatus
    final_verdict: Optional[Verdict] = None
    final_risk_score: Optional[float] = None
    total_windows_processed: int = 0

class WindowResultResponse(BaseModel):
    window_index: int
    verdict: Verdict
    risk_score: float
    confidence: float

class AnalysisResponse(BaseModel):
    session_id: str
    status: SessionStatus
    final_verdict: Optional[Verdict]
    final_risk_score: Optional[float]
    windows: List[WindowResultResponse]