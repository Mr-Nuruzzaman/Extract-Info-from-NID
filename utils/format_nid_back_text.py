import re

def format_nid_back_text(text_list):
    
    formatted_data = {}

    # Convert list to a single string for easier pattern matching
    text = " ".join(text_list)

    # 🔹 Check if the address starts with "ঠিকানা"
    address_match = re.search(r'^(.*?)(?=\s*(?:Blood | Group | Issue | Date))', text, re.DOTALL)
    if address_match:
        address = address_match.group(1).strip()

        # If the address starts with "ঠিকানা", exclude it
        if address.startswith("ঠিকানা"):
            formatted_data["address"] = address[len("ঠিকানা:"):].strip()  # Exclude "ঠিকানা"
        else:
            formatted_data["address"] = address

    # 🔹 Extract Place of Birth (before "Issue Date")
    birth_match = re.search(r'Place of B[iI]r[thn]+[:\-]?\s*([A-Za-z\s]+)(?=\s*Issue Date)', text)
    if birth_match:
        formatted_data["place_of_birth"] = birth_match.group(1).strip()


    # formatted_data["back-text"] = text_list

    return formatted_data
