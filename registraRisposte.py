import registratore


print("inserisci il nome della registrazione: ")
nome = input()
try:
    print("inizio registrazione!")
    fn = registratore.get_audio(duration=4.0, filename=nome)
    print(f'salvato nuovo file come [ {fn} ]')
except Exception as e:
    print(str(e))
