from flask import Flask
app = Flask(__name__)

print(__name__)
@app.route('/')

def hello_world():
    return "Get to work, weirdo!"

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<name>')
def say(name):
    return "Hi " + name

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    print(word * int(num))
    return (word + " ") * int(num)

if __name__=="__main__":

    app.run(debug = True)