import os


# Go to [Table of Contents](/README.md#contents)\
def process_submitted_solutions(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for i in range(len(lines)-1):
        if lines[i+1].strip().startswith('## Solution'):
            lines[i+1] = lines[i+1].replace('## Solution', '## Submitted Solution')
            
    with open(filename, 'w') as file:
        file.writelines(lines)


def process_site_solution(filename, site_solution):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Find the index of "## Notes" line
    for i in range(len(lines)):
        if lines[i].strip().startswith('## Notes'):
            # Insert site_solution before "## Notes"
            lines.insert(i, f"{site_solution}\n\n")
            break
            
    with open(filename, 'w') as file:
        file.writelines(lines)


def process_nb(filename, nb):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    # Find the index of "## Notes" line
    for i in range(len(lines)):
        if lines[i].strip().startswith('Go to [Table of Contents](/README.md#contents)'):
            # Insert site_solution before "## Notes"
            lines.insert(i, f"{nb}\n\n")
            break
            
    with open(filename, 'w') as file:
        file.writelines(lines)




def process_url(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    url_old_1 = "Go to [Table of Contents](/README.md#contents)"
    url_old_2 = "Go to [Overview](/README.md)"

    for i in range(len(lines)):

        if lines[i].strip().startswith(url_old_1):
            lines[i] = "Go to [Index](../?tab=readme-ov-file#index)\\\n"
    
        if lines[i].strip().startswith(url_old_2):
            lines[i] = "Go to [Overview](../?tab=readme-ov-file)\n"


    with open(filename, 'w') as file:
        file.writelines(lines)







# Get all files in solutions directory
files = sorted(os.listdir('solutions/'))

# Process files 1 through 5 # len(files) + 1
for i in range(1, 3):
    filename = f'solutions/{files[i-1]}'
    
    process_url(filename)

    # nb = "## NB\n\nTBD"
    # process_nb(filename, nb)

    #  process_submitted_solutions(filename)

