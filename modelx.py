import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
#from sklearn.classifier import Random
#from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv(r"C:\Users\SAI\Desktop\project\Fraud_check.csv")
l = []


def convert(i):
    if i <= 30000:
        l.append("risky")
    else:
        l.append("good")
#


for n in data["Taxable.Income"]:
    convert(n)

data["taxable_income"] = l
data["taxable_income"].value_counts()

data1 = data.drop(["Taxable.Income"], axis=1)

lb = LabelEncoder()
data1["Undergrad"] = lb.fit_transform(data1["Undergrad"])  # 0 for no and 1 for yes
data1["Marital.Status"] = lb.fit_transform(data1["Marital.Status"])  #
data1["Urban"] = lb.fit_transform(data1["Urban"])  #
data1["taxable_income"] = lb.fit_transform(data1["taxable_income"]) 

x = data1.iloc[:, :5]
y = data1.iloc[:, 5:]
model = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
model.fit(x, y)

pickle.dump(model, open('modellll.pkl', 'wb'))

# Loading model to compare the results
model = pickle.load(open('modellll.pkl', 'rb'))
