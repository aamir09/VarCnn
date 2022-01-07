from tf_keras_vis.utils.scores import BinaryScore
from matplotlib import cm
from tf_keras_vis.gradcam_plus_plus import GradcamPlusPlus
from tf_keras_vis.utils.model_modifiers import ReplaceToLinear
from pretraineModel.model import get_model
import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pypplot as plt


# Step1 Get your model from the files provided
model=get_model()

#import Image 
image=cv2.imread('path') ## Enter path to your image file
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB) ##Converts color channels from BGR to RGB
#Creating gradCamPlusPlus inferecne
score = BinaryScore([0])
replace2linear = ReplaceToLinear()
gradcam = GradcamPlusPlus(model,model_modifier=replace2linear,clone=True)
cam = gradcam(score,np.asarray([image]),penultimate_layer=-1)
heatmap = np.uint8(cm.jet(cam[0])[..., :3] * 255)
plt.set_title('GRADCAM INFERENCE', fontsize=16)
plt.imshow(image)
plt.imshow(heatmap, cmap='jet', alpha=0.5)
plt.axis('off')
plt.show()