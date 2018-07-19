# emof_ai

Emof_ai is a web API which takes a sample video as an input, detects all the faces in each frame of the video and performs classfication. It classifies the emotion of the face into 1 of 8 emotions viz anger, disgust, fear, happy, sad, surprise, neutral and none(this is when there are no faces detected in the frame at all and hence none means no emotion detected in the frame at all). It also classifies the gender of the person. In addition to that, it also classifies the age group of the person into 1 of 4 age groups viz adult, child, old and youth. 

There are 3 models for each of the 3 tasks. The face detection is done using haarcascade xml and the classification is done using  3 convolutional neural networks, each for one of the 3 tasks and made up of 5 layers. After the processing of the video is done, a data analysis graph is constructed and shown which determines the percent count of each emotion in the video. The percentage of each emotion shows the percentage of detection boxes detected with that emotion. Each emotion is grouped by the gender and the age group. Flask framework is used for the creation of the web API.

## Getting Started

After cloning the repository:<br/>
->Run the master-main.py file using the command "python master-main.py" on the terminal. <br/>
->A webhook url will be generated on the terminal. Open the url in a browser. <br/>
->There will be an option on the web page to provide a sample video for processing. Provide a sample video to it. If you want, there is a sample video provided for testing in the repository. <br/>
->The detection on each frame will be shown and at last the statistical analysis graph will displayed. <br/>


### Prerequisites

A file named requirements.txt is provided which contains all the prerequisites required to run the project. <br/>
Navigate to the cloned repo folder and open the terminal there. <br/>
Run the command "pip install -r requirements.txt" to install the requirements. <br/>

## Built With

* [Python](https://www.python.org/) - The language used
* [Tensorflow](https://www.tensorflow.org/api_docs/) - Backend API to create the CNNs
* [Keras](https://keras.io//) - Wrapper library for tensorflow used to create the CNNs
* [Matplotlib](https://matplotlib.org/) - The library used for creating the statistical analysis graph
* [Flask](http://flask.pocoo.org/docs/0.12/) - The web framework used

## Authors

* **Kaumil Trivedi** - [kaumil](https://github.com/kaumil)
* **Dhrumil Sheth**
