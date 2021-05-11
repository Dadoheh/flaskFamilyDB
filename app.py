from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import insert

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///komunikacja.db'
dba = SQLAlchemy(app)

class FamilyPost(dba.Model):
    id = dba.Column(dba.Integer, primary_key=True)
    names = dba.Column(dba.String(50), nullable=False)
    mail = dba.Column(dba.String(25), nullable=False)
    type = dba.Column(dba.String(2), nullable=False)
    date_posted = dba.Column(dba.DateTime, nullable=False, default=datetime.utcnow)
    date_participance = dba.Column(dba.String(20), nullable=True)
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
        post_participance = request.form['date_participance']
        new_post = FamilyPost(names = post_names, mail = post_mail, type = post_type, date_participance = post_participance)
        dba.session.add(new_post)
        dba.session.commit()
        return redirect('/stopnie')
    else:

        all_posts = FamilyPost.query.all()
        return render_template('stopnie.html', stopnie=all_posts)

##########################################################changing type (for everyone)###########################
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
##################################################################################################################


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
        return redirect('/showonea')
    else:

        all_posts = FamilyPost.query.filter_by(type='1A').all()
        return render_template('showonea.html', showonea=all_posts)

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


"""
#how do add a column in sqlalchemy

from sqlalchemy import String, MetaData, create_engine
from migrate.versioning.schema import Table, Column

db_engine =  create_engine(app.config.get('SQLALCHEMY_DATABASE_URI'))
db_meta = MetaData(bind=db_engine)
=======
#ADD  participance year 'rok uczestnictwa'
#ADD sorting by participance

table = Table('tabel_name' , db_meta)
col = Column('new_column_name', String(20), default='foo')
    col.create(table)

"""


##########################################################changing type (for onea)###########################
"""@app.route('/stopnie/uponeb/<int:id>')
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
    return redirect('/stopnie')"""
############################################################################################################
##########################################################changing type (for one)###########################

############################################################################################################
##########################################################changing type (for one)###########################

############################################################################################################
##########################################################changing type (for one)###########################

############################################################################################################

if __name__ == '__main__':
    app.run(debug=True)
