# %%
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

def diabetic_status_prediction(diabetic_status_prediction_list:list):
    dataset=pd.read_csv(r'AIModel/ExercisePlan/diabetes2.csv')
    dataset.head()
    dataset.isnull().sum()
    dataset.dtypes
    print(dataset.groupby('Outcome').size())
    dataset.corr()
    plt.figure(figsize=[7,7])
    sns.heatmap(dataset.corr(), annot= True, fmt= '.0%')

    dataset.plot(kind="box",subplots=True,layout=(7,2),figsize=(15,20));

    X=dataset[dataset.columns]
    X=X.drop(columns=['Outcome','Pregnancies','SkinThickness','DiabetesPedigreeFunction'])
    X.head()

    Y=dataset['Outcome']
    Y.head()

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=0)

    X_train.shape,X_test.shape

    def model_acc(model):
        model.fit(X_train,Y_train)
        acc=model.score(X_test,Y_test)
        print(str(model)+ '-->'+str(acc))

    from sklearn.ensemble import RandomForestClassifier
    rf = RandomForestClassifier()
    model_acc(rf)

    from sklearn.naive_bayes import GaussianNB
    nb_clf = GaussianNB()
    model_acc(nb_clf)

    from sklearn.neighbors import KNeighborsClassifier
    knn_clf = KNeighborsClassifier()
    model_acc(knn_clf)

    from sklearn import ensemble
    gb_clf = ensemble.GradientBoostingClassifier()
    model_acc(gb_clf)

    from sklearn.linear_model import LogisticRegression
    lr_clf = LogisticRegression()
    model_acc(lr_clf)

    from sklearn.model_selection import GridSearchCV

    parameters = {'n_estimators':[10, 50,100]}
    grid_obj = GridSearchCV(estimator=rf, param_grid=parameters)
    grid_fit = grid_obj.fit(X_train,Y_train)
    best_model = grid_fit.best_estimator_
    best_model

    best_model.score(X_train,Y_train)

    import pickle
    with open('Diabetic.pkl','wb') as file:
        pickle.dump(grid_fit, file)

    return_val = best_model.predict([diabetic_status_prediction_list])[0]
    if return_val == 0:
        return('diabetics_0')
    elif return_val ==1:
        return('diabetics_1')



