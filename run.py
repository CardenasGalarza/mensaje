import os
import sys
import streamlit.web.cli as stcli
import streamlit as st
import mysql.connector
from mysql.connector import Error
import time
from datetime import datetime
import streamlit as st
import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')

import streamlit as st
from streamlit_option_menu import option_menu
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
#from soupsieve import select  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
############################################ OCULTAR INFROMACION NO IMPORTANTE
import base64
import mysql.connector
from mysql.connector import Error
#import pyodbc
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
##########################
import time
from datetime import datetime
from datetime import timedelta

if __name__ == '__main__':

    launchdir = os.path.dirname(sys.argv[0])

    #if launchdir == '':
    #    launchdir = '.'

    print(launchdir)
    sys.argv = ["streamlit", "run", "https://raw.githubusercontent.com/CardenasGalarza/mensaje/main/app.py", "--server.port=10000", "--server.headless=true", "--global.developmentMode=false"]
    #sys.argv = ["streamlit", "run", f"{launchdir}/app.py", "--global.developmentMode=false"]
    sys.exit(stcli.main())
