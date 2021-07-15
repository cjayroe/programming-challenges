import unittest
from .solution import (
    find_user_by_name,
    get_data,
    get_users_posts_from_username1,
    get_users_posts_from_username2,
)


class ApiCallingTests(unittest.TestCase):
    def test_get_data(self):
        data = get_data("https://jsonplaceholder.typicode.com/users")
        self.assertIsNotNone(data)

    def test_find_user_by_name(self):
        user = {
            "id": 2,
            "name": "Ervin Howell",
            "username": "Antonette",
            "email": "Shanna@melissa.tv",
            "address": {
                "street": "Victor Plains",
                "suite": "Suite 879",
                "city": "Wisokyburgh",
                "zipcode": "90566-7771",
                "geo": {"lat": "-43.9509", "lng": "-34.4618"},
            },
            "phone": "010-692-6593 x09125",
            "website": "anastasia.net",
            "company": {
                "name": "Deckow-Crist",
                "catchPhrase": "Proactive didactic contingency",
                "bs": "synergize scalable supply-chains",
            },
        }

        found_user = find_user_by_name("howell")
        self.assertEqual(found_user, user)

    def test_get_users_posts_from_username1(self):
        posts = get_users_posts_from_username1("Lebsack")

        self.assertEqual(len(posts), 10)

    def test_get_users_posts_from_username2(self):
        posts = get_users_posts_from_username2("Lebsack")

        self.assertEqual(len(posts), 10)


if __name__ == "__main__":
    unittest.main()
