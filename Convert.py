import os
import pandas as pd
import PyPDF2
from PIL import Image
import pytesseract

def identificar_tipo_arquivo(arquivo):
    """Identifica o tipo do arquivo baseado na extensão"""
    _, ext = os.path.splitext(arquivo)
    ext = ext.lower()

    if ext == '.csv':
        return 'csv'
    elif ext == '.pdf':
        return 'pdf'
    elif ext in ['.jpg', '.jpeg', '.png']:
        return 'imagem'
    else:
        return 'desconhecido'

def csv_para_json(csv_file, json_file):
    """Converte CSV para JSON"""
    df = pd.read_csv(csv_file)
    df.to_json(json_file, orient='records', lines=True)
    print(f'Arquivo CSV foi convertido para JSON e salvo em {json_file}')

def pdf_para_texto(pdf_file, texto_file):
    """Converte PDF para Texto"""
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        texto = ''
        for page in reader.pages:
            texto += page.extract_text()

    with open(texto_file, 'w') as file:
        file.write(texto)
    print(f'Arquivo PDF foi convertido para texto e salvo em {texto_file}')

def imagem_para_texto(imagem_file, texto_file):
    """Converte Imagem para Texto usando OCR"""
    imagem = Image.open(imagem_file)
    texto = pytesseract.image_to_string(imagem)

    with open(texto_file, 'w') as file:
        file.write(texto)
    print(f'Imagem foi convertida para texto e salva em {texto_file}')

def escolha_saida(tipo_arquivo, arquivo_entrada):
    """Escolhe o formato de saída com base no tipo de arquivo de entrada"""
    if tipo_arquivo == 'csv':
        print("Escolha a saída:")
        print("1: CSV para JSON")
        escolha = input("Escolha uma opção (1): ")

        if escolha == '1':
            json_file = input("Digite o nome do arquivo de saída (com .json): ")
            csv_para_json(arquivo_entrada, json_file)
        else:
            print("Opção inválida")

    elif tipo_arquivo == 'pdf':
        print("Escolha a saída:")
        print("1: PDF para Texto")
        escolha = input("Escolha uma opção (1): ")

        if escolha == '1':
            texto_file = input("Digite o nome do arquivo de saída (com .txt): ")
            pdf_para_texto(arquivo_entrada, texto_file)
        else:
            print("Opção inválida")

    elif tipo_arquivo == 'imagem':
        print("Escolha a saída:")
        print("1: Imagem para Texto (OCR)")
        escolha = input("Escolha uma opção (1): ")

        if escolha == '1':
            texto_file = input("Digite o nome do arquivo de saída (com .txt): ")
            imagem_para_texto(arquivo_entrada, texto_file)
        else:
            print("Opção inválida")

    else:
        print("Tipo de arquivo desconhecido ou não suportado.")

def main():
    arquivo_entrada = input("Digite o caminho do arquivo de entrada: ")
    
    # Identificar o tipo de arquivo
    tipo_arquivo = identificar_tipo_arquivo(arquivo_entrada)
    
    if tipo_arquivo == 'desconhecido':
        print("Tipo de arquivo não suportado ou não reconhecido.")
    else:
        print(f"Arquivo identificado como {tipo_arquivo.upper()}.")
        escolha_saida(tipo_arquivo, arquivo_entrada)

# Chama a função principal
if __name__ == "__main__":
    main()