#!/usr/bin/env python3
"""
Integration tests for GithubOrgClient
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the mock for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.m_get = cls.get_patcher.start()

        # Define the side effect to return fixture data based on URL
        def json_si(url):
            if url == "https://api.github.com/orgs/test_org":
                return cls.org_payload
            elif url == "https://api.github.com/orgs/test_org/repos":
                return cls.repos_payload
            return None

        # Configure the mock to use the side effect
        cls.m_get.side_effect = lambda url: Mock(json=lambda: json_si(url))

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that public_repos returns the expected repository names."""
        c = GithubOrgClient("test_org")
        self.assertEqual(c.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test that public_repos returns repos with the specified license."""
        c = GithubOrgClient("test_org")
        self.assertEqual(c.public_repos(license="apache-2.0"), self.apache2_repos)
