from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
logging.basicConfig(filename='count_app.log', level=logging.INFO)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/count_db'
db = SQLAlchemy(app)

class ProcessedNumber(db.Model):
    num = db.Column(db.Integer, primary_key=True)

    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return 'Proccessed number %r>' % self.num

def is_valid_number(n):
    try:
        int(n)
    except ValueError:
        return False
    return int(n)>=0

@app.route('/increase', methods=['POST'])
def increase():
    # Validate request data
    if not request.is_json:
        return jsonify({'error' : 'Expected json'}), 400
    data = request.get_json()
    if not 'num' in data:
        return jsonify({'error' : 'Expected "num" in request body' }), 400
    if not is_valid_number(data['num']):
        return jsonify({'error' : 'Expected "num" to be a natural number'}), 400
    
    num = int(data['num'])

    res = ()

    print(ProcessedNumber.query.filter_by(num=num).first())
    # num is NOT in database
    if ProcessedNumber.query.filter_by(num=num).first() is None:
        # num+1 is NOT in database
        if ProcessedNumber.query.filter_by(num=num+1).first() is None:
            res = (jsonify({'increased_num' : num+1}), 200)
        # num+1 is in database
        else:
            logging.info(f'User {request.remote_addr} sent number {num}. {num} + 1 is found in database')
            res = (jsonify({'error' : str(num) + '+1 exists in database'}), 400)
        try:
            # add num to database 
            new_num = ProcessedNumber(num)
            db.session.add(new_num)
            db.session.commit()
        except SQLAlchemyError as e:
            logging.error(str(e.__dict__['orig']))        
            res = (jsonify({'error' : 'Application server error'}),500)
    # num is in database
    else:
        logging.info(f'User {request.remote_addr} sent number {num}. This number is found in database')
        res = (jsonify({'error' : str(num) + ' exists in database'}), 400)
    
    return res

if __name__ == '__main__':
    app.run(debug=True)



