from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime, timedelta
import dateutil.relativedelta
import bcb_pandas, glob, os


class extract(object):
    
    def __init__(self):
        self.url = 'https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries'
        self.data_1 = datetime.today().replace(day=1)
        self.first_day_prev_month = self.data_1 + dateutil.relativedelta.relativedelta(months=-1)
        self.last_day_prev_month = self.data_1 - timedelta(days=1)

        self.data_inicio = self.first_day_prev_month.strftime('%d%m%Y')
        self.data_fim = self.last_day_prev_month.strftime('%d%m%Y')
    
    def browser(self):
        """
        Processo feito para extrair as informações da Poupança.
        - Abrir o navegador
        - Realizar os comandos necessários de navegação
        - Baixar o arquivo
        """

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get(self.url)

        # Hide alert
        alert = Alert(driver)
        alert.accept()

        poupanca_codigo = driver.find_element(By.ID, 'txCodigo')
        poupanca_codigo.send_keys(24)
        poupanca_codigo.send_keys(Keys.ENTER)

        driver.implicitly_wait(3)
        
        # Changing to iFrame
        driver.switch_to.frame('iCorpo')
        checkbox_select = driver.find_element(By.NAME, 'cbxSelecionaSerie')
        checkbox_select.click()

        # Back to normal content
        driver.switch_to.default_content()
        consult_btn = driver.find_element(By.XPATH, "//input[@title='Consultar séries']")
        consult_btn.click()

        
        driver.implicitly_wait(5)
        element_date_initial = driver.find_element(By.XPATH, '//input[contains(@id, "dataInicio")]')
        element_date_initial.clear()
        element_date_initial.send_keys(self.data_inicio)

        element_date_final = driver.find_element(By.XPATH, "//input[contains(@id, 'dataFim')]")
        element_date_final.clear()
        element_date_final.send_keys(self.data_fim)

        view_btn = driver.find_element(By.XPATH, "//input[@title='Visualizar valores']")
        view_btn.click()

        download_btn = driver.find_element(By.LINK_TEXT, 'Arquivo CSV')
        download_btn.click()

        sleep(1)
        print('Arquivo baixado!')

    
    def data_cleaning(self):
        """
        Limpando os dados utilizando a biblioteca local criada para isso.
        """
        # Data refactoring

        last_file = max(glob.iglob("C:\\Users\\vitoo\Downloads\\*.csv"), key=os.path.getctime)
        save_local = 'selenium\\bcb_extract\\data\\'

        file_name = 'dados_poupanca_'
        month_name = self.first_day_prev_month.date().strftime("%b%y")

        bcb_pandas.data_cleaning(file=last_file, save_local=save_local, file_name=file_name, month_name=month_name)

        print('Finalizado!!!')


starting = extract()
starting.browser()
starting.data_cleaning()