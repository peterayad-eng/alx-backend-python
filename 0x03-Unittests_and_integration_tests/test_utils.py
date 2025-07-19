#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock

class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests that access_nested_map returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        """Tests that access_nested_map raises KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{expected_key}'")

class TestGetJson(unittest.TestCase):
    """Tests the get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Tests that get_json returns the expected result.
        """
        # Configure the mock to return a Mock object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function
        result = get_json(test_url)

        # Test that the mocked get method was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)

        # Test that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """Tests the memoize decorator.
    """
    def test_memoize(self):
        """Tests that memoize decorator works correctly.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock the a_method
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # Create an instance of TestClass
            test_instance = TestClass()

            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Test that both calls return the correct result
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Test that a_method was called only once
            mock_method.assert_called_once()

