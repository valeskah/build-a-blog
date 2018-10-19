from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

posts = []

@app.route('/', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
       blog_title = request.form['blog_title']
       posts.append(blog_title)

    return render_template('blog_posts.html', title='Build-a-Blog', posts=posts)

app.run()