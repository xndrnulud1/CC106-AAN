<<<<<<< HEAD
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class StaffAuthenticationTests(TestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff',
            password='Staff-Test-Password!',
            is_staff=True,
        )
        self.regular = User.objects.create_user(
            username='student',
            password='Student-Test-Password!',
            is_staff=False,
        )

    def test_login_page_is_public(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_users_are_redirected_to_login(self):
        response = self.client.get(reverse('staff_dashboard'))
        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('staff_dashboard')}",
        )

    def test_regular_user_cannot_access_staff_pages(self):
        self.client.login(username='student', password='Student-Test-Password!')
        response = self.client.get(reverse('staff_dashboard'))
        self.assertEqual(response.status_code, 302)

    def test_staff_user_can_access_dashboard(self):
        self.client.login(username='staff', password='Staff-Test-Password!')
        response = self.client.get(reverse('staff_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'staff')


class StaffDashboardQuickLinkTests(TestCase):
    def setUp(self):
        self.staff = User.objects.create_user(
            username='staff',
            password='Staff-Test-Password!',
            is_staff=True,
        )

    def test_staff_dashboard_has_student_directory_button(self):
        self.client.force_login(self.staff)
        response = self.client.get(reverse('staff_dashboard'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Student Management Dashboard')
        self.assertNotContains(response, 'Student Registration')
        self.assertContains(response, reverse('student_list'))
        self.assertContains(response, 'Open Student Directory')
=======
from django.contrib.messages import get_messages
from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentCrudMessageTests(TestCase):
    student_data = {
        'student_id': 'S1001',
        'first_name': 'Alex',
        'last_name': 'Morgan',
        'gender': 'Male',
        'date_of_birth': '2005-04-12',
        'contact_number': '555-0100',
    }

    def test_create_shows_success_message(self):
        response = self.client.post(
            reverse('student_create'),
            self.student_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            [str(message) for message in get_messages(response.wsgi_request)],
            ['Student record created successfully.'],
        )

    def test_update_shows_success_message(self):
        student = Student.objects.create(**self.student_data)
        updated_data = {**self.student_data, 'first_name': 'Jordan'}

        response = self.client.post(
            reverse('student_update', kwargs={'pk': student.pk}),
            updated_data,
        )

        student.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(student.first_name, 'Jordan')
        self.assertEqual(
            [str(message) for message in get_messages(response.wsgi_request)],
            ['Student record updated successfully.'],
        )

    def test_delete_shows_success_message(self):
        student = Student.objects.create(**self.student_data)

        response = self.client.post(
            reverse('student_delete', kwargs={'pk': student.pk}),
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(pk=student.pk).exists())
        self.assertEqual(
            [str(message) for message in get_messages(response.wsgi_request)],
            ['Student record deleted successfully.'],
        )

    def test_invalid_create_does_not_show_success_message(self):
        invalid_data = {**self.student_data, 'student_id': ''}

        response = self.client.post(reverse('student_create'), invalid_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Student.objects.count(), 0)
        self.assertEqual(list(get_messages(response.wsgi_request)), [])
>>>>>>> aae1622c46b2c75ac14801e20ae8ec9a373c9856
