# TableCast
How the turns have tabled

#Einleitung

Die HTL Saalfelden hat im Zuge des Werkstättenunterrichts in der Mechatronikabteilung
einen Produkt Präsentationsdrehteller entworfen. Darauf können kleine Produkte platziert werden welche so den Kunden präsentiert werden
können.
Der Drehteller wird dabei von einem kleinen DC-Motor angetrieben(DC = Gleichstrom). Das Produkt wird von allen 4 Seiten mit Hilfe von LEDs beleuchtet, das Display an der
Vorderseite dient zur Anzeige von Informationen. Bisher wurde die Motorgeschwindigkeit, LED Helligkeit und der Displaytext über eine
Android APP eingestellt. Die Elektronik des Drehtellers war mit einem kleinen
Mikrocontroller inkl. Bluetoothmodul realisiert.


#Anforderungen
Die bestehende Elektroniklösung soll durch einen Raspberry Pi Zero (inkl. WLAN) ersetzt
werden, die Android APP durch eine Webseite damit der Drehteller mit beliebigen
Endgeräten konfiguriert werden kann (und nicht mehr nur mit einem Android Smartphone).

ACHTUNG: Nichtbestandteil des Projektes ist es die Elektronik, welche mit dem Raspberry Pi verbunden ist zu realisieren. Diese wird von der Werkstätte der HTL Saalfelden zur Verfügung gestellt. 
Die Webseite zum Konfigurieren des Drehteller soll folgende Einstellmöglichkeiten bieten. 
- Konfiguration der Motorgeschwindigkeit [0...100]
- Einstellen der LED Helligkeit [0...100]
- Displaytext (20 Zeichen pro Zeile).
- Umschaltgeschwindigkeit zwischen Displaytexten [Sekunden 2...10]

Weitere Einstellmöglichkeiten für Netzwerkverbindung:
Modus: „WLAN-Hotspot“ oder mit „bestehendem WLAN“ verbinden. Der Drehteller soll einen WLAN Hotspot (Modus: WLAN Hotspot) anbieten. Die SSID soll
ebenfalls konfigurierbar sein (Defaultwert: Drehteller1)

Der Modus „bestehendem WLAN“ kann nur konfiguriert werden, wenn der Drehteller zuvor
im Modus „WLAN-Hotspot“ ist. Dazu soll die SSID und Passwort den WLAN eingegeben
werden können. Nach einen „Neustart“ soll sich der Drehteller dann mit dem WLAN
verbinden. Schlägt das fehl, soll er automatisch wieder in den Modus „WLAN- Hotspot“ zurückwechseln. Es soll möglich sei „mehrere“ Zeilen am Display anzuzeigen. Dazu wird in einer einstellbaren Zeit (siehe oben) zwischen den einzelnen Zeilen umgeschaltet. Maximal sollen 10 Zeilen möglich sein. Die eingestellten Werte sollen in einem (mit einem Texteditor) lesbaren Format am
Raspberry abgespeichert werden können. Unmittelbar nach dem Einschalten des Drehtellers soll die IP-Adresse des Drehtellers kurz angezeigt werden, danach sollen die gespeicherten Texte in einer Endlosschleife am Display angezeigt werden. Damit die Konfiguration nicht ohne weiteres geändert werden kann, muss die Webseite Benutzer/Passwort geschützt sein. Um nachträglich Änderungen an der Drehteller Software vorgenommen zu können, soll derRaspberry über einen aktiven SSH Server verfügen.
Es wird in Zukunft geplant sein, mehrere dieser Drehteller in einem gemeinsamen Netzwerk
der HTL-Saalfelden betreiben und verwalten zu können. Daher soll jeder Drehteller eine
einfache API anbieten über welche die Konfgurationsparameter des jeweiligen Gerätes
gesetzt/gelesen werden können. Die Berechtigung soll bei der API über einen Token o.ä. erfolgen. Um einer möglichen Fehlentwicklung entgegenzuwirken, sollen für die Bedienoberfläche
zuvor Mockups erstellt werden, welche dem Kunden vorzulegen sind


#Projektmanagementanforderungen

Das Projekt soll mit Hilfe agiler Methoden (SCRUM) umgesetzt werden. Der Quellcode sowie sämtliche Dokumentation ist in einem GITHUB Repository abzulegen. Das AddOn Zenhub (https://www.zenhub.com/) sorgt für die Integration zwischen Scrum
und Github. Obwohl das Projekt mit agilen Methoden realisiert werden soll ist erforderlich sich zu Beginn gewissen Fragen zu stellen und zu klären:
- Variantenbildung
- Umfeldanalyse (gibt es bereits ähnliche Produkte. Welchen Funktionsumfang bieten diese
  und wie kann sich unsere Lösung von diesen unterscheiden?)
- Grobe Zeitplanung (welche sobald die Teamvelocity bekannt ist, verfeinert werden soll). 

Führen Sie zu Beginn einen „Sprint 0“ durch in welchem sie die Grobplanung vornehmen, UserStories schreiben und schätzen und ein grundsätzliches Design der Software
vornehmen. Dokumentation des Projektes
- Softwarearchitektur
- Klassendiagramme
- Sequenzdiagramme, Aktivitätsdiagramm
- Komponentendiagramm, Verteilungsdiagramm
- Interaktionen
- Use-Case Beschreibung
- Sprintplanung
- Sprint-Demo
- Sprint-Retrospektive und Impediment-Management
- Projektcontrolling

Für die Projektdokumentation wird ein Templatefile zur Verfügung gestellt. Projektlaufzeit: 11. Jänner 2023

~ Stand 11.01.2022, FAL/EIG, Datei SYP_4_Projektbeschreibung_ProduktDrehteller_2022-2023.pdf
