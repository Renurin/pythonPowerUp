import pandas as pd

# Step 1: Read csv
# Step 2: Encode the columns we want the AI to use for learning
# Step 3: Set the training and the test data. x for attributes and y for the score_credito
# Step 4: Import the new customers csv and predict their score
# Step Extra: Test accuracy

# Step 1:
table = pd.read_csv("C:\\Users\\Renan\\Desktop\\Pasta_do_Renan_=)\\Python\\pythonPowerUp\\AI\\clientes.csv")
# print(table.info())
# print(table.columns)

# Step 2:
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
# Encode objects except score
for column in table.columns:
    if table[column].dtype == "object" and column != "score_credito":
        table[column] = encoder.fit_transform(table[column])

#Step 3:
x = table.drop(["score_credito","id_cliente"],axis=1) # Getting rid of id_cliente cause does not aplly in the prediction
y = table["score_credito"]

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size= 0.3, random_state= 1) # train_test_split doc
# I chose KnearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

# Step Extra: Test accuracy
from sklearn.metrics import accuracy_score
prediction = knn.predict(x_test.to_numpy())
print(accuracy_score(y_test,prediction))

# Step 4
new_costumers = pd.read_csv("C:\\Users\\Renan\\Desktop\\Pasta_do_Renan_=)\\Python\\pythonPowerUp\\AI\\novos_clientes.csv")
for column in new_costumers.columns:
    if new_costumers[column].dtype == "object" and column != "score_credito":
        new_costumers[column] = encoder.fit_transform(new_costumers[column])
prediction = knn.predict(new_costumers)
print(prediction)
# Dumb Ai Warning !