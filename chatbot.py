import json

# Load the data.json file
def load_data():
    try:
        with open("data/data.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: data.json file not found.")
        return {}

data = load_data()

def get_response(user_message):
    # Normalize the user message to lowercase and remove extra spaces
    user_message = user_message.lower().strip()  # Convert to lowercase and strip extra spaces

    print(f"User message: {user_message}")  # Debugging: Print the user's message

    # Check for greetings (case-insensitive matching)
    if any(greeting in user_message for greeting in data["greetings"].keys()):
        print("Greeting detected")  # Debugging: Greeting found
        return get_greeting_response(user_message)

    # Handle career-related queries (look for keywords "career", "job", "occupation", etc.)
    elif any(keyword in user_message for keyword in ["career", "job", "occupation", "profession", "work"]):
        print("Career query detected")  # Debugging: Career found
        return handle_career_query(user_message)

    # Handle government schemes (look for keywords "scheme", "government", "support", etc.)
    elif any(keyword in user_message for keyword in ["scheme", "government", "support", "program"]):
        print("Scheme query detected")  # Debugging: Scheme found
        return handle_schemes_query(user_message)

    # Default response if nothing matches
    else:
        print("No match found")  # Debugging: No match
        return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

def get_greeting_response(user_message):
    # Check if any greeting keyword is in the user message (case-insensitive)
    for greeting, response in data["greetings"].items():
        if greeting in user_message:
            return response
    return "Hello!"  # Default greeting if no match found

def handle_career_query(user_message):
    # Check if a specific career is mentioned in the user message
    for career, details in data["careers"].items():
        if career in user_message:
            return f"{details['description']}\n\nSkills needed: {', '.join(details['skills_needed'])}\nAverage Salary: {details['average_salary']}\n\nCourses: " + '\n'.join([f"{course['course_name']}: {course['url']}" for course in details["course_links"]])
    return "I couldn't find a career matching that query."

def handle_schemes_query(user_message):
    # Check for skill development schemes
    if "skill development" in user_message:
        return handle_skill_development_schemes()

    # Check for Uttarakhand-specific schemes
    if "uttarakhand" in user_message:
        return handle_uttarakhand_schemes()

    return "I couldn't find any schemes matching that query."

def handle_skill_development_schemes():
    schemes = data["government_schemes"]["skill_development_schemes"]
    response = "Here are some Skill Development Schemes:\n\n"
    for scheme in schemes:
        response += f"Name: {scheme['name']}\nDescription: {scheme['description']}\nEligibility: {scheme['eligibility']}\nWebsite: {scheme['website']}\n\n"
    return response

def handle_uttarakhand_schemes():
    schemes = data["government_schemes"]["uttarakhand_specific_schemes"]
    response = "Here are some Uttarakhand-specific Schemes:\n\n"
    for scheme in schemes:
        response += f"Name: {scheme['name']}\nDescription: {scheme['description']}\nEligibility: {scheme['eligibility']}\nWebsite: {scheme['website']}\n\n"
    return response
