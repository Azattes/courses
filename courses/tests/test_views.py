from django.test import TestCase, Client
from django.urls import reverse
from courses.models import Category, Course, Contact, Branch
from courses.serializers import CourseSerializers
import json


class CoursesListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        counter = 10
        Category.objects.create(name = "test category", imgpath = "some image")

        for i in range(1, counter + 1):
            Course.objects.create(name = "test course" + str(i), description = "lie-lie" + str(i), logo = "logo" + str(i), category = Category.objects.get(id=1))
            Contact.objects.create(name = 3, value = "blackranger@gmail.com" + str(i), course = Course.objects.get(id=i))
            Branch.objects.create(latitude = "19.062001" + str(i), longitude = "05.112000" + str(i), address = "Djunusalieva 220" + str(i), course = Course.objects.get(id=i))


    def test_lists_all_courses(self):
        response = self.client.get(reverse('courses_list'))
        self.assertEqual(response.status_code, 200)


class CourseDetailsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        counter = 2
        Category.objects.create(name = "test category", imgpath = "some image")

        for i in range(1, counter + 1):
            Course.objects.create(name = "test course" + str(i), description = "lie-lie" + str(i), logo = "logo" + str(i), category = Category.objects.get(id=1))
            Contact.objects.create(name = 3, value = "blackranger@gmail.com" + str(i), course = Course.objects.get(id=i))
            Branch.objects.create(latitude = "19.062001" + str(i), longitude = "05.112000" + str(i), address = "Djunusalieve 220" + str(i), course = Course.objects.get(id=i))

    def test_course_details_GET(self):
        response = self.client.get(reverse('coursesID', kwargs ={'pk': Course.objects.get(id=1).pk}))
        serializer = CourseSerializers(Course.objects.get(id=1))

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_course_details_GET_invalid(self):
        response = self.client.get(reverse('coursesID', kwargs ={'pk': Course.objects.get(id=1).pk}))
        serializer = CourseSerializers(Course.objects.get(id=2))
        
        self.assertFalse(response.data == serializer.data)
        self.assertEqual(response.status_code, 200)

    def test_course_details_DELETE(self):
        response = self.client.delete(reverse('coursesID', kwargs ={'pk': Course.objects.get(id=2).pk}))

        self.assertEquals(response.status_code, 204)
    
