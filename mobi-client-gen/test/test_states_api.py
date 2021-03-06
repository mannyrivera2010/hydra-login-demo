# coding: utf-8

"""
    Mobi

    Mobi REST API Documentation  # noqa: E501

    OpenAPI spec version: 1.22.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.states_api import StatesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStatesApi(unittest.TestCase):
    """StatesApi unit test stubs"""

    def setUp(self):
        self.api = StatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_state(self):
        """Test case for create_state

        Creates a new State for the User making the request  # noqa: E501
        """
        pass

    def test_delete_state(self):
        """Test case for delete_state

        Deletes State as long as it belongs to the User making the request  # noqa: E501
        """
        pass

    def test_get_state(self):
        """Test case for get_state

        Retrieves State by ID as long it belongs to the User making the request  # noqa: E501
        """
        pass

    def test_get_states(self):
        """Test case for get_states

        Retrieves State for the User making the request based on filter criteria  # noqa: E501
        """
        pass

    def test_update_state(self):
        """Test case for update_state

        Updates State as long as it belongs to the User making the request  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
