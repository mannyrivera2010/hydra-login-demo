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

class ShapesgraphsRecordIdBody(object):
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
        'file': 'str',
        'json': 'str',
        'branch_id': 'str',
        'commit_id': 'str',
        'replace_in_progress_commit': 'bool'
    }

    attribute_map = {
        'file': 'file',
        'json': 'json',
        'branch_id': 'branchId',
        'commit_id': 'commitId',
        'replace_in_progress_commit': 'replaceInProgressCommit'
    }

    def __init__(self, file=None, json=None, branch_id=None, commit_id=None, replace_in_progress_commit=None):  # noqa: E501
        """ShapesgraphsRecordIdBody - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._json = None
        self._branch_id = None
        self._commit_id = None
        self._replace_in_progress_commit = None
        self.discriminator = None
        if file is not None:
            self.file = file
        if json is not None:
            self.json = json
        if branch_id is not None:
            self.branch_id = branch_id
        if commit_id is not None:
            self.commit_id = commit_id
        if replace_in_progress_commit is not None:
            self.replace_in_progress_commit = replace_in_progress_commit

    @property
    def file(self):
        """Gets the file of this ShapesgraphsRecordIdBody.  # noqa: E501

        SHACL Shapes Graph file to upload.  # noqa: E501

        :return: The file of this ShapesgraphsRecordIdBody.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this ShapesgraphsRecordIdBody.

        SHACL Shapes Graph file to upload.  # noqa: E501

        :param file: The file of this ShapesgraphsRecordIdBody.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def json(self):
        """Gets the json of this ShapesgraphsRecordIdBody.  # noqa: E501

        SHACL Shapes Graph JSON-LD to upload  # noqa: E501

        :return: The json of this ShapesgraphsRecordIdBody.  # noqa: E501
        :rtype: str
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this ShapesgraphsRecordIdBody.

        SHACL Shapes Graph JSON-LD to upload  # noqa: E501

        :param json: The json of this ShapesgraphsRecordIdBody.  # noqa: E501
        :type: str
        """

        self._json = json

    @property
    def branch_id(self):
        """Gets the branch_id of this ShapesgraphsRecordIdBody.  # noqa: E501


        :return: The branch_id of this ShapesgraphsRecordIdBody.  # noqa: E501
        :rtype: str
        """
        return self._branch_id

    @branch_id.setter
    def branch_id(self, branch_id):
        """Sets the branch_id of this ShapesgraphsRecordIdBody.


        :param branch_id: The branch_id of this ShapesgraphsRecordIdBody.  # noqa: E501
        :type: str
        """

        self._branch_id = branch_id

    @property
    def commit_id(self):
        """Gets the commit_id of this ShapesgraphsRecordIdBody.  # noqa: E501


        :return: The commit_id of this ShapesgraphsRecordIdBody.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this ShapesgraphsRecordIdBody.


        :param commit_id: The commit_id of this ShapesgraphsRecordIdBody.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def replace_in_progress_commit(self):
        """Gets the replace_in_progress_commit of this ShapesgraphsRecordIdBody.  # noqa: E501


        :return: The replace_in_progress_commit of this ShapesgraphsRecordIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._replace_in_progress_commit

    @replace_in_progress_commit.setter
    def replace_in_progress_commit(self, replace_in_progress_commit):
        """Sets the replace_in_progress_commit of this ShapesgraphsRecordIdBody.


        :param replace_in_progress_commit: The replace_in_progress_commit of this ShapesgraphsRecordIdBody.  # noqa: E501
        :type: bool
        """

        self._replace_in_progress_commit = replace_in_progress_commit

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
        if issubclass(ShapesgraphsRecordIdBody, dict):
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
        if not isinstance(other, ShapesgraphsRecordIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
