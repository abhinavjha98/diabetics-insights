from django.shortcuts import render
from .models import Diabetes_table
import time
from django.utils.datastructures import MultiValueDictKeyError
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
# Create your views here.
def home(request):
    
    return render(request,'index.html')

def risk(request):
    print("******************************")
    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['exampleRadios']
        age=request.POST['group']
        #child=request.POST['child']
        blood_pressure=request.POST['exampleRadios1']
        glucose=request.POST['exampleRadios2']
        insulin=request.POST['insulin']
        # insulin_name=request.POST['insulin']
        skin_thickness=request.POST['skin']
        height = request.POST['height']
        weight = request.POST['weight']
        try:
            child = request.POST['children']
        except MultiValueDictKeyError:
            child ="Please select number of children"
       

        if age =='Please select you age':
            age=0
        elif age =='20-30':
            age = 25
        elif age =='30-40':
            age = 35
        elif age =='40-50':
            age = 45
        elif age =='50-60':
            age = 55
        elif age =='60-70':
            age = 65
        elif age =='70-80':
            age = 75


        if height == '130-140':
            height = 135
        elif height =='141-150':
            height = 145
        elif height =='151-160':
            height = 155
        elif height =='161-170':
            height = 165
        elif height =='171-180':
            height = 175
        else:
            height = 185
        
        if child=='Please select number of children':
            child = 0
        elif child =='1':
            child = 1
        elif child =='2':
            child = 2
        elif child =='3':
            child = 3
        elif child =='4':
            child = 4
        elif child =='5':
            child = 5
        elif child =='6':
            child = 6
        else:
            child = 7

        bmi = float(weight)/(height/100)**2
        print(bmi)
        print("name:",name)
        if gender=='option1':
            gender='Male'
        else:
            gender='Female'
        print("gender:",gender)
        print("age:",age)
        #print("child:",child)
        if blood_pressure=='option1':
            blood_pressure=25
        elif blood_pressure=='option2':
            blood_pressure=55
        elif blood_pressure=='option3':
            blood_pressure=85
        elif blood_pressure=='option4':
            blood_pressure=105
        else:
            blood_pressure=120
        print("blood_pressure:",blood_pressure)
        if glucose=='option1':
            glucose=130
        elif glucose=='option2':
            glucose=150
        elif glucose=='option3':
            glucose=170
        elif glucose=='option4':
            glucose=190             
        else:
            glucose=199
        print("glucose:",glucose)
        # if insulin=='option1':
        #     insulin='Yes'
        # else:
        #     insulin='No'
        print("insulin:",insulin)
        
        print("skin_thickness:",skin_thickness)


        print(child,glucose,blood_pressure,int(skin_thickness),int(insulin),round(bmi,4),age)
        input_data = (5,166,72,19,175,25.8,51)
        
        filename = 'diabetes_app/diabetics.sav'
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)
        loaded_scaler = pickle.load(open('diabetes_app/sd_scaler.sav','rb'))
        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        loaded_model = pickle.load(open(filename, 'rb'))
  
        # standardize the input data
        std_data = loaded_scaler.transform(input_data_reshaped)
        print(std_data)

        prediction = loaded_model.predict(std_data)
        print(prediction)
        

        # print(classifier.predict_proba(input_data_reshaped))
        if (prediction[0] == 0):
            data = Diabetes_table(name=name,gender=gender,age=age,blood_pressure=blood_pressure,glucose=glucose,insulin=insulin,bmi=bmi,skin_thickness=skin_thickness,result="Non Diabetics")
            data.save()
            return render(request,'output-2.html')
        else:
            data = Diabetes_table(name=name,gender=gender,age=age,blood_pressure=blood_pressure,glucose=glucose,insulin=insulin,bmi=bmi,skin_thickness=skin_thickness,result="Diabetics")
            data.save()
            return render(request,'output-1.html')
        # data = Diabetes_table(name=name,gender=gender,age=age,blood_pressure=blood_pressure,glucose=glucose,insulin=insulin,insulin_name=insulin_name,skin_thickness=skin_thickness)
        # data.save()
        time.sleep(60)
    print("******************************")
    
    return render(request,'risk.html')