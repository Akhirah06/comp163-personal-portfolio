#Personal Information Storage
student_full_name = "Akhirah Henry"
student_email = "dihenry@ncat.edu"
student_hometown = "Atlanta, GA"
student_grad_semester = "Spring 2029"
student_major = "Computer Science"

#Academic Data Organizational
current_courses = ["COMP 163", "MATH 131", "SPCH 250", "HIST 106", "GEEN 111", "COMP 121"]
completed_courses = ["Psychology", "Physics", "College Algebra", "Elementary Japanese", "World History"]
credit_hours = [3, 4, 1, 1, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

#Contact Information Storage
emergency_contact = ["Mom", "Thelisha Glover", 404-942-7586]
home_address = ["841 Killian Street", "Atlanta, GA", 30316]
instagram_info = ["Instagram", "@ahhkii.be.thinkin", 346]
tiktok_info = ["Tiktok", "@cxiberaltwitch", 32]
student_birthday = ["Birthday", 12, 17, 2006]

#interest Tracking
current_skills = {"Leadership", "Problem Sloving", "Recordkeeping", "Competent Communication"}
skills_to_learn = {"Python basics", "Game Design", "Git", "Public Speaking", "JavaScript"}
career_interests = {"Game Programming", "Game Development", "software Development"}
student_hobbies = {"Gaming", "Meditation", "Reading", "Music", "Anime"}
entertainment_backlog = {"Code Geass", "Gachiakuta", "Tokyo Ghoul"}

#Organizational Mapping
course_credits = {
    "COMP 163": 3,
    "MATH 131": 4,
    "SPCH 250": 3,
    "HIST 106": 3,
    "GEEN 111": 1,
    "COMP 121": 1
}
course_professors = {
    "COMP 163": "Prof. Rhodes",
    "MATH 131": "Prof. Varatharaj",
    "SPCH 250": "Prof. Bush",
    "HIST 106": "Prof. Deveo",
    "GEEN 111": "Prof. Parrish",
    "COMP 121": "Prof. Rhodes"
}
course_rooms = {
    "COMP 163": "Gibbs Hall",
    "MATH 131": "Marteena Hall",
    "SPCH 250": "Digital",
    "HIST 106": "Digital",
    "GEEN 111": "McNair Hall",
    "COMP 121": "Graham Hall"
}
monthly_budgeting = {
    "Food": 450,
    "Entertainment": 200,
    "Books": 89,
    "Transportation": 100
}
study_hours_per_sub = {
    "COMP 163": 1.5,
    "MATH 131": 1.5,
    "SPCH 250": 1.5,
    "HIST 160": 1.5,
    "GEEN 111": 0.5,
    "COMP 121": 0.5
}
contact_directory = {
    "Mom": 404-942-7586,
    "Roommate": 919-236-3476,
    "Academic Advisor": 336-285-4213
}


#Required Calculations
total_current_credits = sum(credit_hours)
# commented out due to being a freshman: cumulative_gpa = round(sum(gpa_history) / (len(gpa_history)), 2)
total_completed_courses = len(completed_courses)
total_weekly_study_hours = sum(study_hours_per_sub.values())
academic_load = sum(credit_hours) + sum(study_hours_per_sub.values())
total_monthly_budget = sum(monthly_budgeting.values())
daily_food_budget = round((monthly_budgeting["Food"] / 30), 2)  
annual_budget_projection = total_monthly_budget * 12
study_cost_per_hour = round((monthly_budgeting["Books"] / total_weekly_study_hours), 2)


#Analytical Calculations
total_social_media_followers = instagram_info[2] + tiktok_info[2]
current_skills_count = len(current_skills)
learning_skills_count = len(skills_to_learn)
contact_directory_size_analysis = len(contact_directory)
entertainment_backlog_management_count = len(entertainment_backlog)
academic_workload_assessment = academic_load


#Formatted Output
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {student_full_name}| Email: {student_email}")
print(f"From: {student_hometown} | Graduating: {student_grad_semester}")
print(f"Major: {student_major}")
print()
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_courses)} courses")
# commented out due to being a freshman: print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {total_weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print()
print("Current Courses:")
print(f"{current_courses[0]} - {course_credits["COMP 163"]} credits - {course_professors["COMP 163"]} - {course_rooms["COMP 163"]}")
print(f"{current_courses[1]} - {course_credits["MATH 131"]} credits - {course_professors["MATH 131"]} - {course_rooms["MATH 131"]}")
print(f"{current_courses[2]} - {course_credits["SPCH 250"]} credits - {course_professors["SPCH 250"]} - {course_rooms["SPCH 250"]}")
print(f"{current_courses[3]} - {course_credits["HIST 106"]} credits - {course_professors["HIST 106"]} - {course_rooms["HIST 106"]}")
print(f"{current_courses[4]} - {course_credits["GEEN 111"]} credits - {course_professors["GEEN 111"]} - {course_rooms["GEEN 111"]}")
print(f"{current_courses[5]} - {course_credits["COMP 121"]} credits - {course_professors["COMP 121"]} - {course_rooms["COMP 121"]}")
print()
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Skills: {skills_to_learn}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {learning_skills_count}")
print()
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${total_monthly_budget}")
print(f"Food: ${monthly_budgeting["Food"]} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budgeting["Entertainment"]}")
print(f"Books: ${monthly_budgeting["Books"]}")
print(f"Transportation: ${monthly_budgeting["Transportation"]}")
print(f"Annual Projection: ${annual_budget_projection}")
print()
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[0]} - {emergency_contact[1]} - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]}")
print(f"Social Media Presence: {total_social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_directory_size_analysis} people in directory")
print()
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {total_completed_courses}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_management_count} items")
print(f"Current Hobbies: {len(student_hobbies)} activities")
print("================================================================")