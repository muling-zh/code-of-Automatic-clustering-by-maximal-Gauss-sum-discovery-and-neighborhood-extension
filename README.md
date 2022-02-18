# our_algorithm

### Introduction
This is the code for the paper "Automatic clustering by maximal Gauss sum discovery and neighborhood extension".
The algorithm flow and core is all in file named *cluster_runThis.py*, and you just run it!


### Dependencies
based on Python 3.9:

- cycler==0.11.0
- fonttools==4.28.5
- joblib==1.1.0
- kiwisolver==1.3.2
- llvmlite==0.38.0
- matplotlib==3.5.1
- numba==0.55.0
- numpy==1.21.5
- packaging==21.3
- Pillow==9.0.0
- pyparsing==3.0.6
- python-dateutil==2.8.2
- scikit-learn==1.0.2
- scipy==1.7.3
- six==1.16.0
- sklearn==0.0
- threadpoolctl==3.0.0



### Install

We give the dependent files, you need to open the python command terminal and run:

`pip install -r requirements.txt`

(You need to install pip first!)

### Usage

In *cluster_runThis.py*, you need to set the file path of your dataset. And you can also define your own distance measure function in *distance_calculation.py*. Then adjust the parameter *dc*  and  *P0* reasonably according to the output for better result.

### Citation

If you find our algorithm useful in your research, please consider citing:

```
@article{pei2022cluster,
  title={Automatic clustering by maximal Gauss sum discovery and neighborhood extension},
  author={Zheng Pei, Bing Luo, Miaolong Ye, Chengbao Zhou, Bo Li and Mingming Kong},
  journal={arXiv preprint arXiv:xxxx.xxxxx},
  year={2022}
}
```
