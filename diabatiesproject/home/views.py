from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import pandas as pd
from django.conf import settings
import json

# Create your views here.


@api_view(['GET'])
def home(request):
    # return Response({'status':200 , 'payload': serializer.data})
    data=request.GET
    #print(data.get('Glucose'),data.get('BMI'),data.get('Age'))
    diabaties_obj=Diabaties.objects.filter(
        Glucose=data.get('Glucose'),BMI = data.get('BMI'), Age = data.get('Age'))
    #serializer=DiabatiesSerializer(diabaties_obj,many=True)
    #print(diabaties_obj)
    context ={'results':diabaties_obj}
    return render(request,'diabatiesRecords.html', context=context)



@api_view(['POST'])
def getdata(request):
    #exceled_upload_obj =  ExcelFileUpload.objects.create(excel_file_upload = request.data['files']) 
    #print(exceled_upload_obj)
    #print(exceled_upload_obj.excel_file_upload)
    df = pd.read_csv(f"{settings.BASE_DIR}/excel/diabetes.csv")
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
