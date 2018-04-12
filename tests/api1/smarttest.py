#!/usr/bin/env python3.6

# Author: Eric Turgeon
# License: BSD
# Location for tests into REST API of FreeNAS

import sys
import os

apifolder = os.getcwd()
sys.path.append(apifolder)
from functions import POST, GET_OUTPUT


def test_01_Create_a_new_SMARTTest():
    disk_identifiers = GET_OUTPUT("/storage/disk", "disk_identifier")
    global disk_ident
    disk_indent = disk_identifiers.split()[0]
    payload = {"smarttest_disks": disk_indent,
               "smarttest_type": "L",
               "smarttest_hour": "*",
               "smarttest_daymonth": "*",
               "smarttest_month": "*",
               "smarttest_dayweek": "*"}
    results = POST("/tasks/smarttest/", payload)
    assert results.status_code == 201, results.text


def test_02_Check_that_API_reports_new_SMARTTest():
    results = GET_OUTPUT("/tasks/smarttest/", "smarttest_disks")
    assert results == disk_ident
