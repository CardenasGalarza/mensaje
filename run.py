import os
import sys
import streamlit.web.cli as stcli
import sys

if __name__ == '__main__':

    launchdir = os.path.dirname(sys.argv[0])

    #if launchdir == '':
    #    launchdir = '.'

    print(launchdir)
    sys.argv = ["streamlit", "run", "https://raw.githubusercontent.com/CardenasGalarza/mensaje/main/app.py", "--server.headless=true", "--global.developmentMode=false"]
    #sys.argv = ["streamlit", "run", f"{launchdir}/app.py", "--global.developmentMode=false"]
    sys.exit(stcli.main())
