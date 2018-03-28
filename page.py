from flask import Flask, render_template
app= Flask (__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route ('/commodities')
def commodities():
    commodities = ["Oil" , "Steel", "Gold"]
    return render_template("commodities.html", commodities=commodities)

if __name__=="__main__":
    app.run()