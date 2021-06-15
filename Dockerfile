# We want containers
    # Containers are isolated processes
# To create a container, you need a container image, aka Docker image
# containers are ephemeral, created and destroyed as needed
# images are immutable, templates to make new containers
# To create an image, you build a dockerfile

# Dockerfiles are instructions to build an image layer by layer
# The instructions are executed in containers of their own

# Step 1 of Dockerfile
# What is the base image for the image that will be built
# you get images from docker registries where people have published
# the default docker registry is docker hub

# two things we want from the base of the image
# 1. as much of the dependencies needed as possible
# 2. 


FROM python:3.9

# two most common commands here
# COPY: for copying files from outside the image into the image
# RUN: for running any shell commands within the image
#       (e.g. install something with apt)

WORKDIR /app

COPY requirements.txt *.py ./
#RUN make /app

CMD [ "python3", "-m", "proj0" ]

# you can overwrite CMD with second argument to docker run

# the docker engine is made with a client-server architecture
# so the CLI that you enter "docker" commands into 
# is a separate program from all of the rest (building images, running containers, etc.)
# all of the rest, the server-side, is the "docker daemon"


