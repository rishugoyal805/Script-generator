import os
import asyncio
from agents.trend_fetcher import fetch_trending_data
from agents.specialized_agents import generate_task_for_theme
from utils.helpers import save_output

async def main():
    themes = [
        "AI tools in 2025"
        # "Fitness hacks in summer",
        # "Quantum computing in education",
        # "Top 5 tech gadgets this year"
    ]

    os.makedirs("outputs/themes", exist_ok=True)

    for theme in themes:
        # Fetch trending data
        trends, all_trend_data = fetch_trending_data(theme)

        # Add theme and trends info
        content = f"\n== THEME: {theme} ==\n\n"
        content += f"TOP TRENDS:\n{all_trend_data}\n\n"

        # Generate script using the theme (aggregated)
        crew = generate_task_for_theme(theme)
        result = await crew.kickoff_async()
        content += "--- BASED ON ALL TRENDS ---\n"
        content += "SHORT SCRIPT:\n" + result.raw + "\n"

        # Generate content for each individual trend
        for i, trend in enumerate(trends):
            crew = generate_task_for_theme(trend)
            result = crew.kickoff()
            content += f"\n--- INDIVIDUAL TREND #{i+1}: {trend} ---\n"
            content += "SHORT SCRIPT:\n" + result.raw + "\n"

        # Print and save the content
        print(content)
        file_name = f"outputs/themes/{theme.replace(' ', '_').lower()}.txt"
        save_output(file_name, content)

if __name__ == "__main__":
    asyncio.run(main())

# import os
# import asyncio
# from agents.trend_fetcher import fetch_trending_data
# from agents.specialized_agents import generate_task_for_theme
# from agents.formatter import format_output
# from utils.helpers import load_themes, save_output

# async def main():
#     themes = [
#         "AI tools in 2025",
#         "Fitness hacks in summer",
#         "Quantum computing in education",
#         "Top 5 tech gadgets this year"
#     ]

#     os.makedirs("outputs/themes", exist_ok=True)

#     for theme in themes:
#         trends, all_trend_data = fetch_trending_data(theme)

#         content = f"\n== THEME: {theme} ==\n\n"
#         content += f"TOP TRENDS:\n{all_trend_data}\n\n"

#         # Generate content using the crew (one task per theme)
#         crew = generate_task_for_theme(theme)
#         result = await crew.kickoff_async()
#         content += "--- BASED ON ALL TRENDS ---\n"
#         content += "SHORT SCRIPT:\n" + result + "\n"

#         # One by one trend processing
#         for i, trend in enumerate(trends):
#             crew = generate_task_for_theme(trend)
#             result = await crew.kickoff_async()
#             content += f"\n--- INDIVIDUAL TREND #{i+1}: {trend} ---\n"
#             content += "SHORT SCRIPT:\n" + result + "\n"

#         print(content)

#         # Save to a file
#         file_name = f"outputs/themes/{theme.replace(' ', '_').lower()}.txt"
#         save_output(file_name, content)

# if __name__ == "__main__":
#     asyncio.run(main())