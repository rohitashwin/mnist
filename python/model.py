import torch
import torch.nn as nn
import torch.nn.functional as F

class CustomNet(nn.Module):
	def __init__(self):
		super(CustomNet, self).__init__()
		self.layers = nn.Sequential(
			nn.Conv2d(1, 32, 5, 1),
			nn.ReLU(),
			nn.MaxPool2d(2, 2),
			nn.Conv2d(32, 64, 5, 1),
			nn.ReLU(),
			nn.MaxPool2d(2, 2),
			nn.Flatten(),
			nn.Linear(1024, 128),
			nn.ReLU(),
			nn.Linear(128, 10),
			nn.LogSoftmax(dim=1)
		).to(torch.device('mps'))

	def forward(self, x):
		x = x.to(torch.float32)
		x = x.to(torch.device('mps'))
		x = x.view(x.size(0), 1, 28, 28)
		x = self.layers(x)
		return x

	# what is the input shape of the model for mnist for 64 batchsize: 64, 1, 28, 28 where 