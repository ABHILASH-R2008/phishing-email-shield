# generate_dataset.py
import pandas as pd
import random

data = []

# Generate 500 Safe URLs variations
for _ in range(500):
    length = random.randint(10, 35) # Safe URLs are usually short
    has_ip = 0
    has_at = 0
    data.append([length, has_ip, has_at, 0]) # 0 = Safe

# Generate 500 Phishing URLs variations
for _ in range(500):
    length = random.randint(55, 110) # Phishing URLs are usually long
    has_ip = random.choice([0, 1])
    has_at = random.choice([0, 1])
    # Ensure at least one malicious feature is triggered
    if has_ip == 0 and has_at == 0:
        has_at = 1 
    data.append([length, has_ip, has_at, 1]) # 1 = Phishing

# Save to our CSV file
df = pd.DataFrame(data, columns=['url_length', 'has_ip', 'has_at_symbol', 'is_phishing'])
df.to_csv('phishing_data.csv', index=False)
print("Target acquired! 'phishing_data.csv' has been upgraded to 1,000 real patterns.")