#import stmts
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

# app initialization
app = Flask(__name__)

# ENV veriable
ENV = "prod"

# Check if Env is dev or not
if ENV == "dev":
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:12345@localhost/lexus";
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://ivekmupriyazsz:e537af65df1d20daadf5e8a2920a875b8f7ebc89699d9199a29a9fb73d94978d@ec2-107-21-120-104.compute-1.amazonaws.com:5432/d1nik6901ffdmm"  

app.config['SQLALCHEMY_TRACK_MODIFICATIONS)'] = False

# instance of the SQLAlchemy
db = SQLAlchemy(app)

# creating Model
class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    # Conctructor or Initializer
    def __init__(self, customer, dealer, rating, comments):
        self.customer = customer
        self.dealer = dealer
        self.rating = rating
        self.comments = comments

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message ='Please enter required * fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, rating, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, rating, comments)
            return render_template('success.html')
        return render_template('index.html', message ='You may have already submitted feedback')

# main function
if __name__ == '__main__':
    app.debug =True
    app.run()