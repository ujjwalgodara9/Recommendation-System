#--------------------Importing Required Libraries/Modules-----------------------#
import numpy as np
import pandas as pd
    
    
from sklearn.linear_model import LinearRegression
from sklearn import metrics



dataset = pd.read_csv('updated_file.csv')
dataset=dataset.head(5100)

# Define a dictionary for the replacements

for col in dataset.columns:
    if dataset[col].dtype == "O":  # Check if the column is of object (string) type
        dataset[col] = dataset[col].fillna("None")
    elif dataset[col].dtype in ["float64", "int64"]:  # Check if the column is numerical
        dataset[col] = dataset[col].fillna(0)
# Use the replace() function to replace the age ranges


y = dataset['SalaryUSD']
X=dataset.drop('SalaryUSD',axis=1)



#---------Testing by displaying whether data is loaded properly or not-----------#
data = dataset.iloc[:,:-1].values
label = dataset.iloc[:,-1].values
len(data[0])
# dataset.iloc[:,14:38]
# dataset.iloc[:,14:38]

#--------------- Lable  Encoding-----------#
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder = LabelEncoder()

#---------------conversion of all categorial column values to vector/numerical--------#
for i in range(3,len(dataset.columns)-1):
    data[:,i] = labelencoder.fit_transform(data[:,i])  
# data[:5]
# data[:5,14:]

#--------------normalizing the non-categorial column values---------#
from sklearn.preprocessing import Normalizer

data1=data[:,:3]
normalized_data = Normalizer().fit_transform(data1)
# print(normalized_data.shape)
data2=data[:,3:]
# print(data2.shape)
df1 = np.append(normalized_data,data2,axis=1)
# print(df1.shape)

#--------------------------Adding Headers-----------------------#
X1 = pd.DataFrame(df1, columns=[
    'Age','YearsCoding', 'YearsCodingProf', 'Country', 'Currency',
    'DevType', 'EdLevel', 'Ethnicity', 'Gender', 'Hobby', 'JobSatisfaction',
    'JobSearchStatus', 'JobStatus', 'OperatingSystem', 'Profession', 'SalaryType',
    'UndergradMajor', 'CompetenceLevel', 'Employment', 'LanguageDesireNextYear1',
    'LanguageDesireNextYear2', 'LanguageDesireNextYear3', 'LanguageWorkedWith1',
    'LanguageWorkedWith2', 'LanguageWorkedWith3'
])

# X1.head()

#------------------Encoding Final Output column Values------------#
#label = labelencoder.fit_transform(label)
# print(len(label))
y=dataset['SalaryUSD']


# y.head()
# print(y)
# print(label)

#------------------Training and testing with Decision Tree----------------#

from sklearn import preprocessing, tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X1,y,test_size=0.2,random_state=10) 

#-----------------decision tree-----------------------#
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
from sklearn.metrics import accuracy_score, confusion_matrix
#[20, 2, 2, 'India', 'Swedish kroner (SEK)', 'Non Developer', 'Masters', 'Hispanic or Latino', 'Male', 'No', 'Extremely satisfied', 'I’m not actively looking, but I am open to new opportunities', 'I am actively looking for a job', 'MacOS', 'Novoice', 'Monthly', 'Engineering', 'A little above average', 'None', 'C', 'Assembly', 'C', 'Java', 'C++', 'HTML']
y_pred = clf.predict(X_test)
y_pred
cm = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)

print("confusion matrics=",cm)
print("  ")
print("accuracy=",accuracy*100)

# #---------------svm------------------------#
# from sklearn import svm

# clf = svm.SVC()
# clf.fit(X_train, y_train)  
# svm_y_pred = clf.predict(X_test)

# svm_cm = confusion_matrix(y_test,svm_y_pred)
# svm_accuracy = accuracy_score(y_test,svm_y_pred)

# print("confusion matrics=",svm_cm)
# print("  ")
# print("accuracy=",svm_accuracy*100)

# #------------------Training and testing with Linear Regression----------------#

# from sklearn.linear_model import LinearRegression

# # Linear Regression model
# linear_reg_model = LinearRegression()
# linear_reg_model.fit(X_train, y_train)

# # Predictions
# linear_reg_y_pred = linear_reg_model.predict(X_test)

# # Calculate accuracy or other metrics if applicable for regression
# linear_reg_accuracy = linear_reg_model.score(X_test, y_test)

# print("Linear Regression R^2 Score:", linear_reg_accuracy)

# #------------------Training and testing with Logistic Regression----------------#

# from sklearn.linear_model import LogisticRegression

# # Logistic Regression model
# logistic_reg_model = LogisticRegression()
# logistic_reg_model.fit(X_train, y_train)

# # Predictions
# logistic_reg_y_pred = logistic_reg_model.predict(X_test)

# # Calculate accuracy or other metrics if applicable for classification
# logistic_reg_accuracy = logistic_reg_model.score(X_test, y_test)
# logistic_reg_accuracy = accuracy_score(y_test, logistic_reg_y_pred)


# print("Logistic Regression Accuracy:", logistic_reg_accuracy*100)








import os
#-------------------Saving the  model------------------------#
import pickle

if not os.path.exists('./newmodels'): # create models directory
    os.mkdir('newmodels')

# Save Models
pickle.dump(clf, open('newmodels/model2_salary.h5', 'wb')) # SVC Model





