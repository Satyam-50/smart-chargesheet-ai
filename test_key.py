import google.genai as genai

# simple key test using the new Client interface
client = genai.Client(api_key="AIzaSyBr2gqb614oXu2JUPQKfUIOdakTWoO6V_E")
response = client.models.generate_content(model="gemini-1.5-flash", contents="Say hello")
print(response.text)