# import os
# import asyncio
# import time
# from agents.specialized_agents1 import generate_task_for_theme
# from agents.feature_finder import generate_feature_task
# from utils.helpers import save_output

# async def main():
#     start_time = time.perf_counter()
#     theme = input("Enter the theme for which you want to generate content: ").strip()
#     if not theme:  # Check if the theme is empty
#         print("❌ No theme provided. Please enter a valid theme.")
#         return
#     print(f"\n🔍 Generating content for theme: {theme}")

#     os.makedirs("outputs/themes", exist_ok=True)
#     content = f"\n== THEME: {theme} ==\n\n"

#     # Generate list of features from the theme
#     crew = generate_feature_task(theme)
#     result = await crew.kickoff_async()

#     print("\n📦 RAW result.raw content:", result.raw)  # <-- DEBUG LINE

#     # Try parsing the result.raw into a Python list
#     try:
#         if isinstance(result.raw, str) and result.raw.startswith("["):
#             import ast  
#             # ast stads for Abstract Syntax Trees, used for parsing Python expressions
#             # Use ast.literal_eval for safe evaluation of string representation of list
#             sub_topics = ast.literal_eval(result.raw)  # safe eval for list from string
#         elif isinstance(result.raw, list):
#             sub_topics = result.raw
#         else:
#             sub_topics = []
#     except Exception as e:
#         print(f"❌ Error parsing result.raw: {e}")
#         sub_topics = []

#     content += "--- BASED ON ALL TRENDS ---\n"
#     content += "FEATURES:\n" + (", ".join(sub_topics) if sub_topics else "[None extracted]") + "\n"

#     # if sub_topics:
#     #     for idx, sub in enumerate(sub_topics, start=1):
#     #         crew_sub = generate_task_for_theme(theme, sub)
#     #         result_sub = await crew_sub.kickoff_async()
#     #         content += f"\n--- TASK #{idx} for: {sub} ---\n"
#     #         content += "SHORT SCRIPT:\n" + result_sub.raw + "\n"
#     if sub_topics:
#         first_feature = sub_topics[0]
#         print(f"\n🔍 Debug: Generating content only for first feature: {first_feature}")
        
#         crew_sub = generate_task_for_theme(theme, first_feature)
#         result_sub = await crew_sub.kickoff_async()

#         content += f"\n--- TASK #1 for: {first_feature} ---\n"
#         content += "SHORT SCRIPT:\n" + result_sub.raw + "\n"
#     else:
#         content += "\n⚠️ No subtopics were extracted from the feature task.\n"

#     # Print and save the content
#     print(content)
#     file_name = f"outputs/themes/{theme.replace(' ', '_').lower()}.txt"
#     save_output(file_name, content)

#     end_time = time.perf_counter()
#     total_time = end_time - start_time
#     print(f"\n✅ Total execution time: {total_time:.2f} seconds")

# if __name__ == "__main__":
#     asyncio.run(main())

# app_core.py

import os
import ast
from agents.specialized_agents1 import generate_task_for_theme
from agents.feature_finder import generate_feature_task
from utils.helpers import save_output

os.makedirs("outputs/themes", exist_ok=True)

async def fetch_features_from_theme(theme: str) -> list:
    crew = generate_feature_task(theme)
    result = await crew.kickoff_async()

    print("\n📦 RAW result.raw content:", result.raw)  # Debug

    try:
        if isinstance(result.raw, str) and result.raw.startswith("["):
            sub_topics = ast.literal_eval(result.raw)
        elif isinstance(result.raw, list):
            sub_topics = result.raw
        else:
            sub_topics = []
    except Exception as e:
        print(f"❌ Error parsing result.raw: {e}")
        sub_topics = []

    return sub_topics

async def generate_content_from_topic(theme: str, feature: str) -> str:
    crew_sub = generate_task_for_theme(theme, feature)
    result_sub = await crew_sub.kickoff_async()
    
    content = f"\n--- TASK for: {feature} ---\n"
    content += "SHORT SCRIPT:\n" + result_sub.raw + "\n"

    file_name = f"outputs/themes/{theme.replace(' ', '_').lower()}__{feature.replace(' ', '_').lower()}.txt"
    save_output(file_name, content)

    return content
