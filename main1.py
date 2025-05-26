import os
import asyncio
import time
from agents.specialized_agents1 import generate_task_for_theme
from agents.feature_finder import generate_feature_task
from utils.helpers import save_output

async def main():
    start_time = time.perf_counter()
    theme = "time"

    os.makedirs("outputs/themes", exist_ok=True)
    # Add theme and trends info
    content = f"\n== THEME: {theme} ==\n\n"
    # Generate script using the theme (aggregated)
    crew = generate_feature_task(theme)
    result = await crew.kickoff_async()
    content += "--- BASED ON ALL TRENDS ---\n"
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
