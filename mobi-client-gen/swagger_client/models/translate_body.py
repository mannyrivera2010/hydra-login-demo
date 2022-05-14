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

class TranslateBody(object):
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
        'type': 'str',
        'ontology_iri': 'str',
        'output_name': 'str',
        'desired_rows': 'int'
    }

    attribute_map = {
        'file': 'file',
        'type': 'type',
        'ontology_iri': 'ontologyIRI',
        'output_name': 'outputName',
        'desired_rows': 'desiredRows'
    }

    def __init__(self, file=None, type=None, ontology_iri=None, output_name=None, desired_rows=10):  # noqa: E501
        """TranslateBody - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._type = None
        self._ontology_iri = None
        self._output_name = None
        self._desired_rows = None
        self.discriminator = None
        if file is not None:
            self.file = file
        if type is not None:
            self.type = type
        if ontology_iri is not None:
            self.ontology_iri = ontology_iri
        if output_name is not None:
            self.output_name = output_name
        if desired_rows is not None:
            self.desired_rows = desired_rows

    @property
    def file(self):
        """Gets the file of this TranslateBody.  # noqa: E501

        Data file to transform.  # noqa: E501

        :return: The file of this TranslateBody.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this TranslateBody.

        Data file to transform.  # noqa: E501

        :param file: The file of this TranslateBody.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def type(self):
        """Gets the type of this TranslateBody.  # noqa: E501

        Optional type to determine needed translator.  # noqa: E501

        :return: The type of this TranslateBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TranslateBody.

        Optional type to determine needed translator.  # noqa: E501

        :param type: The type of this TranslateBody.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def ontology_iri(self):
        """Gets the ontology_iri of this TranslateBody.  # noqa: E501

        Optional namespace to use for the created ontology and instance data.  # noqa: E501

        :return: The ontology_iri of this TranslateBody.  # noqa: E501
        :rtype: str
        """
        return self._ontology_iri

    @ontology_iri.setter
    def ontology_iri(self, ontology_iri):
        """Sets the ontology_iri of this TranslateBody.

        Optional namespace to use for the created ontology and instance data.  # noqa: E501

        :param ontology_iri: The ontology_iri of this TranslateBody.  # noqa: E501
        :type: str
        """

        self._ontology_iri = ontology_iri

    @property
    def output_name(self):
        """Gets the output_name of this TranslateBody.  # noqa: E501

        Optional filename given to the output file. Requires zip extension.  # noqa: E501

        :return: The output_name of this TranslateBody.  # noqa: E501
        :rtype: str
        """
        return self._output_name

    @output_name.setter
    def output_name(self, output_name):
        """Sets the output_name of this TranslateBody.

        Optional filename given to the output file. Requires zip extension.  # noqa: E501

        :param output_name: The output_name of this TranslateBody.  # noqa: E501
        :type: str
        """

        self._output_name = output_name

    @property
    def desired_rows(self):
        """Gets the desired_rows of this TranslateBody.  # noqa: E501

        Optional number of rows to parse to determine property ranges if file is tabular.  # noqa: E501

        :return: The desired_rows of this TranslateBody.  # noqa: E501
        :rtype: int
        """
        return self._desired_rows

    @desired_rows.setter
    def desired_rows(self, desired_rows):
        """Sets the desired_rows of this TranslateBody.

        Optional number of rows to parse to determine property ranges if file is tabular.  # noqa: E501

        :param desired_rows: The desired_rows of this TranslateBody.  # noqa: E501
        :type: int
        """

        self._desired_rows = desired_rows

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
        if issubclass(TranslateBody, dict):
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
        if not isinstance(other, TranslateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other