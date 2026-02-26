import google.generativeai as genai

genai.configure(api_key="AIzaSyA63WfbVo7Uru8J2ZTaQX0xIIOluf8SCD0")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Say hello")

print(response.text)