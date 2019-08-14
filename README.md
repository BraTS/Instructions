# Docker BRATS
**This is an extended version of the informational text that can be found here: https://www.med.upenn.edu/sbia/brats2017/algorithms.html**

**For the data format instructions, see this file here: https://github.com/BraTS/Instructions/blob/master/data_formats.md**


## Introduction

**In a nutshell:** We would like to have your algorithms in a Docker container, as well as in their original source code. We intend to run your dockerized algorithm on the BraTS 2016 test dataset to compare segmentation results as part of the BraTS'14-'16 journal manuscript, and to make all contributed Docker containers available through the upcoming BraTS algorithmic repository. Your source code will not be distributed and will only be used internally by the BraTS organizers, as a proof of code ownership (contact us if you cannot share your source code).

Your algorithm should be able to generate a tumor segmentation on any multimodal brain scan that is preprocessed like a BraTS test subject. To allow for fair comparisons and assessing performance differences across algorithms, you are expected to indicate what training set you have used, during training and/or design of your algorithm, and in the case of private datasets, a description of those datasets.

## Docker containers

To ensure maximum compatibility and distributability, we want to use a container approach with Docker. We therefore want you to put your runnable code in a Docker container in accordance with the requirements listed below.

In most cases, containerization of your code is a simple and straightforward procedure. We will provide an example container with functional code soon. Furthermore, many containers are available on the internet to be used as a basis, probably including your favourite programming environment and neuroimaging tools.

### Containerization

The concept of containerization is to simplify the deployment of applications. Docker is a technique to do so and will be used for the MICCAI BRATS challenge.

Docker can be used to “wrap” your entire segmentation method (including all dependencies and the operating system) into a single container. This container can be run as if it would be a single standalone application, anywhere, on any platform. Because your method and all dependencies are included in the container, the method is guaranteed to run exactly the same all the time.

Dockerization is a very popular concept and has been used successfully in previous MICCAI challenges, e.g., in the MSSEG challenge (https://portal.fli-iam.irisa.fr/msseg-challenge/overview) and the WMH Segmentation Challenge (http://wmh.isi.uu.nl/methods/). The current text is also based on info from the WMH Segmentation Challenge. Docker Hub (https://hub.docker.com/) provides a large overview of existing Docker containers (base images), that can be used to build your own container. Furthermore, many popular programming environments and image analysis methods have Dockerfiles available.

### Step for step instructions

There are Dockerfiles as examples in this repository. They use the python:2.7 image as base and then install dependencies and finally copy the relevant files from the host to the container. The process itself should be pretty intuitive.
Steps:
1. Create a script for your segmentation code that reads the 4 modalities (either nii or nii.gz) from `/data`, performs the segmentation and writes the result back to `/data/results` in either nii or nii.gz format. For further naming instructions, please consult the **BRATS_Docker_Interface.pdf** file in this repository.
2. Create a Dockerfile that uses a base image, installs all necessary dependencies and then copies your code and the script from step 1 to the container.
3. Run `docker build .< Dockerfile` in the directory where your Dockerfile, your code and your script reside.
4. After building, your container should be able to take input via the `-v <host_directory>:/data` mount command and perform your segmentation.

The full run command can be seen below. I suggest you read the introduction to Docker on their website: https://docs.docker.com/get-started/part2/
Further instructions can be found here:
- Python tutorial: https://runnable.com/docker/python/dockerize-your-python-application

**Caffe and Matlab**: If you are using Caffe in combination with Matlab, I suggest to build an image using the Caffe image as base image and then installing the Matlab Runtime inside the container.
- Caffe Docker: https://github.com/BVLC/caffe/tree/master/docker
- Matlab Runtime: https://de.mathworks.com/products/compiler/matlab-runtime.html (Use the Matlab Toolbox Deploy feature to compile your code)
- Matlab example: http://wmh.isi.uu.nl/methods/example-matlab/
- Another example (a bit outdated, but to give a general idea): https://github.com/vistalab/docker/tree/master/matlab/runtime/2015b

### Data access

All test sets will be identical to the 2016 or 2017 test data that you have already processed. They are co-registered, skull-stripped, resampled to 1mm^3 isotropic resolution, and aligned to the SRI space. Data will be in NIfTI GZIP Compressed Tar Archive (.nii.gz) format, with all header information except the spatial resolution removed, and the individual volumes will be named ‘flair.nii.gz’, ‘t1c.nii.gz’, ‘t1.nii.gz’, ‘t2.nii.gz’. You can use any of the BRATS training or testing image volumes to check whether your Docker image runs as expected.

Because your container runs in an isolated environment, the data needs to be mapped into the container. The input data files, i.e., the ‘fla.nii.gz’, ‘t1c.nii.gz’, ‘t1.nii.gz’, ‘t2.nii.gz’ volumes, will be linked to /data and your segmentations must be placed in /data/results. Results should be a NIfTI file with the same resolution as the input data. Please call the resulting file "tumor\_'your_image'\_class.nii.gz", where ‘your\_image’ is an eight character identifier of your algorithm (id of your container, title of your code/project). If your algorithm returns probabilities as well, you can return them accordingly, and name them, e.g., "tumor\_'your_image'\_prob_4.nii.gz" for results of class 4. If your algorithm returns tissue classes, please use “tissue\_’your_name’\_wm.nii.gz” for white matter (\*'\_gm.nii.gz' and ''\*\_csf.nii.gz' for the other two).

There should be no interaction with the container required other than running the Docker command below.

Your code *must* accept the files *exactly* as shown here:
- fla.nii.gz
- t1c.nii.gz
- t1.nii.gz
- t2.nii.gz

### Computing environment & Resources

We will run your container on a selection on test cases. Docker can set resource limits on containers. Please give us an indication how many CPUs and how much RAM is needed for you method, and what the resulting computation time will be.

### GPU computation

**Update: You may also submit a NVIDIA-Docker container, but CPU-only is still preferred if possible (or both).**

In our first instalment, we would like to run all code CPU-only to retain compatibility. Docker does not yet support GPU mapping on all platforms, so please provide a CPU-only version of you code. If you really want/need to use a GPU, please contact us.

### NVIDIA-Docker
The procedure of creating a Docker container with support for GPU computations is similar to the approach for normal Docker containers. To create a NVIDIA-Docker container, please follow the instructions from NVIDIA themselves:
https://devblogs.nvidia.com/nvidia-docker-gpu-server-application-deployment-made-easy/

Github Repo: https://github.com/NVIDIA/nvidia-docker

**Your still need to follow the interface specifications provided above.** Please also submit performance indicators (computation time for the GPU/CPU used in your own tests) and the appropriate `nvidia-docker run`command in addition to the other infos required for a standard Docker implementation (see above).

If you have additional questions or troubles using NVIDIA-Docker, please contact us via e-mail (see PDF for address).

### Examples

To help you containerize your segmentation method with Docker, we will provide some examples.

### Assistance

If you are unsure whether your method can be containerized or how to proceed, please contact us in advance. We will try to help you with Docker.  
We have created a PDF-Document containing the exact specifications which you can download here: https://github.com/njarng/docker_brats/raw/master/BRATS_Docker_Interface.pdf

**Also, be sure to check out the documentation on the Docker website.**

### What we need from you
+ Your version of the Docker run command below with the name of your container and the script call
+ Your requirements as far as resource usage is concerned
+ Additional notes regarding functionality
+ Links to Docker Hub or another platform where the image is available

### Docker commands

Your container will be run with the following commands:
~~~~
docker run −v <directory>:/data −it <your image> <your script call>
~~~~
"directory" will be our test directory containing the four modalities and the empty folder for your results.  
"your image" is the name of your Docker image.  
"your script call" is the script that should be called when running the container.


## Notes regarding this repository

### Purpose
This repository should provide some files and documents to aid in the containerization of BRATS methods.

### Additional documents
This repository also contains the Docker interface definition (PDF) for Docker containers taking part in the MICCAI BRATS competition and a website markdown explaining the details for the participants.

**Please contact me in case of any questions or if you have remarks regarding the documents provided.**
