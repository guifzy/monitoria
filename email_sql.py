import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import numpy as np
import time

server = "smtp.gmail.com"
port = 587

login = "guimonteiro@sempreceub.com"  
password = "Inglescom12"

df = pd.read_csv(r'C:\Users\guipi\Desktop\python\monitoria\oficina_sql.csv')
resultados = df[['Nome completo', 'E-mail (@sempreceub)']]

for _, row in resultados.iterrows():
    nome = row['Nome completo']
    email = row['E-mail (@sempreceub)']
    
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = str(email) 
    msg['Subject'] = "Sala temporária - Oficina de SQL"
    
    body = f"""‼️Oficina de SQL‼️

Bom dia, galera!
Passando pra avisar que o laboratório 1001 está sendo utilizado para realização das provas das matérias EAD.
Por conta disto, hoje estaremos localizados no laboratório 1016.

Local: Campus Asa Norte, laboratório 1016
Período: de 11/04/2025 a 02/05/2025
Horário: das 11h às 12h30, com aulas todas as sextas

Monitoria de TI do CEUB Asa Norte
"""
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP(server, port) as smtp_server:
            smtp_server.starttls()  # criptografia TLS
            smtp_server.login(login, password)
            time.sleep(10)
            text = msg.as_string()
            smtp_server.sendmail(login, email, text)
            print(f"E-mail enviado com sucesso para {nome}!")
    except Exception as e:
        print(f"Falha ao enviar o e-mail: {e}")
        
