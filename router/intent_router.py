from enum import Enum
from typing import Literal
import re

class IntentType(str, Enum):
    DECISION = "decision"
    SCHEDULING = "scheduling"
    UNKNOWN = "unknown"

def detect_intent(user_input: str) -> IntentType:
    text = user_input.lower()

    scheduling_keywords = [
        "schedule",
        "add to calendar",
        "book",
        "set a meeting",
        "plan a session",
        "block time"
    ]

    decision_keywords = [
        "what should i do",
        "prioritize",
        "next task",
        "help me decide",
        "what now",
        "focus on",
        "help me plan"
    ]

    if any(keyword in text for keyword in scheduling_keywords):
        return IntentType.SCHEDULING
    
    if "\n" in text or "," in text:
        return IntentType.DECISION

    if any(keyword in text for keyword in decision_keywords):
        return IntentType.DECISION

    return IntentType.UNKNOWN