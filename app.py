import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings('ignore')
#####3333
##########################
import time
from datetime import datetime
###############33
##data



st.set_page_config(page_title='bdtickets-Averias', page_icon="📨", layout='centered', initial_sidebar_state='auto')

st.title('📨APP GESTION ENVIAR MENSAJE')
## borrar nombres de la pagina

col1, col2, col3 = st.columns(3)



with col2:
    nombre = st.sidebar.selectbox(
        'Ingresa tu nombre',
        ('', 'Gian', 'alexis'))

col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    st.write("")
    st.write("")
    st.write("")

    st.write("")

with col3:
    st.write("")

page_names = ['SMS 7', 'SMS 8', 'SMS 9', 'SMS 10', 'SMS 11', 'SMS 12']
page = st.sidebar.radio('Selecciona inf. de mensaje💻',page_names, index=0)

if page == 'SMS 7':
    with st.form(key='my_form', clear_on_submit=True):
        import mysql.connector
        from mysql.connector import Error

        col1, col2, col3 = st.columns(3)

        with col1:
            celu = st.text_input('Celular')

        with col2:
            suscriptortelefono = st.text_input('suscriptortelefono')
        #with col2:
        #    option = st.selectbox(
        #        'How would you like to be contacted?',
        #        ('Email', 'Home phone', 'Mobile phone'))

        #    st.write('You selected:', option)




        #TODO SIVERVPARA BARRA AZUL

        st.balloons()
    # Every form must have a submit button.

        submitted = st.form_submit_button("✉️Enviar")

        if submitted == True:



            with st.spinner('Enviado mensaje...'):

                cnxn = mysql.connector.connect( host="10.226.120.172",
                                        port="3306",
                                        user="slinea",
                                        passwd="OP81^K@u",
                                        db="segunda_linea"
                                        )
                cursor = cnxn.cursor()


                date = datetime.now()
                tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


                sql = "INSERT INTO MENSAJE (NOMBRE, SMS, HORA) VALUES (%s, %s, %s)"
                val = (nombre, page, tiempo)
                cursor.execute(sql, val)
                cnxn.commit()


                cursor.close()
                cnxn.close()



                options = Options()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--disable-features=NetworkService")
                #options.add_argument("--window-size=1920x1080")
                options.add_argument("--disable-features=VizDisplayCompositor")

                

                st.balloons()


                driver = webdriver.Chrome(options=options, service_log_path='selenium.log')
                driver.maximize_window()

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
                time.sleep(6)


                xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                xpath.click()
                time.sleep(6)

                xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                xpath.click()
                time.sleep(8)

                #celu = '925266696'
                #mensaje = 'Listoooossdddssss'

                xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                xpath.send_keys(celu)
                time.sleep(6)

                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                xpath.send_keys(f"Hola, detectamos que la intermitencia del servicio {suscriptortelefono} se debe al alcance Wifi, recomendamos comprar un repetidor. Mas info al 080011800, Movistar.")
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
if page == 'SMS 8':
    with st.form(key='my_form', clear_on_submit=True):
        import mysql.connector
        from mysql.connector import Error

        col1, col2, col3 = st.columns(3)

        with col1:
            celu = st.text_input('Celular')

        with col2:
            suscriptortelefono = st.text_input('suscriptortelefono')
        #with col2:
        #    option = st.selectbox(
        #        'How would you like to be contacted?',
        #        ('Email', 'Home phone', 'Mobile phone'))

        #    st.write('You selected:', option)




        #TODO SIVERVPARA BARRA AZUL

        st.balloons()
    # Every form must have a submit button.

        submitted = st.form_submit_button("✉️Enviar")

        if submitted == True:



            with st.spinner('Enviado mensaje...'):

                cnxn = mysql.connector.connect( host="10.226.120.172",
                                        port="3306",
                                        user="slinea",
                                        passwd="OP81^K@u",
                                        db="segunda_linea"
                                        )
                cursor = cnxn.cursor()


                date = datetime.now()
                tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


                sql = "INSERT INTO MENSAJE (NOMBRE, SMS, HORA) VALUES (%s, %s, %s)"
                val = (nombre, page, tiempo)
                cursor.execute(sql, val)
                cnxn.commit()


                cursor.close()
                cnxn.close()



                options = Options()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--disable-features=NetworkService")
                #options.add_argument("--window-size=1920x1080")
                options.add_argument("--disable-features=VizDisplayCompositor")

                

                st.balloons()


                driver = webdriver.Chrome(options=options, service_log_path='selenium.log')
                driver.maximize_window()

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
                time.sleep(6)


                xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                xpath.click()
                time.sleep(6)

                xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                xpath.click()
                time.sleep(8)

                #celu = '925266696'
                #mensaje = 'Listoooossdddssss'

                xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                xpath.send_keys(celu)
                time.sleep(6)

                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                xpath.send_keys(f"Hola, se realizó la configuración de tu red WiFi del servicio {suscriptortelefono}. Sigue disfrutando de tu navegación, Movistar.")
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
if page == 'SMS 9':
    with st.form(key='my_form', clear_on_submit=True):
        import mysql.connector
        from mysql.connector import Error

        col1, col2, col3 = st.columns(3)

        with col1:
            celu = st.text_input('Celular')

        with col2:
            motivo2desc = st.text_input('motivo2desc')

        with col3:
            suscriptortelefono = st.text_input('suscriptortelefono')
        #with col2:
        #    option = st.selectbox(
        #        'How would you like to be contacted?',
        #        ('Email', 'Home phone', 'Mobile phone'))

        #    st.write('You selected:', option)




        #TODO SIVERVPARA BARRA AZUL

        st.balloons()
    # Every form must have a submit button.

        submitted = st.form_submit_button("✉️Enviar")

        if submitted == True:



            with st.spinner('Enviado mensaje...'):

                cnxn = mysql.connector.connect( host="10.226.120.172",
                                        port="3306",
                                        user="slinea",
                                        passwd="OP81^K@u",
                                        db="segunda_linea"
                                        )
                cursor = cnxn.cursor()


                date = datetime.now()
                tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


                sql = "INSERT INTO MENSAJE (NOMBRE, SMS, HORA) VALUES (%s, %s, %s)"
                val = (nombre, page, tiempo)
                cursor.execute(sql, val)
                cnxn.commit()


                cursor.close()
                cnxn.close()



                options = Options()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--disable-features=NetworkService")
                #options.add_argument("--window-size=1920x1080")
                options.add_argument("--disable-features=VizDisplayCompositor")

                

                st.balloons()


                driver = webdriver.Chrome(options=options, service_log_path='selenium.log')
                driver.maximize_window()

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
                time.sleep(6)


                xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                xpath.click()
                time.sleep(6)

                xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                xpath.click()
                time.sleep(8)

                #celu = '925266696'
                #mensaje = 'Listoooossdddssss'

                xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                xpath.send_keys(celu)
                time.sleep(6)

                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                xpath.send_keys(f"Hola, nos alegra haberte ayudado, tu servicio de {motivo2desc} con código de servicio {suscriptortelefono} se encuentra operativo. Disfruta de tu navegación, Movistar.")
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
if page == 'SMS 10':
    with st.form(key='my_form', clear_on_submit=True):
        import mysql.connector
        from mysql.connector import Error

        col1, col2, col3 = st.columns(3)

        with col1:
            celu = st.text_input('Celular')

        with col2:
            motivo2desc = st.text_input('motivo2desc')

        with col3:
            suscriptortelefono = st.text_input('suscriptortelefono')
        #with col2:
        #    option = st.selectbox(
        #        'How would you like to be contacted?',
        #        ('Email', 'Home phone', 'Mobile phone'))

        #    st.write('You selected:', option)




        #TODO SIVERVPARA BARRA AZUL

        st.balloons()
    # Every form must have a submit button.

        submitted = st.form_submit_button("✉️Enviar")

        if submitted == True:



            with st.spinner('Enviado mensaje...'):

                cnxn = mysql.connector.connect( host="10.226.120.172",
                                        port="3306",
                                        user="slinea",
                                        passwd="OP81^K@u",
                                        db="segunda_linea"
                                        )
                cursor = cnxn.cursor()


                date = datetime.now()
                tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


                sql = "INSERT INTO MENSAJE (NOMBRE, SMS, HORA) VALUES (%s, %s, %s)"
                val = (nombre, page, tiempo)
                cursor.execute(sql, val)
                cnxn.commit()


                cursor.close()
                cnxn.close()



                options = Options()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--disable-features=NetworkService")
                #options.add_argument("--window-size=1920x1080")
                options.add_argument("--disable-features=VizDisplayCompositor")

                

                st.balloons()


                driver = webdriver.Chrome(options=options, service_log_path='selenium.log')
                driver.maximize_window()

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
                time.sleep(6)


                xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                xpath.click()
                time.sleep(6)

                xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                xpath.click()
                time.sleep(8)

                #celu = '925266696'
                #mensaje = 'Listoooossdddssss'

                xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                xpath.send_keys(celu)
                time.sleep(6)

                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                xpath.send_keys(f"Hola, intentamos contactarte para validar que tu servicio de {motivo2desc} {suscriptortelefono} ya se encuentra operativo, por favor realizar las validaciones, Movistar")
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
if page == 'SMS 11':
    with st.form(key='my_form', clear_on_submit=True):
        import mysql.connector
        from mysql.connector import Error

        col1, col2, col3 = st.columns(3)

        with col1:
            celu = st.text_input('Celular')

        with col2:
            ticket = st.text_input('ticket')
        #with col2:
        #    option = st.selectbox(
        #        'How would you like to be contacted?',
        #        ('Email', 'Home phone', 'Mobile phone'))

        #    st.write('You selected:', option)




        #TODO SIVERVPARA BARRA AZUL

        st.balloons()
    # Every form must have a submit button.

        submitted = st.form_submit_button("✉️Enviar")

        if submitted == True:



            with st.spinner('Enviado mensaje...'):

                cnxn = mysql.connector.connect( host="10.226.120.172",
                                        port="3306",
                                        user="slinea",
                                        passwd="OP81^K@u",
                                        db="segunda_linea"
                                        )
                cursor = cnxn.cursor()


                date = datetime.now()
                tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


                sql = "INSERT INTO MENSAJE (NOMBRE, SMS, HORA) VALUES (%s, %s, %s)"
                val = (nombre, page, tiempo)
                cursor.execute(sql, val)
                cnxn.commit()


                cursor.close()
                cnxn.close()



                options = Options()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--disable-features=NetworkService")
                #options.add_argument("--window-size=1920x1080")
                options.add_argument("--disable-features=VizDisplayCompositor")

                

                st.balloons()


                driver = webdriver.Chrome(options=options, service_log_path='selenium.log')
                driver.maximize_window()

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
                time.sleep(6)


                xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                xpath.click()
                time.sleep(6)

                xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                xpath.click()
                time.sleep(8)

                #celu = '925266696'
                #mensaje = 'Listoooossdddssss'

                xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                xpath.send_keys(celu)
                time.sleep(6)

                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                xpath.send_keys(f"Hola, te contactamos para indicarte que hemos generado el ticket de avería {ticket}. Nos pondremos en contacto en las próximas horas, Movistar")
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
if page == 'SMS 12':
    with st.form(key='my_form', clear_on_submit=True):
        import mysql.connector
        from mysql.connector import Error

        col1, col2, col3 = st.columns(3)

        with col1:
            celu = st.text_input('Celular')

        with col2:
            motivo2desc = st.text_input('motivo2desc')

        with col3:
            suscriptortelefono = st.text_input('suscriptortelefono')
        #with col2:
        #    option = st.selectbox(
        #        'How would you like to be contacted?',
        #        ('Email', 'Home phone', 'Mobile phone'))

        #    st.write('You selected:', option)




        #TODO SIVERVPARA BARRA AZUL

        st.balloons()
    # Every form must have a submit button.

        submitted = st.form_submit_button("✉️Enviar")

        if submitted == True:



            with st.spinner('Enviado mensaje...'):

                cnxn = mysql.connector.connect( host="10.226.120.172",
                                        port="3306",
                                        user="slinea",
                                        passwd="OP81^K@u",
                                        db="segunda_linea"
                                        )
                cursor = cnxn.cursor()


                date = datetime.now()
                tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))


                sql = "INSERT INTO MENSAJE (NOMBRE, SMS, HORA) VALUES (%s, %s, %s)"
                val = (nombre, page, tiempo)
                cursor.execute(sql, val)
                cnxn.commit()


                cursor.close()
                cnxn.close()



                options = Options()
                options.add_argument("--headless")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")
                options.add_argument("--disable-features=NetworkService")
                #options.add_argument("--window-size=1920x1080")
                options.add_argument("--disable-features=VizDisplayCompositor")

                

                st.balloons()


                driver = webdriver.Chrome(options=options, service_log_path='selenium.log')
                driver.maximize_window()

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
                time.sleep(6)


                xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                xpath.click()
                time.sleep(6)

                xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                xpath.click()
                time.sleep(8)

                #celu = '925266696'
                #mensaje = 'Listoooossdddssss'

                xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                xpath.send_keys(celu)
                time.sleep(6)

                xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                xpath.send_keys(f"Hola, nos alegra haberte ayudado, tu {motivo2desc} {suscriptortelefono} se encuentra operativo. Disfruta tu navegación con estos tips http://smvst.com/tipsInt, Movistar.")
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


## fondo total
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2020/05/15/17/55/box-5174459_960_720.jpg 1x, https://cdn.pixabay.com/photo/2020/05/15/17/55/box-5174459_1280.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()


## borrar nombres de la pagina
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)