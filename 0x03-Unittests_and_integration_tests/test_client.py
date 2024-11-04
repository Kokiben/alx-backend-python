#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Unit tests for GithubOrgClient class methods
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """
        Test the org method for various organizations.
        """
        c = GithubOrgClient(org)
        self.assertEqual(c.org, mock_get_json.return_value)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )

    def test_public_repos_url(self):
        """
        Test _public_repos_url property of GithubOrgClient.
        """
        with patch.object(
            GithubOrgClient, 'org', new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test_org/repos"
            }
            c = GithubOrgClient("test_org")
            self.assertEqual(c._public_repos_url,
                             mock_org.return_value["repos_url"])
            mock_org.assert_called_once()

    @patch('client.get_json', return_value=[
        {'name': 'Repo1'}, {'name': 'Repo2'}, {'name': 'Repo3'}
    ])
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos method to check the returned repository list.
        """
        with patch.object(
            GithubOrgClient, '_public_repos_url', new_callable=PropertyMock,
            return_value="https://api.github.com/orgs/test_org/repos"
        ):
            c = GithubOrgClient("test_org")
            repos = c.public_repos()
            self.assertEqual(repos, ['Repo1', 'Repo2', 'Repo3'])
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test has_license method to check if the repository has the specified
        license.
        """
        c = GithubOrgClient("test_org")
        self.assertEqual(c.has_license(repo, license_key), expected)


def requests_get(url):
    """
    Mocks requests.get to return predefined JSON data for integration tests.
    """
    class MockResponse:
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if url == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if url == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])
    return MockResponse(None)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient's public_repos method.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up for TestIntegrationGithubOrgClient: start patcher and initialize
        client.
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.c = GithubOrgClient("google")

    @classmethod
    def tearDownClass(cls):
        """
        Tear down TestIntegrationGithubOrgClient: stop patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repos method without license filter.
        """
        self.assertEqual(self.c.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test public_repos method with a specific license filter.
        """
        self.assertEqual(
            self.c.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
