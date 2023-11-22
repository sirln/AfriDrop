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


# @app.route('/reset_password/<token>', methods=['GET', 'POST'])
# def reset_password(token):
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        pass
    return render_template('reset_password.html', form=form)


# Sample data for the timeline
timeline_data = [
    {'user': 'User1', 'content': 'This is a post about something interesting.', 'image_url': '/static/images/post1.jpg', 'timestamp': '2023-01-01 10:00:00', 'likes': 25, 'views': 150, 'dislikes': 5},
    {'user': 'User2', 'content': 'Another post with some content.', 'image_url': '/static/images/post2.jpg', 'timestamp': '2023-01-02 12:30:00', 'likes': 15, 'views': 120, 'dislikes': 3},
    {'user': 'User3', 'content': 'Check out this amazing image!', 'image_url': '/static/images/post3.jpg', 'timestamp': '2023-01-03 15:45:00', 'likes': 30, 'views': 200, 'dislikes': 8},
    # Add more data as needed
]


@app.route('/timeline')
def timeline():
    return render_template('timeline.html', timeline_data=timeline_data)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
