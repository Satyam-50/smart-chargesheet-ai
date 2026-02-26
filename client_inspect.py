import inspect
import google.genai as genai

print('Client class:', genai.client.Client)
print(inspect.getsource(genai.client.Client))
