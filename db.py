from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# --- DATABASE MODELS ---

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    projects = db.relationship('Project', backref='owner', lazy=True)


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    project_type = db.Column(db.Integer, nullable=False)  # e.g., 1=Highway, 2=Local Road
    road_length = db.Column(db.Float, nullable=False)      # In kilometers
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    images = db.relationship('ProjectImage', backref='project', lazy=True)


class ProjectImage(db.Model):
    __tablename__ = 'project_images'
    id = db.Column(db.Integer, primary_key=True)
    image_filename = db.Column(db.String(255), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
