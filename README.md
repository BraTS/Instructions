# Instructions
Instructions on how to dockerize your algorithm, as applied in the BraTS challenge

# Dockerization / Containerization
In most cases, containerization of your code is a simple and straightforward procedure. We will provide an example container with functional code soon. Furthermore, many containers are available on the internet to be used as a basis, probably including your favorite programming environment and neuroimaging tools.

The concept of containerization is to simplify the deployment of applications. To ensure maximum compatibility and (potentially) distributability, we want to collect algorithms using a container approach with Docker (www.docker.com). Docker is a technique to do so and will be used for the BraTS Algorithmic Repository.

Docker can be used to “wrap” your entire segmentation method (including all dependencies) into a single container. This container can be run as if it would be a single standalone application, anywhere, on any platform. Because your method and all dependencies are included in the container, the method is guaranteed to run exactly the same at all times.

Dockerization is a very popular concept and has been used successfully in previous MICCAI challenges, e.g., in the MSSEG challenge (https://portal.fli-iam.irisa.fr/msseg-challenge/overview) and the WMH Segmentation Challenge (http://wmh.isi.uu.nl/methods/). The current text is also based on info from the WMH Segmentation Challenge. Docker Hub (https://hub.docker.com/) provides a large overview of existing Docker containers (base images), that can be used to build your own container. Furthermore, many popular programming environments and image analysis methods have Dockerfiles available.
