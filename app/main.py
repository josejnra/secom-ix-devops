from flask import Flask, render_template, request

from app.form import IMCForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'who-let-the-dogs-out'


@app.route('/')
def index():
    return render_template("index.html")


    if request.method == 'POST':
        if form.validate_on_submit():
            return redirect(url_for('send_message', status="success", message="Mensagem enviada com sucesso!"))
        else:
            return render_template('contact.jinja2', form=form, status='error', message=form.errors)

    return render_template('contact.jinja2', form=form, status=None, message=None)


@app.route('/imc', methods=['GET', 'POST'])
def imc_calc():
    form = IMCForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            imc = round(form.peso.data / (form.altura.data**2), 2)
            return render_template('imc_result.jinja2', imc_result=imc)
        else:
            return render_template('imc_calc.jinja2', form=form)

    return render_template('imc_calc.jinja2', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
