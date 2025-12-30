# ai-personal-productivity-agent
🧠 AI Personal Productivity Agent
An agentic AI productivity assistant that helps users decide what to do right now or schedule tasks intelligently, based strictly on user input, energy level, and available time — with transparent agent reasoning and observability.
Built for fast-paced environments like hackathons where decision clarity > fancy UI.
🚀 What This Project Does
This app acts as a thinking productivity partner, not just a chatbot.
It:
Understands user intent (decide vs schedule)
Extracts tasks only from user input (no hallucination)
Chooses the best task to work on right now
Explains why that task was chosen
Shows agent execution status for trust
Logs all agent behavior using Langfuse observability
🧩 Core Features
1️⃣ Intent Detection
Routes user input into:
Decision Mode → “What should I do now?”
Scheduling Mode → “Schedule a 2-hour coding session after lunch”
2️⃣ Analyzer Agent (Strict, Guarded)
Extracts tasks from user input
Does NOT invent tasks
Accepts:
comma-separated tasks
newline-separated tasks
Falls back to LLM only if needed
Outputs structured, typed task data
3️⃣ Decision Agent (No Hallucination)
Chooses only from provided tasks
Never suggests breaks, rest, or unrelated actions
Adapts choice based on:
energy level
time available
importance & urgency
Always returns:
chosen task
reasoning
confidence
estimated time
alternative task
4️⃣ Agent Execution Transparency
Users can see:
Whether each agent completed successfully
Clear status indicators for trust and explainability
This mimics real-world agent orchestration systems.
5️⃣ Observability with Langfuse
Every agent call is logged with:
Input
Output
Agent name
This enables:
Debugging
Evaluation
Future optimization
🖥️ Tech Stack
Python
Streamlit – UI
Ollama – Local LLM inference
Pydantic – Typed agent outputs
Langfuse – AI observability
Modular Agent Architecture
ai-personal-productivity-agent/
│
├── app.py
├── agents/
│   ├── analyzer_agent.py
│   ├── decision_agent.py
│   ├── scheduler_agent.py
│
├── router/
│   └── intent_router.py
│
├── llm/
│   └── ollama_client.py
│
├── observability/
│   └── langfuse_logger.py
│
└── README.md

▶️ How to Run Locally
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
Make sure Ollama is running locally.


🎯 Why This Project Matters
Most productivity apps:
Give generic advice
Hallucinate tasks
Hide reasoning

This project:
Respects user intent
Shows agent thinking
Enforces strict task boundaries
Prioritizes correctness over fluff
It’s designed as a foundation for serious agentic systems, not just a demo chatbot.

🔮 Future Improvements:
Calendar API integration
Long-term memory & reflections
Multi-day planning
User profiles
Performance analytics via Langfuse traces


👤 Author
Vedika