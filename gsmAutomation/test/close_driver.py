#!/usr/bin/env python3
import sys
from pathlib import Path
dir=Path(__file__).resolve().parent
sys.path.append('../..')

import time
from gsmAutomation import MainArguments
from gsmAutomation.sites import getSite
from gsmAutomation.Operator import loginSession,closeDriver

site_name,site_hosts = getSite(MainArguments())
session = loginSession(site=site_hosts)
session.login()
close = closeDriver()
close.close()