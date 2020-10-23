from flask import Flask, redirect, url_for, render_template, request

from app.form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'who-let-the-dogs-out'


@app.route('/')
def index(status=None, message=None):
    return render_template("index.html", status=status, message=message)


@app.route('/<status>/<message>')
def send_message(status, message):
    return render_template("index.html", status=status, message=message)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('send_message', status="success", message="Mensagem enviada com sucesso!"))
        else:
            return render_template('contact.jinja2', form=form, status='error', message=form.errors)

    return render_template('contact.jinja2', form=form)


@app.route('/test')
def test():
    return redirect(url_for('send_message', status="success", message="Mensagem enviada com sucesso!"))


@app.route('/test2')
def test2():
    return redirect(url_for('send_message', status="error", message=[{"campo": "erro"}]))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
