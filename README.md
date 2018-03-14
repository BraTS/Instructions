# Dockerization Instructions
Instructions on how to dockerize your algorithm, as applied in the BraTS challenge

# Dockerization / Containerization
In most cases, containerization of your code is a simple and straightforward procedure. We will provide an example container with functional code soon. Furthermore, many containers are available on the internet to be used as a basis, probably including your favorite programming environment and neuroimaging tools.

The concept of containerization is to simplify the deployment of applications. To ensure maximum compatibility and (potentially) distributability, we want to collect algorithms using a container approach with Docker (www.docker.com). Docker is a technique to do so and will be used for the BraTS Algorithmic Repository.

Docker can be used to “wrap” your entire segmentation method (including all dependencies) into a single container. This container can be run as if it would be a single standalone application, anywhere, on any platform. Because your method and all dependencies are included in the container, the method is guaranteed to run exactly the same at all times.

Dockerization is a very popular concept and has been used successfully in previous MICCAI challenges, e.g., in the MSSEG challenge (https://portal.fli-iam.irisa.fr/msseg-challenge/overview) and the WMH Segmentation Challenge (http://wmh.isi.uu.nl/methods/). The current text is also based on info from the WMH Segmentation Challenge. Docker Hub (https://hub.docker.com/) provides a large overview of existing Docker containers (base images), that can be used to build your own container. Furthermore, many popular programming environments and image analysis methods have Dockerfiles available.

# Data Access
All test sets will be identical to the 2016 or 2017 test data that you have already processed. They are co-registered, skull-stripped, resampled to 1mm^3 isotropic resolution, and aligned to the SRI space. Data will be in NIfTI GZIP Compressed Tar Archive (.nii.gz) format, with all header information except the spatial resolution removed, and the individual volumes will be named ‘fla.nii.gz’, ‘t1c.nii.gz’, ‘t1.nii.gz’, ‘t2.nii.gz’. You can use any of the BRATS training or testing image volumes to check whether your Docker image runs as expected.

Because your container runs in an isolated environment, the data needs to be mapped into the container. The input data files, i.e., the ‘fla.nii.gz’, ‘t1c.nii.gz’, ‘t1.nii.gz’, ‘t2.nii.gz’ volumes, will be linked to /data and your segmentations must be placed in /data/results. Results should be a NIfTI file with the same resolution as the input data. Please call the resulting file "tumor_’your_image’_class.nii.gz", where ‘your_image’ is an eight digit identifier of your algorithm. If your algorithm returns probabilities as well, you can return them accordingly, and name them, e.g., "tumor_’your_image’_prob_4.nii.gz" for results of class 4. If your algorithm returns tissue classes, please use “tissue_’your_name’_wm.nii.gz” for white matter (*‘_gm.nii.gz’ and ‘*_csf.nii.gz’ for the other two).

There should be no interaction with the container required other than running the Docker command below, i.e., we can only support fully automatic algorithms.

# Computing environment & resources, GPUs
We will run your container on a selection of test cases from the BraTS 2016 data sets, based on the quality of their skull-stripping. Docker can set resource limits on containers. Please give us an indication how many CPUs and how much RAM is needed for you method, and what the resulting computation time will be.

In our first instalment, we would like to run all code CPU-only to retain compatibility. Docker does not yet support GPU mapping on all platforms, so please provide a CPU-only version of you code. If you really want/need to use a GPU, please contact us.
