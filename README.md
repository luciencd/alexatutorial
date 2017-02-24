# Alexa Tutorial

This is a tutorial for creating a basic Alexa skill. (No Alexa Required)

## Introduction

My goal for this tutorial is to provide knowledge on how to create a basic voice wrapper for a 3rd party service which has a REST API.

This tutorial will show you how to make a voice wrapper for YACS, the RPI course scheduler. It has a good REST API service, which returns useful information.

There are **two** parts to this project: 
1: The Alexa Skills kit "front-end", which defines how the Alexa should convert the voice command into a request JSON object that gets sent to the backend. 
2: The Amazon Lambda instance, which takes in a request object from the Alexa Skills Kit instance, and interprets it based on its intent and arguments; its main file (lambda_function.py) serves as a wrapper function to interact with any 3rd party API.

## Getting Started

### Backend Setup

Create an AWS account with a free trial with your education email account *@*.edu.
[AWS FREE TIER LINK](https://aws.amazon.com/s/dm/optimization/server-side-test/free-tier/free_np/)

Open Amazon Web Services Dashboard. [AWS Dashboard](https://console.aws.amazon.com/console/home?region=us-east-1)
Open Amazon Lambda Dashboard [Amazon Lambda Dashboard](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions?display=list)
Click on blue button "Create a Lambda Function" call it rcostest.
Search through the sample blueprints by looking up "Alexa". Select the alexa-skills-kit-color-expert-python one. Press next.

You should see this: ![Image of rcostest](https://www.dropbox.com/s/9noz6kxh4p4ijvr/Screenshot%202017-02-24%2018.27.16.png?dl=0)

Then clone this repo, and find the YACSwrapper file.




What if we could interact with YACS on a vocal basis?

Goal: 

List a single course to alexa, and it will tell you how many seats are in all sections.

List courses to alexa skill, and it will tell you if there are any possible schedules.


API skills kit.
- Create a name for your app, to get started.

- Create Intents JSON file.

- Define Slot Types.

- Add List of possible values for slots.



Amazon Web Services Backend.
-Get lambda_function.py setup.
-Create separate file to import.


Extra details:

Build tool to create all the files necessary in Alexa skills kit (as slot value possibilities can be dynamic, courses change every year)

