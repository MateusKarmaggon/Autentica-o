#importar o pyrebase4 no pip
import pyrebase

#insira suas credenciais do firebase!!!!
firebaseConfig = {
    "apiKey": "*****************************",
    "authDomain": "************************",
    "projectId": "************************",
    "databaseURL": "https://" + "************************" + "************************",
    "storageBucket": "************************",
    "messagingSenderId": "***************",
    "appId": "**********************",
    "measurementId": "G-************"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

user = input("Digite seu e-mail: ")
password = input("Digite sua senha, com pelo menos 6 caracteres: ")
status = auth.sign_in_with_email_and_password(user,password)
print("Resultado: ", status)



