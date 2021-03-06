import torchvision
import torch
import matplotlib.pyplot as plt
from modules.data_utils import *


def mnistdigits(img_size, delta, num_samples_train, data_dir): #num_samples will not be used 
    
    mean =-delta/(1-delta)
    std=1/(1-delta)
    
    trainset= torchvision.datasets.MNIST(data_dir, train=True, download=True,
                                 transform=torchvision.transforms.Compose([
                                    torchvision.transforms.Resize([img_size, img_size]),
                                    torchvision.transforms.ToTensor(),
                                    torchvision.transforms.Normalize(
                                     (mean,), (std,))
                                 ]))

    valtestset = torchvision.datasets.MNIST(data_dir, train=False, download=True,
                                 transform=torchvision.transforms.Compose([
                                    torchvision.transforms.Resize([img_size, img_size]),
                                    torchvision.transforms.ToTensor(),
                                    torchvision.transforms.Normalize(
                                     (mean,), (std,))
                                 ]))
    
    valset = valtestset
    testset = None ## create this if needed
    
    return trainset, valset, testset

def mnistdigits_grid2patch(img_size, delta, num_samples_train, data_dir):
    
    trainset = mnistgrid_getdataset(img_size, 'train', delta, data_dir, num_samples_train)
    valset= mnistgrid_getdataset(img_size, 'val', delta, data_dir)
    testset= mnistgrid_getdataset(img_size, 'test', delta, data_dir)
    
    return trainset, valset, testset


def confocal(img_size, delta, num_samples_train, data_dir):
    
    trainset = confocal_getdataset(img_size, 'train', delta, data_dir, num_samples_train)
    valset= confocal_getdataset(img_size, 'val', delta, data_dir)
    testset= confocal_getdataset(img_size, 'test', delta, data_dir)
    
    return trainset, valset, testset



def confocal_segment(img_size, delta, num_samples_train, data_dir):    
    trainset = confocal_seg_getdataset(img_size, 'train', delta, data_dir, num_samples_train)
    valset= confocal_seg_getdataset(img_size, 'val', delta, data_dir)
    testset= confocal_seg_getdataset(img_size, 'test', delta, data_dir)
    
    return trainset, valset, testset
