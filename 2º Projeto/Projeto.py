# pip install yfinance 
# pip install pyautogui

import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Digite a Ação Desejada: ")
data_inicial = input("Digite a Data Inicial: ")
data_final = input("Digite a Data Final: ")

# .Ticker() Buscar a ação desejada | .history() Período desejada
dados = yfinance.Ticker(ticker).history(start=data_inicial,end=data_final)
fechamento = dados.Close # Mostrar só a tabela desjada 

maxima = round(fechamento.max(), 2) # Busca a cotação máxima
minima = round(fechamento.min(), 2) # Busca a cotação mínima
valor_medio = round(fechamento.mean(), 2) # Valor Média da cotação

destinatario = "jotavio250@gmail.com"
assunto = "Teste"
mensagem = f"""Prezado gestor,

Segue as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição

Att, João Otavio
"""
# Abrir o navegador
webbrowser.open("www.gmail.com")
time.sleep(5) # 5 segundos | Esperar um tempo para continuar o código

# Clicar no botão escrever
pyautogui.click(x=71, y=202)

# Pausa de 3 segundos
pyautogui.PAUSE = 3 

# Digtar o email e teclar Tab
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digtar o assunto e teclar Tab
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Digtar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão Enviar
pyautogui.click(x=848, y=704)

# Fechar a aba
pyautogui.hotkey("ctrl", "f4")