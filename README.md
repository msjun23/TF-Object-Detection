# TF-Pedestrian-Car-Detection
Pedestrian and car detection with tensorflow for Self Driving Car


# Download Tensorflow API
First install Tensorflow API. Follow the link at here.
- https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1.md
- Add this variable path or just excute at terminal

```bash
# Do this before you test the installation
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
```

We only need research/object_detection & reserch/slim.

Copy & paste these two folders to your workspace.


# Preparing custom data
Download Full Set Images at here.
- http://cbcl.mit.edu/software-datasets/streetscenes/

Download latest version of LabelImg at here.
- http://tzutalin.github.io/labelImg/

To annotate images we will be using the labelImg package. With it, can get \*.xml file for one image.

You have to separate this image and xml files to the train folder and the test folder.


Convert [\*.xml to \*.csv](https://github.com/msjun23/TF-Object-Detection/blob/master/xml_to_csv.py) and [\*.csv to \*.record](https://github.com/msjun23/TF-Object-Detection/blob/master/generate_tfrecord.py).

Finally 2 csv files and 2 record files in your [data folder](https://github.com/msjun23/TF-Object-Detection/tree/master/workspace/data).
