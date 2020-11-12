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


class AzureBareMetalHardwareTypeNamesEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Name of the hardware type (vendor and/or their product name)
    """

    CISCO_UCS = "Cisco_UCS"
    HPE = "HPE"

class AzureBareMetalInstancePowerStateEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Resource power state
    """

    STARTING = "starting"
    STARTED = "started"
    STOPPING = "stopping"
    STOPPED = "stopped"
    RESTARTING = "restarting"
    UNKNOWN = "unknown"

class AzureBareMetalInstanceSizeNamesEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Specifies the AzureBareMetal instance SKU.
    """

    S72_M = "S72m"
    S144_M = "S144m"
    S72 = "S72"
    S144 = "S144"
    S192 = "S192"
    S192_M = "S192m"
    S192_XM = "S192xm"
    S96 = "S96"
    S112 = "S112"
    S224 = "S224"
    S224_M = "S224m"
    S224_OM = "S224om"
    S224_OO = "S224oo"
    S224_OOM = "S224oom"
    S224_OOO = "S224ooo"
    S384 = "S384"
    S384_M = "S384m"
    S384_XM = "S384xm"
    S384_XXM = "S384xxm"
    S448 = "S448"
    S448_M = "S448m"
    S448_OM = "S448om"
    S448_OO = "S448oo"
    S448_OOM = "S448oom"
    S448_OOO = "S448ooo"
    S576_M = "S576m"
    S576_XM = "S576xm"
    S672 = "S672"
    S672_M = "S672m"
    S672_OM = "S672om"
    S672_OO = "S672oo"
    S672_OOM = "S672oom"
    S672_OOO = "S672ooo"
    S768 = "S768"
    S768_M = "S768m"
    S768_XM = "S768xm"
    S896 = "S896"
    S896_M = "S896m"
    S896_OM = "S896om"
    S896_OO = "S896oo"
    S896_OOM = "S896oom"
    S896_OOO = "S896ooo"
    S960_M = "S960m"

class AzureBareMetalProvisioningStatesEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of provisioning of the AzureBareMetalInstance
    """

    ACCEPTED = "Accepted"
    CREATING = "Creating"
    UPDATING = "Updating"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    DELETING = "Deleting"
    MIGRATING = "Migrating"