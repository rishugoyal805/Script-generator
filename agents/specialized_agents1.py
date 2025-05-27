from crewai import Agent, Task, Crew, LLM
import os
from dotenv import load_dotenv

# 📦 Load environment variables
load_dotenv()

# 🔑 Load Gemini LLM
llm = LLM(
    model="gemini/gemini-1.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    verbose=True
)

# ✨ Updated Hinglish + 2-Friend Style
delhi_youth_convo_style = (
    "Tu ek YouTube Shorts style script likh raha hai (max 90 sec) jisme do dost (Aman aur Sid) casually baat kar rahe hain ek tech feature ke baare mein.\n\n"
    "🗣️ Tone: Chill Delhi-NCR college student banter. Thoda roasting, thoda sarcasm, full comedy.\n"
    "💬 Format: Pure conversation (no narration), jaise 2 doston ka casual chat ho raha ho canteen ya hostel me.\n"
    "🎭 Add expressions like 'bhai', 'arey ruk na', 'sach me?', 'scene kya hai', 'ohh bhai! ye toh mast chiz hai', 'Maza aa gya broo', 'thoda detail mai bta na bhai' etc.\n"
    "💡 Use simple language and avoid jargon. Explain complex terms with relatable examples.\n"
    "🤣 Include relatable examples, desi analogies (food, Bollywood, college life), and meme-style lines.\n"
    "📹 Break script into timestamped segments: (0-5 sec), (5-15 sec), ... up to 60 sec.\n"       #Chnaging this to 60 ,90 is too long
    "🚫 No technical lecture, just explain the feature through conversation in Hinglish (Roman Hindi + English)."
)

# 🤖 Feature Agent
feature_agent = Agent(
    name="Feature Explainer",
    role="Tech Bakchod",
    goal="Explain one tech feature through a fun, realistic Delhi-style Hinglish conversation between 2 friends.",
    backstory="Aman and Sid are engineering students who love to explain tech to each other using jokes, food references, and savage humor.",
    llm=llm,
    memory=True,
    verbose=False
)

# 📝 Dynamic task generator for any feature
def generate_task_for_theme(topic: str, feature: str = None):
    description = (
        f"{delhi_youth_convo_style}\n\n"
        f"Topic: {topic}\n"
        f"Feature: {feature}\n\n"
        f"Make sure both friends contribute almost equally. the one who explains should be more detailed and can take more time. Make it funny, fast-paced, and use realistic youth lingo.\n"
        f"End with a savage or funny outro line. No boring explanations. No code."
    )

    expected_output = (
        "A Hinglish YouTube Shorts script with timestamped segments like:\n"
        "(0-5 sec): Sid: Bhai tu GitHub pe Pull Request ka funda samjha...\n"
        "(5-15 sec): Aman: Arey bhai, woh basically teamwork wala scene hai...\n"
        "...up to 60 seconds total."
    )

    task = Task(description=description, agent=feature_agent, expected_output=expected_output)

    crew = Crew(agents=[feature_agent], tasks=[task])
    return crew

# from crewai import Agent, Task, Crew, LLM
# from crewai import Agent, Task, Crew
# import os
# from dotenv import load_dotenv

# load_dotenv()

# llm = LLM(model="gemini/gemini-1.5-flash", api_key=os.getenv("GEMINI_API_KEY"), verbose=True)

# # ✨ Hinglish Script Style Instructions
# hinglish_style_instructions = (
#     "✨ Use Hinglish (casual spoken Hindi + English in Roman script).\n"
#     "🗣️ Tone: Fun, witty, youthful — jaise tu apne dost ko explain kar raha ho.\n"
#     "🤣 Add thoda humor, thoda meme energy — relatable hona chahiye.\n"
#     "✅ Avoid boring technical language — explain simple terms with analogies or desi references.\n"
#     "🎯 Use a timestamp format: (0-4 sec), (4-12 sec), etc., and make sure it all fits within 60 seconds.\n"
#     "📢 Keep energy high and flow engaging!"
# )

# # 🤖 Updated AI Agent for Explaining Features in a Funny, Hinglish Way
# ai_agent = Agent(
#     name="AI Explainer",
#     role="Tech Simplifier with a Twist",
#     goal="Explain one feature or concept (from a topic like GitHub, ChatGPT, etc.) in an easy and funny Hinglish style.",
#     backstory="A chilled-out AI bro who loves breaking down tech terms into jokes and analogies, and explains it all like you're chatting with a friend.",
#     llm=llm,
#     memory=True,
#     verbose=False
# )

# ai_description = (
#     "Tu ek YouTube Shorts script banayega (max 60 sec) jisme tu kisi ek feature ya concept ko explain karega "
#     "from the topic passed (e.g., GitHub ka 'Fork' ya 'Pull Request', ChatGPT ka 'prompt', etc.).\n"
#     f"{hinglish_style_instructions}\n"
#     "Audience should be able to laugh AND learn. Use desi references, meme-style comedy, and real-life analogies."
# )

# ai_output = "A timestamped 60-second YouTube Shorts script explaining a single tech feature in Hinglish with humor, analogies, and easy terms."

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
#     "Make it fun, comparison-rich, and highlight unique features. "
#     "Include timestamps like (0-6 sec), (6-15 sec), etc., but let the time intervals be flexible based on the natural flow of the script. "
#     "Ensure it fits within 60 seconds in total."
# )

# tech_output = "An engaging, timestamped 60-second gadget review script with flexible pacing."

# # --- Function to generate task ---
# def generate_task_for_theme(theme, feature):
#     theme_lower = theme.lower()
#     feature_lower = feature.lower()

#     if any(kw in theme_lower for kw in ["ai", "artificial intelligence", "machine learning"]):
#         agent = ai_agent
#         description = ai_description
#         expected_output = ai_output
#     elif any(kw in theme_lower for kw in ["tech", "gadget", "devices"]):
#         agent = tech_agent
#         description = tech_description
#         expected_output = tech_output

#     current_task = Task(description=description, agent=agent, expected_output=expected_output)
#     crew = Crew(agents=[agent], tasks=[current_task])
#     return crew