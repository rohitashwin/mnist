from torchvision import datasets, transforms
import torch 

def get_train():
	# Define a transform to normalize the data
	transform = transforms.Compose([transforms.ToTensor()])
	# Download and load the training data
	trainset = datasets.MNIST('data', download=True, train=True, transform=transform)
	trainset, valset = torch.utils.data.random_split(trainset, [50_000, 10_000])
	trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)
	valloader = torch.utils.data.DataLoader(valset, batch_size=64, shuffle=True)
	traindata = list(trainloader)
	valdata = list(valloader)
	return traindata, valdata

def get_test():
	# Define a transform to normalize the data
	transform = transforms.Compose([transforms.ToTensor()])
	# Download and load the test data
	testset = datasets.MNIST('data', download=True, train=False, transform=transform)
	testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=True)
	return testloader