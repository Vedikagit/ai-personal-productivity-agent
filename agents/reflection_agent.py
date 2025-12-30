from pydantic import BaseModel
from typing import List

class ReflectionOutput(BaseModel):
    reflection: str
    tomorrow_focus: List[str]

def reflect_tasks(today_tasks: List[str], completed_tasks: List[str]) -> ReflectionOutput:
    remaining = [t for t in today_tasks if t not in completed_tasks]
    completed_count = len(completed_tasks)
    total_count = len(today_tasks)
    completion_pct = int((completed_count / total_count) * 100) if total_count else 0
    return ReflectionOutput(
        reflection=f"You completed {completed_count}/{total_count} tasks today ({completion_pct}%).",
        tomorrow_focus=remaining[:3]  # show top 3 pending tasks for tomorrow
    )

def agent_introspect(agent_name: str, output_done: bool) -> str:
    """
    Checks if agent completed all steps before giving output.
    Returns message to display if incomplete, else returns None.
    """
    if not output_done:
        return f"[{agent_name}] ⚠️ Step incomplete. Cannot proceed."
    return f"[{agent_name}] ✅ All steps completed successfully."