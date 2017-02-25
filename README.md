# Alexa Tutorial

This is a tutorial for creating a basic Alexa skill. (No Alexa Required)

## Introduction

My goal for this tutorial is to provide knowledge on how to create a basic voice wrapper for a 3rd party service which has a REST API.

This tutorial will show you how to make a voice wrapper for YACS, the RPI course scheduler. It has a good REST API service, which returns useful information.

There are **two** parts to this project: 

1: The Alexa Skills kit "front-end", which defines how the Alexa should convert the voice command into a request JSON object that gets sent to the backend. 

2: The Amazon Lambda instance, which takes in a request object from the Alexa Skills Kit instance, and interprets it based on its intent and arguments; its main file (lambda_function.py) serves as a wrapper function to interact with any 3rd party API.

## Getting Started

### AWS Lambda "Backend" Setup

Create an AWS account with a free trial with your education email account *@*.edu.
[AWS FREE TIER LINK](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/)

Open Amazon Web Services Dashboard. [AWS Dashboard](https://console.aws.amazon.com/console/home?region=us-east-1)

Open Amazon Lambda Dashboard [Amazon Lambda Dashboard](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions?display=list)

Click on blue button "Create a Lambda Function" call it rcostest.

Search through the sample blueprints by looking up "Alexa". Select the alexa-skills-kit-color-expert-python one. Press next.

You should see this: ![Image of rcostest](https://www.dropbox.com/s/9noz6kxh4p4ijvr/Screenshot%202017-02-24%2018.27.16.png?dl=1)

Then clone this repo, and find the YACSwrapper file.

It should contain:

```
YACSwrapper
│
└───Alexa
│   │   IntentSchema.txt
│   │   SampleUtterances.txt
│   │   LIST_OF_COURSES.txt
│   
└───Lambda
│   │   lambda_function.py
│   │   YACSwrapper.py
│   │
│
└───Builder
    │   builder.py
```

Select lambda_function.py + YACSwrapper.py and archive them. Then upload the ZIP file in this way:

![Image of zip Upload](https://www.dropbox.com/s/4chure32xil4kev/Screenshot%202017-02-24%2018.46.40.png?dl=1)

Now, whenever the Alexa hears you say an intent, it will direct it directly to your lambda function(lambda_function.py), which will send a function call to YACSwrapper.py, which will call the YACS API. Once you get data back from YACS, you create an output phrase, and send it back to lambda_function.py. That will then get sent all the way back to the Alexa itself in the form of a vocalized sentence.

## Alexa Skills Kit "Front-end" Setup

Now onto the "front-end" of the service.

We are trying to interact with YACS on a vocal basis. What functions do we need? 

1. A basic function that tells you how many seats are available in a class.

2. A function which tells you if a set of classes has any conflicts.

I'm sure there are more possibilities, but these are the two we will focus on.

### Setting up the Intent Schema, Custom Slot Types, and Sample Utterances.

In order for the "front-end" to work properly, you need to define what kind of things people will be asking.

When someone asks alexa a question, the phrase is divided into three parts:

1. Skill Name

2. Intent

3. Slots

The skill name is self explanatory.

The intent is the "function" that alexa thinks you are trying to invoke.

The slots are the "arguments" to the intent that alexa binds to particular parts of the question.

[Anatomy of a skill request](https://www.dropbox.com/s/iy0bxu4o359qy7u/Screenshot%202017-02-24%2019.26.22.png?dl=1)

### Files necessary for Alexa Skills Kit.
We must define all the Intents in a file called intentSchema.json



API skills kit.
- Create a name for your app, to get started.

- Create Intents JSON file.

- Define Slot Types.

- Add List of possible values for slots.



Amazon Web Services Backend.
-Get lambda_function.py setup.
-Create separate file to import.

# Fixes:

Someone make a pull request to ensure any extension to this skill will conform to the Amazon Skill publishing requirements.


# Build tools:

Because the Custom Slot type Course is time-dependant, you have to build this project every semester, to reimport all the courses from YACS.

Builder/build.py

# Bonus
Fork the repo to accept 5, 6, 7 possile courses.
Add functionality and improve the tutorial.
