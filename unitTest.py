import unittest
from Weather_API import get_info, create_URL, get_data


class unitTest(unittest.TestCase):
    def test_get_info(self):
        location = 'Houston'
        self.assertNotEquals(location, '')

    def test_get_data(self):
        key = 'LCRCQE8SWKLGXT6837WYWGATZ'
        location = 'Houston'
        url = create_URL(key, location)
        response = get_data(url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
