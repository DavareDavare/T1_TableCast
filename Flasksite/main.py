from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        helligkeit = request.form["Helligkeit"]
        geschwindigkeit = request.form["Geschwindigkeit"]
        text = request.form["Text"]

        #jsonstring = "{'Helligkeit':" + "\'" + helligkeit + "\', " + "\'Geschwindigkeit\':" + "\'" + geschwindigkeit + "\', " + "'Text':" + "\'" + text + "\'}"
        #data = eval(jsonstring)

        #print(data['Helligkeit'])
        #print(jsonstring)

        #with open("./Flasksite/inputs.json", "w") as fo:
            #fo.write(jsonstring)
        print(text)
        return f"Geschwindigkeit: {geschwindigkeit} \nHelligkeit:{helligkeit} \n"
    return render_template("index.html")

if __name__ == "__main__":
    app.run()