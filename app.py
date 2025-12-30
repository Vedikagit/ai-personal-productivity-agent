import streamlit as st
from router.intent_router import detect_intent, IntentType
from agents.analyzer_agent import analyze_tasks
from agents.decision_agent import decide_task
from agents.scheduler_agent import schedule_task
from agents.reflection_agent import agent_introspect


st.set_page_config(page_title="AI Personal Productivity Agent", layout="centered")
st.title("🧠 AI Personal Productivity Agent")

# -------------------- INPUT --------------------
user_input = st.text_area(
    "Tell me what you want to do or schedule:",
    height=150
)

energy = st.selectbox("Energy Level", ["low", "medium", "high"])
time_available = st.number_input("Available time (minutes)", min_value=15, value=60)

# -------------------- PROCESS BUTTON --------------------
if st.button("Process Request"):
    if not user_input.strip():
        st.warning("Please enter a request.")
    else:
        intent = detect_intent(user_input)
        st.session_state["intent"] = intent
        st.session_state["user_input"] = user_input
        st.session_state["energy"] = energy
        st.session_state["time_available"] = time_available

# -------------------- EXECUTION --------------------
if "intent" in st.session_state:

    intent = st.session_state["intent"]

    with st.spinner("Agent is reasoning..."):

        # -------------------- DECISION AGENT --------------------
        if intent == IntentType.DECISION:
            st.subheader("🧠 Task Prioritization Result")

            analysis = analyze_tasks(st.session_state["user_input"])
            analyzer_status = agent_introspect(
                "Analyzer Agent",
                output_done=bool(analysis and analysis.tasks)
            )

            try:
                decision = decide_task(
                    [t.dict() for t in analysis.tasks],
                    st.session_state["energy"],
                    st.session_state["time_available"]
                )
            except ValueError as e:
                st.error("❌ No valid tasks found in your input.")
                st.info("Try explicitly listing tasks like:\n- finish homework\n- clean room\n- reply to emails")
                st.stop()
            
            decision_status = agent_introspect(
                "Decision Agent",
                output_done=bool(decision and decision.chosen_task)
            )

            # --- SHOW AGENT STEPS ---
            st.markdown("### 🤖 Agent Execution Status")
            st.code(f"{analyzer_status}\n{decision_status}")

            st.success("✅ What you should do right now")

            st.markdown(
                f"""
**👉 Start with:** {decision.chosen_task}

**Why this?**  
{decision.reason}

⏱ Estimated time: **{decision.estimated_time} min**  
🔁 Backup option: **{decision.alternative_task}**  
📊 Confidence: **{int(decision.confidence * 100)}%**
"""
            )

        # -------------------- SCHEDULING AGENT --------------------
        elif intent == IntentType.SCHEDULING:
            st.subheader("📅 Scheduled Successfully")

            schedule = schedule_task(st.session_state["user_input"])

            st.markdown(
                f"""
### 🗓️ Task Scheduled

**Task:** {schedule.scheduled_task}  
⏰ **Time:** {schedule.start_time} – {schedule.end_time}

**Why this works:**  
{schedule.reasoning}
"""
            )

        # -------------------- UNKNOWN --------------------
        else:
            st.warning(
                "I couldn't understand your request.\n\n"
                "Try:\n"
                "- 'What should I do now?'\n"
                "- 'Schedule a 2-hour coding session after lunch'"
            )

    st.write("🧠 Detected Intent:", intent)