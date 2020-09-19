import os
# load env
from dotenv import load_dotenv
# don't touch this - can't touch this :7

load_dotenv(verbose=True)


def envVars():
    DOCKER = os.environ.get('DOCKER', False)

    APPLICATION_NAME = os.getenv("APPLICATION_NAME")
    APPLICATION_VERSION = os.getenv("APPLICATION_VERSION")

    if DOCKER:
        print(APPLICATION_NAME, 'running in a Docker container!')
        INPUT_FOLDER = os.getenv("INPUT_FOLDER_DOCKER")
        OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER_DOCKER")
    else:
        INPUT_FOLDER = os.getenv("INPUT_FOLDER")
        OUTPUT_FOLDER = os.getenv("OUTPUT_FOLDER")


INPUT_FOLDER, OUTPUT_FOLDER, APPLICATION_NAME, APPLICATION_VERSION = envVars()
