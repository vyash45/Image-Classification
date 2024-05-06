
# CMPE 258 Assignment 2
To adapt and enhance the LeNet architecture, traditionally used for grayscale image recognition, for effective use with the CIFAR-10 dataset, which consists of 32x32 pixel color images across 10 different categories.


# Prerequisites
Before you can run this project, you need to ensure you have the following installed:

* Python 3.8 or higher
* PyTorch and torchvision
* Visual Studio Code (VSCode)


# Code organization
* [DatasetTools](./DatasetTools): common tools and code scripts for processing datasets
* [TFClassifier](./TFClassifier): Tensorflow-based classifier
  * [myTFDistributedTrainerv2.py](./TFClassifier/myTFDistributedTrainerv2.py): main training code
  * [myTFInference.py](./TFClassifier/myTFInference.py): main inference code
  * [exportTFlite.py](./TFClassifier/exportTFlite.py): convert form TF model to TFlite
* [TorchClassifier](./TorchClassifier): Pytorch-based classifier
  * [myTorchTrainer.py](./TorchClassifier/myTorchTrainer.py): Pytorch main training code
  * [myTorchEvaluator.py](./TorchClassifier/myTorchEvaluator.py): Pytorch model evaluation code 

# Setup
Clone the repository to your local machine using Git:



# Running the Program
You can run the program directly within VSCode using the pre-configured settings in .vscode/launch.json.

