import torch
# setting device on GPU if available, else CPU
print(torch.__version__)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('Using device:', device)
#Additional Info when using cuda
if device.type == 'cuda':
    print("Device name: ", torch.cuda.get_device_name(0))
    print("Device properties:", torch.cuda.get_device_properties(0))
    print("Utilization:", torch.cuda.utilization(0)) #need to pip install pynvml
    print('Memory Usage:')
    print('Allocated:', round(torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(torch.cuda.memory_reserved(0)/1024**3,1), 'GB')

print("device count:", torch.cuda.device_count())
# torch.cuda.current_device()
# torch.cuda.device(0)
# torch.cuda.get_device_name(0)

print(torch.rand(2,3).cuda())

#python3 -m pip install --upgrade tensorrt
import tensorrt
print(tensorrt.__version__)
assert tensorrt.Builder(tensorrt.Logger())