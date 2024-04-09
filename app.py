from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return render_template('chit_chat/index.html')


@app.route('/login-user', methods=['GET', 'POST'])
def login():
    return render_template('chit_chat/login.html')


@app.route('/add_user', methods=['GET', 'POST'])
def register():
    return render_template('chit_chat/register.html')


if __name__ == '__main__':
    app.run()
