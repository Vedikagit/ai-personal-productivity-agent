from pydantic import BaseModel
from typing import List
import json
from llm.ollama_client import call_ollama
from observability.langfuse_logger import logger


class DecisionOutput(BaseModel):
    chosen_task: str
    reason: str
    confidence: float
    estimated_time: int
    alternative_task: str


def decide_task(tasks: List[dict], energy: str, time_available: int) -> DecisionOutput:
    # ---------- GUARD: stop execution if analyzer failed ----------
    if not tasks or len(tasks) == 0:
        logger.log_agent_call(
            agent_name="DecisionAgent",
            input_data={
                "tasks": tasks,
                "energy": energy,
                "time_available": time_available
            },
            output_data={
                "error": "No valid tasks received from AnalyzerAgent"
            }
        )
        raise ValueError("No valid tasks received from AnalyzerAgent")

    prompt = f"""
You are a strict productivity decision agent.

CRITICAL RULES:
- You MUST choose ONLY from the provided tasks.
- You are NOT allowed to suggest rest, breaks, meditation, or new tasks.
- You are NOT allowed to invent tasks not in the list.
- Even if energy is low, choose the LIGHTEST task from the list.
- Do NOT mention messages, emails, or recovery unless they exist in tasks.

Tasks (ONLY THESE ARE ALLOWED):
{tasks}

User energy: {energy}
Available time (minutes): {time_available}

Decision logic:
- Prefer tasks that fit within available time
- Prefer lower effort if energy is low
- Still prioritize importance and urgency

Return STRICT JSON with EXACT keys:
chosen_task (string, must match one task),
reason (conversational, 2–3 lines),
confidence (float 0–1),
estimated_time (int minutes),
alternative_task (must also be from list)

NO extra text.
"""

    response = call_ollama(prompt)

    # ---------- Safe JSON parsing ----------
    try:
        data = json.loads(response)
    except json.JSONDecodeError:
        print("LLM response was not valid JSON:")
        print(response)
        data = {
            "chosen_task": "",
            "reason": "",
            "confidence": 0.0,
            "estimated_time": 0,
            "alternative_task": ""
        }

    # ---------- Langfuse logging ----------
    logger.log_agent_call(
        agent_name="DecisionAgent",
        input_data={
            "tasks": tasks,
            "energy": energy,
            "time_available": time_available
        },
        output_data=data
    )

    return DecisionOutput(**data)