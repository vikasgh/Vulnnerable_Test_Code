import os

def render_page(html):
    return html  # unsanitized HTML returned directly

def run_command(cmd):
    return os.popen(cmd).read()  # OS command injection