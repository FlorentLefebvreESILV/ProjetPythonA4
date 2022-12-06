# ProjetPythonA4
Machine learning API - Online Video Characteristics and Transcoding Time Dataset Data Set
Python for Data Analysis - Project
Florent LEFEBVRE & Lucas MONTEILS - DIA4
 

Assigned dataset : https://archive.ics.uci.edu/ml/datasets/Online+Video+Characteristics+and+Transcoding+Time+Dataset

 

Foreword :

 

Who are we ?

We are two future data science engineers in their fourth year at ESILV. During our curriculum, various projects are submitted to us and we are then evaluated on their achievement. Here we have to process and exploit the data of this dataset, find a problematic which fits in the context of the study and explore it through Data pre-processing (encoding, normalization, imputation...), Data visualization, and Modeling.

 

What is this dataset ?

The presented dataset is composed of two tsv files named 'youtube_videos.tsv' and 'transcoding_mesurment.tsv'. The first contains 10 columns of fundamental video characteristics for 1.6 million youtube videos; It contains YouTube video id, duration, bitrate(total in Kbits), bitrate(video bitrate in Kbits), height(in pixle), width(in pixles), framrate, estimated framerate, codec, category, and direct video link. This dataset can be used to gain insight in characteristics of consumer videos found on UGC(Youtube).

The second file of our dataset contains 20 columns(see column names for names) which include input and output video characteristics along with their transcoding time and memory resource requirements while transcoding videos to diffrent but valid formats. The second dataset was collected based on experiments on an Intel i7-3720QM CPU through randomly picking two rows from the first dataset and using these as input and output parameters of a video transcoding application, ffmpeg 4 . In section 6 we will use the second dataset to build a transcoding time prediction model and show the significance of our datasets.

 

What changes have we made to it and why ?

We had a pretty clean dataset where the data was of the right type, with no NaN, each column corresponded to only one variable, everything was clear to us and there was no need to transform the dataset a lot. Thus, we just added columns mixing several data such as the output_height / input_height ratio, the same for the width of the videos.

 

What is the API able to do ?

Our API presents the dataset in a global way by some significant visuals concerning the transcoding time of a video, then allows to estimate the transcoding time of a video by entering certain parameters thanks to the model that we have made.

 

Browse API :

- polls/ : presentation page

- polls/visu/ : visualize the dataset

- polls/model/ : use the model and make a prediction of the transcoding time
