from flask import Flask, request, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'chamberofsecrets'

class Blog_post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_body = db.Column(db.String(120))

    def __init__(self, blog_title, blog_body):
        self.blog_title = blog_title
        self.blog_body = blog_body


@app.route('/new_post', methods=['POST', 'GET'])
def new_post():

    return render_template('new_post.html')
    

@app.route('/', methods = ['POST', 'GET'])
def index():
    title_error = ''
    body_error = ''

    if request.method == 'POST':
        blog_title = request.form['blog_title']
        blog_body = request.form['blog_body']
        errors = 0

        if blog_title == '':
            title_error = "Please fill in title"
            errors = errors + 1
        if blog_body == '':
            body_error = "Please fill in body"
            errors = errors + 1
        
        if errors > 0:
            return render_template('new_post.html', blog_title=blog_title, blog_body=blog_body, title_error=title_error, body_error=body_error)

        else:
            blog_post = Blog_post(blog_title, blog_body)
            db.session.add(blog_post)
            db.session.commit()
            return render_template('blog_page.html', blog_title=blog_title, blog_body=blog_body, id=id)
            
    posts = Blog_post.query.all()
    return render_template('blog_list.html', posts=posts)

@app.route('/blog', methods=['GET'])
def blog_page():

    return render_template('blog_page.html')


if __name__ == '__main__':
    app.run()