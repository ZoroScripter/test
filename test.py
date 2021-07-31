import requests
import os
import time

cnpj_input = input("CNPJ: ")

if len(cnpj_input) !=18:
	print("""
	===> CNPJ ESTA INVALIDO POR CAUSA DA QUANTIDADE. <===
	===> OU PORQUE ESTA INVALIDO!! <===
	""")
	time.sleep(10)

url = requests.get("https://www.receitaws.com.br/v1/cnpj/{}" .format(cnpj_input))

cnpj_data=url.json()

if "erro" not in cnpj_data:
    print("Situação: {}".format(cnpj_data["situacao"]))
    print("UF: {}".format(cnpj_data["uf"]))
    print("Municipio: {}".format(cnpj_data["municipio"]))
    print("Logradouro: {}".format(cnpj_data["logradouro"]))
    print("Numero: {}".format(cnpj_data["numero"]))
    print("Complemento: {}".format(cnpj_data["complemento"]))
    print("Porte: {}".format(cnpj_data["porte"]))
    print("Natureza: {}".format(cnpj_data["natureza_juridica"]))
    print("Data de abertura: {}".format(cnpj_data["abertura"]))
    print("Tipo: {}".format(cnpj_data["tipo"]))
    print("Capital: {}".format(cnpj_data["capital_social"]))