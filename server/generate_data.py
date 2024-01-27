import os
import django
from django_seed import Seed
from faker import Faker

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# Import your models
from app.models import Category, Award, Nominee

# Create an instance of the Faker class
fake = Faker()

# Set the random seed for reproducibility
Faker.seed(42)

# Function to generate dummy data
def generate_dummy_data():
    # Use django-seed to seed data
    seeder = Seed.seeder()

    # Seed Category model
    seeder.add_entity(Category, 5, {
        'name': lambda x: fake.word(),
        'description': lambda x: fake.sentence(),
    })

    # Seed Award model
    seeder.add_entity(Award, 20, {
        'category': lambda x: Category.objects.order_by('?').first(),
        'name': lambda x: fake.word(),
        'description': lambda x: fake.sentence(),
    })

    # Seed Nominee model
    seeder.add_entity(Nominee, 1500, {
        'award': lambda x: Award.objects.order_by('?').first(),
        'full_name': lambda x: fake.name(),
        'email': lambda x: fake.email(),
        'phone': lambda x: fake.phone_number(),
        'affiliation_company': lambda x: fake.company(),
        'position_job_title': lambda x: fake.job(),
        'linkedin_profile': lambda x: fake.url(),
        'brief_description': lambda x: fake.text(),
        'achievements_contributions': lambda x: fake.text(),
        'educational_background': lambda x: fake.text(),
        'professional_certifications': lambda x: fake.text(),
        'work_experience': lambda x: fake.text(),
        'notable_projects_products': lambda x: fake.text(),
        'impact_description': lambda x: fake.text(),
        'innovations_introduced': lambda x: fake.text(),
        'patents_publications_contributions': lambda x: fake.text(),
        'recommendation_letters': lambda x: fake.text(),
        'testimonials_quotes': lambda x: fake.text(),
        'project_links': lambda x: fake.url(),
        'screenshots_demos': lambda x: fake.text(),
        'participation_in_events': lambda x: fake.text(),
        'ongoing_professional_development': lambda x: fake.text(),
        'tech_community_involvement': lambda x: fake.text(),
        'open_source_contributions': lambda x: fake.text(),
        'volunteering_mentorship': lambda x: fake.text(),
        'additional_information': lambda x: fake.text(),
        'awards_recognitions_received': lambda x: fake.text(),
    })

    # Execute the seeding process
    seeder.execute()

if __name__ == "__main__":
    generate_dummy_data()
    print("Dummy data generation completed.")
