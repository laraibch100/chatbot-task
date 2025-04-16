from google import genai

# Initialize the GenAI client
client = genai.Client(api_key='AIzaSyCjXsIE0elpYeLZnpmhZJlNaheIIb10n3c')

# Get user input
user_question = input("Ask Iron Man anything: ")

# Iron Man-style prompt with the user's question
prompt = (
    f"You're Tony Stark, aka Iron Man. Someone asked: '{user_question}'\n"
    "Answer with your usual witty, sarcastic, and genius-level tone. "
    "Make it entertaining but still informative."
)

# Generate the content
response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=prompt
)

# Print the Iron Man-style answer
print("\nIron Man says:")
print(response.text)
