import os

from flask import Flask, render_template_string, request, redirect, url_for

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
       template = f'<h1><center><img src="/static/images/logo.jpg"></img><hr> Hello {name}!</h1>'
       return render_template_string(template)
   else:
       return redirect(url_for('index'))


# @app.route('/run-command')
# def run_command():
#     command = request.args.get('rto-rce')
#     if command:
#         try:
#             result = os.popen(command).read()  # Executes the command and captures the output
#             return f"Command executed: {command}\nResult:\n{result}"
#         except Exception as e:
#             return f"Error executing command: {str(e)}"
#     else:
#         return "No command provided"



if __name__ == '__main__':
   app.run()
