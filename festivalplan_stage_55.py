# === Stage 55: Add a setting to disable colorized output ===
# Project: FestivalPlan
USE_COLOR = os.environ.get("FESTIVALPLAN_COLOR", "auto").lower() != "0"

def colorize(text, color):
    if not USE_COLOR:
        return text
    attr = {
        "red": "31", "green": "32", "yellow": "33", "blue": "34",
        "magenta": "35", "cyan": "36", "white": "37",
    }.get(color, "0")
    return "\033[{}m{}\033[0m".format(attr, text)

def cprint(text, color="white", **kwargs):
    print(colorize(text, color), **kwargs)
