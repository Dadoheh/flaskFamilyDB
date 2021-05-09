from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kom1A.db'
dba = SQLAlchemy(app)

class FamilyPost(dba.Model):
    id = dba.Column(dba.Integer, primary_key=True)
    names = dba.Column(dba.String(50), nullable=False)
    mail = dba.Column(dba.String(25), nullable=False)
    type = dba.Column(dba.String(2), nullable=False)
    date_posted = dba.Column(dba.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return 'Family:' + str(self.id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stopnie', methods=['GET','POST'])
def stopnie():
    if request.method == 'POST':
        post_names = request.form['names']
        post_mail = request.form['mail']
        post_type = request.form['type']
        new_post = FamilyPost(names = post_names, mail = post_mail, type = post_type)
        dba.session.add(new_post)
        dba.session.commit()
        return redirect('/stopnie')
    else:

        all_posts = FamilyPost.query.all()
        return render_template('stopnie.html', stopnie=all_posts)


@app.route('/stopnie/uponeb/<int:id>')
def uponeb(id):
    family = FamilyPost.query.get_or_404(id)
    family.type = '1B'
    dba.session.commit()
    return redirect('/stopnie')

@app.route('/stopnie/uptwo/<int:id>')
def uptwo(id):
    family = FamilyPost.query.get_or_404(id)
    family.type = '2'
    dba.session.commit()
    return redirect('/stopnie')

@app.route('/stopnie/upthree/<int:id>')
def upthree(id):
    family = FamilyPost.query.get_or_404(id)
    family.type = '3'
    dba.session.commit()
    return redirect('/stopnie')


@app.route('/stopnie/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    family = FamilyPost.query.get_or_404(id)
    if request.method == 'POST':
        family.names = request.form['names']
        family.mail = request.form['mail']
        family.type = request.form['type']
        dba.session.commit()
        return redirect('/stopnie')
    else:
        return render_template('edit.html', stopnie=family)


@app.route('/showonea', methods=['GET','POST'])
def showonea():
    if request.method == 'POST':
        post_names = request.form['names']
        post_mail = request.form['mail']
        post_type = request.form['type']
        new_post = FamilyPost(names = post_names, mail = post_mail, type = post_type)
        dba.session.add(new_post)
        dba.session.commit()
        return redirect('/stopnie')
    else:

        all_posts = FamilyPost.query.all()
        return render_template('stopnie.html', stopnie=all_posts)

@app.route('/showoneb', methods=['GET','POST'])
def showoneb():
    if request.method == 'POST':
        post_names = request.form['names']
        post_mail = request.form['mail']
        post_type = request.form['type']
        new_post = FamilyPost(names = post_names, mail = post_mail, type = post_type)
        dba.session.add(new_post)
        dba.session.commit()
        return redirect('/stopnie')
    else:

        all_posts = FamilyPost.query.all()
        return render_template('stopnie.html', stopnie=all_posts)

@app.route('/showtwo', methods=['GET','POST'])
def showtwo():
    if request.method == 'POST':
        post_names = request.form['names']
        post_mail = request.form['mail']
        post_type = request.form['type']
        new_post = FamilyPost(names = post_names, mail = post_mail, type = post_type)
        dba.session.add(new_post)
        dba.session.commit()
        return redirect('/stopnie')
    else:

        all_posts = FamilyPost.query.all()
        return render_template('stopnie.html', stopnie=all_posts)


@app.route('/showthree', methods=['GET','POST'])
def showthree():
    if request.method == 'POST':
        post_names = request.form['names']
        post_mail = request.form['mail']
        post_type = request.form['type']
        new_post = FamilyPost(names = post_names, mail = post_mail, type = post_type)
        dba.session.add(new_post)
        dba.session.commit()
        return redirect('/stopnie')
    else:

        all_posts = FamilyPost.query.all()
        return render_template('stopnie.html', stopnie=all_posts)


#TODO
#DRY - refactorize code btwn 73-133
#ADD html type's pages
#ADD  participance year 'rok uczestnictwa'
#ADD sorting by participance




if __name__ == '__main__':
    app.run(debug=True)
