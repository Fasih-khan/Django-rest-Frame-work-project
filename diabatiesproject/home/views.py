from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import pandas as pd
from django.conf import settings
import json

# Create your views here.


@api_view(['GET','POST'])
def home(request):
    print(request.data)
    context={}
    if request.method == 'POST':
        serializer = DiabatiesSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403 , 'payload': serializer.errors, 'message':'Data is not correct'})        
        serializer.save()
        context ={'results':serializer.data}
    
    
    return render(request,'diabetesRecords.html', context=context)


@api_view(['POST'])
def getdata(request):
    #exceled_upload_obj =  ExcelFileUpload.objects.create(excel_file_upload = request.data['files']) 
    #print(exceled_upload_obj)
    #print(exceled_upload_obj.excel_file_upload)
    df = pd.read_csv(f"{settings.BASE_DIR}/excel/Diabetes.csv")
    json_data = df.to_dict(orient ='records')
    #print(json_data[0])
    for i in range(0,len(json_data)):
        # print((df.loc[i].to_frame().T.to_json(orient ='records')))
        # df_final = df.loc[i].to_frame().T.to_json(orient ='records')
        serialzer = DiabatiesSerializer(data=json_data[i])
        if not serialzer.is_valid():
            print(serialzer.errors)
            return Response({'status':403 , 'payload': serialzer.errors, 'message':'Data is not correct'})        
        serialzer.save()
    return Response({'status':200 , 'message':'you sent'})

@api_view(['GET'])
def byOutcome(request):
    data=request.GET 
    Diabetes_obj=Diabetes.objects.filter(
        Outcome=data.get('Outcome'))
    #serializer=DiabetesSerializer(Diabetes_obj,many=True)
    #print(Diabetes_obj)
    context ={'results':Diabetes_obj}
    return render(request,'byOutcome.html', context=context)

@api_view(['GET'])
def byAgeRange(request):
    data=request.GET 
    Diabetes_obj=Diabetes.objects.filter(Age__range=(data.get('min_age'), data.get('max_age')))
    #serializer=DiabetesSerializer(Diabetes_obj,many=True)
    #print(Diabetes_obj)
    context ={'results':Diabetes_obj}
    return render(request,'byAge.html', context=context)


@api_view(['GET'])
def byBmiCategory(request):
    data=request.GET 
    Diabetes_obj=''
    if(data.get('bmi_category')=='overWeight'):
        Diabetes_obj=Diabetes.objects.filter(BMI__gt=25)

    elif(data.get('bmi_category')=='underWeight'):
        Diabetes_obj=Diabetes.objects.filter(BMI__lt=18)

    elif(data.get('bmi_category')=='normal'):
        Diabetes_obj=Diabetes.objects.filter(BMI__range=(18, 25))

    context ={'results':Diabetes_obj}

    #serializer=DiabetesSerializer(Diabetes_obj,many=True)
    #print(Diabetes_obj)
    return render(request,'byBmiCategory.html', context=context)

@api_view(['GET'])
def listOutcome(request):
    Diabetes_obj=Diabetes.objects.all()
    context ={'results':Diabetes_obj}
    return render(request,'listOutcome.html', context=context)


@api_view(['GET','PATCH','POST'])
def updateOutcome(request,Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome):

    Diabetes_obj=Diabetes.objects.get(Pregnancies=Pregnancies,Glucose=Glucose,BloodPressure=BloodPressure,SkinThickness=SkinThickness,
                                         Insulin=Insulin,BMI=BMI,DiabetesPedigreeFunction=DiabetesPedigreeFunction,Age=Age,Outcome=Outcome)
    if request.method =='PATCH':
        data=request.data
        u_outcome= data.get('Outcome')
        # u_age=data.get('Age')
        Diabetes_obj.Outcome = u_outcome
        # Diabetes_obj.Age = u_age
        Diabetes_obj.save()
        return redirect('/api/diabetes-records/update-outcome')
    if request.method =='POST'  :
        data=request.data
        u_outcome= data.get('Outcome')
        # u_age=data.get('Age')
        Diabetes_obj.Outcome = u_outcome
        # Diabetes_obj.Age = u_age
        Diabetes_obj.save()
        return redirect('/api/diabetes-records/update-outcome')
    context={'results':Diabetes_obj}
    return render(request,'updateData.html',context=context)


@api_view(['GET'])    
def byGlucoseRange(request):
    data=request.GET
    Diabetes.objects.filter(Glucose__range=(data.get('min_glucose'),data.get('max_glucose'))).delete()
    context= {'results':{'msg':'Data Deleted Successfully'}}
    return render(request,'deleteByGlucoseRange.html',context=context)

