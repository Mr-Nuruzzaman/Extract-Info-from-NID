import re

def format_nid_front_text(text_list):
    formatted_data = {}

    # Convert list to a single string for easier pattern matching
    text = " ".join(text_list)

    # Extract Bangla Name (between Date of Birth and "Name")
    bangla_name_match = re.search(r'\b\d{1,2} [A-Za-z]+ \d{4}\b\s+([\u0980-\u09FF\s]+)\s+Name', text)
    if bangla_name_match:
        formatted_data["bangla_name"] = bangla_name_match.group(1).strip()

    # Extract Name (after "Name")
    name_match = re.search(r'Name\s+([A-Z\s]+)', text)
    if name_match:
        formatted_data["name"] = name_match.group(1).strip()

    # Extract Date of Birth (format: "10 Dec 1998")
    dob_match = re.search(r'\b(\d{2} [A-Z][a-z]{2} \d{4})\b', text)
    if dob_match:
        formatted_data["date_of_birth"] = dob_match.group(1)

    # Extract NID Number (format: "915 503 1165")
    nid_match = re.search(r'\b(\d{3} \d{3} \d{4})\b', text)
    if nid_match:
        formatted_data["nid_no"] = nid_match.group(1)

    # Check if both পিতা and মাতা exist and extract text in between
    between_match = re.search(r'পিতা\s+([\u0980-\u09FF\s]+?)\s+মাতা', text)

    # If only "পিতা" exists, extract after "পিতা"
    after_father_match = re.search(r'পিতা\s+([\u0980-\u09FF\s]+)', text)

    # If only "মাতা" exists, extract before "মাতা"
    before_mother_match = re.search(r'([\u0980-\u09FF\s]+)\s+মাতা', text)

    if between_match:
        formatted_data["father_name"] = between_match.group(1).strip()
    elif after_father_match:
        formatted_data["father_name"] = after_father_match.group(1).strip()
    elif before_mother_match:
        formatted_data["father_name"] = before_mother_match.group(1).strip()

    # Default pattern: Capture Bangla characters before "Date"
    mother_match = re.search(r'([\u0980-\u09FF\s]+?)(?=\s*(?:Date))', text)

    # If "মাতা" exists, extract after "মাতা"
    mata_match = re.search(r'মাতা\s+([\u0980-\u09FF\s]+?)(?=\s*(?:Date))', text)

    if mata_match:
        formatted_data["mother_name"] = mata_match.group(1).strip()
    elif mother_match:
        formatted_data["mother_name"] = mother_match.group(1).strip()

    # formatted_data["Text"] = text_list

    return formatted_data
