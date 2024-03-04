from flask import Flask, render_template, redirect, url_for, request

app=Flask(__name__)

users='user'
key='pass'
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
	
	
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Dummy user validation
        return render_template('index.html' ,name=username+"you have succusfully registered")
		
		
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Dummy user validation
        if username in users and password in key:
            return render_template('home.html' ,name=username)
        else:
            return render_template('register.html' ,name=username)
    else:
        return render_template('index.html')
	
@app.route('/logout')
def logout():
    return redirect(url_for('login'))
		
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)