from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
# from .serializers import CardSerializer
import json


from .models import CardModel


class CardFrontTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.card = CardModel.objects.create(
            card_name="Charizard",
            condition=4,
            category="Pokemon",
            owner=self.user,
            description="Final evolution of Charmander",
            year_set="1998",
            price="$100.00",
            card_num="404",
            promotional=True,

        )

    def test_string_representation(self):
        self.assertEqual(str(self.card.card_name), "Charizard")

    def test_card_content(self):
        self.assertEqual(f"{self.card.card_name}", "Charizard")
        self.assertEqual(f"{self.card.owner}", "tester")
        self.assertEqual(self.card.condition, 4)

    def test_list_page_status_code(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('card_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_status_code(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('card_list_detail', args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_context(self):
        self.client.login(username="tester", password="pass")  # need to log in
        url = reverse('card_list_detail', args=(1,))
        response = self.client.get(url)
        # print(response.__dir__())
        card = json.loads(response.content.decode('utf-8'))
        print(card)# Decode bytes and parse JSON
        self.assertEqual(card["card_name"], "Charizard")
        self.assertEqual(card["condition"], 4)
        # self.assertEqual(card["owner"], 1)


class CardApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()

        test_card = CardModel.objects.create(
            card_name="Charizard",
            condition=4,
            category="Pokemon",
            owner=testuser1,
            description="Final evolution of Charmander",
            year_set="1998",
            price="$100.00",
            card_num="404",
            promotional=True,
        )
        test_card.save()

    def test_cards_model(self):
        card = CardModel.objects.get(id=1)
        actual_owner = str(card.owner)
        actual_name = str(card.card_name)
        actual_description = str(card.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "Charizard")
        self.assertEqual(
            actual_description, "Final evolution of Charmander"
        )

    def test_get_card_list(self):
        self.client.login(username="testuser1", password="pass")  # need to log in
        url = reverse("card_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cards = json.loads(response.content.decode('utf-8'))  # Decode bytes and parse JSON
        self.assertEqual(len(cards), 1)
        self.assertEqual(cards[0]["card_name"], "Charizard")
