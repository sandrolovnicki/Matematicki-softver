# Matematički Softver

This is a repository of homeworks and projects for Mathematical Software, a course at

University of Zagreb, Faculty of Science, Department of Mathematics (Graduate Programme: Computer Science and Mathematics)

---
## How to run Jupyter Notebooks?
Jupyter Notebooks use Python3.6, are shown in your web-browser at localhost and can be run with Anaconda. You'll need to set those up on your machine.
The following steps will lead you in installing anaconda3, setting up python virtual environment and running notebooks.  
**NOTE:** Python3.6 is also required and steps bellow will not cover its setup.

#### Installing Anaconda3
You can download it and read more about at https://www.anaconda.com/download/. After you installed anaconda3, you have everything needed to run jupyter notebooks.

You might need to export anaconda's path with following command in your terminal:
```
export PATH=<your-path-to-anaconda3>/bin:$PATH
```

#### Creating Python3.6 virtual environment

First we need to create a Python3.6 virtual environment and call it, let say py36env. Once created, py36env exists on your system so you don't have to create it again if you already have done this step (or have an existing python3.6 environment ready to use).
```
conda create -n py36env python=3.6 anaconda
```

#### Running Notebooks
- Again, you might need to export anaconda's path with following command in your terminal:
```
export PATH=<your-path-to-anaconda3>/bin:$PATH
```
- Now we activate our python3.6 virtual environment:
```
source activate py36env
```
- And lastly run our jupyter notebook:  
_**NOTE:** In case you already are in the directory where your notebooks are (or just don't care), you don't need to pass the --notebook-dir parameter. Also, port value is arbitrary._
```
jupyter notebook --notebook-dir=<your-path-to-notebooks> --port=12345
```
