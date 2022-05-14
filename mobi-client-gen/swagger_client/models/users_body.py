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

class UsersBody(object):
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
        'username': 'str',
        'password': 'str',
        'roles': 'list[str]',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password',
        'roles': 'roles',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email'
    }

    def __init__(self, username=None, password=None, roles=None, first_name=None, last_name=None, email=None):  # noqa: E501
        """UsersBody - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._password = None
        self._roles = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if password is not None:
            self.password = password
        if roles is not None:
            self.roles = roles
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email

    @property
    def username(self):
        """Gets the username of this UsersBody.  # noqa: E501

        Required username of the User to create  # noqa: E501

        :return: The username of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UsersBody.

        Required username of the User to create  # noqa: E501

        :param username: The username of this UsersBody.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this UsersBody.  # noqa: E501

        Required password of the User to create  # noqa: E501

        :return: The password of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UsersBody.

        Required password of the User to create  # noqa: E501

        :param password: The password of this UsersBody.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def roles(self):
        """Gets the roles of this UsersBody.  # noqa: E501

        List of roles of the User to create  # noqa: E501

        :return: The roles of this UsersBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UsersBody.

        List of roles of the User to create  # noqa: E501

        :param roles: The roles of this UsersBody.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def first_name(self):
        """Gets the first_name of this UsersBody.  # noqa: E501

        Optional first name of the User to create  # noqa: E501

        :return: The first_name of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UsersBody.

        Optional first name of the User to create  # noqa: E501

        :param first_name: The first_name of this UsersBody.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UsersBody.  # noqa: E501

        Optional last name of the User to create  # noqa: E501

        :return: The last_name of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UsersBody.

        Optional last name of the User to create  # noqa: E501

        :param last_name: The last_name of this UsersBody.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UsersBody.  # noqa: E501

        Optional email of the User to create  # noqa: E501

        :return: The email of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UsersBody.

        Optional email of the User to create  # noqa: E501

        :param email: The email of this UsersBody.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if issubclass(UsersBody, dict):
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
        if not isinstance(other, UsersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other