# #########################################################################
#
# WARNING: DO NOT MODIFY THIS CONFIG FILE.
#
# Manual modifications may cause unintended behavior.
# The system will manage this file automatically.
#
# #########################################################################





"""
Project Start Date
===========================================================================

Controls initialization behavior through start date setting.

Parameters
----------
SEQ_START : str
    Values:
        '' : Empty string - enables initialization on first run
        'YYYY-MM-DD' : Specific date - prevents initialization
    Default: '' (empty string)

Example:
    '2025-01-01'

Notes:
    When set to empty string, initialization will occur on first run
    and SEQ_START will be set to that date. Once set, initialization
    will not occur again.
"""
SEQ_START='2024-09-28'





"""
Index Table: Optional Extra Column
===========================================================================

Adds an optional sixth column to the Index table for additional 
notes and annotations.

Parameters
----------
NB : int
    Controls visibility of the sixth column in Index table.
    Values:
        0: Disable sixth column display (default)
        1: Enable sixth column display

NB_NAME : str
    The header title for the sixth column when enabled.
    Only relevant when NB=1.
    Default: 'NB'

Example:
    NB=0 keeps number of columns to five.
    NB=1, NB_NAME='Notes' creates a sixth column titled 'Notes'
"""
NB=1
NB_NAME='NB'





"""
Index Table: Sequential Numbering Format for First Column ('Day')
===========================================================================

This setting determines how the values in the first column ('Day') of the
Index table are formatted.

Parameters
----------
SEQ_NOTATION : int
    Values:
        0: Three-digit zero-padded number (e.g., '001', '002')
        1: Full ISO date format (e.g., '2001-01-01')
    Default: 0

Notes:
    The chosen format affects all 'Day' values throughout the sequence. 
    Three-digit format (0) is more compact but date format (1) provides 
    more temporal context.
"""
SEQ_NOTATION=0





"""
Index Table: Sequential Numbering Gaps for First Column ('Day')
===========================================================================

NOTE: Feature not yet implemented.

This setting determines how the system handles 'Day' values that are 
missing from the sequence numbering.

Parameters
----------
SEQ_SPARSE : int
    Values:
        0: Continuous sequence - no gaps for missed days
        1: Sparse sequence - adds blank entries in index for missed days
    Default: 0
        
Example:
    For three-digit format (SEQ_NOTATION=0):
    If SEQ_SPARSE=0: Missing a day creates sequence
        001
        002
    If SEQ_SPARSE=1: Missing a day creates sequence
        001
        002 [all other columns blank]
        003
    
    For date format (SEQ_NOTATION=1):
    If SEQ_SPARSE=0: Missing a day creates sequence
        2025-01-01
        2025-01-03
    If SEQ_SPARSE=1: Missing a day creates sequence
        2025-01-01
        2025-01-02 [all other columns blank]
        2025-01-03

Notes:
    Setting SEQ_SPARSE=1 helps with accountability by making missed days 
    visible in the sequence, rather than hiding gaps.
"""
SEQ_SPARSE=0





"""
Locations of Critical Directories
===========================================================================

Controls the paths to critical directories.

Parameters
----------
SOLUTIONS_DIR : str
    Relative path to the directory containing solution files
    Default: 'solutions'
CONFIG_DIR : str
    Relative path to the configuration files directory
    Default: 'src/main/config'
TEMPLATES_DIR : str
    Relative path to the templates directory
    Default: 'src/main/templates' 
"""
SOLUTIONS_DIR='solutions'
CONFIG_DIR='src/main/config'
TEMPLATES_DIR='src/main/templates'
