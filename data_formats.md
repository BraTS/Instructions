# BraTS Data Formats for Docker containers

Here is a short overview over all the filename conventions expected by various Docker containers used in the BraTS challenge. You can find the Docker images <a href="https://hub.docker.com/u/brats/">here</a> and every repository description has a data format given which the code in the container expects. Each algorithm works with 4 modalities: T1, T1c, T2 and FLAIR.
Depending on which container you use, your inputs should be in the right format. The info below should help you figure out how your filenames should be specified for optimal operation.

### BraTS 2019 

For this year's challenge, we only accept Docker images which support input conforming to the following format (same format as the provided dataset). In short, your code must be able to read and process the following files:  
- `*_flair.nii.gz`
- `*_t1ce.nii.gz`
- `*_t1.nii.gz`
- `*_t2.nii.gz`

These 4 modalities will be made accessible in the directory `/data` when we run your Docker container and all resulting segmentation/survival files must be saved in the provided directory `/data/results`. 

### Data format codes for past challenges and entries:
**gz** for compressed, e.g. flair.nii.gz

**b17** for files in the format as specified in the interface definition from last year's request for containers (e.g. flair.nii** without a subject prefix e.g. pat123_flair.nii.gz) and b18 for filenames as used in this year's validation set.

**t1** and **f** signal minor variations of filenames (f is fla.nii**, t1 is t1ce.nii**, otherwise flair.nii** and t1c.nii**, respectively).

### The Categories:
Some of those may not be used at all, they are just here for completeness.

- **gz-b17**: flair.nii.gz, t1.nii.gz, t1c.nii.gz, t2.nii.gz

- **gz-b17-f**: fla.nii.gz, t1.nii.gz, t1c.nii.gz, t2.nii.gz

- **gz-b17-t1**: flair.nii.gz, t1.nii.gz, t1ce.nii.gz, t2.nii.gz

- **b17**: flair.nii, t1.nii, t1c.nii, t2.nii

- **b18**: e.g. Brats17_CBICA_ATW_1_flair.nii.gz, Brats17_CBICA_ATW_1_t1.nii.gz Brats17_CBICA_ATW_1_t1ce.nii.gz, Brats17_CBICA_ATW_1_t2.nii.gz

likewise for uncompressed versions (without a **gz** prefix).

### Notes
We aim to have one format that all containers use for the BraTS 2019 challenge to avoid this workaround by specifying naming schemes. For any questions, please contact <a href="mailto:c.berger@tum.de">me</a>.
