import pandas as pd
from joblib import load

tips_pred = load('tips_pred_joblib')

total_bill = float(input('Enter the amount of bill: '))
size = int(input("Enter the size of people: "))
user_input = pd.DataFrame(
    [[total_bill, size]],
    columns=[total_bill, size]
)

print(f'Tips Prediction: {tips_pred.predict(user_input)}')