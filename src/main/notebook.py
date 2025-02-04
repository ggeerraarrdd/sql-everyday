"""
Form interface for Jupyter notebook.

Creates and manages an interactive form using ipywidgets to collect, validate
and process data. The form interface is specifically designed for use within a 
Jupyter notebook environment.
"""


# Python Standard Library
from ast import literal_eval
from datetime import datetime
import os

# Third-Party Libraries
import ipywidgets as widgets

# Local
from .helpers import PackageHandler
from .main import validate_runs
from .main import initialize_runs










# Common layout settings
base_layout = {
    'width': '50%',
    'margin': '0 0 25px 0'
}

text_layout = {**base_layout}
textarea_layout = {**base_layout, 'height': '100px'}
solution_layout = {**base_layout, 'height': '200px'}

# Widget Definitions
url_widget = widgets.Textarea(
    value='',
    placeholder='Enter url',
    layout=text_layout
)

title_widget = widgets.Textarea(
    value='',
    placeholder='Enter problem title',
    layout=text_layout
)

site_options = os.getenv('SITE_OPTIONS')

if site_options:
    # Convert list to string representation for literal_eval
    if isinstance(site_options, list):
        site_options_str = str(site_options) # pylint: disable=invalid-name
    else:
        site_options_str = site_options

    options_list = literal_eval(site_options_str)

    # If only one option, make it both the options and default value
    if len(options_list) == 1:
        site_widget = widgets.Dropdown(
            options=[options_list[0]],
            value=options_list[0],
            layout=text_layout
        )
    else:
        site_widget = widgets.Dropdown(
            options=[''] + options_list,
            value='',
            layout=text_layout
        )
else:
    # Default options if environment variable is not set
    site_widget = widgets.Dropdown(
        options=['', 'Codewars', 'DataLemur', 'LeetCode'],
        value='',
        layout=text_layout
    )

difficulty_widget = widgets.Dropdown(
    options=['', 'Easy', 'Medium', 'Hard'],
    value='',
    layout=text_layout
)

problem_widget = widgets.Textarea(
    value='',
    placeholder='Enter problem description',
    layout=textarea_layout
)

submitted_solution_widget = widgets.Textarea(
    value='',
    placeholder='Enter your solution here',
    layout=solution_layout
)

site_solution_widget = widgets.Textarea(
    value='',
    placeholder='Enter site solution here',
    layout=solution_layout
)

notes_widget = widgets.Textarea(
    value='TBD',
    layout=textarea_layout
)

nb_widget = widgets.Textarea(
    value='TBD',
    layout=textarea_layout
)

page_title_widget = widgets.Text(
    value='',
    placeholder='Enter page title',
    layout=textarea_layout
)





def create_form_head() -> widgets.VBox:
    """
    Creates the header section of the form.

    Returns:
        VBox: A vertical box container with the form header elements.
    """
    label_layout = widgets.Layout(
        width='50%',
        margin='30px 0',
    )

    container_layout = widgets.Layout(
        display='flex',
        flex_flow='column',
        align_items='center',
        width='100%'
    )

    description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

    heading = widgets.HTML(value='<span style="font-size:20px;"><b>EEVVEERRYYDDAAYY</b></span>', layout=label_layout)
    description = widgets.HTML(value=description, layout=label_layout)

    section_head = widgets.VBox([heading], layout=container_layout)

    return section_head


def create_form_main(handler: PackageHandler) -> widgets.VBox:
    """
    Creates the main section of the form with input fields.

    Args:
        handler: PackageHandler instance for configuration management.

    Returns:
        VBox: A vertical box container with all form input fields.
    """
    label_layout = widgets.Layout(
        width='50%',
        margin='0'
    )

    container_layout = widgets.Layout(
        display='flex',
        flex_flow='column',
        align_items='center',
        width='100%'
    )

    sections = [
        ('URL', url_widget),
        ('Title', title_widget),
        ('Site', site_widget),
        ('Difficulty', difficulty_widget),
        ('Problem', problem_widget),
        ('Your Solution', submitted_solution_widget),
        ('Site Solution', site_solution_widget),
        ('Notes', notes_widget)
    ]

    if handler.get_value('config_base', 'nb_loc') == 1:
        sections.append((handler.get_value('config_base', 'nb_name_loc'), nb_widget))

    section_list = []
    for heading, widget in sections:
        label = widgets.HTML(value=f'<b>{heading}</b>', layout=label_layout)
        section_list.append(widgets.VBox([label, widget], layout=container_layout))

    section_main = widgets.VBox(section_list, layout=container_layout)


    return section_main


def create_form_button(handler: PackageHandler, today: datetime) -> widgets.VBox:
    """
    Creates the form submission button section with validation logic.

    This function creates the button UI element. It also includes nested functions 
    that are triggered when the button is clicked:
    - validate_form_data(): Validates all form inputs
    - execute_runs(): Triggers handle_runs_default() in main

    Args:
        handler: PackageHandler instance for configuration management.
        today: datetime object representing current date (time component stripped).

    Returns:
        VBox: A vertical box container with the submission button.
    """
    container_layout = widgets.Layout(
        display='flex',
        flex_flow='column',
        align_items='center',
        width='100%'
    )


    def validate_form_data():

        form_inputs = {
            'url': url_widget.value,
            'title': title_widget.value, 
            'site': site_widget.value,
            'difficulty': difficulty_widget.value,
            'problem': problem_widget.value,
            'submitted_solution': submitted_solution_widget.value,
            'site_solution': site_solution_widget.value,
            'notes': notes_widget.value,
            'nb': nb_widget.value
        }

        for key, value in form_inputs.items():

            if key == 'nb':
                key = handler.get_value('config_base', 'nb_name_loc')
                key_label = key.replace('_', ' ').title()
            else:
                key_label = key.replace('_', ' ').title()

            if not isinstance(value, str):
                return False, f'Field {key_label} must be a string'
            if not value.strip():
                return False, f'Field {key_label} cannot be empty'


        return True, form_inputs


    def execute_runs(b):

        is_valid, form_inputs_validated = validate_form_data()

        if not is_valid:
            print(f'Validation error: {form_inputs_validated}')
            return

        print(b.tooltip)

        # Clear all form fields
        url_widget.value = ''
        title_widget.value = ''
        try:
            site_widget.value = ''
        except:
            pass
        difficulty_widget.value = ''
        problem_widget.value = ''
        submitted_solution_widget.value = ''
        site_solution_widget.value = ''
        notes_widget.value = 'TBD'
        nb_widget.value = 'TBD'

        from src import handle_runs_default # pylint: disable=import-outside-toplevel

        handle_runs_default(handler, today, form_inputs_validated)


    create_button = widgets.Button(description='Process Entry', tooltip='Processing...')
    create_button.on_click(execute_runs)
    section_button = widgets.VBox([create_button], layout=container_layout)


    return section_button


def form() -> widgets.VBox:
    """
    Creates and returns the complete form interface.

    Returns:
        VBox: The complete form interface containing header, main input fields,
              and submission button.
    """
    # ######################################
    # GET HANDLER
    # ######################################
    handler = PackageHandler()


    # ######################################
    # GET RUNS VALIDATED (FIRST OR REGULAR)
    # ######################################
    is_run_first = validate_runs(handler)



    # ######################################
    # GET RUNS INITIALIZED (FIRST)
    # ######################################
    today = datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)

    if is_run_first:

        initialize_runs(handler, today)

    elif not is_run_first:

        pass

    else:

        raise ValueError('Invalid configuration: TODO')


    # ######################################
    # GET FORM
    # ######################################
    container_layout = widgets.Layout(
        display='flex',
        flex_flow='column',
        align_items='center',
        width='100%'
    )

    head = create_form_head()
    main = create_form_main(handler)
    button = create_form_button(handler, today)

    full_section = widgets.VBox([head, main, button], layout=container_layout)


    return full_section
