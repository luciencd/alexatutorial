import json
import urllib2
from urllib import quote
def courseNameToCourseId(course_name):

    url = "https://yacs.cs.rpi.edu/api/v5/courses?search="+course_name+"&show_sections"
    url = quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    #print url
    response = urllib2.urlopen(url)
    result = json.load(response)

    course_ids = []
    for section in result["courses"]:
        if section["name"].lower() == course_name.lower():
            course_ids.append(str(section["id"]))

    return course_ids



def getSchedulingConflict(course_names):
    section_ids = []
    for course in course_names:
        section_ids += courseNameToCourseId(course)

    url = "https://yacs.cs.rpi.edu/api/v5/schedules?section_ids="+",".join(section_ids)
    url = quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    #print url
    response = urllib2.urlopen(url)
    result = json.load(response)

    response = ""
    if(len(result["schedules"])==0):
        response = "These classes have time conflicts."
    elif(len(result["schedules"])==1):
        response = "1 schedule was generated."
    else:
        reponse = len(result["schedules"])+" schedules were generated."

    return response

def getSeatsLeft(course_name):
    url = "https://yacs.cs.rpi.edu/api/v5/courses?search="+course_name+"&show_sections"
    url = quote(url, safe="%/:=&?~#+!$,;'@()*[]")
    #print url
    response = urllib2.urlopen(url)
    result = json.load(response)
    ##graduate vs undergrad seats left?
    seats_left = 0
    for course in result["courses"]:
        if course["name"].lower() == course_name.lower():
            sections = course["sections"]
            for section in sections:
                #print section["seats"],section["seats_taken"]
                seats_left += max(0,section["seats"]-section["seats_taken"])


    if(seats_left <= 0):
        response = "No seats are left in "+course_name
    elif(seats_left == 1):
        response = "1 seat are left in "+course_name
    else:
        response = str(seats_left)+" seats are left in "+course_name
    #print response
    return response
#print getSchedulingConflict(["introduction to biology","software design and documentation","RCOS","Observational Astronomy"])
#print getSeatsLeft("Introduction to Biology")
