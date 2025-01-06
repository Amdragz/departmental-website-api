from django.core.management.base import BaseCommand
from api.models import Document, Course, Resource, Notification, Profile, CustomUser
from datetime import datetime
import json

class Command(BaseCommand):
    help = 'Load dummy data into the database'

    def handle(self, *args, **kwargs):
        try:
            # Load the JSON data
            with open('dummy_data.json', 'r') as file:
                data = json.load(file)
            
            # Clear existing data to avoid duplicates
            self.stdout.write('Clearing existing data...')
            Document.objects.all().delete()
            Course.objects.all().delete()
            Resource.objects.all().delete()
            Notification.objects.all().delete()
            Profile.objects.all().delete()
            CustomUser.objects.all().delete()
            
            self.stdout.write('Loading Documents...')
            for doc_data in data['documents']:
                Document.objects.create(
                    document_name=doc_data['documentName'],
                    document_category=doc_data['documentCategory'],
                    document_status=doc_data['documentStatus'],
                    document_deadline=datetime.strptime(doc_data['documentDeadline'], '%Y-%m-%d').date()
                )
            
            self.stdout.write('Loading Courses...')
            # Keep track of created courses
            course_dict = {}
            for course_data in data['courses']:
                course = Course.objects.create(
                    course_title=course_data['courseTitle'],
                    course_code=course_data['courseCode'],
                    course_unit=course_data['courseUnit'],
                    current_semester=course_data['currentSemester'],
                    level=course_data['level'],
                    course_venue=course_data['courseVenue'],
                    course_description=course_data['courseDescription']
                )
                course_dict[course_data['courseCode']] = course
            
            self.stdout.write('Loading Resources...')
            for resource_data in data['resources']:
                Resource.objects.create(
                    category=resource_data['category'],
                    articles=resource_data['articles'],
                    research_papers=resource_data['researchPapers']
                )
            
            self.stdout.write('Loading Notifications...')
            for notif_data in data['notifications']:
                Notification.objects.create(
                    notification_date=datetime.strptime(notif_data['notificationDate'], '%Y-%m-%d').date(),
                    notification_subject=notif_data['notificationSubject'],
                    notification_body=notif_data['notificationBody'],
                    is_read=notif_data['isRead']
                )
            
            self.stdout.write('Loading Profiles...')
            for profile_data in data['profiles']:
                # Create CustomUser first
                user = CustomUser.objects.create_user(
                    username=profile_data['email'],
                    email=profile_data['email'],
                    first_name=profile_data['name'].split()[0],
                    last_name=profile_data['name'].split()[1],
                    department=profile_data['department'],
                    matricno=profile_data['matricNumber'],
                    phonenumber=profile_data['phoneNumber']
                )
                
                # Create Profile
                profile = Profile.objects.create(
                    user=user,
                    total_units=profile_data['totalUnits'],
                    level=profile_data['level'],
                    phone_number=profile_data['phoneNumber'],
                    about=profile_data['about'],
                    department=profile_data['department'],
                    matric_number=profile_data['matricNumber']
                )
                
                # Add registered courses using the dictionary
                for course_code in profile_data['registeredCourses']:
                    if course_code in course_dict:
                        profile.registered_courses.add(course_dict[course_code])
                    else:
                        self.stdout.write(self.style.WARNING(f'Course {course_code} not found'))

            self.stdout.write(self.style.SUCCESS('Successfully loaded all dummy data'))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading data: {str(e)}'))