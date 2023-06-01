import os
import csv
import unittest
import requests

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOADS_PATH = os.path.join(PROJECT_ROOT, 'uploads')
TEST_FILE_PATH = os.path.join(UPLOADS_PATH, 'test.csv')


def create_test_file():
    # Создаем директорию uploads, если она не существует
    if not os.path.exists(UPLOADS_PATH):
        os.makedirs(UPLOADS_PATH)

    # Создаем тестовый файл
    with open(TEST_FILE_PATH, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['John', '25'])
        writer.writerow(['Alice', '30'])


class ServiceTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        create_test_file()

    def test_upload_file(self):
        url = 'http://localhost:5000/upload'
        files = {'file': open(TEST_FILE_PATH, 'rb')}
        response = requests.post(url, files=files)
        self.assertEqual(response.status_code, 200)

    def test_get_files(self):
        url = 'http://localhost:5000/files'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        files = response.json().get('files')
        self.assertIsInstance(files, list)

    def test_get_data(self):
        url = 'http://localhost:5000/data'
        params = {'filename': 'test.csv'}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        data = response.json().get('data')
        self.assertIsInstance(data, list)

    def test_delete_file(self):
        url = 'http://localhost:5000/delete/test.csv'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
