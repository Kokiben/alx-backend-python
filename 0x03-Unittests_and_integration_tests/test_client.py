#!/usr/bin/env python3
""" Module for testing client """


import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos

class TestGithubOrgClient(unittest.TestCase):
    
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        # Arrange
        org_client = GithubOrgClient(org_name)
        expected_payload = {"login": org_name}  # Mocked expected payload
        mock_get_json.return_value = expected_payload

        # Act
        result = org_client.org

        # Assert
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )
        self.assertEqual(result, expected_payload)


@parameterized_class(
    [
        {
            "org_payload": org_payload,
            "repos_payload": repos_payload,
            "expected_repos": expected_repos,
            "apache2_repos": apache2_repos,
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):    
    @classmethod
    def setUpClass(cls):
        # Start patching requests.get
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect to return the correct fixture based on the URL
        def mock_get_side_effect(url):
            if url == f'https://api.github.com/orgs/google':
                return cls.mock_response(cls.org_payload)
            elif url == f'https://api.github.com/orgs/google/repos':
                return cls.mock_response(cls.repos_payload)
            else:
                return cls.mock_response({})

        cls.mock_get.side_effect = mock_get_side_effect

    @classmethod
    def tearDownClass(cls):
        # Stop patching requests.get
        cls.get_patcher.stop()

    @staticmethod
    def mock_response(payload):
        """Helper method to create a mock response object."""
        mock_resp = patch('requests.Response')
        instance = mock_resp.start()
        instance.json.return_value = payload
        return instance

    def test_public_repos(self):
        # Arrange
        org_client = GithubOrgClient("google")

        # Act
        repos = org_client.public_repos()

        # Assert
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        # Arrange
        org_client = GithubOrgClient("google")

        # Act
        repos = org_client.public_repos(license="apache-2.0")

        # Assert
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
