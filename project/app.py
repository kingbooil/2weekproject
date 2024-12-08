from flask import Flask, render_template, request  

app = Flask(__name__)  

@app.route("/") 
def home():
   return render_template("index.html")  

@app.route("/login") 
def login():
   username = request.args.get('username')
   password = request.args.get('password')

   if username == "admin" and password == "1234":
       return render_template("home.html", username=username)
   
   if username == "booil" and password == "1234":
       return render_template("home.html", username=username)
   
   return render_template("retry.html")

@app.route("/logout") 
def logout():
   return render_template("login.html")  

if __name__ == "__main__":
   app.run()