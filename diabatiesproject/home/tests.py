from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .serializers import *
# Create your tests here.
class diabetesTestCases_home(TestCase):
    def setUp(self):
        pass

    def test_create_view(self):

        # Diabetes_obj=Diabetes.objects.create(Pregnancies= 10,
        #     Glucose= 10,
        #     BloodPressure= 10,
        #     SkinThickness= 10,
        #     Insulin=10,
        #     BMI=10,
        #     DiabetesPedigreeFunction=10,
        #     Age=10,
        #     Outcome=10
        # )
        # Diabetes_obj.save()
        # Diabetes_obj1 = Diabetes.objects.get(Pregnancies= 10,
        #     Glucose= 10,
        #     BloodPressure= 10,
        #     SkinThickness= 10,
        #     Insulin=10,
        #     BMI=10,
        #     DiabetesPedigreeFunction=10,
        #     Age=10,
        #     Outcome=10)
        # self.assertEqual(Diabetes_obj1,Diabetes_obj)
        response = self.client.get(reverse('home'))
        return self.assertEqual(response.status_code,200)

class diabetesTestCases_byOutcome(TestCase):
    def setUp(self):
        pass

    def test_create_view(self):
        response = self.client.get(reverse('byOutcome'))
        return self.assertEqual(response.status_code,200)

class diabetesTestCases_byAgeRange(TestCase):
    def setUp(self):
        pass

    def test_create_view(self):
        response = self.client.get(reverse('byAgeRange'))
        return self.assertEqual(response.status_code,200)


class diabetesTestCases_byBmiCategory(TestCase):
    def setUp(self):
        pass

    def test_create_view(self):
        response = self.client.get(reverse('byBmiCategory'))
        return self.assertEqual(response.status_code,200)


class diabetesTestCases_listOutcome(TestCase):
    def setUp(self):
        pass

    def test_create_view(self):
        response = self.client.get(reverse('listOutcome'))
        return self.assertEqual(response.status_code,200)


class diabetesTestCases_byGlucoseRange(TestCase):
    def setUp(self):
        pass

    def test_create_view(self):
        response = self.client.get(reverse('byGlucoseRange'))
        return self.assertEqual(response.status_code,200)



   
