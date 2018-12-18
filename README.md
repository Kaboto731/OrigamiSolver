# OrigamiSolver
The Goal of this project is to find the underlying structure of origami pieces through simply taking a photo. Generally, there are only a few starting folds that are repeated in order to give an initial structure to origami pieces. If we are able to build a machine that can recognize these patterns, there is hope for a generalized origami network that will be able to come up with its own variations with just a photo. 

# General Overview:

Take a video of an origami base, for easier feature recognition, we will contrast this image with a plain background. Lighting will also take a key importance, since we are recognizing shapes and angles. We will then split this video into each frame and save that frame as a picture with all the pictures of one video in a folder.

The origami bases will be the training set, as initially learning this base is important to recognize where it might be applied. The next step will be to do the validation with some frames from videos, this is done on finished origami pieces (i.e. we will train on bird base, check validation on other pieces and bases, i.e. waterbomb base,(No (0)) origami cranes (Yes (1))) then check the performance on a test, that the machine has not seen. A great benefit of this, is that ceiling analysis is very easy, as ideally all images in a folder will be the same value, and that every folder created will almost always have a known value beforehand.
  Current bases in system:
  Bird Base
  Waterbomb Base
  Further Implementation:
  Fish Base


Build a CNN for origami base imaging:
  Greyscale that CNN, as the color of the paper is not valuable. We also want to get rid of any paper designs
  background subtraction will be an asset.
  Since we are looking for creases, we want lighting to be a valuable asset.
    initially we will solve sharp changes, i.e. no wet folding
 Through the use of an ANN we will probabilistically determine:
  The corresponding base.
  For further tuning, since the files are seperated by piece, we can do:
  Do a cieling analysis for further optimization of the algorithm.
  Extended for multi-class or other bases. 
  
  # Setup
  For simplicity and organizational sanity, I have labeled each batch of images by the corresponding base, or finished design. Since we are training on all of the bases these folders will have to be combined into one master folder containing all the images:
  our train file will include all images of:
  WaterbombBase
  Birdbase
We will be training on these two bases to provide a simplistic view and be using the following as our test cases
  our test file will include all images of:
  Balloon
  Origami Crane
  This is because the Balloon and the origami crane are relatively simple origami pieces that use the corresponding bases above. Since these are of the simpler variety, it offers a better chance to get an accurate feature representation started, as not much is hidden through more advanced techniques. Intuitively, as a piece undergoes more and more folds, the geometry should change and become harder and harder to identify. Thus the problem we have for machine learning is giving it enough variance and boundary conditions to find the borders of each base classification.
  
  # Contribute
  
  I welcome all different kinds of contributions, if you want to just submit some images or just want to express some code implementation.
  
  
 
  
