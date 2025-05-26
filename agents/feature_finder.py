# feature_finder_agent.py

from crewai import Agent, Task, Crew, LLM
import os
from dotenv import load_dotenv

load_dotenv()

# 🔑 Load LLM using Gemini Flash
llm = LLM(model="gemini/gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"), verbose=True)

# 🧠 Agent to find features of a given tool/platform/topic
feature_agent = Agent(
    name="Feature Finder",
    role="Tool Features Specialist",
    goal="Identify and explain the top features of any technical tool in a simple and helpful way.",
    backstory="An expert product explorer who breaks down complex tools into digestible highlights that even beginners can follow.",
    llm=llm,
    memory=True,
    verbose=False
)

# 📝 Task description (flexible for different tech topics)
feature_description = (
    "You are given a tech topic or tool name (e.g., GitHub, ChatGPT, VS Code, Canva, etc.). "
    "Your job is to identify 5 to 7 cool, useful, or popular features of that tool. "
    "Keep the language simple and beginner-friendly. No code or jargon unless explained in plain terms. "
    "Return output as a clean Python list of strings — each describing one feature clearly."
)

# ✅ Expected output format
feature_output = (
    "A Python list of 5 to 7 strings, where each string describes one useful/popular feature of the given topic."
)

# --- Function to generate a task using the agent ---
def generate_feature_task(topic: str):
    formatted_description = feature_description + f"\n\nTopic: {topic}"
    task = Task(description=formatted_description, agent=feature_agent, expected_output=feature_output)

    crew = Crew(agents=[feature_agent], tasks=[task])
    return crew