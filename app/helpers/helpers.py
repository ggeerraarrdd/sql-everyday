# Python Standard Library
import re
import os

# Third-Party Libraries
from jinja2 import Template








def strip_newlines(text):
    results = text.strip("\n")
    
    return results


def clean_strings(*args):
    results = [strip_newlines(arg) for arg in args]

    return results


def get_current_day():
    files = sorted(os.listdir("../solutions"))
    last_file = files[-1]
    number = int(last_file[:3]) + 1

    results = f"{number:03d}"
    
    return results


def create_filename(title, day):
    filename = title.lower()
    filename = re.sub(r"[^a-z0-9\s-]", "", filename)
    filename = filename.replace(" ", "_")
    filename = filename.replace("-", "_")

    results = f"{day}_{filename.strip()}.md"
    
    return results


def load_and_render_template(template_path, data):
    with open(template_path, "r") as file:
        template_content = file.read()
    template = Template(template_content)

    results = template.render(data)
    
    return results


def write_to_file(filepath, content):
    with open(filepath, "w") as file:
        results = file.write(content)
        
    return results


def create_readme_entry(day, title, url, output_filename, site, difficulty, note2self):
    entry_title = f"[{title}]({url})"
    extra_spaces_title = " " * (156 - (len(entry_title)))
    extra_spaces_solution = " " * (63 - (len(output_filename)))
    extra_spaces_site = " " * (11 - (len(site)))
    extra_spaces_difficulty = " " * (12 - (len(difficulty)))

    results = f"| {day}   | {entry_title}{extra_spaces_title}  | [Solution](solutions/{output_filename}){extra_spaces_solution} | {site}{extra_spaces_site} | {difficulty}{extra_spaces_difficulty} | {note2self}  |"
 
    return results


def update_readme(entry):
     # Read contents of README.md
    with open("../README.md", "r") as file:
        lines = file.readlines()

    # Get line number to insert new entry
    for i, line in enumerate(lines):
        if line.strip("\n") == "## Getting Started":
            position = i - 1
            break
        else:
            position = len(lines)
    
    # Insert new entry at specified line number
    lines.insert(position, entry.strip("\n") + '\n')

    # Write the modified contents back to README.md
    with open("../README.md", "w") as file:
        file.writelines(lines)

    return 1
