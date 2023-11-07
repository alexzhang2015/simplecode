import unittest
from flask import Flask
from sse import sse_blueprint, send_message

class TestSendMessage(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(sse_blueprint)
        self.client = self.app.test_client()

    def test_send_message_returns_string(self):
        response = self.client.get('/send')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, str)

    def test_send_message_publishes_message(self):
        with self.app.test_request_context('/send'):
            send_message()
            self.assertEqual(len(sse_blueprint.queue), 1)
            self.assertEqual(sse_blueprint.queue[0]['data'], b'{"message": "Hello!"}')

    def test_send_message_returns_correct_message(self):
        response = self.client.get('/send')
        self.assertEqual(response.data, b'Message sent!')

if __name__ == '__main__':
    unittest.main()