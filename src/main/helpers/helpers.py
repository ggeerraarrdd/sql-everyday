"""
TD
"""


# Python Standard Library
from typing import Any, Dict, List

# Third-Party Libraries
from jinja2 import Template

# Local
from src.main.config import TEMPLATES_DIR










def clean_strings(*args: str) -> List[str]:
    """
    Remove newline characters from multiple string arguments.

    Args:
        *args: Variable number of strings to clean

    Returns:
        List[str]: List of cleaned strings with newlines removed
    """
    results = []
    for arg in args:
        results.append(arg.strip('\n'))

    return results


def get_files_created(data: Dict[str, Any]) -> int:
    """
    Create a solution file using a template and provided data.

    Args:
        data: Dictionary containing template variables including "filename"

    Returns:
        int: 1 on successful file creation
    """

    with open(f'{TEMPLATES_DIR}/solution.txt', 'r', encoding='utf-8') as file:
        template_content = file.read()

    # Create a Jinja2 template object
    template = Template(template_content)

    # Render the template with the data
    filled_document = template.render(data)

    with open(f'solutions/{data["filename"]}', 'w', encoding='utf-8') as file:
        file.write(filled_document)

    return 1


def get_target_line_dict(nb_loc, line: str) -> Dict[str, str]:
    """
    Parse a table line into a dictionary based on notebook configuration.

    Args:
        line: String containing pipe-separated table data

    Returns:
        Dict[str, str]: Dictionary with parsed table data fields

    Raises:
        ValueError: If notebook configuration is invalid
    """
    data = {
        'day': '',
        'title': '',
        'solution': '',
        'site': '',
        'difficulty': '',
        'nb': '',
    }

    if nb_loc == 0:

        keys = list(data.keys())[:-1]  # Exclude 'nb'

    elif nb_loc == 1:

        keys = list(data.keys())

    else:

        raise ValueError('Invalid configuration: TODO')


    segments = []
    for segment in line.split('|'):
        segment = segment.strip()
        if segment:
            segments.append(segment)

    for i, key in enumerate(keys):
        if i < len(segments):
            data[key] = f'{segments[i]}'

    results = data

    return results


def get_target_line_updated(nb_loc, data: Dict[str, str], widths: Dict[str, int]) -> str:
    """
    Format a table line with proper padding based on column widths.

    Args:
        data: Dictionary containing table cell values
        widths: Dictionary containing column widths

    Returns:
        str: Formatted table line with proper padding

    Raises:
        ValueError: If notebook configuration is invalid
    """
    target_line = '|'

    if nb_loc == 0:

        for key, value in data.items():

            if key != 'nb':  # Skip the "nb" key
                value_str = str(value)
                is_second_line = all(char == '-' for char in value_str.strip())
                diff = widths[key] - len(value_str)

                if is_second_line:
                    padding = '-' * diff
                else:
                    padding = ' ' * diff

                target_line += f' {value_str}{padding} |'

    elif nb_loc == 1:

        for key, value in data.items():

            value_str = str(value)

            is_second_line = value_str and all(char == '-' for char in value_str.strip())
            diff = widths[key] - len(value_str)

            if is_second_line:
                padding = '-' * diff
            else:
                padding = ' ' * diff

            target_line += f' {value_str}{padding} |'

    else:

        raise ValueError('Invalid configuration: TODO')

    results = target_line

    return results
