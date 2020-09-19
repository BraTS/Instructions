from env import APPLICATION_NAME, APPLICATION_VERSION, INPUT_FOLDER, OUTPUT_FOLDER
from src.utils.utilities import helper
from shutil import copyfile


import os


def logicWrapper():
    inputFileT1 = os.path.normpath(INPUT_FOLDER + "something_t1.nii.gz")
    # ... do the same for t1c, flair and t2 here
    outputFile = os.path.normpath(OUTPUT_FOLDER + "tumor_chuck_norris_class.nii.gz")

    # copy paste your amazing logic here
    print("wrapper: I can feel the magic happening..it feels like a little sun rising inside me!")

    # example logic
    copyfile(inputFile, outputFile)
    helper()


def runCode():
    print("*** code execution started:",
          APPLICATION_NAME, "version:", APPLICATION_VERSION, "! ***")
    logicWrapper()
    print("*** code execution finished:",
          APPLICATION_NAME, "version:", APPLICATION_VERSION, "! ***")
