from agents.trend_fetcher import fetch_trending_data
from agents.content_generator import generate_short_script, generate_long_script
from agents.formatter import format_output
from utils.helpers import load_themes, save_output

def main():
    themes = load_themes("data/themes.txt")
    for theme in themes:
        trend_data = fetch_trending_data(theme)
        short_script = generate_short_script(theme, trend_data)
        long_script = generate_long_script(theme, trend_data)
        final_output = format_output(theme, short_script, long_script)
        save_output("outputs/video_script.txt", final_output)

if __name__ == "__main__":
    main()
