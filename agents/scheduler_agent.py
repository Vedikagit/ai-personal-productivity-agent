from pydantic import BaseModel  
from typing import List  
import re  
import datetime  

# Mock calendar to store scheduled tasks
MOCK_CALENDAR: List[dict] = []

class ScheduleOutput(BaseModel):  
    scheduled_task: str  
    start_time: str  
    end_time: str  
    reasoning: str  

def schedule_task(user_input: str, default_duration=120) -> ScheduleOutput:  
    """
    Mock scheduler:
    - Extract duration from user input if present
    - Extract time hint (e.g., after lunch -> 14:00)
    - Avoid conflicts with mock calendar
    """
    # Duration extraction
    duration_match = re.search(r'(\d+)\s*(hour|hr|minute|min)', user_input.lower())  
    if duration_match:  
        value, unit = duration_match.groups()  
        duration = int(value) * (60 if 'hour' in unit else 1)  
    else:  
        duration = default_duration  

    # Time hint (demo purposes)
    start_time = "14:00" if "after lunch" in user_input.lower() else "09:00"  
    start_dt = datetime.datetime.strptime(start_time, "%H:%M")  

    # Check mock calendar for conflicts
    conflict_found = True
    attempts = 0
    while conflict_found and attempts < 10:
        conflict_found = False
        end_dt = start_dt + datetime.timedelta(minutes=duration)
        for event in MOCK_CALENDAR:
            ev_start = datetime.datetime.strptime(event['start_time'], "%H:%M")
            ev_end = datetime.datetime.strptime(event['end_time'], "%H:%M")
            if (start_dt < ev_end and end_dt > ev_start):
                # Conflict found, push start time by 30 minutes
                start_dt += datetime.timedelta(minutes=30)
                conflict_found = True
                break
        attempts += 1

    # Add scheduled task to mock calendar
    MOCK_CALENDAR.append({
        "task": user_input,
        "start_time": start_dt.strftime("%H:%M"),
        "end_time": end_dt.strftime("%H:%M")
    })

    reasoning = f"Scheduled at {start_dt.strftime('%H:%M')} for {duration} mins, avoiding conflicts in mock calendar."

    return ScheduleOutput(  
        scheduled_task=user_input,  
        start_time=start_dt.strftime("%H:%M"),  
        end_time=end_dt.strftime("%H:%M"),  
        reasoning=reasoning  
    )