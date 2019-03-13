# BRATS Algorithmic Repository

This is a repository of links to Docker images that conform to the BRATS Challenge Interface requirements for Docker containers and have been tested successfully.

The official Docker Hub page for BraTS 2018 is <a href="https://hub.docker.com/u/brats/">now online</a>. If you would like your Docker image to be hosted here, please contact us.

To use the images, pull them using `docker pull <repo>/<image>` and then run them according to the instructions provided in `README.md` and the `BRATS_Docker_Interface.pdf` file.

<b><u>For licensing information, please contact the individual authors linked below.</b></u>

## Available Docker Containers

### BraTS 2018


Most Dockers for segmentations of the BraTS 2018 challenge are hosted on our own <a href="https://hub.docker.com/u/brats/"> Docker Hub Page </a>. Please check that page for the newest versions of our images. Please read the description of the individual images to obtain usage instructions. A detailed list of images will follow here soon.


### BraTS 2017
#### Native Docker (CPU-only)
| `<repo>/<image>`       | Author          | Author's Link | Paper |
| ------------------ |---------------|----------| ------- |
| `kamleshp/brats17` | Kamlesh Pawar | <a href="https://hub.docker.com/r/kamleshp/brats17/">Docker Hub link</a> | Kamlesh Pawar, Zhaolin Chen, N. Jon Shah, Gary Egan. Residual Encoder and Convolutional Decoder Neural Network for Glioma Segmentation. <a href="https://link.springer.com/chapter/10.1007%2F978-3-319-75238-9_23">LNCS paper link</a> |
| `brats/brats_dc`| Guotai Wang |  <a href="https://cmiclab.cs.ucl.ac.uk/gwang/brats_dc">Institutional Link</a> | Guotai Wang, Wenqi Li, Sebastien Ourselin, Tom Vercauteren. Automatic Brain Tumor Segmentation using Cascaded Anisotropic Convolutional Neural Networks. <a href="https://doi.org/10.1007/978-3-319-75238-9_16">LNCS paper link</a>, <a href="https://arxiv.org/abs/1709.00382">arXiv preprint link</a> |
| `mikaelagn/magnrbm`| Mikael Agn | <a href="https://hub.docker.com/r/mikaelagn/magnrbm/">Docker Hub link</a> | <link missing> |
| `romainsauvestre/gevaertlab` | Romain Sauvestre | <a href="https://hub.docker.com/r/romainsauvestre/gevaertlab/">Docker Hub link</a> | <link missing>
| `saras/saras_test_brats_2017`| Sara Sedlar |  <a href="https://github.com/Sara04/BRATS">Github link</a> | Sara Sedlar. Brain Tumor Segmentation Using a Multi-path CNN Based Method. <a href="https://link.springer.com/chapter/10.1007%2F978-3-319-75238-9_35">LNCS paper link</a> |
| `ekrivov/brats2017_old` | Egor Krivov | <a href="https://hub.docker.com/r/ekrivov/brats2017_old/">Docker Hub link</a> | Egor Krivov, Maxim Pisov, Mikhail Belyaev. MRI Augmentation via Elastic Registration for Brain Lesions Segmentation. <a href="https://link.springer.com/chapter/10.1007%2F978-3-319-75238-9_32">LNCS paper link</a> |
| `silvanac/uniandes` | Luis C. Rivera Monroy | <a href="https://hub.docker.com/r/silvanac/uniandes/">Docker Hub link</a> | Laura Silvana Castillo, Laura Alexandra Daza, Luis Carlos Rivera, Pablo Arbelaez. Brain Tumor Segmentation and Parsing on MRIs Using Multiresolution Neural Networks. <a href="https://link.springer.com/chapter/10.1007%2F978-3-319-75238-9_29">LNCS paper link</a> |
| `qtimlab/qtimlab_brats_2017` | Andrew Beers, Ken Chang, James Brown, Jayashree Kalpathy-Cramer | <a href="https://hub.docker.com/r/qtimlab/qtimlab_brats_2017/">Docker Hub link</a> | Andrew Beers, Ken Chang, James Brown, Elizabeth Gerstner, Bruce Rosen, Jayashree Kalpathy-Cramer. Sequential neural networks for biologically-informed glioma segmentation. <a href="https://www.spiedigitallibrary.org/conference-proceedings-of-spie/10574/1057433/Sequential-neural-networks-for-biologically-informed-glioma-segmentation/10.1117/12.2293941.short">SPIE paper link</a> |
| `brats/brats_ac` | Adrià Casamitjana | <a href="https://hub.docker.com/r/brats/brats_ac/">Docker Hub link</a> | 3D Convolutional Neural Networks for Brain Tumor Segmentation: A Comparison of Multi-resolution Architectures <a href="https://link.springer.com/chapter/10.1007/978-3-319-55524-9_15"> LCNS paper link </a> |
| `brats/istb_aj`| Alain Jungo | <a href="https://hub.docker.com/r/brats/istb_aj/"> Docker Hub link </a> | Alain Jungo, Richard McKinley, Raphael Meier, Urspeter Knecht, Luis Vera, Julián Pérez-Beteta, David Molina-García, Víctor M. Pérez-García, Roland Wiest, Mauricio Reyes.Towards Uncertainty-Assisted Brain Tumor Segmentation and Survival Prediction. <a href="https://link.springer.com/chapter/10.1007/978-3-319-75238-9_40">LNCS paper link</a> |

#### Nvidia-Docker (GPU-support needed)
| `<repo>/<image>`       | Author          | Author's Link | Paper |
| ------------------ |---------------|----------| ------- |
| `fabianisensee/brats2017_isensee` | Fabian Isensee | <a href="https://hub.docker.com/r/fabianisensee/brats2017_isensee/">Docker Hub link</a> | Fabian Isensee, Philipp Kickingereder, Wolfgang Wick, Martin Bendszus, Klaus H. Maier-Hein. Brain Tumor Segmentation and Radiomics Survival Prediction: Contribution to the BRATS 2017 Challenge. <a href="https://link.springer.com/chapter/10.1007%2F978-3-319-75238-9_25">LNCS paper link</a> |
| `libphy/brats17ens9` | Geena Kim | <a href="https://hub.docker.com/r/libphy/brats17ens9/">Docker Hub link</a> | Kim G. (2018) Brain Tumor Segmentation Using Deep Fully Convolutional Neural Networks. In: Crimi A., Bakas S., Kuijf H., Menze B., Reyes M. (eds) Brainlesion: Glioma, Multiple Sclerosis, Stroke and Traumatic Brain Injuries. BrainLes 2017. Lecture Notes in Computer Science, vol 10670. <a href="https://link.springer.com/chapter/10.1007/978-3-319-75238-9_30">LNCS paper link</a> |

More to come soon. If you would like to add your BRATS challenge implementation in Docker here, please contact us.

#### Contact
Author: C. Berger
