## DevopsAssignment2

Create two services using Python, one web server with one path called /api that can be called using the path using a ***GET request*** in order to receive a random generated number.

Create requirements files to list all the dependencies for each of the services(api and request scripts).

Containerise the two scripts.

### Implementation
**_API script_**: 
-->After choosing Flask library for implementing the webservice,
I imported the Flask and random modules.
-->A single route was defined **"/api"** which responds to **GET** requests.
-->When a **GET** request is received at **"/api"**, the function **'get_random_number'** is called
in order to generate a random number between 1 and 100000.

**_GET Request script_**
-->Makes a GET request to the specified address where the webserver is running.
--> **_requests_** library was imported for making HTTP requests in Python.
--> _generate_number()_ function was created as the core of the script in order to send a HTTP GET to the specified URL.
--> The service returns a JSON format that is then parsed in a Python dictionary that is printed.

Each of the scripts are located in different directories, where there is the requirements.txt files necessary to be installed before running the scripts or while building the docker image(as written in each Dockerfile).

Overall, each Dockerfile contains the set of instructions to create a container that has Python, all the needed libraries and the application code in order to perfectly run the two services and also communicate.

A _**docker-compose.yml**_ file was created in order to run multi-container Docker apps.
-->After defining the Docker services from my application, I specified the location where each of the services can be found.
-->The port mapping part was done in order for the containers to be accessible from outside.
-->A network was defined to be used by the two services(without any settings Docker will use the default options) to make sure they can communicate successfully.
