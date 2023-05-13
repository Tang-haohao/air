from django.test import TestCase

# Create your tests here.
# test.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Air
import json


class AirTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_air = Air.objects.create(
            airCode="Test",
            airCna="Test",
            status="Active",
            reserve1="Test1",
            reserve2="Test2",
            reserve3="Test3",
            reserve4="Test4",
            reserve5="Test5",
            airC="TestC",
            airF="TestF",
            airFna="TestFna",
            airTotal="TestTotal",
            airY="TestY",
            airYna="TestYna"
        )

    def test_list(self):
        response = self.client.get(reverse('air_list'))  # Assuming 'air_list' as url name for list view
        self.assertEqual(response.status_code, 200)

    def test_info(self):
        response = self.client.get(
            reverse('air_info', kwargs={'id': self.test_air.id}))  # Assuming 'air_info' as url name for info view
        self.assertEqual(response.status_code, 200)

    def test_info1(self):
        response = self.client.get(reverse('air_info1', kwargs={
            'airCode': self.test_air.airCode}))  # Assuming 'air_info1' as url name for info1 view
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.client.get(
            reverse('air_delete', kwargs={'id': self.test_air.id}))  # Assuming 'air_delete' as url name for delete view
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Air.objects.filter(id=self.test_air.id).exists())

    def test_update(self):
        updated_data = {
            'airCode': 'Updated',
            'airCna': 'Updated'
        }
        response = self.client.post(reverse('air_update'), data=json.dumps(updated_data),
                                    content_type='application/json')  # Assuming 'air_update' as url name for update view
        self.assertEqual(response.status_code, 200)
        self.test_air.refresh_from_db()
        self.assertEqual(self.test_air.airCode, 'Updated')
        self.assertEqual(self.test_air.airCna, 'Updated')

    def test_page(self):
        data = {
            'pageNum': 1,
            'pageSize': 10,
            'search': None
        }
        response = self.client.post(reverse('air_page'), data=json.dumps(data),
                                    content_type='application/json')  # Assuming 'air_page' as url name for page view
        self.assertEqual(response.status_code, 200)

    def test_save(self):
        data = {
            'airCode': 'New',
            'airCna': 'New',
            'status': 'Active',
            'reserve1': 'New1',
            'reserve2': 'New2',
            'reserve3': 'New3',
            'reserve4': 'New4',
            'reserve5': 'New5',
            'airC': 'NewC',
            'airF': 'NewF',
            'airFna': 'NewFna',
            'airTotal': 'NewTotal',
            'airY': 'NewY',
            'airYna': 'NewYna'
        }
        response = self.client.post(reverse('air_save'), data=json.dumps(data),
                                    content_type='application/json')  # Assuming 'air_save' as url name for save view
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Air.objects.filter(airCode='New').exists())

