# SHU-CAPTCHA-solver-based-on-CNN
SHU CAPTCHA solver based on CNN, need python, [kears](https://keras.io/) ,numpy and PIL as dependencies.
<br>

### structure
The network is composed of two convolution layers and one max pooling layer. Drop-out and softmax are also used.<br>
If you intend to change the structure of the network, check train.py.<br>
The structure and parameters of the trained network are stored in shu_captcha_CNN_structure.json and shu_captcha_CNN_weights.h5.

### dataset
The pictures in the datasets are from the [curricula-variable system of ShangHai University](http://cj.shu.edu.cn/).
The raw picture is a 60x22 captcha image of 4 English letters or numbers.<br>
We devide the images averagely into 4 parts and mannually labeled it, totaled 6284 samples.<br>
As the images are RBG format, they're stored in X_train.npy as a numpy array with the shape of (6284, 22, 15, 3).<br>
Each result is a 62 demension one-hot vecotr, as 10 digits, 26 capital letters and 26 lower-case letters, they're stored in Y_train.py as a (6284, 62).<br>
If you intend to append any data to the dataset, check these files.

### usage
Run train.py and it will load the training set and train the network. 
Afterwords it will stored the network using keras's model.save_weights and model.to_json function to save the data.<br>
Also, you can simplely import CaptchaSolver into your script and use the solve method by passing it a loaded Image object(from PIL). See test.py.<br>
Be aware each time that CaptchaSolver.py starts, it loads the network from the json and h5 files above,
 so if you want to make it a service of some type(eg web api), it's better to keep the proccess as a resident one.
