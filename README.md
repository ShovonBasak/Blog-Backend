# Live Site
[API Documentation!](https://api.blog.shovon.dev/docs)

# Installation
1. Update the 'hosts' file and add example.com against the localhost ip: 127.0.0.1
1. Clone the Project
``` 
git clone git@github.com:ShovonBasak/Blog-Backend.git
cd Blog-Backend
code .
```
3. Create Environment Variables
Create a .env file from the provided .env.sample file and update the environment variables accordingly.
Edit the .env file and update the values with your configuration.
1. Make sure Docker is installed on your machine and the Docker daemon is running.

1. Build and Start the Project
Run the following commands to build and start the project:
```
docker-compose -f docker-compose-dev.yaml build
docker-compose -f docker-compose-dev.yaml up
```
Once the containers are up and running, you can access the site on example.com and access the documentation on example.com/docs

6. Making Changes:

After making any changes to the project, follow these steps to rebuild the container:

```
docker-compose -f docker-compose-dev.yaml down
docker-compose -f docker-compose-dev.yaml build
docker-compose -f docker-compose-dev.yaml up
```

You can then access the project on example.com