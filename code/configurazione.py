class Config:

    def __init__(self, diz: dict):
        self.orario_sveglia = diz['orario_sveglia']
        self.stato_sveglia = diz['stato_sveglia']
        self.id_chat_telegram = diz['id_chat_telegram']

    def cambia_orario_sveglia(self, orario: str):
        self.orario_sveglia = orario
        self.stato_sveglia = True

    def cambia_stato_sveglia(self, stato: bool):
        self.stato_sveglia = stato

    def cambia_id_chat_telegram(self, idchat: int):
        self.id_chat_telegram = idchat
