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
