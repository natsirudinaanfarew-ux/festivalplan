# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: FestivalPlan
ANSI = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bg_black": "\033[40m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_yellow": "\033[43m",
    "bg_blue": "\033[44m",
    "bg_magenta": "\033[45m",
    "bg_cyan": "\033[46m",
    "bg_white": "\033[47m",
}


class Color:
    def __init__(self, enabled=True):
        self.enabled = enabled

    def _wrap(self, code, text):
        if not self.enabled:
            return text
        return f"{code}{text}{ANSI['reset']}"

    def style(self, text, color):
        return self._wrap(ANSI.get(color, ""), text)

    def header(self, text):
        return self.style(text, "bold")

    def info(self, text):
        return self.style(text, "cyan")

    def success(self, text):
        return self.style(text, "green")

    def warning(self, text):
        return self.style(text, "yellow")

    def error(self, text):
        return self.style(text, "red")

    def tag(self, text):
        return self.style(text, "bg_black")

    def accent(self, text):
        return self.style(text, "magenta")


color = Color()
