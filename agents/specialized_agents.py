import google.generativeai as genai
import os
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# llm = genai.GenerativeModel("gemini-1.5-flash")
llm = LLM(model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"), verbose=True)
AGENTS = {
    "ai": Agent(
        name="AI Trends Expert",
        role="AI Tech Explainer",
        goal="Explain and summarize AI-related news.",
        backstory="Specializes in tracking and simplifying AI trends for the general audience.",
        llm=llm,
        memory=True,
        verbose=False
    ),
    "fitness": Agent(
        name="Health Coach",
        role="Fitness Expert",
        goal="Deliver engaging fitness and health content.",
        backstory="A virtual trainer who loves giving summer fitness hacks and lifestyle advice.",
        llm=llm,
        memory=True,
        verbose=False
    ),
    "quantum": Agent(
        name="Quantum Educator",
        role="Quantum Tech Explainer",
        goal="Make quantum computing easy for students and educators.",
        backstory="Helps make complex quantum topics accessible to all.",
        llm=llm,
        memory=True,
        verbose=False
    ),
    "tech": Agent(
        name="Tech Reviewer",
        role="Gadget Analyst",
        goal="Present top tech gadgets in a fun and informative way.",
        backstory="A gadget nerd who reviews the latest devices and makes comparisons.",
        llm=llm,
        memory=True,
        verbose=False
    )
}

default_agent = Agent(
    name="Default Content Creator",
    role="Content Generalist",
    goal="Generate engaging YouTube content on any theme.",
    backstory="A versatile content writer who adapts to any niche on the fly.",
    llm=llm,
    memory=True,
    verbose=False
)

def get_agent_by_theme(theme):
    theme = theme.lower()
    if "ai" in theme:
        return AGENTS["ai"]
    elif "fitness" in theme or "health" in theme:
        return AGENTS["fitness"]
    elif "quantum" in theme:
        return AGENTS["quantum"]
    elif "tech" in theme or "gadget" in theme:
        return AGENTS["tech"]
    else:
        return default_agent
