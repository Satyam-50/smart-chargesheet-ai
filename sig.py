import google.genai as genai
import inspect
client = genai.Client(api_key='TEST')
print('models object', client.models)
print('signature:', inspect.signature(client.models.generate_content))
