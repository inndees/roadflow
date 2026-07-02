from flask import Flask, jsonify
from datetime import datetime
from db import db, User, Project, ProjectImage

app = Flask(__name__)

# Standard SQLite configuration for local prototyping
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prototype.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'proto-secret-key-12345'

db.init_app(app)

# --- ROUTE FOR VISUALIZING THE DATA ---

@app.route('/api/projects', methods=['GET'])
def get_projects():
    """ Fetches all projects along with their linked user and image metadata """
    projects = Project.query.all()
    output = []
    
    for proj in projects:
        project_data = {
            'project_id': proj.id,
            'name': proj.name,
            'description': proj.description,
            'type_code': proj.project_type,
            'road_length_km': proj.road_length,
            'created_by': proj.owner.username,
            'images': [
                {
                    'filename': img.image_filename,
                    'geo_location': {'lat': img.latitude, 'lng': img.longitude}
                } for img in proj.images
            ]
        }
        output.append(project_data)
        
    return jsonify({'projects': output})

if __name__ == '__main__':
    app.run(debug=True)