from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:lc101@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog_post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(120))
    blog_body = db.Column(db.String(120))

    def __init__(self, blog_title, blog_body):
        self.blog_title = blog_title
        self.blog_body = blog_body



posts = []

@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
       blog_title = request.form['blog_title']
       posts.append(blog_title)

    return render_template('blog_posts.html', title='Build-a-Blog', posts=posts)

if __name__ == '__main__':
    app.run()