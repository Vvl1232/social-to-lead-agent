from typing import TypedDict, List, Optional

class AgentState(TypedDict):
    messages: List[str]
    intent: str
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]
    last_question: Optional[str]
    lead_captured: bool