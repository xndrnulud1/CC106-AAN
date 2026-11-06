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
