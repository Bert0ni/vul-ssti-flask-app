import os

from flask import Flask, render_template, request, send_from_directory, url_for, redirect, render_template_string


app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')
   if name:
       template = f'<h1><center><h1>EPAM Red Team</h1><img src="/static/images/logo.jpg"></img><hr>Knowlege sharing session<hr> Hello {name}!</h1>'
       return render_template_string(template)
   else:
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()
