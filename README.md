This is my image processing exercise for car detection with YOLOv5 model. 

First, I labelled my images with Roboflow and split them into train and test files. Then as you can see in the train_ex, I trained my data with YOLOv5, I tried to choose the best batch size and epoch number for this training. I followed the parameters. After training, I download the weights to use them in my real-time project. You can see how I run the real-time part in main.py by using OpenCV. I also needed PyTorch to load my weights, and used some other tools that complete my project.   
