# ai-personal-productivity-agent
*🧠 AI Personal Productivity Agent*
<br>
An agentic AI productivity assistant that helps users decide what to do right now or schedule tasks intelligently, based strictly on user input, energy level, and available time — with transparent agent reasoning and observability.
<br><br>
## The Problem I faced
I was overwhelmed. Maths assignment, DSA practise, notes revision, coding project and a million small tasks. Every productivity app just gave me *more* to look at longer lists, more categories, more overwhelm.

**What I actually needed:**
<br>
Someone to tell  me: *"Do THIS. Right now. Here's why."*

## The Solution

A multi-agent AI system that:
<br>
Understands user intent (decide vs schedule)
<br>
Extracts tasks only from user input
<br>Chooses the best task to work on right now
<br>Explains why that task was chosen
<br>Shows agent execution status for trust

🧩 Core Features
<br><br>1️⃣ Intent Detection
<br>Routes user input into:
<br>Decision Mode → “What should I do now?”
<br>Scheduling Mode → “Schedule a 2-hour coding session after lunch”
<br><br>2️⃣ Analyzer Agent (Strict, Guarded)
<br>Extracts tasks from user input
<br>Accepts:
<br>comma-separated tasks
<br>newline-separated tasks
<br>Falls back to LLM only if needed
<br>Outputs structured, typed task data
<br><br>3️⃣ Decision Agent
<br>Chooses only from provided tasks
<br>Adapts choice based on:
<br>energy level
<br>time available
<br>importance & urgency
<br>Always returns:
<br>chosen task
<br>reasoning
<br>confidence
<br>estimated time
<br>alternative task
<br><br>4️⃣ Agent Execution Transparency
<br>Users can see:
<br>Whether each agent completed successfully
<br>Clear status indicators for trust and explainability
<br>This mimics real-world agent orchestration systems.

🖥️ Tech Stack

Python<br>
Streamlit – UI<br>
Ollama – Local LLM inference<br>
Pydantic – Typed agent outputs<br>
MCP-compatible architecture – Observability<br>
(Langfuse integration planned)<br>
Modular Agent Architecture<br>
<br><br>
▶️ How to Run Locally
# Install Ollama

# Pull the model
ollama pull llama3.1:8b

# Clone and setup

# Create virtual environment
python -m venv venv<br>
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
<br>Make sure Ollama is running locally.

<br>
🎯 Why This Project Matters
<br>Most productivity apps:
<br>Shows you all tasks
<br>Give generic advice
<br>Static Lists
<br>Hide reasoning

<br>This project:
<br>Shows ONE task
<br>Personalised to YOUR energy
<br>Respects user intent
<br>Shows agent thinking

<br>🔮 Future Improvements:
<br>Calendar API integration
<br>Long-term memory & reflections
<br>Learn from completion patterns
<br>Multi-day planning
<br>User profiles
<br>Performance analytics & agent tracing

**License**
<br>MIT

**Built with ❤️**
<br>For the Amulate 2025 Hackathon

👤 Author
<br>Vedika
