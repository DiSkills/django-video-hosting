from django.test import TestCase
import requests


HEADERS = {'Accept': 'application/json'}
URL = 'http://localhost:8000/api/'


class APITestCase(TestCase):
    """ API tests """

    def test_get_all_categories(self):
        response = requests.get(URL + 'categories/', headers=HEADERS)
        data = response.json()
        true_data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "name": "Lections",
                    "slug": "lections"
                }
            ]
        }
        self.assertEqual(data, true_data)

    def test_get_all_videos(self):
        response = requests.get(URL + 'videos/', headers=HEADERS)
        data = response.json()
        true_data = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "category": 1,
                    "title": "GNU Linux 2",
                    "slug": "lections2",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in justo in nisl lacinia fermentum ac a ante. Suspendisse eu nulla purus. Maecenas facilisis mauris in leo molestie, nec bibendum mi faucibus. Aenean lacinia libero nisl, eget blandit neque pretium eu. Ut ex urna, efficitur quis congue consectetur, condimentum ultricies nisi. Aenean pulvinar erat eget quam hendrerit efficitur. Pellentesque nec mi sodales risus placerat molestie sed eu mauris. Nulla eu neque quis mauris pharetra venenatis nec id lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer nec porta lectus. Maecenas vulputate ex eu vehicula fermentum.",
                    "author": 1,
                    "file": "http://localhost:8000/media/1622974511.315084.mp4",
                    "created_at": "2021-06-06T10:15:11.315439Z",
                    "preview": "http://localhost:8000/media/1622974511.315493.png",
                    "views": 2
                },
                {
                    "category": 1,
                    "title": "GNU Linux",
                    "slug": "linux",
                    "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in justo in nisl lacinia fermentum ac a ante. Suspendisse eu nulla purus. Maecenas facilisis mauris in leo molestie, nec bibendum mi faucibus. Aenean lacinia libero nisl, eget blandit neque pretium eu. Ut ex urna, efficitur quis congue consectetur, condimentum ultricies nisi. Aenean pulvinar erat eget quam hendrerit efficitur. Pellentesque nec mi sodales risus placerat molestie sed eu mauris. Nulla eu neque quis mauris pharetra venenatis nec id lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer nec porta lectus. Maecenas vulputate ex eu vehicula fermentum.",
                    "author": 1,
                    "file": "http://localhost:8000/media/1622973257.624398.mp4",
                    "created_at": "2021-06-06T09:54:17.624921Z",
                    "preview": "http://localhost:8000/media/1622974425.265205.png",
                    "views": 5
                }
            ]
        }
        self.assertEqual(data, true_data)

    def test_get_category(self):
        response = requests.get(URL + 'category/1/', headers=HEADERS)
        data = response.json()
        true_data = {
            "id": 1,
            "name": "Lections",
            "slug": "lections"
        }
        self.assertEqual(data, true_data)

    def test_get_video(self):
        response = requests.get(URL + 'video/1/', headers=HEADERS)
        data = response.json()
        true_data = {
            "category": 1,
            "title": "GNU Linux",
            "slug": "linux",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In in justo in nisl lacinia fermentum ac a ante. Suspendisse eu nulla purus. Maecenas facilisis mauris in leo molestie, nec bibendum mi faucibus. Aenean lacinia libero nisl, eget blandit neque pretium eu. Ut ex urna, efficitur quis congue consectetur, condimentum ultricies nisi. Aenean pulvinar erat eget quam hendrerit efficitur. Pellentesque nec mi sodales risus placerat molestie sed eu mauris. Nulla eu neque quis mauris pharetra venenatis nec id lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Integer nec porta lectus. Maecenas vulputate ex eu vehicula fermentum.",
            "author": 1,
            "file": "http://localhost:8000/media/1622973257.624398.mp4",
            "created_at": "2021-06-06T09:54:17.624921Z",
            "preview": "http://localhost:8000/media/1622974425.265205.png",
            "views": 5
        }
        self.assertEqual(data, true_data)
