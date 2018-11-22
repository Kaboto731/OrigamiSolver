# OrigamiSolver
To use machine learning techniques to help solve for origami bases

General Overview:

Build a CNN for origami base imaging:
  Greyscale that CNN, as the color of the paper is not valuable. We also want to get rid of any paper designs
  background subtraction will be an asset.
  Since we are looking for creases, we want lighting to be a valuable asset.
    initially we will solve sharp changes, i.e. no wet folding
  Binary solution for one base.
  Do a cieling analysis for further optimization of the algorithm.
  Extended for multi-class or other bases. 
