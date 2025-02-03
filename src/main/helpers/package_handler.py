"""
TD
"""


# Local
from src.main.config import SEQ_START
from src.main.config import NB
from src.main.config import NB_NAME
from src.main.config import SEQ_NOTATION
from src.main.config import SEQ_SPARSE
from src.main.config import SOLUTIONS_DIR
from src.main.config import CONFIG_DIR
from src.main.config import TEMPLATES_DIR
from src.main.config import COLS_WIDTH










class PackageHandler:
    """
    TD
    """
    def __init__(self):
        self._data = {
            'package': {
                'day': '',
                'url': '',
                'title': '',
                'site': '',
                'difficulty': '',
                'problem': '',
                'submitted_solution': '',
                'site_solution': '',
                'notes': '',
                'nb': '',
                'filename': '',
                'lastline': '\n',
            },

            'entry_data': {
                'day': '',
                'title': '',
                'solution': '',
                'site': '',
                'difficulty': '',
                'nb': '',
            },

            'entry_data_widths': {
                'day': 0,
                'title': 0,
                'solution': 0,
                'site': 0,
                'difficulty': 0,
                'nb': 0,
            },

            # 'target_line_data': {
            #     'day': '',
            #     'title': '',
            #     'solution': '',
            #     'site': '',
            #     'difficulty': '',
            #     'nb': '',
            # },

            'config_base': {
                'seq_start_loc': SEQ_START,
                'nb_loc': NB,
                'nb_name_loc': NB_NAME,
                'seq_notation_loc': SEQ_NOTATION,
                'seq_sparse_loc': SEQ_SPARSE,
                'solutions_dir_loc': SOLUTIONS_DIR,
                'config_dir_loc': CONFIG_DIR,
                'templates_dir_loc': TEMPLATES_DIR,
            },

            'config_cols_widths': {
                'day': COLS_WIDTH['day'],
                'title': COLS_WIDTH['title'],
                'solution': COLS_WIDTH['solution'],
                'site': COLS_WIDTH['site'],
                'difficulty': COLS_WIDTH['difficulty'],
                'nb': COLS_WIDTH['nb'],
            }
        }

        # Store initial state for reset functionality
        self._initial_state = {
            'package': {
                'day': '',
                'url': '',
                'title': '',
                'site': '',
                'difficulty': '',
                'problem': '',
                'submitted_solution': '',
                'site_solution': '',
                'notes': '',
                'nb': '',
                'filename': '',
                'lastline': '\n',
            },

            'entry_data': {
                'day': '',
                'title': '',
                'solution': '',
                'site': '',
                'difficulty': '',
                'nb': '',
            },

            'entry_data_widths': {
                'day': 0,
                'title': 0,
                'solution': 0,
                'site': 0,
                'difficulty': 0,
                'nb': 0,
            },

            # 'target_line_data': {
            #     'day': '',
            #     'title': '',
            #     'solution': '',
            #     'site': '',
            #     'difficulty': '',
            #     'nb': '',
            # },

            'config_base': {
                'seq_start_loc': SEQ_NOTATION,
                'nb_loc': NB,
                'nb_name_loc': NB_NAME,
                'seq_notation_loc': SEQ_NOTATION,
                'seq_sparse_loc': SEQ_SPARSE,
                'solutions_dir_loc': SOLUTIONS_DIR,
                'config_dir_loc': CONFIG_DIR,
                'templates_dir_loc': TEMPLATES_DIR,
            },

            'config_cols_widths': {
                'day': COLS_WIDTH['day'],
                'title': COLS_WIDTH['title'],
                'solution': COLS_WIDTH['solution'],
                'site': COLS_WIDTH['site'],
                'difficulty': COLS_WIDTH['difficulty'],
                'nb': COLS_WIDTH['nb'],
            }
        }


    def get_value(self, dict_name, key):
        """Get value from specified dictionary"""
        if dict_name in self._data and key in self._data[dict_name]:
            return self._data[dict_name][key]
        raise KeyError(f'Invalid dictionary name \'{dict_name}\' or key \'{key}\'')


    def update_value(self, dict_name, key, value):
        """Update value in specified dictionary"""
        if dict_name in self._data and key in self._data[dict_name]:
            self._data[dict_name][key] = value
        else:
            raise KeyError(f'Invalid dictionary name \'{dict_name}\' or key \'{key}\'')


    def get_dictionary(self, dict_name):
        """Get entire dictionary by name"""
        if dict_name in self._data:
            return self._data[dict_name]
        raise KeyError(f'Invalid dictionary name \'{dict_name}\'')

    def reset_dictionaries(self, dict_names=None):
        """Reset specified dictionaries or all dictionaries to their initial state"""
        if dict_names is None:
            self._data = self._initial_state.copy()
        else:
            for dict_name in dict_names:
                if dict_name in self._initial_state:
                    self._data[dict_name] = self._initial_state[dict_name].copy()
                else:
                    raise KeyError(f'Invalid dictionary name \'{dict_name}\'')
