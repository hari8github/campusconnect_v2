import unittest
from std_bot import app

class TestCampusConnect(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_login_page(self):
        res = self.client.get('/login')
        self.assertEqual(res.status_code, 200)

    def test_signup_page(self):
        res = self.client.get('/signup/', follow_redirects=True)
        self.assertEqual(res.status_code, 200)

    def test_login_post_valid(self):
        res = self.client.post(
            '/login',
            data={
                'username': 'admin',
                'password': 'admin'
            },
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            follow_redirects=True
        )
        self.assertIn(b'Student Academic Chatbot', res.data)

if __name__ == '__main__':
    unittest.main()