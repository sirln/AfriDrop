import os
import uuid
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, session
from forms import SignUpForm, SignInForm, ForgotPasswordForm, ResetPasswordForm, PostForm


app = Flask(__name__)
# app.secret_key = str(uuid.uuid4())
SECRET_KEY = str(uuid.uuid4())
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = 'uploads'

# Load environment variables from .env
load_dotenv()


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


@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        # Handle form submission logic here
        pass
    return render_template('reset_password.html', form=form)


@app.route('/search')
def search():
    query = request.args.get('query', '')
    # Implement search logic based on the query
    # For simplicity, let's assume the search results are the same as the timeline data
    search_results = timeline_data
    return render_template('timeline.html', timeline_data=search_results)


# Sample data for the timeline
timeline_data = [
    {'user': 'User1', 'user_image_url': '/static/images/post1.png', 'content': 'This is a post about something interesting.', 'image_url': '/static/images/post1.png', 'timestamp': '2023-01-01', 'likes': 25, 'views': 150, 'dislikes': 5},
    {'user': 'User2', 'user_image_url': '/static/images/post2.png', 'content': 'Another post with some content.', 'image_url': '/static/images/post2.png', 'timestamp': '2023-01-02', 'likes': 15, 'views': 120, 'dislikes': 3},
    {'user': 'User3', 'user_image_url': '/static/images/post3.png', 'content': 'Check out this amazing image!', 'image_url': '/static/images/post3.png', 'timestamp': '2023-01-03', 'likes': 30, 'views': 200, 'dislikes': 8},
    # Add more data as needed
]

@app.route('/timeline')
def timeline():
    return render_template('timeline.html', timeline_data=timeline_data)


#@app.route('/')
#def home():
#    if 'username' in session:
#        return redirect(url_for('timeline'))
#    return render_template('home.html')

#@app.route('/timeline')
#def timeline():
#    if 'username' not in session:
#        return redirect(url_for('signin'))  # Redirect to the signin page if the user is not signed in

#    username = session['username']
#    user_data = users.get(username, {'timeline_data': []})
#    return render_template('timeline.html', timeline_data=user_data['timeline_data'], username=username)


@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        # Save the file to the 'uploads' folder
        file = request.files['file']
        file.save(f'uploads/{file.filename}')

        # Process the description and file as needed (e.g., save to a database)

        return 'Post submitted successfully!'
    return render_template('post_form.html', form=form)


@app.route('/review')
def review_page():
    return render_template('review_page.html')


@app.route('/')
def home():
    # Access the API key
    API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    cities = ['Nairobi', 'Eldoret', 'Mombasa', 'Thika', 'Kisumu']
    services = ['Spa/Salon services', 'Healthcare', 'Groceries', 'Luxury products']

    return render_template('afri_home.html', cities=cities, services=services, API_KEY=API_KEY)


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000, debug=True)
