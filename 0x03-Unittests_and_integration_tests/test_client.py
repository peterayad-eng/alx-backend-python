#!/usr/bin/env python3
"""Module for testing client functions.
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        expected_payload = {"name": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(url)
        self.assertEqual(result, expected_payload)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL from .org"""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=unittest.mock.PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": https://api.github.com/orgs/google/repos
            }
            client = GithubOrgClient("google")
            self.assertEqual(
                client._public_repos_url,
                https://api.github.com/orgs/google/repos
            )
            # Ensure the `org` property was accessed once
            mock_org.assert_called_once()

        @patch('client.get_json')
        def test_public_repos(self, mock_get_json):
            """Test GithubOrgClient.public_repos returns expected repo list"""
            test_payload = [
                {"name": "repo1"},
                {"name": "repo2"},
            ]
            mock_get_json.return_value = test_payload

            with patch(
                    'client.GithubOrgClient._public_repos_url', 
                    new_callable=PropertyMock, 
                    return_value=https://api.github.com/orgs/testorg/repos
            ) as mock_url:
                client = GithubOrgClient("testorg")
                repos = client.public_repos()
                self.assertEqual(repos, ["repo1", "repo2"])

                mock_get_json.assert_called_once()
                mock_url.assert_called_once()
