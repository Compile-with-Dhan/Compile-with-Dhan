def display_profile():
    role = "BTech 2nd Year Student"
    skills = ["HTML", "CSS", "JavaScript", "Python", "Java"]
    status = "Beginner learning through projects"
    
    print(f"Role: {role}")
    print(f"Status: {status}")
    print("Skills:")
    for skill in skills:
        print(f"  - {skill}")

if __name__ == "__main__":
    display_profile()