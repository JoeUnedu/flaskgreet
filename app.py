from flask import  Flask

app = Flask(__name__)



@app.route("/welcome")
def welcome(welcome):
  if(welcome.lower() == "welcome") or  (welcome.lower() == "John"):
  
   return " welcome   Mr John"
  else:
   return   None



@app.route("welcome")
def  welcome_home(welcome_home):
  if((welcome_home.lower() == "welcome") or (welcome_home.lower()=="John")):
    
   return "welcome home Mr John"
  else:
    return  None