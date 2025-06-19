from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

# Define the path to your CSV file
CSV_PATH = os.path.join("data", "data.csv")

def search_in_csv(query, search_type):
    """
    Searches for a query in the CSV file based on the search type.
    
    Args:
        query (str): The search term.
        search_type (str): The column to search in ('roll', 'name', 'father_name').

    Returns:
        list: A list of matching rows (dictionaries).
    """
    results = []
    try:
        with open(CSV_PATH, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                field_to_check = ""
                # Determine which column to search based on search_type
                if search_type == 'roll':
                    field_to_check = row.get("ROLL", "")
                    # For roll number, we want an exact match
                    if query == field_to_check:
                        results.append(row)
                elif search_type == 'name':
                    field_to_check = row.get("NAME", "").lower()
                    # For name, we check if the query is part of the name
                    if query.lower() in field_to_check:
                        results.append(row)
                elif search_type == 'father_name':
                    field_to_check = row.get("FATHERNAME", "").lower()
                    # For father's name, check if query is part of the name
                    if query.lower() in field_to_check:
                        results.append(row)
    except FileNotFoundError:
        print(f"Error: The file at {CSV_PATH} was not found.")
        return []
        
    return results

@app.route('/')
def index():
    """
    Renders the main search page.
    """
    return render_template('index.html')

@app.route('/search')
def search():
    """
    API endpoint to handle search requests from the frontend JavaScript.
    """
    query = request.args.get('query', '').strip()
    search_type = request.args.get('search_type', 'roll').strip()

    if not query:
        return jsonify({'error': 'Please provide a search term.'}), 400

    # Validate roll number input
    if search_type == 'roll' and not query.isdigit():
        return jsonify({'error': 'Roll number must be a valid number.'}), 400

    results = search_in_csv(query, search_type)

    if results:
        # If results are found, return the first match in the expected format.
        # The frontend is designed to show one primary result.
        first_result = results[0]
        response_data = {
            'status': 'found',
            'roll': first_result.get('ROLL'),
            'name': first_result.get('NAME'),
            'father_name': first_result.get('FATHERNAME'),
            'mother_name': first_result.get('MOTHERNAME'),
            'category': first_result.get('CATEGORY'),
            'source_file': first_result.get('SOURCE_FILE')
        }
        return jsonify(response_data)
    else:
        # If no results are found
        return jsonify({'status': 'not_found'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)