#**********MailKiller Spam by Mehdi UHQ*************
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(num_emails):
    sender_email = "adressesend@gmail.com" #Remplacez par le mail source avec laquelle on va spam
    receiver_email = "mailreceiver@gmail.com" #Remplacez par le mail de la vic
    password = "u*pn n*gz fb*z *gt*"  # Remplacez par votre mot de passe d'application du mail qui spam

    # Connexion sécurisée au serveur SMTP de Gmail
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as server: #Remplacez par smtp du service mail
        server.starttls(context=context)  # Sécuriser la connexion
        server.login(sender_email, password)  # Se connecter au serveur SMTP
        
        for i in range(num_emails):
            # Créer le message
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = receiver_email
            msg["Subject"] = "Mehdi le SPAMMEUR UHQ | Test d'envoi d'email via SMTP"

            # Corps du message
            body = f"Ceci est un test d'envoi d'e-mail numéro {i+1} en utilisant Python et SMTP."
            msg.attach(MIMEText(body, "plain"))

            # Envoyer l'email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"E-mail numéro {i+1} envoyé avec succès !")
        
        print(f"Tous les {num_emails} e-mails ont été envoyés avec succès.")

# Demander le nombre d'e-mails à envoyer
num_emails = int(input("Combien d'e-mails voulez-vous envoyer ? : "))
send_email(num_emails)
