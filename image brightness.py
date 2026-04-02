import numpy as np

image = np.random.randint(0,256,(5,5))  
bright = image + 30
bright = np.clip(bright,0,255) 
avg_brightness = np.mean(bright)
print("Original image:\n", image)
print("Brightened image:\n", bright)
print("Average brightness:", avg_brightness)