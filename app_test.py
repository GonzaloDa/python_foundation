from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route('/finder')
def index():
    flash('Where would you like to go?')
    return render_template('index.html')


@app.route('/search', methods=['POST', 'GET'])
def search():
    flash('that would be an option: ' + str(request.form['event_input']))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_debugger=False, use_reloader=False)