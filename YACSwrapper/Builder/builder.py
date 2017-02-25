import urllib2
import json



def importYACScourses():
    url = "https://yacs.cs.rpi.edu/api/v5/courses"
    response = urllib2.urlopen(url)
    result = json.load(response)

    list_of_course_ids = []

    with open("../Alexa/LIST_OF_COURSES.txt","w") as f:
        for course in result["courses"]:
            f.write(course["name"]+"\n")




if __name__ == "__main__":
    importYACScourses()
