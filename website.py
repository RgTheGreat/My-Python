from flask import Flask

app = Flask(__name__)

@app.route('/')
def test():
  return "<h2>Hello</h1>"



if __name == '__main__':
  app.run()
