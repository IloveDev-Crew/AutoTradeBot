"""
πππππππππ
Copyright : iLoveDev-Crew
LastUpdate : 2021-03-29 μ΅νΈλ¦
Title : Auto Trading Bot 
Version 1.0
πππππππππ
"""

import os
import jwt
import uuid
import hashlib
import time
import datetime
import pybithumb
import logging
import requests
import json
import Logger
import strategy
from BithumbAPI import *

from urllib.parse import urlencode
from slacker import Slacker
from pandas.io.json import json_normalize

#μ λ΅ μλ¦½
#my_strategy = strategy.Strategy().strategy1()

#logger μμ±
logger = Logger.Logger()
## λ‘κΉ ################################################
## logger.log("INFO","Test") 
##   -- λ‘κ·Έλ λ²¨ : DEBUG,INFO, WARNING, ERROR, CRITICAL
## logger.sendMSG_to_slack("Test μ±κ³΅") 
##   --μ¬λλ³΄λ΄κΈ°
## logger.logger_set()
##   -- λ‘κΉ μΈν - μμ  μ€ν μ€μΌμ₯΄νμ
########################################################

tickers = pybithumb.get_tickers()      






    






