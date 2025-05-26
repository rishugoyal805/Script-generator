import os
import asyncio
import time
from agents.trend_fetcher import fetch_trending_data
from agents.specialized_agents import generate_task_for_theme
from utils.helpers import save_output

async def main():
    start_time = time.perf_counter()
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

        trend_crews = [generate_task_for_theme(trend) for trend in trends[:1]]
        trend_tasks = [crew.kickoff_async() for crew in trend_crews]
        trend_results = await asyncio.gather(*trend_tasks)

        for i, (trend, result) in enumerate(zip(trends[:1], trend_results)):
            content += f"\n--- INDIVIDUAL TREND #{i+1}: {trend} ---\n"
            content += "SHORT SCRIPT:\n" + result.raw + "\n"

        # Print and save the content
        print(content)
        file_name = f"outputs/themes/{theme.replace(' ', '_').lower()}.txt"
        save_output(file_name, content)
        end_time = time.perf_counter()  # ⏱️ End timer
        total_time = end_time - start_time
        print(f"\n✅ Total execution time: {total_time:.2f} seconds")

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