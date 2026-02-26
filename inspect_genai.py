import google.genai as genai

print('module path', genai.__file__)
print('attributes:')
for attr in dir(genai):
    if not attr.startswith('_'):
        print(' ', attr)

# try to access configure
has_conf = hasattr(genai, 'configure')
print('has configure:', has_conf)

# check for Client or other classes
for name in ['Client', 'OpenAI', 'GenerativeModel', 'session']:
    if hasattr(genai, name):
        print(f'found {name} ->', getattr(genai, name))
