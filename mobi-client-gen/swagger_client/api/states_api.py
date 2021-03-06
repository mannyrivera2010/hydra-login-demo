# coding: utf-8

"""
    Mobi

    Mobi REST API Documentation  # noqa: E501

    OpenAPI spec version: 1.22.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class StatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_state(self, body, application, **kwargs):  # noqa: E501
        """Creates a new State for the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_state(body, application, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: JSON-LD of all resources to be linked to the new State (required)
        :param str application: ID of the Application to associate the new State with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_state_with_http_info(body, application, **kwargs)  # noqa: E501
        else:
            (data) = self.create_state_with_http_info(body, application, **kwargs)  # noqa: E501
            return data

    def create_state_with_http_info(self, body, application, **kwargs):  # noqa: E501
        """Creates a new State for the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_state_with_http_info(body, application, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: JSON-LD of all resources to be linked to the new State (required)
        :param str application: ID of the Application to associate the new State with (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'application']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_state`")  # noqa: E501
        # verify the required parameter 'application' is set
        if ('application' not in params or
                params['application'] is None):
            raise ValueError("Missing the required parameter `application` when calling `create_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'application' in params:
            query_params.append(('application', params['application']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/states', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_state(self, state_id, **kwargs):  # noqa: E501
        """Deletes State as long as it belongs to the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_state(state_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state_id: ID of the State to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_state_with_http_info(state_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_state_with_http_info(state_id, **kwargs)  # noqa: E501
            return data

    def delete_state_with_http_info(self, state_id, **kwargs):  # noqa: E501
        """Deletes State as long as it belongs to the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_state_with_http_info(state_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state_id: ID of the State to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'state_id' is set
        if ('state_id' not in params or
                params['state_id'] is None):
            raise ValueError("Missing the required parameter `state_id` when calling `delete_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'state_id' in params:
            path_params['stateId'] = params['state_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/states/{stateId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_state(self, state_id, **kwargs):  # noqa: E501
        """Retrieves State by ID as long it belongs to the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_state(state_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state_id: ID of the State to retrieve (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_state_with_http_info(state_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_state_with_http_info(state_id, **kwargs)  # noqa: E501
            return data

    def get_state_with_http_info(self, state_id, **kwargs):  # noqa: E501
        """Retrieves State by ID as long it belongs to the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_state_with_http_info(state_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state_id: ID of the State to retrieve (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'state_id' is set
        if ('state_id' not in params or
                params['state_id'] is None):
            raise ValueError("Missing the required parameter `state_id` when calling `get_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'state_id' in params:
            path_params['stateId'] = params['state_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/states/{stateId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_states(self, application, **kwargs):  # noqa: E501
        """Retrieves State for the User making the request based on filter criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_states(application, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: ID of the Application to filter State by (required)
        :param list[str] subjects:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_states_with_http_info(application, **kwargs)  # noqa: E501
        else:
            (data) = self.get_states_with_http_info(application, **kwargs)  # noqa: E501
            return data

    def get_states_with_http_info(self, application, **kwargs):  # noqa: E501
        """Retrieves State for the User making the request based on filter criteria  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_states_with_http_info(application, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: ID of the Application to filter State by (required)
        :param list[str] subjects:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application', 'subjects']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_states" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application' is set
        if ('application' not in params or
                params['application'] is None):
            raise ValueError("Missing the required parameter `application` when calling `get_states`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'application' in params:
            query_params.append(('application', params['application']))  # noqa: E501
        if 'subjects' in params:
            query_params.append(('subjects', params['subjects']))  # noqa: E501
            collection_formats['subjects'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/states', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_state(self, body, state_id, **kwargs):  # noqa: E501
        """Updates State as long as it belongs to the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_state(body, state_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: JSON-LD serialization of the new resources to associate with the State (required)
        :param str state_id: ID of the State to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_state_with_http_info(body, state_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_state_with_http_info(body, state_id, **kwargs)  # noqa: E501
            return data

    def update_state_with_http_info(self, body, state_id, **kwargs):  # noqa: E501
        """Updates State as long as it belongs to the User making the request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_state_with_http_info(body, state_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: JSON-LD serialization of the new resources to associate with the State (required)
        :param str state_id: ID of the State to update (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'state_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_state`")  # noqa: E501
        # verify the required parameter 'state_id' is set
        if ('state_id' not in params or
                params['state_id'] is None):
            raise ValueError("Missing the required parameter `state_id` when calling `update_state`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'state_id' in params:
            path_params['stateId'] = params['state_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/states/{stateId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
