#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/alfredo/")
sys.path.insert(0,"/var/www/alfredo/alfredo/")

import logging
logging.basicConfig(stream=sys.stderr)

from alfredo import app as application
