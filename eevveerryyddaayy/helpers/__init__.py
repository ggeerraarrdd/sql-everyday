from .helpers import *










def everyday(title, problem, url, submitted_solution, site_solution, notes, note2self, site, difficulty):
    # Clean input strings
    title, problem, url, submitted_solution, site_solution, notes, note2self = clean_strings(
        title, problem, url, submitted_solution, site_solution, notes, note2self
    )

    # Get day and create filename
    day = get_current_day()
    output_filename = create_filename(title, day)

    # Prepare template data
    template_data = {
        "day": day,
        "title": title,
        "site": site,
        "difficulty": difficulty,
        "problem": problem,
        "url": url,
        "submitted_solution": submitted_solution,
        "site_solution": site_solution,
        "notes": notes,
        "lastline": "\n"
    }

    # Generate and save solution file
    filled_document = load_and_render_template("templates/solution.txt", template_data)
    write_to_file(f"../solutions/{output_filename}", filled_document)
    print("Solution markdown file created!")

    # Update README
    entry = create_readme_entry(day, title, url, output_filename, site, difficulty, note2self)
    update_readme(entry)
    print("README.md updated with new entry!")
    
    results = f"Everyday completed"

    return results
