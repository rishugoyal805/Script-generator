from crewai import Agent, Task, Crew, LLM
import os
from dotenv import load_dotenv

load_dotenv()

# 🔑 Load Gemini LLM
llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    verbose=True
)

# 🧠 Function to create an agent dynamically based on topic
def create_feature_agent(topic: str):
    return Agent(
        name="Feature Finder",
        role=f"Specialist in {topic}",
        goal=f"Identify all the necessary key features of {topic} and list only their names.",
        backstory=f"A tool analysis expert who focuses on extracting the most used or talked-about features of {topic}, helping beginners get an overview.",
        llm=llm,
        memory=True,
        verbose=False
    )

# 📝 Static task prompt template (customized with topic)
feature_description_template = (
    "You are given a topic: '{topic}'.\n"
    "Your task is to extract only the names of the top all useful or popular features of that tool/platform.\n"
    "Return a clean Python list of strings — only feature names, no extra description or explanation.\n"
    "Example Output:\n['Pull Requests', 'GitHub Actions', 'Code Review', 'GitHub Pages', 'Issue Tracking']"
)

# 🎯 Expected output
feature_output = "A Python list of all strings, each string being the name of one useful/popular feature."

# 🚀 Function to generate a crew based on topic
def generate_feature_task(topic: str):
    agent = create_feature_agent(topic)
    task_description = feature_description_template.format(topic=topic)

    task = Task(
        description=task_description,
        agent=agent,
        expected_output=feature_output
    )

    crew = Crew(agents=[agent], tasks=[task])
    return crew

# ✅ Optional: Run directly for testing
# if __name__ == "__main__":
#     topic = "GitHub"
#     crew = generate_feature_task(topic)
#     result = crew.run()
#     print("\n🔍 Feature Names for:", topic)
#     print(result)
