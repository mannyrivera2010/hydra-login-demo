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

class GroupsBody(object):
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
        'roles': 'list[str]',
        'members': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'roles': 'roles',
        'members': 'members'
    }

    def __init__(self, title=None, description=None, roles=None, members=None):  # noqa: E501
        """GroupsBody - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._description = None
        self._roles = None
        self._members = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if roles is not None:
            self.roles = roles
        if members is not None:
            self.members = members

    @property
    def title(self):
        """Gets the title of this GroupsBody.  # noqa: E501

        Title of the Group  # noqa: E501

        :return: The title of this GroupsBody.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GroupsBody.

        Title of the Group  # noqa: E501

        :param title: The title of this GroupsBody.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this GroupsBody.  # noqa: E501

        Description of the Group  # noqa: E501

        :return: The description of this GroupsBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GroupsBody.

        Description of the Group  # noqa: E501

        :param description: The description of this GroupsBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def roles(self):
        """Gets the roles of this GroupsBody.  # noqa: E501

        List of roles of the Group  # noqa: E501

        :return: The roles of this GroupsBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this GroupsBody.

        List of roles of the Group  # noqa: E501

        :param roles: The roles of this GroupsBody.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def members(self):
        """Gets the members of this GroupsBody.  # noqa: E501

        List of members of the Group  # noqa: E501

        :return: The members of this GroupsBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this GroupsBody.

        List of members of the Group  # noqa: E501

        :param members: The members of this GroupsBody.  # noqa: E501
        :type: list[str]
        """

        self._members = members

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
        if issubclass(GroupsBody, dict):
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
        if not isinstance(other, GroupsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other