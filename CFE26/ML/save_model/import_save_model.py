# Although we haven't created any model over here
# But we can recall our saved model to perform predication

import pickle
import pandas as pd
with open('tips_pred', 'rb') as f:
    tips_pred = pickle.load(f)

t_bill = float(input("Enter the total bill paid: "))
size = int(input('Enter the size of the group (1 for single person): '))
user_input = pd.DataFrame(
    [[t_bill, size]],
    columns=['total_bill', 'size']
)

print(f'Tips Predication: {tips_pred.predict(user_input)}')