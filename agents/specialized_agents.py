from crewai import Agent, Task, Crew, LLM
from crewai import Agent, Task, Crew
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(model="gemini/gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"), verbose=True)

ai_agent = Agent(
    name="AI Trends Expert",
    role="AI Tech Explainer",
    goal="Explain and summarize AI-related news.",
    backstory="Specializes in tracking and simplifying AI trends for the general audience.",
    llm=llm,
    memory=True,
    verbose=False
)

ai_description = (
    "Write a compelling, human-sounding YouTube Shorts script (max 60 seconds) on the theme of AI. "
    "Hook the viewer with a futuristic or surprising fact, keep it concise, and explain one clear insight. "
    "Format the script using clearly labeled timestamps (e.g., (0-4 sec), (4-12 sec), etc.) so that the pacing is natural and well-balanced across the 60 seconds."
)

ai_output = "A timestamped 60-second YouTube script explaining an AI trend with custom intervals."

fitness_agent = Agent(
    name="Health Coach",
    role="Fitness Expert",
    goal="Deliver engaging fitness and health content.",
    backstory="A virtual trainer who loves giving summer fitness hacks and lifestyle advice.",
    llm=llm,
    memory=True,
    verbose=False
)

fitness_description = (
    "Create a fun, engaging 60-second YouTube Shorts script that shares a quick summer fitness tip or hack. "
    "It should be energetic, motivating, and easy to follow. "
    "Use a timestamp format like (0-3 sec), (3-10 sec), etc., and divide the script into well-paced time intervals that fit within 60 seconds."
)

fitness_output = "A timestamped 60-second script promoting fitness hacks for summer with custom intervals."

quantum_agent = Agent(
    name="Quantum Educator",
    role="Quantum Tech Explainer",
    goal="Make quantum computing easy for students and educators.",
    backstory="Helps make complex quantum topics accessible to all.",
    llm=llm,
    memory=True,
    verbose=False
)

quantum_description = (
    "Write a simplified, engaging YouTube Shorts script (max 60 seconds) that explains a core quantum computing concept. "
    "Use a relatable analogy or scenario to help the audience understand quickly. "
    "Break the script using timestamp labels like (0-5 sec), (5-14 sec), etc., with the interval lengths decided naturally to match the script pacing."
)

quantum_output = "A clear and fun timestamped 60-second script on quantum computing with natural intervals."

tech_agent = Agent(
    name="Tech Reviewer",
    role="Gadget Analyst",
    goal="Present top tech gadgets in a fun and informative way.",
    backstory="A gadget nerd who reviews the latest devices and makes comparisons.",
    llm=llm,
    memory=True,
    verbose=False
)

tech_description = (
    "Generate a 60-second YouTube Shorts script reviewing a trending tech gadget. "
    "Make it fun, comparison-rich, and highlight unique features. "
    "Include timestamps like (0-6 sec), (6-15 sec), etc., but let the time intervals be flexible based on the natural flow of the script. "
    "Ensure it fits within 60 seconds in total."
)

tech_output = "An engaging, timestamped 60-second gadget review script with flexible pacing."

default_agent = Agent(
    name="Default Content Creator",
    role="Content Generalist",
    goal="Generate engaging YouTube content on any theme.",
    backstory="A versatile content writer who adapts to any niche on the fly.",
    llm=llm,
    memory=True,
    verbose=False
)

default_description = (
    "Write a concise and engaging 60-second YouTube Shorts script based on the provided theme. "
    "Include timestamps like (start sec - end sec) for each part of the script. "
    "Decide the intervals yourself to ensure smooth pacing and clarity across the 60-second video."
)

default_output = "A well-structured timestamped 60-second content script suitable for YouTube Shorts."


# --- Agents setup ---
# ai_agent = Agent(
#     name="AI Trends Expert",
#     role="AI Tech Explainer",
#     goal="Explain and summarize AI-related news.",
#     backstory="Specializes in tracking and simplifying AI trends for the general audience.",
#     llm=llm,
#     memory=True,
#     verbose=False
# )

# ai_description = (
#     "Write a compelling, human-sounding YouTube Shorts script (max 60 seconds) on the theme of AI. "
#     "Hook the viewer with a futuristic or surprising fact, keep it concise, and explain one clear insight."
# )

# ai_output = "A snappy, 60-second YouTube script explaining an AI trend."

# fitness_agent = Agent(
#     name="Health Coach",
#     role="Fitness Expert",
#     goal="Deliver engaging fitness and health content.",
#     backstory="A virtual trainer who loves giving summer fitness hacks and lifestyle advice.",
#     llm=llm,
#     memory=True,
#     verbose=False
# )

# fitness_description = (
#     "Create a fun, engaging 60-second YouTube Shorts script that shares a quick summer fitness tip or hack. "
#     "It should be energetic, motivating, and easy to follow."
# )

# fitness_output = "A motivating 60-second script promoting fitness hacks for summer."

# quantum_agent = Agent(
#     name="Quantum Educator",
#     role="Quantum Tech Explainer",
#     goal="Make quantum computing easy for students and educators.",
#     backstory="Helps make complex quantum topics accessible to all.",
#     llm=llm,
#     memory=True,
#     verbose=False
# )

# quantum_description = (
#     "Write a simplified, engaging YouTube Shorts script (max 60 seconds) that explains a core quantum computing concept. "
#     "Use a relatable analogy or scenario to help the audience understand quickly."
# )

# quantum_output = "A 60-second script that makes a quantum computing idea fun and clear."

# tech_agent = Agent(
#     name="Tech Reviewer",
#     role="Gadget Analyst",
#     goal="Present top tech gadgets in a fun and informative way.",
#     backstory="A gadget nerd who reviews the latest devices and makes comparisons.",
#     llm=llm,
#     memory=True,
#     verbose=False
# )

# tech_description = (
#     "Generate a 60-second YouTube Shorts script reviewing a trending tech gadget. "
#     "Make it fun, comparison-rich, and highlight unique features."
# )

# tech_output = "An engaging, quick gadget review script suitable for Shorts."

# default_agent = Agent(
#     name="Default Content Creator",
#     role="Content Generalist",
#     goal="Generate engaging YouTube content on any theme.",
#     backstory="A versatile content writer who adapts to any niche on the fly.",
#     llm=llm,
#     memory=True,
#     verbose=False
# )

# default_description = (
#     "Write a concise and engaging 60-second YouTube Shorts script based on the provided theme. "
#     "Focus on clarity, tone, and one strong insight."
# )

# default_output = "A general 60-second content script fit for a YouTube Short."

# --- Function to generate task ---
def generate_task_for_theme(theme):
    theme_lower = theme.lower()

    if any(kw in theme_lower for kw in ["ai", "artificial intelligence", "machine learning"]):
        agent = ai_agent
        description = ai_description
        expected_output = ai_output
    elif any(kw in theme_lower for kw in ["fitness", "health", "workout", "summer"]):
        agent = fitness_agent
        description = fitness_description
        expected_output = fitness_output
    elif any(kw in theme_lower for kw in ["quantum", "computing", "physics"]):
        agent = quantum_agent
        description = quantum_description
        expected_output = quantum_output
    elif any(kw in theme_lower for kw in ["tech", "gadget", "devices"]):
        agent = tech_agent
        description = tech_description
        expected_output = tech_output
    else:
        agent = default_agent
        description = default_description
        expected_output = default_output

    current_task = Task(description=description, agent=agent, expected_output=expected_output)
    crew = Crew(agents=[agent], tasks=[current_task])
    return crew


# import google.generativeai as genai
# import os
# from crewai import Agent, Task, Crew, LLM
# from dotenv import load_dotenv

# load_dotenv()
# llm = LLM(model="gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"), verbose=True)
# ai_agent = Agent(
#         name="AI Trends Expert",
#         role="AI Tech Explainer",
#         goal="Explain and summarize AI-related news.",
#         backstory="Specializes in tracking and simplifying AI trends for the general audience.",
#         llm=llm,
#         memory=True,
#         verbose=False
# )

# fitness_agent = Agent(
#         name="Health Coach",
#         role="Fitness Expert",
#         goal="Deliver engaging fitness and health content.",
#         backstory="A virtual trainer who loves giving summer fitness hacks and lifestyle advice.",
#         llm=llm,
#         memory=True,
#         verbose=False
#     )

# quantum_agent = Agent(
#         name="Quantum Educator",
#         role="Quantum Tech Explainer",
#         goal="Make quantum computing easy for students and educators.",
#         backstory="Helps make complex quantum topics accessible to all.",
#         llm=llm,
#         memory=True,
#         verbose=False
#     )

# tech_agent = Agent(
#         name="Tech Reviewer",
#         role="Gadget Analyst",
#         goal="Present top tech gadgets in a fun and informative way.",
#         backstory="A gadget nerd who reviews the latest devices and makes comparisons.",
#         llm=llm,
#         memory=True,
#         verbose=False
#     )

# default_agent = Agent(
#     name="Default Content Creator",
#     role="Content Generalist",
#     goal="Generate engaging YouTube content on any theme.",
#     backstory="A versatile content writer who adapts to any niche on the fly.",
#     llm=llm,
#     memory=True,
#     verbose=False
# )

# def generate_task_for_theme(theme):
#     theme_lower = theme.lower()

#     if any(kw in theme_lower for kw in ["ai", "artificial intelligence", "machine learning"]):
#         agent = ai_agent
#         description = f"Generate content about AI trends and news for theme: {theme}"
#         expected_output = "Engaging AI-related video content."

#     elif any(kw in theme_lower for kw in ["fitness", "health", "workout", "summer"]):
#         agent = fitness_agent
#         description = f"Generate summer fitness hacks and lifestyle tips for theme: {theme}"
#         expected_output = "Engaging and healthy fitness content."

#     elif any(kw in theme_lower for kw in ["quantum", "computing", "physics"]):
#         agent = quantum_agent
#         description = f"Generate a simplified explanation of quantum computing in education for theme: {theme}"
#         expected_output = "Educational content on quantum computing."

#     elif any(kw in theme_lower for kw in ["tech", "gadget", "devices"]):
#         agent = tech_agent
#         description = f"Generate a review script for trending tech gadgets for theme: {theme}"
#         expected_output = "Informative gadget review content."

#     else:
#         agent = default_agent
#         description = f"Generate general content for theme: {theme}"
#         expected_output = "Creative and adaptable content."

#     current_task = Task(description=description, agent=agent, expected_output=expected_output)
#     crew = Crew(agents=[agent], tasks=[current_task])
#     return crew


# # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# # llm = genai.GenerativeModel("gemini-1.5-flash")


# # AGENTS = {
# #     "ai": Agent(
# #         name="AI Trends Expert",
# #         role="AI Tech Explainer",
# #         goal="Explain and summarize AI-related news.",
# #         backstory="Specializes in tracking and simplifying AI trends for the general audience.",
# #         llm=llm,
# #         memory=True,
# #         verbose=False
# #     ),
# #     "fitness": Agent(
# #         name="Health Coach",
# #         role="Fitness Expert",
# #         goal="Deliver engaging fitness and health content.",
# #         backstory="A virtual trainer who loves giving summer fitness hacks and lifestyle advice.",
# #         llm=llm,
# #         memory=True,
# #         verbose=False
# #     ),
# #     "quantum": Agent(
# #         name="Quantum Educator",
# #         role="Quantum Tech Explainer",
# #         goal="Make quantum computing easy for students and educators.",
# #         backstory="Helps make complex quantum topics accessible to all.",
# #         llm=llm,
# #         memory=True,
# #         verbose=False
# #     ),
# #     "tech": Agent(
# #         name="Tech Reviewer",
# #         role="Gadget Analyst",
# #         goal="Present top tech gadgets in a fun and informative way.",
# #         backstory="A gadget nerd who reviews the latest devices and makes comparisons.",
# #         llm=llm,
# #         memory=True,
# #         verbose=False
# #     )
# # }