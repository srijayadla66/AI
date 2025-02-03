import numpy as np

def similar(user_skills, course_skills):
    intersection = len(set(user_skills) & set(course_skills))
    union = len(set(user_skills) | set(course_skills))
    return intersection / union if union != 0 else 0

def recommend(user_id, courses, user_profiles, top_n=5):
    user_profile = user_profiles.get(user_id, None)
    if not user_profile:
        return []
    
    user_interests = set(user_profile['interests'])
    user_skills = set(user_profile['skills'])
    
    recommendations = []
    for course in courses:
        skill_match = similar(user_skills, course['skills'])
        interest_match = len(user_interests & set(course['category']))
        score = 0.7 * skill_match + 0.3 * interest_match  
        recommendations.append((course['id'], course['title'], score))
    
    recommendations.sort(key=lambda x: x[2], reverse=True)
    return recommendations[:top_n]


courses = [
    {"id": 1, "title": "Python", "skills": ["Python", "Programming"], "category": ["Programming"]},
    {"id": 2, "title": "MachineLearning", "skills": ["ML", "Python", "Statistics"], "category": ["AI/ML"]},
    {"id": 3, "title": "ADS", "skills": ["C++", "Data Structures"], "category": ["Programming"]}
]

user_profiles = {
    "user_1": {"interests": ["AI/ML"], "skills": ["Python"], "preferences": "Programming"},
    "user_2": {"interests": ["Programming"], "skills": ["C++"], "preferences": "Programming"}
}

print(recommend("user_1", courses, user_profiles)) 