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


class JobCollectionQuota(Model):
    """JobCollectionQuota.

    :param max_job_count: Gets or set the maximum job count.
    :type max_job_count: int
    :param max_job_occurrence: Gets or sets the maximum job occurrence.
    :type max_job_occurrence: int
    :param max_recurrence: Gets or set the maximum recurrence.
    :type max_recurrence: :class:`JobMaxRecurrence
     <azure.mgmt.scheduler.models.JobMaxRecurrence>`
    """

    _attribute_map = {
        'max_job_count': {'key': 'maxJobCount', 'type': 'int'},
        'max_job_occurrence': {'key': 'maxJobOccurrence', 'type': 'int'},
        'max_recurrence': {'key': 'maxRecurrence', 'type': 'JobMaxRecurrence'},
    }

    def __init__(self, max_job_count=None, max_job_occurrence=None, max_recurrence=None):
        self.max_job_count = max_job_count
        self.max_job_occurrence = max_job_occurrence
        self.max_recurrence = max_recurrence
