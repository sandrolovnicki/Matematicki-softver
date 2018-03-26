# Matematički softver

This is a repository for homeworks and projects for Mathematical Software, a course at

University of Zagreb, Faculty of Science, Department of Mathematics (Graduate Programme: Computer Science and Mathematics)

#### How to run Jupyter Notebooks?
First, you'll nedd to have anaconda3 set up on your machine. You can download it and read more about at https://www.anaconda.com/download/
After you installed anaconda3, you might need to export its path with following command in your terminal:
```
export PATH=<your-path-to-anaconda3>/bin:$PATH
```

##### Setting up
- First we create a Python3.6 virtual environment and call it, let say py36env:
```
conda create -n py36env python=3.6 anaconda
```
- Now we activate the created environment:
```
source activate py36env
```
- And lastly run our jupyter notebook:
(Note that in case you already are in the directory where your notebooks are, you do not need to pass the --notebook-dir parameter. Also, port value is arbitrary.)
```
jupyter notebook --notebook-dir=<your-path-to-notebooks> --port=12345
```
