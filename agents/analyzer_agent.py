from pydantic import BaseModel
from typing import List
import json
from llm.ollama_client import call_ollama
from observability.langfuse_logger import logger


class Task(BaseModel):
    task: str
    estimated_time: int  # minutes
    importance: int
    urgency: int


class AnalyzerOutput(BaseModel):
    tasks: List[Task]


def analyze_tasks(user_input: str) -> AnalyzerOutput:
    # ---------- HARD GUARDED PRE-PARSER ----------
    raw = user_input.replace("\n", ",")
    parts = [p.strip() for p in raw.split(",") if p.strip()]

    # If user clearly listed tasks, trust user > LLM
    if len(parts) >= 1:
        tasks = []
        for p in parts:
            tasks.append({
                "task": p,
                "estimated_time": 30,
                "importance": 3,
                "urgency": 3
            })

        data = {"tasks": tasks}

        logger.log_agent_call(
            agent_name="AnalyzerAgent",
            input_data={"user_input": user_input},
            output_data=data
        )

        return AnalyzerOutput(**data)

    # ---------- FALLBACK TO LLM ONLY IF NEEDED ----------
    prompt = f"""
Extract tasks ONLY from the user's input.
Return STRICT JSON like:
{{"tasks":[{{"task":"", "estimated_time":30, "importance":3, "urgency":3}}]}}

User input:
{user_input}
"""

    response = call_ollama(prompt)

    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        data = {"tasks": []}

    logger.log_agent_call(
        agent_name="AnalyzerAgent",
        input_data={"user_input": user_input},
        output_data=data
    )

    return AnalyzerOutput(**data)