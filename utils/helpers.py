def load_themes(path):
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def save_output(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content + "\n")