import google.generativeai as genai

# Your API key
API_KEY = 'AIzaSyCJDQQBio__2Okg-ESfFsZ4JdWThaAfQ0E'

try:
    # Configure the API
    genai.configure(api_key=API_KEY)

    # Try to list available models
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    print("API Key is Valid!")
    print("Available Models:", models)

    # Try a simple generation to further verify
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Hello, can you confirm the API is working?")
    print("\nTest Response:", response.text)

except Exception as e:
    print(f"Error validating API key: {e}")
