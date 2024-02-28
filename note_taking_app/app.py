from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

notes = []
@app.route('/', methods=['GET','POST'])
def index():
    note = request.form.get("note")
    if note:
        notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/clear', methods=['POST'])
def clear_notes():
    global notes
    notes = []
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)