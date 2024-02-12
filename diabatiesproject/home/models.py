from django.db import models

# Create your models here.
class Diabetes(models.Model):
    Pregnancies = models.IntegerField()
    Glucose = models.IntegerField()
    BloodPressure = models.IntegerField()
    SkinThickness = models.IntegerField()
    Insulin = models.IntegerField()
    BMI = models.FloatField()
    DiabetesPedigreeFunction = models.FloatField()
    Age = models.IntegerField()
    Outcome = models.IntegerField()

class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to="excel")
