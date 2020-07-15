# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorResponse(Model):
    """Describes the format of Error response.

    :param code: Error code
    :type code: str
    :param message: Error message indicating why the operation failed.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str=None, message: str=None, **kwargs) -> None:
        super(ErrorResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class ManagementGroupProxyOnlyResource(Model):
    """A proxy only azure resource object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Location of the resource
    :type location: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, **kwargs) -> None:
        super(ManagementGroupProxyOnlyResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location


class ManagementGroupDiagnosticSettingsResource(ManagementGroupProxyOnlyResource):
    """The management group diagnostic setting resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param location: Location of the resource
    :type location: str
    :param storage_account_id: The resource ID of the storage account to which
     you would like to send Diagnostic Logs.
    :type storage_account_id: str
    :param service_bus_rule_id: The service bus rule Id of the diagnostic
     setting. This is here to maintain backwards compatibility.
    :type service_bus_rule_id: str
    :param event_hub_authorization_rule_id: The resource Id for the event hub
     authorization rule.
    :type event_hub_authorization_rule_id: str
    :param event_hub_name: The name of the event hub. If none is specified,
     the default event hub will be selected.
    :type event_hub_name: str
    :param logs: The list of logs settings.
    :type logs:
     list[~azure.mgmt.monitor.v2020_01_01_preview.models.ManagementGroupLogSettings]
    :param workspace_id: The full ARM resource ID of the Log Analytics
     workspace to which you would like to send Diagnostic Logs. Example:
     /subscriptions/4b9e8510-67ab-4e9a-95a9-e2f1e570ea9c/resourceGroups/insights-integration/providers/Microsoft.OperationalInsights/workspaces/viruela2
    :type workspace_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'storage_account_id': {'key': 'properties.storageAccountId', 'type': 'str'},
        'service_bus_rule_id': {'key': 'properties.serviceBusRuleId', 'type': 'str'},
        'event_hub_authorization_rule_id': {'key': 'properties.eventHubAuthorizationRuleId', 'type': 'str'},
        'event_hub_name': {'key': 'properties.eventHubName', 'type': 'str'},
        'logs': {'key': 'properties.logs', 'type': '[ManagementGroupLogSettings]'},
        'workspace_id': {'key': 'properties.workspaceId', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, storage_account_id: str=None, service_bus_rule_id: str=None, event_hub_authorization_rule_id: str=None, event_hub_name: str=None, logs=None, workspace_id: str=None, **kwargs) -> None:
        super(ManagementGroupDiagnosticSettingsResource, self).__init__(location=location, **kwargs)
        self.storage_account_id = storage_account_id
        self.service_bus_rule_id = service_bus_rule_id
        self.event_hub_authorization_rule_id = event_hub_authorization_rule_id
        self.event_hub_name = event_hub_name
        self.logs = logs
        self.workspace_id = workspace_id


class ManagementGroupLogSettings(Model):
    """Part of Management Group diagnostic setting. Specifies the settings for a
    particular log.

    All required parameters must be populated in order to send to Azure.

    :param category: Required. Name of a Management Group Diagnostic Log
     category for a resource type this setting is applied to.
    :type category: str
    :param enabled: Required. a value indicating whether this log is enabled.
    :type enabled: bool
    """

    _validation = {
        'category': {'required': True},
        'enabled': {'required': True},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(self, *, category: str, enabled: bool, **kwargs) -> None:
        super(ManagementGroupLogSettings, self).__init__(**kwargs)
        self.category = category
        self.enabled = enabled
