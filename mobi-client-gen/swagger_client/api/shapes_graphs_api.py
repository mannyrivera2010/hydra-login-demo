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


class ShapesGraphsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_shapes_graph(self, record_id, **kwargs):  # noqa: E501
        """Deletes the SHACL Shapes Graph record with the associated record ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_shapes_graph(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID. NOTE: Assumes id represents an IRI unless String begins with \"_:\" (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_shapes_graph_with_http_info(record_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_shapes_graph_with_http_info(record_id, **kwargs)  # noqa: E501
            return data

    def delete_shapes_graph_with_http_info(self, record_id, **kwargs):  # noqa: E501
        """Deletes the SHACL Shapes Graph record with the associated record ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_shapes_graph_with_http_info(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID. NOTE: Assumes id represents an IRI unless String begins with \"_:\" (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_shapes_graph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `delete_shapes_graph`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shapes-graphs/{recordId}', 'DELETE',
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

    def download_shapes_graph(self, record_id, **kwargs):  # noqa: E501
        """Streams the SHACL Shapes Graph associated with the requested record ID to an OutputStream  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_shapes_graph(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID. NOTE: Assumes id represents an IRI unless String begins with \"_:\" (required)
        :param str branch_id: Optional String representing the Branch Resource id. NOTE: Assumes id represents an IRI unless String begins with \"_:\". Defaults to Master branch if missing
        :param str commit_id: Optional String representing the Commit Resource id. NOTE: Assumes id represents an IRI unless String begins with \"_:\". Defaults to head commit if missing. The provided commitId must be on the Branch identified by the provided branchId; otherwise, nothing will be returned
        :param str rdf_format: Desired RDF return format
        :param str file_name: File name for the SHACL Shapes Graph file
        :param bool apply_in_progress_commit: Whether or not any in progress commits by user should be applied to the return value
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_shapes_graph_with_http_info(record_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_shapes_graph_with_http_info(record_id, **kwargs)  # noqa: E501
            return data

    def download_shapes_graph_with_http_info(self, record_id, **kwargs):  # noqa: E501
        """Streams the SHACL Shapes Graph associated with the requested record ID to an OutputStream  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_shapes_graph_with_http_info(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID. NOTE: Assumes id represents an IRI unless String begins with \"_:\" (required)
        :param str branch_id: Optional String representing the Branch Resource id. NOTE: Assumes id represents an IRI unless String begins with \"_:\". Defaults to Master branch if missing
        :param str commit_id: Optional String representing the Commit Resource id. NOTE: Assumes id represents an IRI unless String begins with \"_:\". Defaults to head commit if missing. The provided commitId must be on the Branch identified by the provided branchId; otherwise, nothing will be returned
        :param str rdf_format: Desired RDF return format
        :param str file_name: File name for the SHACL Shapes Graph file
        :param bool apply_in_progress_commit: Whether or not any in progress commits by user should be applied to the return value
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_id', 'branch_id', 'commit_id', 'rdf_format', 'file_name', 'apply_in_progress_commit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_shapes_graph" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `download_shapes_graph`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']  # noqa: E501

        query_params = []
        if 'branch_id' in params:
            query_params.append(('branchId', params['branch_id']))  # noqa: E501
        if 'commit_id' in params:
            query_params.append(('commitId', params['commit_id']))  # noqa: E501
        if 'rdf_format' in params:
            query_params.append(('rdfFormat', params['rdf_format']))  # noqa: E501
        if 'file_name' in params:
            query_params.append(('fileName', params['file_name']))  # noqa: E501
        if 'apply_in_progress_commit' in params:
            query_params.append(('applyInProgressCommit', params['apply_in_progress_commit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shapes-graphs/{recordId}', 'GET',
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

    def get_entity1(self, record_id, entity_id, **kwargs):  # noqa: E501
        """Retrieves the triples for a specified entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity1(record_id, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID (required)
        :param str entity_id: String representing the entity Resource ID (required)
        :param str branch_id: String representing the Branch Resource ID
        :param str commit_id: String representing the Commit Resource ID
        :param str format: Specified format for the return data. Valid values include 'jsonld', 'turtle', 'rdf/xml', and 'trig'
        :param bool apply_in_progress_commit: Whether or not to apply the in progress commit for the user making the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_entity1_with_http_info(record_id, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_entity1_with_http_info(record_id, entity_id, **kwargs)  # noqa: E501
            return data

    def get_entity1_with_http_info(self, record_id, entity_id, **kwargs):  # noqa: E501
        """Retrieves the triples for a specified entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_entity1_with_http_info(record_id, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID (required)
        :param str entity_id: String representing the entity Resource ID (required)
        :param str branch_id: String representing the Branch Resource ID
        :param str commit_id: String representing the Commit Resource ID
        :param str format: Specified format for the return data. Valid values include 'jsonld', 'turtle', 'rdf/xml', and 'trig'
        :param bool apply_in_progress_commit: Whether or not to apply the in progress commit for the user making the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_id', 'entity_id', 'branch_id', 'commit_id', 'format', 'apply_in_progress_commit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_entity1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `get_entity1`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_entity1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'branch_id' in params:
            query_params.append(('branchId', params['branch_id']))  # noqa: E501
        if 'commit_id' in params:
            query_params.append(('commitId', params['commit_id']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501
        if 'apply_in_progress_commit' in params:
            query_params.append(('applyInProgressCommit', params['apply_in_progress_commit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shapes-graphs/{recordId}/entities/{entityId}', 'GET',
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

    def get_shapes_graph_content(self, record_id, **kwargs):  # noqa: E501
        """Retrieves the triples for a specified entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shapes_graph_content(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID (required)
        :param str branch_id: String representing the Branch Resource ID
        :param str commit_id: String representing the Commit Resource ID
        :param str format: Specified format for the return data. Valid values include 'jsonld', 'turtle', 'rdf/xml', and 'trig'
        :param bool apply_in_progress_commit: Whether or not to apply the in progress commit for the user making the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shapes_graph_content_with_http_info(record_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shapes_graph_content_with_http_info(record_id, **kwargs)  # noqa: E501
            return data

    def get_shapes_graph_content_with_http_info(self, record_id, **kwargs):  # noqa: E501
        """Retrieves the triples for a specified entity  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shapes_graph_content_with_http_info(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID (required)
        :param str branch_id: String representing the Branch Resource ID
        :param str commit_id: String representing the Commit Resource ID
        :param str format: Specified format for the return data. Valid values include 'jsonld', 'turtle', 'rdf/xml', and 'trig'
        :param bool apply_in_progress_commit: Whether or not to apply the in progress commit for the user making the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_id', 'branch_id', 'commit_id', 'format', 'apply_in_progress_commit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shapes_graph_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `get_shapes_graph_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']  # noqa: E501

        query_params = []
        if 'branch_id' in params:
            query_params.append(('branchId', params['branch_id']))  # noqa: E501
        if 'commit_id' in params:
            query_params.append(('commitId', params['commit_id']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501
        if 'apply_in_progress_commit' in params:
            query_params.append(('applyInProgressCommit', params['apply_in_progress_commit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shapes-graphs/{recordId}/content', 'GET',
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

    def get_shapes_graph_id(self, record_id, **kwargs):  # noqa: E501
        """Retrieves the Shapes Graph ID for the specified record, branch, and commit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shapes_graph_id(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID (required)
        :param str branch_id: String representing the Branch Resource ID
        :param str commit_id: String representing the Commit Resource ID
        :param bool apply_in_progress_commit: Whether or not to apply the in progress commit for the user making the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shapes_graph_id_with_http_info(record_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shapes_graph_id_with_http_info(record_id, **kwargs)  # noqa: E501
            return data

    def get_shapes_graph_id_with_http_info(self, record_id, **kwargs):  # noqa: E501
        """Retrieves the Shapes Graph ID for the specified record, branch, and commit  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shapes_graph_id_with_http_info(record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str record_id: String representing the Record Resource ID (required)
        :param str branch_id: String representing the Branch Resource ID
        :param str commit_id: String representing the Commit Resource ID
        :param bool apply_in_progress_commit: Whether or not to apply the in progress commit for the user making the request
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['record_id', 'branch_id', 'commit_id', 'apply_in_progress_commit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shapes_graph_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `get_shapes_graph_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'record_id' in params:
            path_params['recordId'] = params['record_id']  # noqa: E501

        query_params = []
        if 'branch_id' in params:
            query_params.append(('branchId', params['branch_id']))  # noqa: E501
        if 'commit_id' in params:
            query_params.append(('commitId', params['commit_id']))  # noqa: E501
        if 'apply_in_progress_commit' in params:
            query_params.append(('applyInProgressCommit', params['apply_in_progress_commit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shapes-graphs/{recordId}/id', 'GET',
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

    def upload_file1(self, **kwargs):  # noqa: E501
        """Uploads a shapes-graph file to the data store  # noqa: E501

        Uploads and imports a shapes-graph file to a data store and creates an associated ShapesGraphRecord using the form data. A master Branch is created and stored with an initial Commit containing the data provided in the SHACL Shapes Graph file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file:
        :param str json:
        :param str title:
        :param str description:
        :param str markdown:
        :param list[str] keywords:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_file1_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.upload_file1_with_http_info(**kwargs)  # noqa: E501
            return data

    def upload_file1_with_http_info(self, **kwargs):  # noqa: E501
        """Uploads a shapes-graph file to the data store  # noqa: E501

        Uploads and imports a shapes-graph file to a data store and creates an associated ShapesGraphRecord using the form data. A master Branch is created and stored with an initial Commit containing the data provided in the SHACL Shapes Graph file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_file1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str file:
        :param str json:
        :param str title:
        :param str description:
        :param str markdown:
        :param list[str] keywords:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file', 'json', 'title', 'description', 'markdown', 'keywords']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_file1" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']  # noqa: E501
        if 'json' in params:
            form_params.append(('json', params['json']))  # noqa: E501
        if 'title' in params:
            form_params.append(('title', params['title']))  # noqa: E501
        if 'description' in params:
            form_params.append(('description', params['description']))  # noqa: E501
        if 'markdown' in params:
            form_params.append(('markdown', params['markdown']))  # noqa: E501
        if 'keywords' in params:
            form_params.append(('keywords', params['keywords']))  # noqa: E501
            collection_formats['keywords'] = 'multi'  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/shapes-graphs', 'POST',
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
