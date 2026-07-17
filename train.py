# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

print("--- Step 1: Loading the Dataset ---")
# pandas is a library used to read and manipulate data tables
data = pd.read_csv('phishing_data.csv')
print(data)

print("\n--- Step 2: Splitting Clues (X) from Answers (y) ---")
# X contains only our features (drop the answer column)
X = data.drop('is_phishing', axis=1)

# y contains only the final answers
y = data['is_phishing']

print("Features (X):")
print(X.head())

print("\n--- Step 3: Splitting into Training and Testing Sets ---")
# We split our data: 80% to train the AI, and 20% to test it later
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training rows: {len(X_train)} | Testing rows: {len(X_test)}")

print("\n--- Step 4: Training the Decision Tree Brain ---")
# Create the blank model structure
model = DecisionTreeClassifier()

# Train the model by passing it the training features and answers
model.fit(X_train, y_train)
print("Training complete! The AI has generated its classification rules.")

print("\n--- Step 5: Testing Model Accuracy ---")
# Ask the AI to make predictions on the test features it hasn't evaluated yet
predictions = model.predict(X_test)

# Compare the AI's guesses against the actual real answers (y_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy Score: {accuracy * 100}%")
import pickle

print("\n--- Step 6: Saving the Trained Model File ---")
# Open a new file named 'phishing_model.pkl' in Write-Binary ('wb') mode
with open('phishing_model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

print("Success! 'phishing_model.pkl' has been saved to your project folder.")