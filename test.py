from unittest import TestCase
from app import app
from flask import Flask
from forex_python.converter import CurrencyCodes, CurrencyRates


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_convert_from_currency(self):
        """Make sure from Currency Code is properly selected"""
    # we are looking to make sure that USD = USD, EURO = EURO etc.
    
    def test_convert_to_currency(self):
        """Make sure to Currency Code is properly selcect"""
    # we are looking to make sure that USD = USD, EURO = EURO etc.
    
    def test_convert_currencies(self):
        """make sure the conversion is working"""