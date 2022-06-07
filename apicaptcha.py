#Exemplo prático

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from anticaptchaofficial.recaptchav2proxyless import *
import time

import os

navegador = webdriver.Chrome(ChromeDriverManager().install())

link = "https://google.com/recaptcha/api2/demo"
navegador.get("https://google.com/recaptcha/api2/demo")

chave_captcha = navegador.find_element(By.XPATH, '//*[@id="recaptcha-demo"]').get_attribute('data-sitekey')

solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(os.environ['chave_api']) #!!
solver.set_website_url(link)
solver.set_website_key(chave_captcha)

resposta = solver.solve_and_return_solution()

if resposta != 0:
    print(resposta)
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{resposta}'")
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(solver.err_string)

# navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML = '{var}'")
time.sleep(10)
