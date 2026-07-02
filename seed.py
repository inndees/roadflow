from app import app
from db import db, User, Project, ProjectImage

def simulate_app():
    with app.app_context():
        print("🔨 Initializing prototype database...")
        db.drop_all()
        db.create_all()

        # 1. Simulate creating a User session/account
        print("👤 Creating mock user...")
        mock_user = User(username="johndoe_admin", email="john@constructioncorp.com")
        db.session.add(mock_user)
        db.session.commit() # Commit to generate user ID

        # 2. Simulate creating a Project entry
        print("🚧 Adding mock construction project...")
        mock_project = Project(
            name="Route 66 Highway Expansion",
            description="Widening of the primary northern transport corridor.",
            project_type=1, # 1 representing Highway infrastructure
            road_length=14.75,
            user_id=mock_user.id
        )
        db.session.add(mock_project)
        db.session.commit()

        # 3. Simulate uploading images with Geo-location Metadata
        print("📸 Attaching geo-tagged construction images...")
        img1 = ProjectImage(
            image_filename="progress_site_east_01.jpg",
            latitude=34.0522,   # Mock Coordinates
            longitude=-118.2437,
            project_id=mock_project.id
        )
        img2 = ProjectImage(
            image_filename="asphalt_laying_west_02.jpg",
            latitude=34.0528,
            longitude=-118.2445,
            project_id=mock_project.id
        )
        db.session.add_all([img1, img2])
        db.session.commit()
        
        print("✅ Mock data generation complete!\n")
        print("="*50)
        print("🖥️  SIMULATING A BACKEND DATABASE QUERY:")
        print("="*50)

        # Query simulation
        project = Project.query.filter_by(name="Route 66 Highway Expansion").first()
        print(f"Project Name: {project.name}")
        print(f"Managed By:   {project.owner.username} ({project.owner.email})")
        print(f"Road Length:  {project.road_length} km")
        print(f"Total Images: {len(project.images)}")
        
        for index, img in enumerate(project.images, 1):
            print(f"  └─ Image {index}: {img.image_filename}")
            print(f"     📍 Location: Lat {img.latitude}, Lng {img.longitude}")
        print("="*50)

if __name__ == '__main__':
    simulate_app()