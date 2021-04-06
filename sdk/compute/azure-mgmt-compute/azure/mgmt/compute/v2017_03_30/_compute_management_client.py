# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import ComputeManagementClientConfiguration
from .operations import AvailabilitySetsOperations
from .operations import VirtualMachineExtensionImagesOperations
from .operations import VirtualMachineExtensionsOperations
from .operations import VirtualMachinesOperations
from .operations import VirtualMachineImagesOperations
from .operations import UsageOperations
from .operations import VirtualMachineSizesOperations
from .operations import ImagesOperations
from .operations import ResourceSkusOperations
from .operations import VirtualMachineScaleSetsOperations
from .operations import VirtualMachineScaleSetExtensionsOperations
from .operations import VirtualMachineScaleSetRollingUpgradesOperations
from .operations import VirtualMachineScaleSetVMsOperations
from .operations import DisksOperations
from .operations import SnapshotsOperations
from .operations import VirtualMachineRunCommandsOperations
from . import models


class ComputeManagementClient(object):
    """Compute Client.

    :ivar availability_sets: AvailabilitySetsOperations operations
    :vartype availability_sets: azure.mgmt.compute.v2017_03_30.operations.AvailabilitySetsOperations
    :ivar virtual_machine_extension_images: VirtualMachineExtensionImagesOperations operations
    :vartype virtual_machine_extension_images: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineExtensionImagesOperations
    :ivar virtual_machine_extensions: VirtualMachineExtensionsOperations operations
    :vartype virtual_machine_extensions: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineExtensionsOperations
    :ivar virtual_machines: VirtualMachinesOperations operations
    :vartype virtual_machines: azure.mgmt.compute.v2017_03_30.operations.VirtualMachinesOperations
    :ivar virtual_machine_images: VirtualMachineImagesOperations operations
    :vartype virtual_machine_images: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineImagesOperations
    :ivar usage: UsageOperations operations
    :vartype usage: azure.mgmt.compute.v2017_03_30.operations.UsageOperations
    :ivar virtual_machine_sizes: VirtualMachineSizesOperations operations
    :vartype virtual_machine_sizes: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineSizesOperations
    :ivar images: ImagesOperations operations
    :vartype images: azure.mgmt.compute.v2017_03_30.operations.ImagesOperations
    :ivar resource_skus: ResourceSkusOperations operations
    :vartype resource_skus: azure.mgmt.compute.v2017_03_30.operations.ResourceSkusOperations
    :ivar virtual_machine_scale_sets: VirtualMachineScaleSetsOperations operations
    :vartype virtual_machine_scale_sets: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetsOperations
    :ivar virtual_machine_scale_set_extensions: VirtualMachineScaleSetExtensionsOperations operations
    :vartype virtual_machine_scale_set_extensions: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetExtensionsOperations
    :ivar virtual_machine_scale_set_rolling_upgrades: VirtualMachineScaleSetRollingUpgradesOperations operations
    :vartype virtual_machine_scale_set_rolling_upgrades: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetRollingUpgradesOperations
    :ivar virtual_machine_scale_set_vms: VirtualMachineScaleSetVMsOperations operations
    :vartype virtual_machine_scale_set_vms: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineScaleSetVMsOperations
    :ivar disks: DisksOperations operations
    :vartype disks: azure.mgmt.compute.v2017_03_30.operations.DisksOperations
    :ivar snapshots: SnapshotsOperations operations
    :vartype snapshots: azure.mgmt.compute.v2017_03_30.operations.SnapshotsOperations
    :ivar virtual_machine_run_commands: VirtualMachineRunCommandsOperations operations
    :vartype virtual_machine_run_commands: azure.mgmt.compute.v2017_03_30.operations.VirtualMachineRunCommandsOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ComputeManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.availability_sets = AvailabilitySetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_extension_images = VirtualMachineExtensionImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_extensions = VirtualMachineExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machines = VirtualMachinesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_images = VirtualMachineImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_sizes = VirtualMachineSizesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.images = ImagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.resource_skus = ResourceSkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_sets = VirtualMachineScaleSetsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_set_extensions = VirtualMachineScaleSetExtensionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_set_rolling_upgrades = VirtualMachineScaleSetRollingUpgradesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_scale_set_vms = VirtualMachineScaleSetVMsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.disks = DisksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.snapshots = SnapshotsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.virtual_machine_run_commands = VirtualMachineRunCommandsOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> ComputeManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
