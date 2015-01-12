from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
  a = 'hello'
  b = 'world'
  return a+b
  

@app.route('/goodbye')
def goodbye():
  a = 'goodbye'
  b = 'world'
  return a+b
  
@app.route('/whattree')
def tree():
  return 'oak'
  
  
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)