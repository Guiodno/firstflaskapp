from flask import Flask , request, render_template

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET"])
def login():
    email = 'Guiodnolaguerre@yahoo.fr'
    print(request.form.get('email'))
    if request.form.get('email') == email:
        login = True
        return render_template('index.html', login=login)
    else:
        return render_template('index.html')

