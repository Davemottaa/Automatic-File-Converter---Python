# Conversor Automático de Arquivos - Python

Este projeto é um sistema automatizado desenvolvido em Python para **conversão de arquivos** entre diferentes formatos. O sistema identifica automaticamente o tipo de arquivo de entrada e permite ao usuário escolher o formato de saída desejado, tornando o processo simples e eficiente.

## Funcionalidades

- **Detecção Automática de Arquivo**: O sistema identifica o tipo de arquivo de entrada com base na sua extensão (CSV, PDF ou Imagem).
- **Conversões Suportadas**:
  - **CSV para JSON**
  - **PDF para Texto**
  - **Imagem para Texto (OCR)**
- **Interatividade com o Usuário**: O usuário escolhe o formato de saída desejado e fornece o nome do arquivo de saída.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **pandas**: Para manipulação e conversão de arquivos CSV.
- **PyPDF2**: Para leitura e extração de texto de arquivos PDF.
- **pytesseract** e **Pillow**: Para realizar OCR (Reconhecimento Óptico de Caracteres) em imagens.
- **os**: Para manipulação de arquivos e detecção de extensões.

## Como Usar

1. **Instale as dependências**:
   Você pode instalar as bibliotecas necessárias usando o `pip`:

   ```bash
   pip install pandas PyPDF2 pytesseract pillow
