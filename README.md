# Syracuse University Event Management System
## Project Description
Institutions as large as Syracuse University often face challenges in effectively disseminating information about campus events to students and faculty across diverse academic departments and student organizations. Our project aims to address this by creating a cloud-based service that streamlines event management and discovery on campus.

The core functionality of our service revolves around enabling event organizers to post details about their events, including the event name, description, location, and additional services provided. Users, including students and faculty, can then access the service to discover and participate in events that align with their interests and schedules.

## Cloud Services Used
Azure App Services: We utilize Azure App Services to host a user-friendly HTML landing page where users can browse through all the events posted on the platform.

Azure SQL Database: Our project relies on Azure SQL Database to store essential information, including user details, organizer information, venue details, event listings, and services provided. We maintain multiple tables within the database to manage various aspects of event management efficiently.

Intelligent Recommendations (Machine Learning): We explore the possibility of integrating intelligent recommendations using machine learning algorithms. This feature aims to provide users with personalized event recommendations based on their preferences and interests.

## Cloud Architecture
Our cloud architecture consists of the following components:

#### Azure SQL Server: 
We utilize a standard SQL server hosted on Azure with default configurations to manage our SQL database securely.

#### SQL Database: 
The SQL database is created on Azure as a general-purpose, serverless database with ample storage capacity. We establish connections and manage the database using Azure Data Studio.

#### Python Code: 
We develop Python scripts to interact with the SQL database, retrieve event data, and serve it to the HTML landing page using Flask, a lightweight web application framework.

#### HTML Code: 
Our HTML code defines the structure and layout of the landing page, providing users with an intuitive interface to explore and interact with event listings.

#### App Services: 
Azure App Services hosts our web application, providing scalable and reliable hosting infrastructure. We leverage Visual Studio Code for streamlined deployment of our web application to Azure App Services.

## Issues Encountered
Throughout the development process, we encountered several challenges, including:

Database Connectivity: Initially, we faced difficulties with database connectivity due to firewall exceptions and changing IP addresses. We resolved this by creating a separate database and server to streamline collaboration.

Complex Coding Requirements: The project required extensive coding in Python and HTML, which posed challenges in terms of implementation and integration. However, thorough research and collaboration helped us overcome these hurdles.

Resource Group Configuration: A configuration error led to deployment issues when our app service couldn't locate the database. We resolved this by adjusting the TCP settings in our Python code.

Integrating Intelligent Recommendations: While we aimed to incorporate intelligent recommendations for event discovery, the complexity and prerequisites of the feature posed challenges within our existing architecture.

Despite these challenges, our project demonstrates the effective utilization of cloud services to streamline event management and enhance campus-wide communication at Syracuse University.


Below is a link to a demo showing how we used Azure app services to host our final webpage and what the final web page looks like.
Demo video link: https://video.syr.edu/media/t/1_5fwmppym

This project was completed as part of the IST 615 course at Syracuse University.
