from django.test import Client, TestCase

from django.contrib.auth.models import User

from .forms import UserRegistrationForm


class RegisterTestCase(TestCase):

    TAKEN_USERNAME = 'emma'
    TAKEN_EMAIL = 'watson@hogwart.uk'

    def setUp(self):
        User.objects.create(username = self.TAKEN_USERNAME,
                            email    = self.TAKEN_EMAIL,
                            password = 'knowledge2000')

    def test_register_url_returns_registration_page(self):
        ''' Test that /register/ path returns registration form. '''
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_successful_registration_redirects_to_user_profile(self):
        response = self.client.post('/register/',
                    {'username':'john',
                     'gender': 1,
                     'email': 'johnsmith@gmail.com',
                     'password': '12345678'
                     })
        self.assertRedirects(response, '/john')

    def test_registration_fails_if_username_already_exists(self):
        response = self.client.post('/register/',
                    {'username':self.TAKEN_USERNAME,
                     'gender': 1,
                     'email': 'johnsmith@gmail.com',
                     'password': '12345678'
                     })
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
        "User with that 'username' or 'email' already exists:(")

    def test_registration_fails_if_email_already_exists(self):
        response = self.client.post('/register/',
                    {'username': 'sarah',
                     'gender': 1,
                     'email': self.TAKEN_EMAIL,
                     'password': '12345678'
                     })
        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
        "User with that 'username' or 'email' already exists:(")

    def test_registration_fails_if_no_email_given(self):
        response = self.client.post('/register/',
                    {'username': 'sarah',
                        'gender': 1,
                        'email': '',
                        'password': '12345678'
                        })
        self.assertFormError(response, 'form', 'email', 'Please enter your email address :)')

    def test_registration_fails_if_invalid_email_given(self):
        response = self.client.post('/register/',
                    {'username': 'sarah',
                        'gender': 1,
                        'email': 'abcde',
                        'password': '12345678'
                        })
        self.assertFormError(response, 'form', 'email', 'Please enter a valid email address :(')

    def test_registration_fails_if_no_username_given(self):
        response = self.client.post('/register/',
                    {'username': '',
                        'gender': 1,
                        'email': 'sarah@mail.ru',
                        'password': '12345678'
                        })
        self.assertFormError(response, 'form', 'username', 'Please enter your username :)')

    def test_registration_fails_if_no_password_given(self):
        response = self.client.post('/register/',
                    {'username': 'sarah',
                        'gender': 1,
                        'email': 'sarah@mail.ru',
                        'password': '' 
                        })
        self.assertFormError(response, 'form', 'password', 'Please enter your password :)')
