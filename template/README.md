# BraTS Challenge 2020 Docker Submission Template

Pleaseread this carefully, for feedback / questions please contact either Christoph Berger https://github.com/christophbrgr or Florian Kofler https://github.com/neuronflow . ** However, the preferred way is to open an issue in this repository so you also help others. **

This is the blueprint structure for BraTS 2020 Algorithmic repository submissions. Use the respective Dockerfiles for CUDA/CPU applications.

## FAQ
- code processes only a single patient?
Yes, we run our tests on multiple GPUs using an internal fork of https://github.com/neuronflow/BraTS-Toolkit . We spawn a container for every exam processed. This way it is easier for us to orchestrate and you don't need to worry about batch processing.


## copy paste your code

look through the repo. fill in the code at the places indicated by the comments.
pay special attention to `.env` and `Dockerfile_*` and fill in your author and application information there

## system specs

* CUDA 10.1
* Ubuntu 18.04
* Python 3.6.9

if you need to, you can also change the Docker file to whatever framework and OS you need.

###  build docker image

CPU:

```
docker build -t your_application_name . -f Dockerfile_CPU

```

GPU:

```
docker build -t your_application_name . -f Dockerfile_CUDA

```

ATTENTION: make sure you build your docker without sudo, otherwise it will run as a root user and they files will belong to root, please see: https://vsupalov.com/docker-shared-permissions/

### run it for testing
CPU:
```
docker run -it --rm --name your_container_name -v "/your/input/folder/":"/app/data/"  your_application_name
```

GPU:
```
docker run -it --rm --gpus device=0 --name your_container_name -v "/your/input/folder/":"/app/data/" your_application_name
```

### save docker image

```
docker save your_application_name | gzip > ./docker_builds/your_application_name.tar.gz
```

### submit 

Submit your image either privately as the exported tar.gz file or upload it to Docker Hub and send the usage instructions to the BraTS organizers.
