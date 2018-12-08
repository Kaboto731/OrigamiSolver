# OrigamiSolver
The Goal of this project is to find the underlying structure of origami pieces through simply taking a photo. Generally, there are only a few starting folds that are repeated in order to give an initial structure to origami pieces. If we are able to build a machine that can recognize these patterns, there is hope for a generalized origami network that will be able to come up with its own variations with just a photo. 

# General Overview:

Take a video of an origami base, for easier feature recognition, we will contrast this image with a plain background. Lighting will also take a key importance, since we are recognizing shapes and angles. We will then split this video into each frame and save that frame as a picture with all the pictures of one video in a folder.

The origami bases will be the training set, as initially learning this base is important to recognize where it might be applied. The next step will be to do the validation with some frames from videos, this is done on finished origami pieces (i.e. we will train on bird base, check validation on other pieces and bases, i.e. waterbomb base,(No (0)) origami cranes (Yes (1))) then check the performance on a test, that the machine has not seen. A great benefit of this, is that ceiling analysis is very easy, as ideally all images in a folder will be the same value, and that every folder created will almost always have a known value beforehand.

Build a CNN for origami base imaging:
  Greyscale that CNN, as the color of the paper is not valuable. We also want to get rid of any paper designs
  background subtraction will be an asset.
  Since we are looking for creases, we want lighting to be a valuable asset.
    initially we will solve sharp changes, i.e. no wet folding
  Binary solution for one base.
  Do a cieling analysis for further optimization of the algorithm.
  Extended for multi-class or other bases. 
  
  # Contribute
  
  I welcome all different kinds of contributions, if you want to just submit some images or just want to express some code implementation.
  
  
 
  
