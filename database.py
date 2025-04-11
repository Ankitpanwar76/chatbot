import json

# Load the data from the JSON file
def load_data():
    with open("data/data.json", "r", encoding="utf-8") as file:
        return json.load(file)

data = load_data()

def get_response(user_message):
    user_message = user_message.lower()

    # Check for greetings
    if any(greeting in user_message for greeting in data["greetings"].keys()):
        return data["greetings"].get(user_message, "Hello!")
    
    # Handle career-related queries
    if any(career in user_message for career in data["careers"].keys()):
        return handle_career_query(user_message)

    # Handle government schemes
    if "government schemes" in user_message or "scheme" in user_message:
        return handle_schemes_query(user_message)

    # Handle Uttarakhand schemes
    if "uttarakhand" in user_message:
        return handle_uttarakhand_schemes()

    # Default response if nothing matches
    return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

def handle_career_query(user_message):
    # Check if a specific career is mentioned
    for career, details in data["careers"].items():
        if career in user_message:
            return f"{details['description']}\n\nSkills needed: {', '.join(details['skills_needed'])}\nAverage Salary: {details['average_salary']}\n\nCourses: " + '\n'.join([f"{course['course_name']}: {course['url']}" for course in details["course_links"]])
    return "I couldn't find a career matching that query."

def handle_schemes_query(user_message):
    # Check for government schemes
    if "skill development" in user_message:
        return handle_skill_development_schemes()
    return "I couldn't find any schemes matching that query."

def handle_uttarakhand_schemes():
    schemes = data["government_schemes"]["uttarakhand_specific_schemes"]
    response = "Here are some Uttarakhand-specific Schemes:\n\n"
    for scheme in schemes:
        response += f"Name: {scheme['name']}\nDescription: {scheme['description']}\nEligibility: {scheme['eligibility']}\nWebsite: {scheme['website']}\n\n"
    return response

def handle_skill_development_schemes():
    schemes = data["government_schemes"]["skill_development_schemes"]
    response = "Here are some Skill Development Schemes:\n\n"
    for scheme in schemes:
        response += f"Name: {scheme['name']}\nDescription: {scheme['description']}\nEligibility: {scheme['eligibility']}\nWebsite: {scheme['website']}\n\n"
    return response
