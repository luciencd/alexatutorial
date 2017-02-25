import urllib2
import json



def importYACScourses():
    url = "https://yacs.cs.rpi.edu/api/v5/courses"
    response = urllib2.urlopen(url)
    result = json.load(response)

    classesset = set()

    with open("../Alexa/LIST_OF_COURSES.txt","w") as f:
        for course in result["courses"]:
            classesset.add(course["name"])

        for course in classesset:
            f.write(course+"\n")




if __name__ == "__main__":
    importYACScourses()
