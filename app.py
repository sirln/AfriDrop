import uuid
from flask import Flask, render_template
from forms import SignUpForm, SignInForm, ForgotPasswordForm, ResetPasswordForm

app = Flask(__name__)
SECRET_KEY = str(uuid.uuid4())
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        pass
    return render_template('sign_up.html', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        pass
    return render_template('sign_in.html', form=form)


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        pass
    return render_template('forgot_password.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        pass
    return render_template('reset_password.html', form=form)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
