# coding: utf-8

from pycti import OpenCTIApiClient

# Variables
api_url = 'https://demo.opencti.io'
api_token = 'bb4aca90-b98c-49ee-9582-7eac92b61b82'

# OpenCTI initialization
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# File to import
file_to_import = './test.json'

# Import the bundle
opencti_api_client.stix2.import_bundle_from_file(file_to_import)