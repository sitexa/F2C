import torch
import torch.nn as nn

print("##################Check GPU#######################")
device = torch.device('cpu')
if torch.cuda.is_available():
    device = torch.device('cuda:0')
    torch.cuda.empty_cache()
    print("Set device to : " + str(torch.cuda.get_device_name(device)))
else:
    print("Set device to : CPU")

print("##################Check PyTorch#######################")
print(torch.rand(5, 3))

print(torch.cuda.get_device_name(0))

