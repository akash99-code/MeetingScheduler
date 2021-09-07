from flask import Flask, render_template, request,redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://u0sf5f7crjrg2nie:oU40voJTtXLurF9fxDGW@bmneo6iuwyphevtyy2a7-mysql.services.clever-cloud.com:3306/bmneo6iuwyphevtyy2a7"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TTdb(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    mon = db.Column(db.String(500), nullable=True)
    tue = db.Column(db.String(500), nullable=True)
    wed = db.Column(db.String(500), nullable=True)
    thu = db.Column(db.String(500), nullable=True)
    fri = db.Column(db.String(500), nullable=True)
    sat = db.Column(db.String(500), nullable=True)
    sun = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'[{self.sno}, "{self.mon}", "{self.tue}", "{self.wed}", "{self.thu}", "{self.fri}", "{self.sat}"]'


@app.route('/', methods=['GET'])
def home():
    try:
        TTdata = TTdb.query.all()
    except:
        return redirect('/')
    if(not TTdata):
        return redirect('/')
    return render_template('index.html', TTdata=TTdata)

@app.route('/edit', methods=['GET'])
def edit():
    TTdata = TTdb.query.all()
    return render_template('edit.html', TTdata=TTdata)

@app.route('/update/<int:sno>/<day>', methods=['POST'])
def update(sno, day):
    dat = request.form['input']
    rows_updated = TTdb.query.filter_by(sno=sno).update({day:dat})
    db.session.commit()
    return redirect('/edit')



if __name__ == "__main__":
    app.run(debug=True)    