
 # Social Media Website
 ##  Setup Instructions
The program interfaces with an SQL database to store data. The intended database state can be recreated using the script in `sql_scripts/Dump.sql`.

To configure the connection to the database, edit the values in `db/db_credentials.py`.
 # Project Overview


## Introduction

### The service operates as a social media platform, allowing users to create accounts, make posts with attached text and media, interact with other users’ posts, and message other users. Users can follow other users and view a record of followed activity that they have not yet viewed.
<br>


## Problem Statement

### People are naturally social creatures, and want to interact with each other in a convenient way. Since people often cannot meet in person, or live far away from each other, our service allows them to socialize and share media conveniently and remotely.
<br>


## Target Audience

### The target audience for the social media platform could be any user looking for a website to share their content. The platform’s purpose is to be a place where users can post images, statuses, and have other users interact with said posts. A user should be able to create an account with a unique ID and password. They should also be able to create a post either fully text or with an image.
<br>


## Design Requirements

### User registration and authentication, posting text and images. Profile management, some kind of feedback system to post (upvote, like dislike, share, comment, etc), user and post search and a follow/friend request option. Security, usability and performance.
<br>


## Software Architecture

![Alt text](box-diagram.jpg "Our box diagram")
<br>


## Technology Stack

### The application will run in Python, using Flask to host a web server. The following python modules will be used:

sqlalchemy, flask-sqlalchemy, pymysql - SQL Database Management

cryptography - Encryption of sensitive information.
<br>


## Team Members

Micah Lasala - 2nd-year Junior at UNCC majoring in Computer Science.

George Viveros-Zavaleta

Colin Childers - Senior at UNCC majoring in  Comp Science

Ryan Lowell - Junior at UNCC majoring in Computer Science

 Steve Andreas - Senior at UNCC majoring in Comp Science
