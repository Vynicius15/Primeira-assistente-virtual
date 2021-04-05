#Our main file.

isport speech_recognition as sr 

# cria um reconhecedor
r = sr.recognizer ()

# Abrir o microfone para captura
with sr. microfone() as sowrce:
   audio - r.listen(sowrce) # Define microfone como fonte de áudio 

with true: 
print(r. recognize_google(audio))
