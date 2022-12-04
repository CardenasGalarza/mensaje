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



st.set_page_config(page_title='bdtickets-Averias', page_icon="🌀", layout='centered', initial_sidebar_state='auto')

## borrar nombres de la pagina
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
            background-attachment: fixed;True
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()
#st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
# --- USER AUTHENTICATION ---
names = ['Giancarlos Cardenas', 'Genesis Medrano', 'Luis Llerena', 'DIANA BERNEDO', 'VIVIAN CERVERA', 'CAROL CHUNGA', 'LAURA VIERA', 'MERCEDES RAYMUNDO', 'MONTES CABANILLAS', 'RENZO RIMARACHIN', 'LORENA BENAVIDES', 'NANCY YEREN', 'GIULIANA BELLIDO', 'CARMEN HUAMANCHUMO', 'GABRIEL SANTA ANA', 'CARMEN POMA REYES', 'JOSE ECHEVARRIA', 'YORMAN MORI', 'ENZO PAULINO', 'GUSTAVO SALCEDO', 'KAREN MAYORCA', 'LESLIE PRUDENCIO', 'BARBARA HUAMANCHUMO', 'Jose Ricardo', 'Eber Hinostroza', 'Bot cardenas', 'YERSON HINOSTROZA', 'Roberto Faustor', 'John Jairo Bravo', 'Mauro Arturo Garcia']
usernames = ['Cardenas', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot', 'YERSON', 'Roberto', 'jbravob', 'Mauroar']
hashed_passwords = ['123', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot', 'YERSON', 'Roberto', 'jbravob', 'Mauroar']

hashed_passwords = stauth.Hasher(hashed_passwords).generate()
####
authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)


name, authentication_status, username = authenticator.login('Login', 'main')
#print(username)
#### fondo al costado
def sidebar_bg(side_bg):
   side_bg_ext = 'jpg'
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'nooa.jpg'
sidebar_bg(side_bg)


st.markdown(
    """
    <style>

    header .css-1595djx e8zbici2{
    display: flex;
    flex-direction: column;
    align-items: center;
    }

    header .logo-text{
        margin: 0;
        padding: 10px 26px;
        font-weight: bold;
        color: rgb(60, 255, 0);
        font-size: 0.8em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# para los botones horizontal
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)



if authentication_status == False:
    st.error("Username/password is incorrect")

        ## borrar nombres de la pagina
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if authentication_status == None:
    st.warning("Please enter your username and password")

        ## borrar nombres de la pagina
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


    st.markdown(
        """
        <style>

        header .css-1595djx e8zbici2{
        display: flex;
        flex-direction: column;
        align-items: center;
        }

        header .logo-text{
            margin: 0;
            padding: 10px 26px;
            font-weight: bold;
            color: rgb(60, 255, 0);
            font-size: 0.8em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # para los botones horizontal
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)



    st.markdown(
        f"""
        <header class="css-1595djx e8zbici2">
            <p class="logo-text">App Alarmas 👨🏻‍💻Giancarlos .C</p>
        </header>
        """,
        unsafe_allow_html=True
    )

    def hide_anchor_link():
        st.markdown("""
            <style>
            .css-15zrgzn {display: none}
            .css-eczf16 {display: none}
            .css-jn99sy {display: none}
            </style>
            """, unsafe_allow_html=True)
    texto  = ('🔒Estamos mejorando la privacidad de la información, si aún no cuentas con tus credenciales, comunicarte con:')
    st.caption( f'<h6 style="color:#FFFFFF;">{texto}</h6>', unsafe_allow_html=True )

    textoo = ('\n\n👨🏻‍💻Luis Llerena. \n\n👨🏻‍💻Giancarlos Cardenas.')
    st.caption( f'<h6 style="color:#FFFFFF;">{textoo}</h6>', unsafe_allow_html=True )
    ###
    ####
    ####
    ####
    ######



if authentication_status:
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Bienvenid@ {name}")
    #### fondo al costado



    # 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
    EXAMPLE_NO = 1


    def streamlit_menu(example=1):
        if example == 1:
            # 1. as sidebar menu
            with st.sidebar:
                selected = option_menu(
                    menu_title="Main Menu",  # required
                    options=["CargarDt", "Projects", "Contact"],  # required
                    icons=["house", "book", "envelope"],  # optional
                    menu_icon="cast",  # optional
                    default_index=0,  # optional
                )
            return selected

        if example == 2:
            # 2. horizontal menu w/o custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["CargarDt", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
            )
            return selected

        if example == 3:
            # 2. horizontal menu with custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["CargarDt", "Projects", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                },
            )
            return selected

    selected = streamlit_menu(example=EXAMPLE_NO)

    if selected == "CargarDt":

        with st.form(key='my_form', clear_on_submit=True):

            col1, col2, col3 = st.columns(3)

            with col1:
                celu = st.text_input('Celular')
            with col2:
                option = st.selectbox(
                    'How would you like to be contacted?',
                    ('Email', 'Home phone', 'Mobile phone'))

                st.write('You selected:', option)

            mensaje = st.selectbox(
                "Mensaje",
                (
                    "SMS1",
                    "SMS2",
                ),
                key="filter_type8",
                help="""
                Ten encuenta tu accion `Ticket` inf.
                """,
            )


            #TODO SIVERVPARA BARRA AZUL

            st.balloons()
        # Every form must have a submit button.

            submitted = st.form_submit_button("✉️Enviar")

            if submitted == True:

                with st.spinner('Enviado mensaje...'):

                    date = datetime.now()
                    tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


                    options = Options()
                    options.add_argument("--headless")
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-dev-shm-usage")
                    options.add_argument("--disable-gpu")
                    options.add_argument("--disable-features=NetworkService")
                    options.add_argument("--window-size=1920x1080")
                    options.add_argument("--disable-features=VizDisplayCompositor")

                    

                    st.balloons()

                    

                    driver = webdriver.Chrome(options=options, service_log_path='selenium.log')

                    username = 'caramburu_TDP'
                    passwordd = 'WebSys29*T*'
                    driver.get("https://auth.movistaradvertising.com/login?logout")
                    time.sleep(1)

                    #pyautogui.hotkey("ctrl","F5")

                    

                    xpath = driver.find_element("xpath", '//INPUT[@id="username"]')
                    xpath.send_keys(username)
                    time.sleep(2)

                    xpath = driver.find_element("xpath", '//INPUT[@id="password"]')
                    xpath.send_keys(passwordd)
                    time.sleep(2)


                    xpath = driver.find_element("xpath", '//BUTTON[@type="submit"][text()="Ingresar"]')
                    xpath.click()
                    time.sleep(4)


                    xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                    xpath.click()
                    time.sleep(6)

                    xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                    xpath.click()
                    time.sleep(4)

                    #celu = '925266696'
                    #mensaje = 'Listoooossdddssss'

                    xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                    xpath.send_keys(celu)
                    time.sleep(6)

                    if 'SMS1' == mensaje:

                        xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                        xpath.send_keys("Hola, intentamos contactarte para solucionar la avería en tu, estaremos contactandote nuevamente, Movistar.")
                        time.sleep(6)


                        xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                        xpath.click()
                        time.sleep(6)

                        xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                        xpath.click()
                        time.sleep(5)

                        driver.quit()

                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)
                        #st.success('Mensaje enviado')
                        st.balloons()
                        #st.experimental_rerun()

                    
                    if 'SMS2' == mensaje:


                        xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                        xpath.send_keys("Hola, intentamos contactarte para validar que tu , ya se encuentra operativo, por favor realizar las validaciones, Movistar")
                        time.sleep(6)


                        xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                        xpath.click()
                        time.sleep(6)

                        xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                        xpath.click()
                        time.sleep(5)

                        driver.quit()

                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)


