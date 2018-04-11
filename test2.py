from flask import Flask, request
app= Flask (__name__)

@app.route ('/')
def index():
    return 'Method used: %s' % request.method

@app.route ("/methodology", methods =['GET','POST'])
def methodology():
    if request.method == 'POST':
        return "You are  using Method POST"
    else:
        return "Most likely you are using GET"



if __name__=="__main__":
    app.run()