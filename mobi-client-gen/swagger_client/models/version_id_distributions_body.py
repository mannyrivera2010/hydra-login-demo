# coding: utf-8

"""
    Mobi

    Mobi REST API Documentation  # noqa: E501

    OpenAPI spec version: 1.22.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class VersionIdDistributionsBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'title': 'str',
        'description': 'str',
        'format': 'str',
        'access_url': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'format': 'format',
        'access_url': 'accessURL',
        'download_url': 'downloadURL'
    }

    def __init__(self, title=None, description=None, format=None, access_url=None, download_url=None):  # noqa: E501
        """VersionIdDistributionsBody - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._description = None
        self._format = None
        self._access_url = None
        self._download_url = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if format is not None:
            self.format = format
        if access_url is not None:
            self.access_url = access_url
        if download_url is not None:
            self.download_url = download_url

    @property
    def title(self):
        """Gets the title of this VersionIdDistributionsBody.  # noqa: E501

        String representing the Version ID  # noqa: E501

        :return: The title of this VersionIdDistributionsBody.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this VersionIdDistributionsBody.

        String representing the Version ID  # noqa: E501

        :param title: The title of this VersionIdDistributionsBody.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this VersionIdDistributionsBody.  # noqa: E501

        Required title for the new Distribution. If the title is null, throws a 400 Response  # noqa: E501

        :return: The description of this VersionIdDistributionsBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VersionIdDistributionsBody.

        Required title for the new Distribution. If the title is null, throws a 400 Response  # noqa: E501

        :param description: The description of this VersionIdDistributionsBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def format(self):
        """Gets the format of this VersionIdDistributionsBody.  # noqa: E501

        Optional format string for the new Distribution. Expects a MIME type  # noqa: E501

        :return: The format of this VersionIdDistributionsBody.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this VersionIdDistributionsBody.

        Optional format string for the new Distribution. Expects a MIME type  # noqa: E501

        :param format: The format of this VersionIdDistributionsBody.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def access_url(self):
        """Gets the access_url of this VersionIdDistributionsBody.  # noqa: E501

        Optional access URL for the new Distribution  # noqa: E501

        :return: The access_url of this VersionIdDistributionsBody.  # noqa: E501
        :rtype: str
        """
        return self._access_url

    @access_url.setter
    def access_url(self, access_url):
        """Sets the access_url of this VersionIdDistributionsBody.

        Optional access URL for the new Distribution  # noqa: E501

        :param access_url: The access_url of this VersionIdDistributionsBody.  # noqa: E501
        :type: str
        """

        self._access_url = access_url

    @property
    def download_url(self):
        """Gets the download_url of this VersionIdDistributionsBody.  # noqa: E501

        Optional download URL for the new Distribution  # noqa: E501

        :return: The download_url of this VersionIdDistributionsBody.  # noqa: E501
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        """Sets the download_url of this VersionIdDistributionsBody.

        Optional download URL for the new Distribution  # noqa: E501

        :param download_url: The download_url of this VersionIdDistributionsBody.  # noqa: E501
        :type: str
        """

        self._download_url = download_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(VersionIdDistributionsBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VersionIdDistributionsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
