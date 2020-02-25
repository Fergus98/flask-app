 # import render_template function from the flask module
from flask import render_template, redirect, url_for
 # import the app object from the ./application/__init__.py
from application import app, db, bcrypt

from application.models import Posts, Users
from application.forms import PostForm, RegistrationForm
 # define routes for / & /home, this function will be called when these are accessed

@app.route('/')
@app.route('/home')
def home():
    blogData = Posts.query.first()
    return render_template('home.html', title='Home', posts = blogData)

@app.route('/posts', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        postData = Posts(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            title = form.title.data,
            content = form.content.data
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('posts.html', title='Post', form=form)
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data.decode('utf-8'))

        user = Users(email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('post'))
    return render_template('register.html', title='Register', form=form)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')
@app.route('/bantz')
def bantz():
    info = "bants"
    return render_template('bantz.html', title = 'Bantz')
