import json
import urllib2

def courseNameToCourseId(course_name):

    url = "https://yacs.cs.rpi.edu/api/v5/courses?search="+course_name+"&show_sections"
    response = urllib2.urlopen(url)
    result = json.load(response)

    course_ids = []
    for section in result["courses"]:
        if section["name"] == course_name:
            course_ids.append(section["id"])

    return result



def getSchedulingConflict(course_names):
    section_ids = []
    for course in course_names:
        section_ids += courseNameToCourseId(course)

    url = "https://yacs.cs.rpi.edu/api/v5/schedules?section_ids="+",".join(section_ids)
    response = urllib2.urlopen(url)
    result = json.load(response)

    response = ""
    if(len(result["schedules"])==0):
        response = "These classes have conflicts"
    elif(len(result["schedules"])==1):
        response = "1 schedule generated"
    else:
        reponse = len(result["schedules"])+" schedules generated"

    return response

def getSeatsLeft(course_name):
    url = "https://yacs.cs.rpi.edu/api/v5/courses?name="+course_name+"&show_sections"
    response = urllib2.urlopen(url)
    result = json.load(response)
    ##graduate vs undergrad seats left?
    seats_left = 0
    for course in result["courses"]:
        if course["name"] == course_name:
            sections = section["sections"]
            for section in sections:
                seats_left += section["seats"]-section["seats_taken"]

    if(seats_left <= 0):
        response = "No seats left in "+course_name
    elif(seats_left == 1):
        response = "1 seat left in "+course_name
    else:
        response = str(seats_left)+" seats left in "+course_name

    return course_name
