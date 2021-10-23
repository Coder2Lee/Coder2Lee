from __future__ import print_function
import torch

x = torch.randn(3, requires_grad=True)
print(x)
y = x * 2
print(y)
while y.data.norm() < 1000:
    y = y * 2

print(y)