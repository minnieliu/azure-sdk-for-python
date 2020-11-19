# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class AgreementType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The agreement type.
    """

    NOT_SPECIFIED = "NotSpecified"
    AS2 = "AS2"
    X12 = "X12"
    EDIFACT = "Edifact"

class ApiDeploymentParameterVisibility(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Api deployment parameter visibility.
    """

    NOT_SPECIFIED = "NotSpecified"
    DEFAULT = "Default"
    INTERNAL = "Internal"

class ApiTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Api tier.
    """

    NOT_SPECIFIED = "NotSpecified"
    ENTERPRISE = "Enterprise"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class ApiType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    REST = "Rest"
    SOAP = "Soap"

class AzureAsyncOperationState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The Azure async operation state.
    """

    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    PENDING = "Pending"
    CANCELED = "Canceled"

class DayOfWeek(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The day of the week.
    """

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class DaysOfWeek(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"

class EdifactCharacterSet(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The edifact character set.
    """

    NOT_SPECIFIED = "NotSpecified"
    UNOB = "UNOB"
    UNOA = "UNOA"
    UNOC = "UNOC"
    UNOD = "UNOD"
    UNOE = "UNOE"
    UNOF = "UNOF"
    UNOG = "UNOG"
    UNOH = "UNOH"
    UNOI = "UNOI"
    UNOJ = "UNOJ"
    UNOK = "UNOK"
    UNOX = "UNOX"
    UNOY = "UNOY"
    KECA = "KECA"

class EdifactDecimalIndicator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The edifact decimal indicator.
    """

    NOT_SPECIFIED = "NotSpecified"
    COMMA = "Comma"
    DECIMAL = "Decimal"

class EncryptionAlgorithm(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The encryption algorithm.
    """

    NOT_SPECIFIED = "NotSpecified"
    NONE = "None"
    DES3 = "DES3"
    RC2 = "RC2"
    AES128 = "AES128"
    AES192 = "AES192"
    AES256 = "AES256"

class ErrorResponseCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The error response code.
    """

    NOT_SPECIFIED = "NotSpecified"
    INTEGRATION_SERVICE_ENVIRONMENT_NOT_FOUND = "IntegrationServiceEnvironmentNotFound"
    INTERNAL_SERVER_ERROR = "InternalServerError"
    INVALID_OPERATION_ID = "InvalidOperationId"

class EventLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The event level.
    """

    LOG_ALWAYS = "LogAlways"
    CRITICAL = "Critical"
    ERROR = "Error"
    WARNING = "Warning"
    INFORMATIONAL = "Informational"
    VERBOSE = "Verbose"

class HashingAlgorithm(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The signing or hashing algorithm.
    """

    NOT_SPECIFIED = "NotSpecified"
    NONE = "None"
    MD5 = "MD5"
    SHA1 = "SHA1"
    SHA2256 = "SHA2256"
    SHA2384 = "SHA2384"
    SHA2512 = "SHA2512"

class IntegrationAccountSkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The integration account sku name.
    """

    NOT_SPECIFIED = "NotSpecified"
    FREE = "Free"
    BASIC = "Basic"
    STANDARD = "Standard"

class IntegrationServiceEnvironmentAccessEndpointType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The integration service environment access endpoint type.
    """

    NOT_SPECIFIED = "NotSpecified"
    EXTERNAL = "External"
    INTERNAL = "Internal"

class IntegrationServiceEnvironmentNetworkDependencyCategoryType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The integration service environment network dependency category type.
    """

    NOT_SPECIFIED = "NotSpecified"
    AZURE_STORAGE = "AzureStorage"
    AZURE_MANAGEMENT = "AzureManagement"
    AZURE_ACTIVE_DIRECTORY = "AzureActiveDirectory"
    SSL_CERTIFICATE_VERIFICATION = "SSLCertificateVerification"
    DIAGNOSTIC_LOGS_AND_METRICS = "DiagnosticLogsAndMetrics"
    INTEGRATION_SERVICE_ENVIRONMENT_CONNECTORS = "IntegrationServiceEnvironmentConnectors"
    REDIS_CACHE = "RedisCache"
    ACCESS_ENDPOINTS = "AccessEndpoints"
    RECOVERY_SERVICE = "RecoveryService"
    SQL = "SQL"
    REGIONAL_SERVICE = "RegionalService"

class IntegrationServiceEnvironmentNetworkDependencyHealthState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The integration service environment network dependency health state.
    """

    NOT_SPECIFIED = "NotSpecified"
    HEALTHY = "Healthy"
    UNHEALTHY = "Unhealthy"
    UNKNOWN = "Unknown"

class IntegrationServiceEnvironmentNetworkEndPointAccessibilityState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The integration service environment network endpoint accessibility state.
    """

    NOT_SPECIFIED = "NotSpecified"
    UNKNOWN = "Unknown"
    AVAILABLE = "Available"
    NOT_AVAILABLE = "NotAvailable"

class IntegrationServiceEnvironmentSkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The integration service environment sku name.
    """

    NOT_SPECIFIED = "NotSpecified"
    PREMIUM = "Premium"
    DEVELOPER = "Developer"

class IntegrationServiceEnvironmentSkuScaleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The integration service environment sku scale type.
    """

    MANUAL = "Manual"
    AUTOMATIC = "Automatic"
    NONE = "None"

class KeyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The key type.
    """

    NOT_SPECIFIED = "NotSpecified"
    PRIMARY = "Primary"
    SECONDARY = "Secondary"

class MapType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The map type.
    """

    NOT_SPECIFIED = "NotSpecified"
    XSLT = "Xslt"
    XSLT20 = "Xslt20"
    XSLT30 = "Xslt30"
    LIQUID = "Liquid"

class MessageFilterType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The message filter type.
    """

    NOT_SPECIFIED = "NotSpecified"
    INCLUDE = "Include"
    EXCLUDE = "Exclude"

class OpenAuthenticationProviderType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Open authentication policy provider type.
    """

    AAD = "AAD"

class ParameterType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The parameter type.
    """

    NOT_SPECIFIED = "NotSpecified"
    STRING = "String"
    SECURE_STRING = "SecureString"
    INT = "Int"
    FLOAT = "Float"
    BOOL = "Bool"
    ARRAY = "Array"
    OBJECT = "Object"
    SECURE_OBJECT = "SecureObject"

class PartnerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The partner type.
    """

    NOT_SPECIFIED = "NotSpecified"
    B2_B = "B2B"

class RecurrenceFrequency(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The recurrence frequency.
    """

    NOT_SPECIFIED = "NotSpecified"
    SECOND = "Second"
    MINUTE = "Minute"
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"
    MONTH = "Month"
    YEAR = "Year"

class SchemaType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The schema type.
    """

    NOT_SPECIFIED = "NotSpecified"
    XML = "Xml"

class SegmentTerminatorSuffix(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The segment terminator suffix.
    """

    NOT_SPECIFIED = "NotSpecified"
    NONE = "None"
    CR = "CR"
    LF = "LF"
    CRLF = "CRLF"

class SigningAlgorithm(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The signing or hashing algorithm.
    """

    NOT_SPECIFIED = "NotSpecified"
    DEFAULT = "Default"
    SHA1 = "SHA1"
    SHA2256 = "SHA2256"
    SHA2384 = "SHA2384"
    SHA2512 = "SHA2512"

class SkuName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The sku name.
    """

    NOT_SPECIFIED = "NotSpecified"
    FREE = "Free"
    SHARED = "Shared"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"

class StatusAnnotation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status annotation.
    """

    NOT_SPECIFIED = "NotSpecified"
    PREVIEW = "Preview"
    PRODUCTION = "Production"

class SwaggerSchemaType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The swagger schema type.
    """

    STRING = "String"
    NUMBER = "Number"
    INTEGER = "Integer"
    BOOLEAN = "Boolean"
    ARRAY = "Array"
    FILE = "File"
    OBJECT = "Object"
    NULL = "Null"

class TrackEventsOperationOptions(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The track events operation options.
    """

    NONE = "None"
    DISABLE_SOURCE_INFO_ENRICH = "DisableSourceInfoEnrich"

class TrackingRecordType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The tracking record type.
    """

    NOT_SPECIFIED = "NotSpecified"
    CUSTOM = "Custom"
    AS2_MESSAGE = "AS2Message"
    AS2_MDN = "AS2MDN"
    X12_INTERCHANGE = "X12Interchange"
    X12_FUNCTIONAL_GROUP = "X12FunctionalGroup"
    X12_TRANSACTION_SET = "X12TransactionSet"
    X12_INTERCHANGE_ACKNOWLEDGMENT = "X12InterchangeAcknowledgment"
    X12_FUNCTIONAL_GROUP_ACKNOWLEDGMENT = "X12FunctionalGroupAcknowledgment"
    X12_TRANSACTION_SET_ACKNOWLEDGMENT = "X12TransactionSetAcknowledgment"
    EDIFACT_INTERCHANGE = "EdifactInterchange"
    EDIFACT_FUNCTIONAL_GROUP = "EdifactFunctionalGroup"
    EDIFACT_TRANSACTION_SET = "EdifactTransactionSet"
    EDIFACT_INTERCHANGE_ACKNOWLEDGMENT = "EdifactInterchangeAcknowledgment"
    EDIFACT_FUNCTIONAL_GROUP_ACKNOWLEDGMENT = "EdifactFunctionalGroupAcknowledgment"
    EDIFACT_TRANSACTION_SET_ACKNOWLEDGMENT = "EdifactTransactionSetAcknowledgment"

class TrailingSeparatorPolicy(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The trailing separator policy.
    """

    NOT_SPECIFIED = "NotSpecified"
    NOT_ALLOWED = "NotAllowed"
    OPTIONAL = "Optional"
    MANDATORY = "Mandatory"

class UsageIndicator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The usage indicator.
    """

    NOT_SPECIFIED = "NotSpecified"
    TEST = "Test"
    INFORMATION = "Information"
    PRODUCTION = "Production"

class WorkflowProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The workflow provisioning state.
    """

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    READY = "Ready"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    MOVING = "Moving"
    UPDATING = "Updating"
    REGISTERING = "Registering"
    REGISTERED = "Registered"
    UNREGISTERING = "Unregistering"
    UNREGISTERED = "Unregistered"
    COMPLETED = "Completed"
    RENEWING = "Renewing"
    PENDING = "Pending"
    WAITING = "Waiting"
    IN_PROGRESS = "InProgress"

class WorkflowState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The workflow state.
    """

    NOT_SPECIFIED = "NotSpecified"
    COMPLETED = "Completed"
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    DELETED = "Deleted"
    SUSPENDED = "Suspended"

class WorkflowStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The workflow status.
    """

    NOT_SPECIFIED = "NotSpecified"
    PAUSED = "Paused"
    RUNNING = "Running"
    WAITING = "Waiting"
    SUCCEEDED = "Succeeded"
    SKIPPED = "Skipped"
    SUSPENDED = "Suspended"
    CANCELLED = "Cancelled"
    FAILED = "Failed"
    FAULTED = "Faulted"
    TIMED_OUT = "TimedOut"
    ABORTED = "Aborted"
    IGNORED = "Ignored"

class WorkflowTriggerProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The workflow trigger provisioning state.
    """

    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    READY = "Ready"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    MOVING = "Moving"
    UPDATING = "Updating"
    REGISTERING = "Registering"
    REGISTERED = "Registered"
    UNREGISTERING = "Unregistering"
    UNREGISTERED = "Unregistered"
    COMPLETED = "Completed"

class WsdlImportMethod(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The WSDL import method.
    """

    NOT_SPECIFIED = "NotSpecified"
    SOAP_TO_REST = "SoapToRest"
    SOAP_PASS_THROUGH = "SoapPassThrough"

class X12CharacterSet(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The X12 character set.
    """

    NOT_SPECIFIED = "NotSpecified"
    BASIC = "Basic"
    EXTENDED = "Extended"
    UTF8 = "UTF8"

class X12DateFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The x12 date format.
    """

    NOT_SPECIFIED = "NotSpecified"
    CCYYMMDD = "CCYYMMDD"
    YYMMDD = "YYMMDD"

class X12TimeFormat(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The x12 time format.
    """

    NOT_SPECIFIED = "NotSpecified"
    HHMM = "HHMM"
    HHMMSS = "HHMMSS"
    HHMMS_SDD = "HHMMSSdd"
    HHMMS_SD = "HHMMSSd"