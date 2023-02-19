from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from api.views import *

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': [
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ]
}
factory = APIRequestFactory()


class TestAPIs(APITestCase):
    def setUp(self):
        User.objects.create(id=1, password="123", last_login=None, is_active=1, is_staff=1, is_superuser=1,
                            username="user", first_name="user", last_name="user", email="123",
                            date_joined="2023-02-12 14:34:53.359639")

        Product.objects.create(id=1, name="test_product_1", min_duration=1, max_duration=100, min_amount=1,
                               max_amount=300, type='test_type_1')
        Product.objects.create(id=2, name="test_product_2", min_duration=200, max_duration=600, min_amount=200,
                               max_amount=500, type='test_type_2')

        Promo.objects.create(id=1, product_id=1, description="test_1")
        Promo.objects.create(id=2, product_id=2, description="test_2")

        Support_Request.objects.create(id=1, date="2023-02-12", topic="test_1", name="test_1", phone_num="1234567")
        Support_Request.objects.create(id=2, date="2023-02-12", topic="test_2", name="test_2", phone_num="1234567")

        Interest_Rate.objects.create(id=1, duration_more_than=1, duration_less_than_or_equal=100, rate=3.9,
                                     product_id=1)
        Interest_Rate.objects.create(id=2, duration_more_than=1, duration_less_than_or_equal=400, rate=15.9,
                                     product_id=2)

        ClientProfile.objects.create(id=1, name="test_1", last_name="test_1", phone_number="123", type="test",
                                     user_id=1)
        ClientProfile.objects.create(id=2, name="test_2", last_name="test_2", phone_number="123", type="test",
                                     user_id=1)

        Application.objects.create(id=1, product_id=1, client_profile_id=1, date_applied="2023-02-12", status="fdsfds")
        Application.objects.create(id=2, product_id=2, client_profile_id=2, date_applied="2023-02-12", status="fdsfds")

        Deal.objects.create(id=1, duration=1, rate=1.0, loan_amount=10000, regular_payment_size=111, status="test", payment_by_deed=100, client_profile_id=1, product_id=1)
        Deal.objects.create(id=2, duration=1, rate=1.0, loan_amount=10000, regular_payment_size=111, status="test", payment_by_deed=100, client_profile_id=2, product_id=2)
    # PRODUCTS
    def test_products_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/products')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_products_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/productss')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_products_post(self):
        sample = {
            "name": "test",
            "min_duration": 1,
            "max_duration": 100,
            "type": "test",
            "min_amount": 1.0,
            "max_amount": 100.0
        }
        response = self.client.post('http://127.0.0.1:8000/api/products', sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_products_post_invalid_data(self):
        sample = {
            "name": "test",
            "min_duration": 'hhhh',
            "max_duration": 100,
            "type": "test",
            "min_amount": 1.0,
            "max_amount": 100.0
        }
        response = self.client.post('http://127.0.0.1:8000/api/products', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_products_post_no_data(self):
        response = self.client.post('http://127.0.0.1:8000/api/products')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_products_wrong_method(self):
        response = self.client.put('http://127.0.0.1:8000/api/products')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_product_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/products/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_product_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/products/234556')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_product_wrong_method(self):
        response = self.client.post('http://127.0.0.1:8000/api/products/1')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_product_put(self):
        sample = {
            "id": 1,
            "name": "test",
            "min_duration": 1,
            "max_duration": 100,
            "type": "test",
            "min_amount": 1.0,
            "max_amount": 100.0
        }
        response = self.client.put('http://127.0.0.1:8000/api/products/1', sample)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_product_put_not_found(self):
        sample = {
            "id": 1,
            "name": "test",
            "min_duration": 1,
            "max_duration": 100,
            "type": "test",
            "min_amount": 1.0,
            "max_amount": 100.0
        }
        response = self.client.put('http://127.0.0.1:8000/api/products/788787', sample)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_product_put_wrong_data(self):
        sample = {
            "id": 1,
            "name": "test",
            "min_duration": "7jhjkj",
            "max_duration": 100,
            "type": "test",
            "min_amount": 1.0,
            "max_amount": 100.0
        }
        response = self.client.put('http://127.0.0.1:8000/api/products/1', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_single_product_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/api/products/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # PROMOS
    def test_promos_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/news')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_promos_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/newss')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_promos_post(self):
        sample = {
            "id": 1,
            "product": 1,
            "description": "23456jbh"
        }
        response = self.client.post('http://127.0.0.1:8000/api/news', sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_promos_post_invalid_data(self):
        sample = {
            "id": 1,
            "product": "j",
            "description": "23456jbh"
        }
        response = self.client.post('http://127.0.0.1:8000/api/news', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_promos_post_no_data(self):
        response = self.client.post('http://127.0.0.1:8000/api/news')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_promos_wrong_method(self):
        response = self.client.put('http://127.0.0.1:8000/api/news')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_promo_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/news/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_promo_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/news/234556')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_promo_wrong_method(self):
        response = self.client.post('http://127.0.0.1:8000/api/news/1')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_promo_put(self):
        sample = {
            "id": 1,
            "product": 2,
            "description": "23456jbh"
        }
        response = self.client.put('http://127.0.0.1:8000/api/news/1', sample)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_promo_put_not_found(self):
        sample = {
            "id": 1,
            "product": 1,
            "description": "23456jbh"
        }
        response = self.client.put('http://127.0.0.1:8000/api/news/788787', sample)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_promo_put_wrong_data(self):
        sample = {
            "id": 1,
            "product": "jj",
            "description": "23456jbh"
        }
        response = self.client.put('http://127.0.0.1:8000/api/news/1', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_single_promo_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/api/news/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # SUPPORT
    def test_support_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/support_requests')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_support_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/support_requestss')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_support_post(self):
        sample = {
            "id": 4,
            "date": "2023-02-12",
            "topic": "test1",
            "name": "uiouiodsf",
            "phone_num": "89793423"
        }
        response = self.client.post('http://127.0.0.1:8000/api/support_requests', sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_support_post_invalid_data(self):
        sample = {
            "id": 4,
            "date": 7,
            "topic": "test1",
            "name": "uiouiodsf",
            "phone_num": "89793423"
        }
        response = self.client.post('http://127.0.0.1:8000/api/support_requests', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_support_post_no_data(self):
        response = self.client.post('http://127.0.0.1:8000/api/support_requests')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_support_wrong_method(self):
        response = self.client.put('http://127.0.0.1:8000/api/support_requests')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_support_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/support_requests/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_support_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/support_requests/234556')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_support_wrong_method(self):
        response = self.client.post('http://127.0.0.1:8000/api/support_requests/1')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_support_put(self):
        sample = {
            "id": 2,
            "date": "2023-02-12",
            "topic": "test1",
            "name": "uiouiodsf",
            "phone_num": "89793423"
        }
        response = self.client.put('http://127.0.0.1:8000/api/support_requests/1', sample)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_support_put_not_found(self):
        sample = {
            "id": 4,
            "date": "2023-02-12",
            "topic": "test1",
            "name": "uiouiodsf",
            "phone_num": "89793423"
        }
        response = self.client.put('http://127.0.0.1:8000/api/support_requests/788787', sample)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_support_put_wrong_data(self):
        sample = {
            "id": 2,
            "date": 88,
            "topic": "test1",
            "name": "uiouiodsf",
            "phone_num": "89793423"
        }
        response = self.client.put('http://127.0.0.1:8000/api/support_requests/1', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_single_support_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/api/support_requests/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # INTEREST RATE
    def test_rates_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/interest_rates')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_rates_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/interest_ratess')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_rates_post(self):
        sample = {
            "id": 1,
            "product": 2,
            "duration_more_than": 3,
            "duration_less_than_or_equal": 100,
            "rate": 15.0
        }
        response = self.client.post('http://127.0.0.1:8000/api/interest_rates', sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rates_post_invalid_data(self):
        sample = {
            "id": 1,
            "product": 2,
            "duration_more_than": 3,
            "duration_less_than_or_equal": 100,
            "rate": "f"
        }
        response = self.client.post('http://127.0.0.1:8000/api/interest_rates', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rates_post_no_data(self):
        response = self.client.post('http://127.0.0.1:8000/api/interest_rates')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rates_wrong_method(self):
        response = self.client.put('http://127.0.0.1:8000/api/interest_rates')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_rate_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/interest_rates/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_rate_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/interest_rates/234556')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_rate_wrong_method(self):
        response = self.client.post('http://127.0.0.1:8000/api/interest_rates/1')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_rate_put(self):
        sample = {
            "id": 2,
            "product": 1,
            "duration_more_than": 3,
            "duration_less_than_or_equal": 100,
            "rate": 15.0
        }
        response = self.client.put('http://127.0.0.1:8000/api/interest_rates/2', sample)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_rate_put_not_found(self):
        sample = {
            "id": 2,
            "product": 1,
            "duration_more_than": 3,
            "duration_less_than_or_equal": 100,
            "rate": 15.0
        }
        response = self.client.put('http://127.0.0.1:8000/api/interest_rates/788787', sample)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_rate_put_wrong_data(self):
        sample = {
            "id": 1,
            "product": "fdfsdf",
            "duration_more_than": 3,
            "duration_less_than_or_equal": 100,
            "rate": 15.0
        }
        response = self.client.put('http://127.0.0.1:8000/api/interest_rates/1', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_single_rate_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/api/interest_rates/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # CLIENT PROFILE
    def test_clients_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/client_profiles')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_clients_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/client_profiless')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_clients_post(self):
        sample = {
            "id": 1,
            "name": "test",
            "last_name": "test",
            "phone_number": "12345",
            "type": "Физлицо",
            "user": 1
        }
        response = self.client.post('http://127.0.0.1:8000/api/client_profiles', sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_clients_post_invalid_data(self):
        sample = {
            "id": 1,
            "name": "test",
            "last_name": "test",
            "phone_number": "12345",
            "type": "Физлицо",
            "user": "fdg"
        }
        response = self.client.post('http://127.0.0.1:8000/api/client_profiles', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_clients_post_no_data(self):
        response = self.client.post('http://127.0.0.1:8000/api/client_profiles')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_clients_wrong_method(self):
        response = self.client.put('http://127.0.0.1:8000/api/client_profiles')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_client_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/client_profiles/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_client_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/client_profiles/234556')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_client_wrong_method(self):
        response = self.client.post('http://127.0.0.1:8000/api/client_profiles/1')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_client_put(self):
        sample = {
            "id": 2,
            "name": "test",
            "last_name": "test",
            "phone_number": "1sfdfdsf2345",
            "type": "Физлицо",
            "user": 1
        }
        response = self.client.put('http://127.0.0.1:8000/api/client_profiles/2', sample)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_client_put_not_found(self):
        sample = {
            "id": 1,
            "name": "test",
            "last_name": "test",
            "phone_number": "12345",
            "type": "Физлицо",
            "user": 1
        }
        response = self.client.put('http://127.0.0.1:8000/api/client_profiles/788787', sample)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_client_put_wrong_data(self):
        sample = {
            "id": 1,
            "name": "test",
            "last_name": "test",
            "phone_number": "12345",
            "type": "Физлицо",
            "user": "fdsfds"
        }
        response = self.client.put('http://127.0.0.1:8000/api/client_profiles/1', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_single_client_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/api/client_profiles/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # APPLICATION
    def test_applications_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/applications')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_applications_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/applicationss')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_applications_post(self):
        sample = {
            "id": 1,
            "client_profile": 1,
            "product": 1,
            "date_applied": "2023-02-12",
            "status": "Одобрена"
        }
        response = self.client.post('http://127.0.0.1:8000/api/applications', sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_applications_post_invalid_data(self):
        sample = {
            "id": 1,
            "client_profile": "fdsfsd",
            "product": 1,
            "date_applied": "2023-02-12",
            "status": "Одобрена"
        }
        response = self.client.post('http://127.0.0.1:8000/api/applications', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_applications_post_no_data(self):
        response = self.client.post('http://127.0.0.1:8000/api/applications')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_applications_wrong_method(self):
        response = self.client.put('http://127.0.0.1:8000/api/applications')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_application_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/applications/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_application_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/applications/234556')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_application_wrong_method(self):
        response = self.client.post('http://127.0.0.1:8000/api/applications/1')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_application_put(self):
        sample = {
            "id": 2,
            "client_profile": 2,
            "product": 1,
            "date_applied": "2023-02-12",
            "status": "Одобрена"
        }
        response = self.client.put('http://127.0.0.1:8000/api/applications/2', sample)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_application_put_not_found(self):
        sample = {
            "id": 1,
            "client_profile": 2,
            "product": 1,
            "date_applied": "2023-02-12",
            "status": "Одобрена"
        }
        response = self.client.put('http://127.0.0.1:8000/api/applications/788787', sample)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_application_put_wrong_data(self):
        sample = {
            "id": 1,
            "client_profile": "dsfdsf",
            "product": 1,
            "date_applied": "2023-02-12",
            "status": "Одобрена"
        }
        response = self.client.put('http://127.0.0.1:8000/api/applications/1', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_single_application_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/api/applications/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # DEAL
    def test_deals_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/deals')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_deals_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/dealss')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_deals_post(self):
        sample = {
            "id": 1,
            "client_profile": 1,
            "product": 1,
            "duration": 300,
            "rate": 3.0,
            "loan_amount": 100000.0,
            "regular_payment_size": 100000.0,
            "status": "В анализе",
        }
        response = self.client.post('http://127.0.0.1:8000/api/deals', sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_deals_post_invalid_data(self):
        sample = {
            "id": 1,
            "client_profile": "j",
            "product": 1,
            "duration": 300,
            "rate": 3.0,
            "loan_amount": 100000.0,
            "regular_payment_size": 100000.0,
            "status": "В анализе",
        }
        response = self.client.post('http://127.0.0.1:8000/api/deals', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deals_post_no_data(self):
        response = self.client.post('http://127.0.0.1:8000/api/deals')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_deals_wrong_method(self):
        response = self.client.put('http://127.0.0.1:8000/api/deals')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_deal_get(self):
        response = self.client.get('http://127.0.0.1:8000/api/deals/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_deal_get_not_found(self):
        response = self.client.get('http://127.0.0.1:8000/api/deals/234556')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_deal_wrong_method(self):
        response = self.client.post('http://127.0.0.1:8000/api/deals/1')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_single_deal_put(self):
        sample = {
            "id": 1,
            "client_profile": 2,
            "product": 2,
            "duration": 300,
            "rate": 3.0,
            "loan_amount": 100000.0,
            "regular_payment_size": 100000.0,
            "status": "В анализе",
        }
        response = self.client.put('http://127.0.0.1:8000/api/deals/1', sample)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_single_deal_put_not_found(self):
        sample = {
            "id": 1,
            "client_profile": 1,
            "product": 1,
            "duration": 300,
            "rate": 3.0,
            "loan_amount": 100000.0,
            "regular_payment_size": 100000.0,
            "status": "В анализе",
        }
        response = self.client.put('http://127.0.0.1:8000/api/deals/788787', sample)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_single_deal_put_wrong_data(self):
        sample = {
            "id": 1,
            "client_profile": "798h",
            "product": 1,
            "duration": 300,
            "rate": 3.0,
            "loan_amount": 100000.0,
            "regular_payment_size": 100000.0,
            "status": "В анализе",
        }
        response = self.client.put('http://127.0.0.1:8000/api/deals/1', sample)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_single_deal_delete(self):
        response = self.client.delete('http://127.0.0.1:8000/api/deals/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
