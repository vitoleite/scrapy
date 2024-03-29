import glob
import os
from xmlrpc.client import DateTime
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime, timedelta
import dateutil.relativedelta
from bcb_pandas import formatting


class Extract(object):
    def __init__(self):
        self.url: str = "https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries"
        self.data_initial: DateTime = datetime.today().replace(day=1)
        self.first_day_prev_month: DateTime = (
            self.data_initial + dateutil.relativedelta.relativedelta(months=-1)
        )
        self.last_day_prev_month: DateTime = self.data_initial - timedelta(days=1)

        self.data_inicio: str = self.first_day_prev_month.strftime("%d%m%Y")
        self.data_fim: str = self.last_day_prev_month.strftime("%d%m%Y")

    def Browser(self):
        """
        Processo feito para extrair as informações da Poupança.
        - Abrir o navegador
        - Realizar os comandos necessários de navegação
        - Baixar o arquivo
        """

        driver = webdriver.Chrome().maximize_window()

        driver.get(self.url)

        # Hide alert
        alert = Alert(driver)
        alert.accept()

        poupanca_codigo = driver.find_element(By.ID, "txCodigo")
        poupanca_codigo.send_keys(24)
        poupanca_codigo.send_keys(Keys.ENTER)

        driver.implicitly_wait(3)

        # Changing to iFrame
        driver.switch_to.frame("iCorpo")
        checkbox_select = driver.find_element(By.NAME, "cbxSelecionaSerie")
        checkbox_select.click()

        # Back to normal content
        driver.switch_to.default_content()
        consult_btn = driver.find_element(
            By.XPATH, "//input[@title='Consultar séries']"
        )
        consult_btn.click()

        driver.implicitly_wait(3)
        element_date_initial = driver.find_element(
            By.XPATH, '//input[contains(@id, "dataInicio")]'
        )
        element_date_initial.clear()
        element_date_initial.send_keys(self.data_inicio)

        element_date_final = driver.find_element(
            By.XPATH, "//input[contains(@id, 'dataFim')]"
        )
        element_date_final.clear()
        element_date_final.send_keys(self.data_fim)

        view_btn = driver.find_element(By.XPATH, "//input[@title='Visualizar valores']")
        view_btn.click()

        download_btn = driver.find_element(By.LINK_TEXT, "Arquivo CSV")
        download_btn.click()

        sleep(1)
        print("O arquivo baixado!")

    def Data_cleaning(self):
        """
        Limpando os dados utilizando a biblioteca local criada para isso.
        """

        file: str = max(
            glob.iglob("C:/Users/vitor/Downloads/*.csv"), key=os.path.getctime
        )
        save_local: str = "scrapy/selenium/bcb_extract/data/"

        file_name: str = "dados_poupanca_"
        month_year: str = self.first_day_prev_month.date().strftime("%b%y")

        formatting(
            file=file, file_name=file_name, month_name=month_year, save_local=save_local
        )

        print("O processo foi finalizado!")


if __name__ == '__main__':
    starting = Extract()
    starting.Browser()
    starting.Data_cleaning()
