from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from bp.bp_mission import mission_bp
from bp.bp_analyse import analysis_bp
from models.DB import db


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/wwi_missions'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(mission_bp, url_prefix='/api/mission')
app.register_blueprint(analysis_bp, url_prefix='/api/analysis')





if __name__ == '__main__':
    with app.app_context():
        try:
            db.session.execute(text('SELECT 1'))
            print("Connection successful!")
        except Exception as e:
            print("Connection failed:", str(e))

    app.run(debug=True)