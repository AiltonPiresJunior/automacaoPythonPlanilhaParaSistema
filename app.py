from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import openpyxl

driver = webdriver.Chrome()

driver.get('https://contabilidade-devaprender.netlify.app/')
sleep(3)

email = driver.find_element(By.ID,"email").send_keys('admin@contabilidade.com')
sleep(2)

driver.find_element(By.ID,"senha").send_keys('contabilidade123456')
sleep(2)

driver.find_element(By.ID,"Entrar").click()
sleep(5)

empresas = openpyxl.load_workbook("./empresas.xlsx")
pagina_empresas = empresas["dados empresas"]

for linha in pagina_empresas.iter_rows(min_row=2,values_only=True):
    nome_da_empresa, email, telefone, endereco, cnpj, area_de_atuacao, quantidade_de_funcionarios, data_de_fundacao = linha

    driver.find_element(By.ID,"nomeEmpresa").send_keys(nome_da_empresa)
    sleep(1)

    driver.find_element(By.ID,"emailEmpresa").send_keys(email)
    sleep(1)

    driver.find_element(By.ID,"telefoneEmpresa").send_keys(telefone)
    sleep(1)

    driver.find_element(By.ID,"enderecoEmpresa").send_keys(endereco)
    sleep(1)

    driver.find_element(By.ID,"cnpj").send_keys(cnpj)
    sleep(1)

    driver.find_element(By.ID,"areaAtuacao").send_keys(area_de_atuacao)
    sleep(1)

    driver.find_element(By.ID,"numeroFuncionarios").send_keys(quantidade_de_funcionarios)
    sleep(1)

    driver.find_element(By.ID,"dataFundacao").send_keys(data_de_fundacao)
    sleep(1)

    driver.find_element(By.ID,"Cadastrar").click()
    sleep(2)
