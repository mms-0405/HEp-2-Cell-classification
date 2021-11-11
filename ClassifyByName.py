#Classify the images into 6 classes by name
import os
import shutil
path = "C:/Users/12705/Desktop/ELEC5622 Signals Software & Health/5622project2/Three/validation/"
new_path ='C:/Users/12705/Desktop/ELEC5622 Signals Software & Health/5622project2/ThreeDatasets/validation/'
filelist = os.listdir(path)
for file in filelist:
    filename = os.path.basename(file)
    filenum = int(os.path.basename(file)[0:5])
    sourcepath = os.path.join(path,filename)
    if (1 <= filenum <= 2494):
        newpath = os.path.join(new_path,'Homogeneous/',filename)
        shutil.copyfile(sourcepath,newpath)
    if (2495 <= filenum <= 5325):
        newpath = os.path.join(new_path,'Speckled/',filename)
        shutil.copyfile(sourcepath,newpath)
    if (5326 <= filenum <= 7923):
        newpath = os.path.join(new_path,'Nucleolar/',filename)
        shutil.copyfile(sourcepath,newpath)
    if (7924 <= filenum <= 10664):
        newpath = os.path.join(new_path,'Centromere/',filename)
        shutil.copyfile(sourcepath,newpath)
    if (10665 <= filenum <= 12872):
        newpath = os.path.join(new_path,'NuMem/',filename)
        shutil.copyfile(sourcepath,newpath)
    if (12873 <= filenum <= 13596):
        newpath = os.path.join(new_path,'Golgi/',filename)
        shutil.copyfile(sourcepath,newpath)

