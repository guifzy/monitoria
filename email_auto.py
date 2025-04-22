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

df = pd.read_csv(r'C:\Users\guipi\Desktop\python\monitoria\oficina_python1.csv')
resultados = df[['Nome completo', 'E-mail (@sempreceub)']]

for _, row in resultados.iterrows():
    nome = row['Nome completo']
    email = row['E-mail (@sempreceub)']
    
    msg = MIMEMultipart()
    msg['From'] = login
    msg['To'] = str(email) 
    msg['Subject'] = "Aula 05 - Oficina de Introdrodução ao Python"
    
    body = f"""Boa tarde, galera!

            Passando pra reforçar a necessidade da realização da atividade postada na aula 04. A atividade é obrigatória e caso não tenham realizado, peço que não faltem a correção da mesma amanhã, e realizem o envio.
            
            Utilizaremos o envio da atividade como metodo de avaliação.

            Em caso de dúvidas, podem entrar em contato pelo grupo do WhatsApp ou e-mail.

            Boa tarde a todos e até amanhã!	
            
            Local: Campus Asa Norte, laboratório 1001
            Período: de 07/04/2025 a 30/04/2025
            Horário: das 11h às 12h30, com aulas todas as segundas e quartas-feiras

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
        
