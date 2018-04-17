# Real speech dataset in the emergent systems laboratory.
-----------------------------------
## Infomation
Name: Aioi dataset  
Author: Ryo Nakashima  
Subject: Kaede Hayashi  

The data consists of 60 spoken sentences comprised of five words, and five vowels.
Five artificial words {aioi, aue, ao, ie, uo}, which contain five Japanese vowels {a, i, u, e, o} were prepared.
By connecting the words, 30 sentences that included all possible two-word sentences, e.g., “aioi ao,” “aue aue,” and “ie aioi,”;
and five three-word sentences, i.e., “ie ie uo,” “uo aue ie,” “ao ie ao,” “aue ao ie,” and “aioi uo ie” were prepared.
Each sentence was read by a native Japanese speaker twice and recorded in the dataset.
-----------------------------------
## File list
-DATA/ (Speech data.)
-HTKSCRIPT/ (Scripts to convert to MFCC using HTK.)
-NORMALIZE/ (Speech data which was adjusted volume and added a silent section in beginning and ending．)
-ORIGINAL/ (Original recorded data. No adjusted, e.g., sampling-rate.)
-PHONELABEL/ (Phoneme labels.)
-PHONELABELF/ (Phoneme labels in each frame.)
-WORDLABEL/ (Word labels.)
-WORDLAEELF/ (Word labels in each frame.)
-aioi_3dim/
  -DATA/ (3-dimensional MFCC features which compressed by deep sparse auto-encoder.)
  -LABEL/ (Label datas.)
-aioi_12dim/
  -DATA/ (12-dimensional MFCC features which picked from 39-dimentional MFCC features.)
  -LABEL/ (Label datas.)
-----------------------------------
## Quick start
You can use 3 or 12 features in aioi_3dim or aioi_12dim directories.
If you want to read features to Python code, you could include read using loadtxt function which in Numpy.
E.g., as follows.
```
import numpy as np
features = np.loadtxt("aioi_3dim/DATA/aioi_aioi.txt")
```
-----------------------------------
## How to use
Preparation: install [HTK](http://htk.eng.cam.ac.uk/).
1. Make a directory.
```
$ mkdir work
```
2. Copy files from DATA and HTKSCRIPT directories to work directory.
```
$ cp DATA/* work/
$ cp HTKSCRIPT/* work/
```
3. Move to work directory and run "htk.sh".
```
$ cd work
$ sh htk.sh
```
That's all!!
The 39-dimensional MFCC features created in work directory as the text file.
