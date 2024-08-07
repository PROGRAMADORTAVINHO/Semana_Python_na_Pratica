# Gerando o PDF de Orçamento
# !pip install fpdf
from fpdf import FPDF

Projeto = input("Digite a Descrição do Projeto: ")
Hora_previstas = float(input("Digite a Quantidade de Horas Previstas: "))
Valor_Horas = float(input("Digite o Valor das Horas Trabalhadas: "))
Prazo = input("Digite o Prazo Estimado: ")

Valor_Total = Hora_previstas * Valor_Horas

pdf = FPDF() # Criando PDF

pdf.add_page() # Adicionando Página
pdf.set_font("Arial") # Escolher a Font

pdf.image("D:\\Programação\\Python\\Semana do Python na Pratica\\Projeto_1\\Template.png", x=0, y=0) # Adicionando Imagem (arquio da imagem, coordenada x, coordenada y)

pdf.text(115, 145, Projeto) # Colocando Texto (coordenada x, coordenada y, texto)
pdf.text(115, 160, str(Hora_previstas)) 
pdf.text(115, 175, str(Valor_Horas)) 
pdf.text(115, 190, Prazo)
pdf.text(115, 205, str(Valor_Total))

pdf.output("Orçamento.pdf") # Salvando PDF

print("Orçamento Gerado com Sucesso!!!")