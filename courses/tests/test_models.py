from django.test import TestCase

from courses.models import Category, Course, Contact, Branch


class CourseModelTest(TestCase):
    @classmethod
    def setUpTest(cls):
        branch = Branch.objects.create(latitude='1233', longitude='2288', address='Bokonbaeva 198')
        contact = Contact.objects.create(choices = 'Phone')
        category = Category.objects.create(name='Language', imgpath='image')
        course=Course.objects.create(name='Java course', description='bla-bla', logo='Java logo')

    def test_contact(self):
        course_contact = Course.object.get(id = 1).contact.choice
        self.assertEquals(course_contact, 'Phone')

    def test_category(self):
        course_category = Course.objects.get(id=1).category.name
        course_img = Course.objects.get(id=1).category.imgpath
        self.assertEquals(course_category, "Language")
        self.assertEquals(course_img, "image")

    def test_branch(self):
        branch = Branch.objects.get(id=1)
        course = Course.objects.get(id=1)
        self.assertEquals(branch.course, course)
        branch_latitude = branch.latitude
        branch_longtitude = branch.longtitude
        branch_address = branch.adress
        self.assertEquals(branch_latitude, '1233')
        self.assertEquals(branch_longtitude, '2288')
        self.assertEquals(branch_address, 'Bokonbaeva 198')

    def test_course(self):
        max_length = Course.objects.get(id=1)._meta.get_field("description").max_length
        course_logo = Course.objects.get(id=1).category.logo
        self.assertEquals(max_length, 500)
        self.assertEquals(course_logo, 'Java logo')

