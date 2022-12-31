import json
import torch 
import torchvision
import dataset
import torch.optim as optim
import model as m
from tqdm import tqdm
import numpy as np
import warnings 
warnings.filterwarnings("ignore", category=UserWarning)
import argparse

def train():
	# epoch count
	epochs = 10
	lr = 0.003
	lossctr = 0
	patience = 3
	# create model
	model = m.CustomNet()
	# create optimizer adam
	optimizer = optim.Adam(model.parameters(), lr=lr)
	# create loss function
	criterion = torch.nn.CrossEntropyLoss()
	# train
	# prev loss is used to check for early stopping starting at infinity
	prevloss = np.inf
	for epoch in range(epochs):
		train, val = dataset.get_train()
		print(f'Epoch: {epoch}')
		for images, labels in tqdm(train):
			# clear gradients
			optimizer.zero_grad()
			# forward pass
			outputs = model(images)
			# calculate loss
			loss = criterion(outputs, labels.to(torch.device('mps')))
			# backward pass
			loss.backward()
			# update parameters
			optimizer.step()
			# print loss
			lossctr += loss.item()
			lossctr = 0
		currloss = validate(model, val)
		# early stopping
		if currloss > prevloss:
			patience -= 1
			if patience == 0:
				print('Early stopping')
				break
		else:
			patience = 3

	# save model
	torch.save(model.state_dict(), 'model.pth')
	print('Model saved')


def validate(model, val):
	# create loss function
	criterion = torch.nn.CrossEntropyLoss()
	# validate
	with torch.no_grad():
		print('Validating...')
		loss = 0
		accuracy = 0
		ctr = 0
		for images, labels in tqdm(val):
			# forward pass
			outputs = model(images)
			# calculate loss
			loss = criterion(outputs, labels.to(torch.device('mps')))
			# print loss
			loss += loss.item()
			# calculate accuracy
			accuracy += np.mean(np.argmax(outputs.to("cpu").numpy(), axis=1) == labels.to("cpu").numpy())
			ctr += 1
		avgloss = loss/len(val)
		print(f'Average loss: {avgloss}, Accuracy: {accuracy*100/ctr}')
		return avgloss

def test():
	# load model
	model = m.CustomNet()
	model.load_state_dict(torch.load('model.pth'))
	model.eval()
	# test
	test = dataset.get_test()
	criterion = torch.nn.CrossEntropyLoss()
	with torch.no_grad():
		print('Testing...')
		loss = 0
		accuracy = 0
		ctr = 0
		for images, labels in tqdm(test):
			# forward pass
			outputs = model(images)
			# calculate loss
			loss = criterion(outputs, labels.to(torch.device('mps')))
			# print loss
			loss += loss.item()
			# calculate accuracy
			accuracy += np.mean(np.argmax(outputs.to("cpu").numpy(), 1) == labels.to("cpu").numpy())
			ctr += 1
		avgloss = loss/len(test)
		print(f'Average loss: {avgloss}, Accuracy: {accuracy*100/ctr}')

def predict(image, model_path):
	# load model
	model = m.CustomNet()
	model.load_state_dict(torch.load(model_path))
	model.eval()
	# make prediction
	with torch.no_grad():
		outputs = model(image)
		return np.argmax(outputs.to('cpu').numpy())

if __name__ == '__main__':
	# parse args, the predict flag should receive an file with 28x28 pixels representing a number
	parser = argparse.ArgumentParser()
	parser.add_argument('--train', action='store_true')
	parser.add_argument('--test', action='store_true')
	parser.add_argument('--predict', action='store_true')
	parser.add_argument('--image', type=str)
	parser.add_argument('--model', type=str)
	args = parser.parse_args()
	if args.train:
		train()
	elif args.test:
		test()
	elif args.predict:
		# the image is a json file with 28x28 pixels representing a number, parse it, and then convert it to a tensor and pass it to the predict function
		jsonfile = open(args.image, 'r')
		image = json.load(jsonfile)
		image = torch.tensor(image)
		image = image.view(1, 1, 28, 28)
		# save the image pixel values to a file
		with open('image.txt', 'w') as f:
			for i in range(28):
				for j in range(28):
					f.write(str(image[0][0][i][j].item()) + ' ')
				f.write('\n')
		print(predict(image, args.model))