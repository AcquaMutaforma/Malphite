# Malphite - CareGiverBot
Il CareGiverBot (CGB) ha lo scopo di aiutare gli anziani che hanno bisogno di
sostegno in tutti i momenti del giorno e potrà essere utilizzato nelle case di riposo
per facilitare il lavoro degli operatori. Il CGB farà da supporto riproducendo, in base a
quello che ascolta, le registrazioni di chi si occupa degli anziani. Questo sistema è
composto da una scheda Raspberry compresa di microfono e cassa, inoltre se
connesso alla rete sono disponibili anche un’interfaccia web e feedback in tempo
reale tramite Telegram.

## Cosa fa in breve
La principale funzione del CGB è rispondere a domande o affermazioni tramite la
riproduzione di registrazioni effettuate precedentemente. Quando il sistema è in
ascolto effettua un’analisi delle parole che riesce a comprendere, e in base ad esse
sceglie la risposta da riprodurre più opportuna.
Nel caso in cui l’audio analizzato non trovi una corrispondenza con le risposte che
sono state inserite nel sistema, il CGB provvederà ad inviare un messaggio
all’operatore attraverso l’app Telegram. L’operatore ha la possibilità di rispondere
direttamente alla richiesta tramite un messaggio vocale, che verrà riprodotto dal
raspberry. Più nel dettaglio il sistema riproduce i messaggi che riceve attraverso
Telegram in maniera proattiva, utile per rispondere a domande particolari
dell’anziano o fare avvisi.
Il CareGiverBot può essere gestito tramite un’interfaccia web, utile per la modifica
delle impostazioni della funzione sveglia, per il collegamento alla chat Telegram e la
gestione delle risposte che il CGB riproduce. Per svolgere le sue funzioni di
assistenza tramite Telegram è fondamentale che il CGB sia connesso ad Internet,
mentre per l’interfaccia web è necessario che sia collegato alla rete locale.

## Linguaggi e tecnologie utilizzati
Python - Abbiamo deciso di utilizzare il linguaggio Python per la sua elasticità e
portabilità.
Telegram API - Per consentire ad un operatore di ricevere in tempo reale domande
non comprese dal nostro sistema, abbiamo deciso di utilizzare un bot Telegram.
Coqui AI - Per la traduzione da parlato a testo abbiamo utilizzato l’intelligenza
artificiale Coqui dato che si tratta di un progetto OPEN ed è possibile addestrarla
utilizzando file audio personalizzati.
Django - Django è un framework per le applicazioni web, lo abbiamo scelto per la
sua semplicità d’utilizzo e la compatibilità con il linguaggio Python. Questo strumento
ci aiuta a gestire le pagine web e la comunicazione con il Database.
PostgreSQL - Abbiamo scelto questo tipo di database dato che è compatibile con
Django.
Raspberry pi 3 - Scheda utilizzata per i test, abbiamo utilizzato quella insieme a
microfono e casse che avevamo già a casa.
Raspberry + Debian - Come host abbiamo deciso di utilizzare una scheda
raspberry con il sistema operativo consigliato, ovvero Debian 11 - Bullseye.

## Thanks
Il resto dei dettagli sono presenti nel file [Relazione.pdf](./Relazione.pdf) in cui è descritta la procedura.