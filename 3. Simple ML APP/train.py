import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('dataset.csv')

df['Gender'] = pd.get_dummies(df['Gender'], prefix='Gender')

features = df.drop(['Spending Score (1-100)','CustomerID'], axis=1)
target = df['Spending Score (1-100)']


random = RandomForestRegressor(n_estimators=3)
random.fit(features,target)

with open('model.pkl','wb') as file:
    pickle.dump(random,file)
    print("Model saved successfully")