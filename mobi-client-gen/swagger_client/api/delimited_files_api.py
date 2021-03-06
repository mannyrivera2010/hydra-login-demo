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


class DelimitedFilesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def etl_file(self, document_name, mapping_record_iri, dataset_record_iri, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using an uploaded Mapping file and load data into a Dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file(document_name, mapping_record_iri, dataset_record_iri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str mapping_record_iri: ID (IRI) of the MappingRecord (required)
        :param str dataset_record_iri: ID (IRI) of the DatasetRecord (required)
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.etl_file_with_http_info(document_name, mapping_record_iri, dataset_record_iri, **kwargs)  # noqa: E501
        else:
            (data) = self.etl_file_with_http_info(document_name, mapping_record_iri, dataset_record_iri, **kwargs)  # noqa: E501
            return data

    def etl_file_with_http_info(self, document_name, mapping_record_iri, dataset_record_iri, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using an uploaded Mapping file and load data into a Dataset  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file_with_http_info(document_name, mapping_record_iri, dataset_record_iri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str mapping_record_iri: ID (IRI) of the MappingRecord (required)
        :param str dataset_record_iri: ID (IRI) of the DatasetRecord (required)
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_name', 'mapping_record_iri', 'dataset_record_iri', 'contains_headers', 'separator']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method etl_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if ('document_name' not in params or
                params['document_name'] is None):
            raise ValueError("Missing the required parameter `document_name` when calling `etl_file`")  # noqa: E501
        # verify the required parameter 'mapping_record_iri' is set
        if ('mapping_record_iri' not in params or
                params['mapping_record_iri'] is None):
            raise ValueError("Missing the required parameter `mapping_record_iri` when calling `etl_file`")  # noqa: E501
        # verify the required parameter 'dataset_record_iri' is set
        if ('dataset_record_iri' not in params or
                params['dataset_record_iri'] is None):
            raise ValueError("Missing the required parameter `dataset_record_iri` when calling `etl_file`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_name' in params:
            path_params['documentName'] = params['document_name']  # noqa: E501

        query_params = []
        if 'mapping_record_iri' in params:
            query_params.append(('mappingRecordIRI', params['mapping_record_iri']))  # noqa: E501
        if 'dataset_record_iri' in params:
            query_params.append(('datasetRecordIRI', params['dataset_record_iri']))  # noqa: E501
        if 'contains_headers' in params:
            query_params.append(('containsHeaders', params['contains_headers']))  # noqa: E501
        if 'separator' in params:
            query_params.append(('separator', params['separator']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delimited-files/{documentName}/map', 'POST',
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

    def etl_file1(self, document_name, mapping_record_iri, file_name, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using an uploaded Mapping file and download the data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file1(document_name, mapping_record_iri, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str mapping_record_iri: ID of the MappingRecord (required)
        :param str file_name: Name for the downloaded file (required)
        :param str format: RDF serialization to use
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.etl_file1_with_http_info(document_name, mapping_record_iri, file_name, **kwargs)  # noqa: E501
        else:
            (data) = self.etl_file1_with_http_info(document_name, mapping_record_iri, file_name, **kwargs)  # noqa: E501
            return data

    def etl_file1_with_http_info(self, document_name, mapping_record_iri, file_name, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using an uploaded Mapping file and download the data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file1_with_http_info(document_name, mapping_record_iri, file_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str mapping_record_iri: ID of the MappingRecord (required)
        :param str file_name: Name for the downloaded file (required)
        :param str format: RDF serialization to use
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_name', 'mapping_record_iri', 'file_name', 'format', 'contains_headers', 'separator']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method etl_file1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if ('document_name' not in params or
                params['document_name'] is None):
            raise ValueError("Missing the required parameter `document_name` when calling `etl_file1`")  # noqa: E501
        # verify the required parameter 'mapping_record_iri' is set
        if ('mapping_record_iri' not in params or
                params['mapping_record_iri'] is None):
            raise ValueError("Missing the required parameter `mapping_record_iri` when calling `etl_file1`")  # noqa: E501
        # verify the required parameter 'file_name' is set
        if ('file_name' not in params or
                params['file_name'] is None):
            raise ValueError("Missing the required parameter `file_name` when calling `etl_file1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_name' in params:
            path_params['documentName'] = params['document_name']  # noqa: E501

        query_params = []
        if 'mapping_record_iri' in params:
            query_params.append(('mappingRecordIRI', params['mapping_record_iri']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501
        if 'contains_headers' in params:
            query_params.append(('containsHeaders', params['contains_headers']))  # noqa: E501
        if 'separator' in params:
            query_params.append(('separator', params['separator']))  # noqa: E501
        if 'file_name' in params:
            query_params.append(('fileName', params['file_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delimited-files/{documentName}/map', 'GET',
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

    def etl_file_ontology(self, document_name, mapping_record_iri, ontology_record_iri, branch_iri, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using an uploaded Mapping file and commit it to an OntologyRecord  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file_ontology(document_name, mapping_record_iri, ontology_record_iri, branch_iri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str mapping_record_iri: ID of  the MappingRecord (required)
        :param str ontology_record_iri: ID of the DatasetRecord (required)
        :param str branch_iri: ID of the BranchRecord (required)
        :param bool update: Whether to treat the mapped data as an update or new additions
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.etl_file_ontology_with_http_info(document_name, mapping_record_iri, ontology_record_iri, branch_iri, **kwargs)  # noqa: E501
        else:
            (data) = self.etl_file_ontology_with_http_info(document_name, mapping_record_iri, ontology_record_iri, branch_iri, **kwargs)  # noqa: E501
            return data

    def etl_file_ontology_with_http_info(self, document_name, mapping_record_iri, ontology_record_iri, branch_iri, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using an uploaded Mapping file and commit it to an OntologyRecord  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file_ontology_with_http_info(document_name, mapping_record_iri, ontology_record_iri, branch_iri, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str mapping_record_iri: ID of  the MappingRecord (required)
        :param str ontology_record_iri: ID of the DatasetRecord (required)
        :param str branch_iri: ID of the BranchRecord (required)
        :param bool update: Whether to treat the mapped data as an update or new additions
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_name', 'mapping_record_iri', 'ontology_record_iri', 'branch_iri', 'update', 'contains_headers', 'separator']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method etl_file_ontology" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if ('document_name' not in params or
                params['document_name'] is None):
            raise ValueError("Missing the required parameter `document_name` when calling `etl_file_ontology`")  # noqa: E501
        # verify the required parameter 'mapping_record_iri' is set
        if ('mapping_record_iri' not in params or
                params['mapping_record_iri'] is None):
            raise ValueError("Missing the required parameter `mapping_record_iri` when calling `etl_file_ontology`")  # noqa: E501
        # verify the required parameter 'ontology_record_iri' is set
        if ('ontology_record_iri' not in params or
                params['ontology_record_iri'] is None):
            raise ValueError("Missing the required parameter `ontology_record_iri` when calling `etl_file_ontology`")  # noqa: E501
        # verify the required parameter 'branch_iri' is set
        if ('branch_iri' not in params or
                params['branch_iri'] is None):
            raise ValueError("Missing the required parameter `branch_iri` when calling `etl_file_ontology`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_name' in params:
            path_params['documentName'] = params['document_name']  # noqa: E501

        query_params = []
        if 'mapping_record_iri' in params:
            query_params.append(('mappingRecordIRI', params['mapping_record_iri']))  # noqa: E501
        if 'ontology_record_iri' in params:
            query_params.append(('ontologyRecordIRI', params['ontology_record_iri']))  # noqa: E501
        if 'branch_iri' in params:
            query_params.append(('branchIRI', params['branch_iri']))  # noqa: E501
        if 'update' in params:
            query_params.append(('update', params['update']))  # noqa: E501
        if 'contains_headers' in params:
            query_params.append(('containsHeaders', params['contains_headers']))  # noqa: E501
        if 'separator' in params:
            query_params.append(('separator', params['separator']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delimited-files/{documentName}/map-to-ontology', 'POST',
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

    def etl_file_preview(self, document_name, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using mapping JSON-LD  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file_preview(document_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str jsonld:
        :param str format: RDF serialization to use if getting a preview
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.etl_file_preview_with_http_info(document_name, **kwargs)  # noqa: E501
        else:
            (data) = self.etl_file_preview_with_http_info(document_name, **kwargs)  # noqa: E501
            return data

    def etl_file_preview_with_http_info(self, document_name, **kwargs):  # noqa: E501
        """ETL an uploaded delimited document using mapping JSON-LD  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.etl_file_preview_with_http_info(document_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param str jsonld:
        :param str format: RDF serialization to use if getting a preview
        :param bool contains_headers: Whether the delimited file has headers
        :param str separator: Character the columns are separated by if it is a CSV
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_name', 'jsonld', 'format', 'contains_headers', 'separator']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method etl_file_preview" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if ('document_name' not in params or
                params['document_name'] is None):
            raise ValueError("Missing the required parameter `document_name` when calling `etl_file_preview`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_name' in params:
            path_params['documentName'] = params['document_name']  # noqa: E501

        query_params = []
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501
        if 'contains_headers' in params:
            query_params.append(('containsHeaders', params['contains_headers']))  # noqa: E501
        if 'separator' in params:
            query_params.append(('separator', params['separator']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'jsonld' in params:
            form_params.append(('jsonld', params['jsonld']))  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delimited-files/{documentName}/map-preview', 'POST',
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

    def get_rows(self, document_name, **kwargs):  # noqa: E501
        """Gather rows from an uploaded delimited document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rows(document_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param int row_count: Number of rows to retrieve from the delimited document
        :param str separator: Character the columns are separated by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_rows_with_http_info(document_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_rows_with_http_info(document_name, **kwargs)  # noqa: E501
            return data

    def get_rows_with_http_info(self, document_name, **kwargs):  # noqa: E501
        """Gather rows from an uploaded delimited document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rows_with_http_info(document_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: Name of the delimited document in the data/tmp/ directory (required)
        :param int row_count: Number of rows to retrieve from the delimited document
        :param str separator: Character the columns are separated by
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_name', 'row_count', 'separator']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_rows" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if ('document_name' not in params or
                params['document_name'] is None):
            raise ValueError("Missing the required parameter `document_name` when calling `get_rows`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_name' in params:
            path_params['documentName'] = params['document_name']  # noqa: E501

        query_params = []
        if 'row_count' in params:
            query_params.append(('rowCount', params['row_count']))  # noqa: E501
        if 'separator' in params:
            query_params.append(('separator', params['separator']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delimited-files/{documentName}', 'GET',
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

    def upload(self, **kwargs):  # noqa: E501
        """Upload delimited file sent as form data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str delimited_file:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.upload_with_http_info(**kwargs)  # noqa: E501
            return data

    def upload_with_http_info(self, **kwargs):  # noqa: E501
        """Upload delimited file sent as form data  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str delimited_file:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delimited_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'delimited_file' in params:
            local_var_files['delimitedFile'] = params['delimited_file']  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delimited-files', 'POST',
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

    def upload1(self, document_name, **kwargs):  # noqa: E501
        """Replace an uploaded delimited file with another  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload1(document_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: (required)
        :param str delimited_file:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upload1_with_http_info(document_name, **kwargs)  # noqa: E501
        else:
            (data) = self.upload1_with_http_info(document_name, **kwargs)  # noqa: E501
            return data

    def upload1_with_http_info(self, document_name, **kwargs):  # noqa: E501
        """Replace an uploaded delimited file with another  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload1_with_http_info(document_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_name: (required)
        :param str delimited_file:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_name', 'delimited_file']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_name' is set
        if ('document_name' not in params or
                params['document_name'] is None):
            raise ValueError("Missing the required parameter `document_name` when calling `upload1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_name' in params:
            path_params['documentName'] = params['document_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'delimited_file' in params:
            local_var_files['delimitedFile'] = params['delimited_file']  # noqa: E501

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/delimited-files/{documentName}', 'PUT',
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
