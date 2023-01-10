import os


def input_val(prompt, input_type=int, default=None):
    raw = input(prompt)
    result = default
    try:
        result = input_type(raw)
    except:
        pass
    
    return result

def input_path(prompt):
    while True:
        path = input(prompt)
        try:
            os.stat(path)
            return path
        except:
            pass
        
