def print_lines(lines):
    sentence = ""
    for line in lines:
        print(line, end="")

def header(lines):
    while True:
        level = int(input("- level: "))
        if 1 <= level <= 6:
            break
        print("The level should be within the range of 1 to 6")
    text = input("- text: ")
    mark = "#" * level
    lines.append(mark + " " + text + "\n")

def plain(lines):
    text = input("- text: ")
    lines.append(text)

def new_line(lines):
    lines.append("\n")

def link(lines):
    label = input("- label: ")
    url = input("- URL: ")
    lines.append(f"[{label}]({url})")

def bold(lines):
    text = input("- text: ")
    lines.append("**" + text + "**")

def italic(lines):
    text = input("- text: ")
    lines.append("*" + text + "*")

def inline_code(lines):
    text = input("- text: ")
    lines.append("`"+ text + "`")

def ordered_list(lines):
    while True:
        rows = int(input("- Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")
    for i in range(rows):
        text = input(f"- Row #{i + 1}: ")
        lines.append(f"{i + 1}. {text}\n")

def unordered_list(lines): 
    while True:
        rows = int(input("- Number of rows: "))
        if rows > 0:
            break
        print("The number of rows should be greater than zero")
    for i in range(rows):
        text = input(f"- Row #{i + 1}: ")
        lines.append(f"* {text}\n")

def save(lines):
    text = ""
    for line in lines:
        text = text + line
    file = open("output.md", "w", encoding="utf-8")
    file.write(text)
    file.close()

formatter_list = {"plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list", "new-line", "!help", "!done"}
lines = []

while True:
    while True:
        formatter = input("- Choose a formatter: ")
        if formatter in formatter_list:
            break
        print("Unknown formatting type or command")

    if formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
        continue

    if formatter == "!done":
        save(lines)
        break

    if formatter == "header":
        header(lines)

    if formatter == "plain":
        plain(lines)

    if formatter == "new-line":
        new_line(lines)

    if formatter == "link":
        link(lines)

    if formatter == "bold":
        bold(lines)

    if formatter == "italic":
        italic(lines)

    if formatter == "inline-code":
        inline_code(lines)

    if formatter == "ordered-list":
        ordered_list(lines)

    if formatter == "unordered-list":
        unordered_list(lines)

    print_lines(lines)
    print()

