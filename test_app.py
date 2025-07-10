# test_app.py
import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Khởi tạo Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_main_page(self):
        # Gửi yêu cầu GET đến trang chủ
        response = self.app.get('/')
        # Kiểm tra mã trạng thái HTTP
        self.assertEqual(response.status_code, 200)
        # Kiểm tra nội dung phản hồi
        self.assertIn(b"Hello from Flask", response.data)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
