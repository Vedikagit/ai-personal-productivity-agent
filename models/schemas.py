from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Task(BaseModel):
    task_id: str
    title: str
    estimated_minutes: int
    deadline: Optional[datetime]
    importance: int  # 1–5
    effort_level: str  # low / medium / high
    dependencies: List[str]


class AnalyzerOutput(BaseModel):
    tasks: List[Task]


class DecisionOutput(BaseModel):
    chosen_task: Task
    reasoning: dict
    alternative_task: Optional[str]
    confidence_score: float
    estimated_time: int


class ReflectionOutput(BaseModel):
    reflection: str
    next_focus: str


class UserGoal(BaseModel):
    goal_text: str
    deadline: Optional[datetime]
    importance: int  # 1–5


class UserContext(BaseModel):
    energy_level: Literal["low", "medium", "high"]
    available_minutes: int


class UserInput(BaseModel):
    goals: List[UserGoal]
    context: UserContext
    intent: Literal["decide_next_task", "schedule_block", "daily_reflection"]


class ScheduledBlock(BaseModel):
    task_name: str
    start_time: datetime
    end_time: datetime
    duration_minutes: int


class SchedulingReasoning(BaseModel):
    why_this_time: str
    conflict_check: str
    energy_alignment: str


class SchedulingOutput(BaseModel):
    status: str  # "scheduled" | "failed"
    scheduled_block: ScheduledBlock
    reasoning: SchedulingReasoning