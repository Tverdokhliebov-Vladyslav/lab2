import numpy as np

f = lambda x: 2*x**4 - 8*x**3 - 16*x**2 - 1

def find_segments(): # відокремлюємо корені
    search_range = np.arange(-10, 10, 1)
    
    a = None
    previous_x = None
    current_x  = None
    segments = []

    for x in search_range:
        x = round(x, 4)
        current_x = f(x)
        if previous_x is not None and previous_x * current_x < 0:
            segments.append((a, x))
        a = x
        previous_x = current_x
    return segments

segments = find_segments()
for a, b in segments:
    print(f'Found segment: [{a}, {b}]')

