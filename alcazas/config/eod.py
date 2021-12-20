from __future__ import unicode_literals
import frappe
from frappe import _
def get_data():
        return [
                {
                        "label": _("EODR"),
                        "icon": "fa fa-cog",
                        "items": [
                                {
                                "type": "doctype",
                                "name": "EODR Requirements",
                                "description": _("EODR Requirements")
                                },
                                {
                                "type": "doctype",
                                "name": "EODR",
                                "description": _("End Of Day Report")
                                }
                        ]
                },
                {
                        "label": _("Setup"),
                        "items": [

                                        {
                                        "type": "doctype",
                                        "name": "Job Scope",
                                        "description": _("Job Scope"),
                                        },
                                        {
                                        "type": "doctype",
                                        "name": "Job Tier",
                                        "description": _("Job Tier/Level"),
                                        },
                                        {
                                        "type": "doctype",
                                        "name": "Job Description",
                                        "description": _("Job Description"),
                                        },
                                        {
                                        "type": "doctype",
                                        "name": "Job UOM",
                                        "description": _("Job UOM"),
                                        },
                                        {
                                        "type": "doctype",
                                        "name": "Job Code",
                                        "description": _("Job Code")
                                        },
                        ]
                },
                {
                        "label": _("Reports"),
                        "items": [
                                {
                                        "type": "report",
                                        "name": "EODR Summary",
                                        "is_query_report": True,
                                        "description": _("EODR Summary"),
                                }
                        ]
                }
        ]


