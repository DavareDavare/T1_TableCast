from flask import Flask, request, render_template, redirect, url_for, json, escape
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/settings", methods=["GET", "POST"])
def settings():
    if request.method == "POST":
        helligkeit = request.form["Helligkeit"]
        geschwindigkeit = request.form["Geschwindigkeit"]
        text = request.form["Text"]
        wlan = request.form["WLAN-Name"]
        wlanpw = request.form["WLAN-Passwort"]

        text = text.replace('\r', ', ').replace('\n', '')
        stringsss = ["12","321","321"]
        print(text)

        jsonstring = "{\"Helligkeit\":" + "\"" + helligkeit + "\", " + "\"Geschwindigkeit\":" + "\"" + geschwindigkeit + "\", " + "\"Text\":" + "\"" + text + "\", " + "\"WLAN\":" + "\"" + wlan + "\", ""\"WLAN-Passwort\":" + "\"" + wlanpw + "\"}"
        data = eval(jsonstring)
        print(jsonstring)

        #print(data['Helligkeit'])
        #print(jsonstring)

        with open("./Flasksite/inputs.json", "w") as fo:
            fo.write(jsonstring)

        return f"""
        <h3>Folgende Werte wurden eingegeben:</h3>
        <ul>
            <li>Helligkeit:{escape(helligkeit)}</li>
            <li>Geschwindigkeit: {escape(geschwindigkeit)}</li>
            <li>WLAN-Name:{escape(wlan)}</li>
            <li>WLAN-Passwort:{escape(wlanpw)}</li>
            <li>Text:</li>
        </ul>
        
        <a href="{"/"}"> Zurück zum Hauptmenü </a>
        """
    return render_template("settings.html")


@app.route("/load", methods=["GET", "POST"])
def load():
    with open("./Flasksite/inputs.json") as json_file:
        data = json.load(json_file)

    return f"""
    <H3>Folgende Daten Geladen:</h3> 
    <ul>
        <li>Helligkeit:{escape(data['Helligkeit'])}</li>
        <li>Geschwindigkeit:{escape(data['Geschwindigkeit'])}</li>
        <li>Wlanname:{escape(data['WLAN'])}</li>
        <li>Wlanpasswort:{escape(data['WLAN-Passwort'])}</li>
        <li>Text:{escape(data['Text'])}</li>
    </ul>

    <a href="{"/"}">Zurück zum Hauptmenü</a>
    """

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()