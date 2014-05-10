from flask import Flask, Response, render_template, request, copy_current_request_context

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')



if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0')
