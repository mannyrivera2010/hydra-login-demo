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
from swagger_client.api.mappings_api import MappingsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMappingsApi(unittest.TestCase):
    """MappingsApi unit test stubs"""

    def setUp(self):
        self.api = MappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_mapping(self):
        """Test case for delete_mapping

        Delete an uploaded mapping  # noqa: E501
        """
        pass

    def test_get_mapping(self):
        """Test case for get_mapping

        Retrieve JSON-LD of an uploaded mapping  # noqa: E501
        """
        pass

    def test_upload2(self):
        """Test case for upload2

        Upload mapping sent as form data  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()