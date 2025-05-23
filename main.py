from agents.trend_fetcher import fetch_trending_data
from agents.content_generator import generate_short_script, generate_long_script
from agents.formatter import format_output
from agents.specialized_agents import get_agent_by_theme
from utils.helpers import load_themes, save_output
import os

def main():
    themes = load_themes("data/themes.txt")
    os.makedirs("outputs/themes", exist_ok=True)

    for theme in themes:
        trends, all_trend_data = fetch_trending_data(theme)
        agent = get_agent_by_theme(theme)

        content = f"\n== THEME: {theme} ==\n\n"
        content += f"TOP TRENDS:\n{all_trend_data}\n\n"

        # Generate content using all trends
        content += "--- BASED ON ALL TRENDS ---\n"
        content += "SHORT SCRIPT:\n" + generate_short_script(theme, all_trend_data, agent) + "\n"
        content += "LONG SCRIPT:\n" + generate_long_script(theme, all_trend_data, agent) + "\n\n"

        # One by one trend processing
        for i, trend in enumerate(trends):
            content += f"\n--- INDIVIDUAL TREND #{i+1}: {trend} ---\n"
            content += "SHORT SCRIPT:\n" + generate_short_script(theme, trend, agent) + "\n"
            content += "LONG SCRIPT:\n" + generate_long_script(theme, trend, agent) + "\n"

        print(content)
        # Save to a separate file
        file_name = f"outputs/themes/{theme.replace(' ', '_').lower()}.txt"
        save_output(file_name, content)

if __name__ == "__main__":
    main()

# from agents.trend_fetcher import fetch_trending_data
# from agents.content_generator import generate_short_script, generate_long_script
# from agents.formatter import format_output
# from utils.helpers import load_themes, save_output

# def main():
#     themes = load_themes("data/themes.txt")
#     for theme in themes:
#         trend_data = fetch_trending_data(theme)
#         short_script = generate_short_script(theme, trend_data)
#         long_script = generate_long_script(theme, trend_data)
#         final_output = format_output(theme, short_script, long_script)
#         save_output("outputs/video_script.txt", final_output)

# if __name__ == "__main__":
#     main()