# MNIST Digit Recognition

A website to demonstrate handwritten digit recognition

### How to run?

> Requirements
- python >= 3.10
- node >= 1.18

#### Loading a demonstration
- **If you're not using an apple silicon equipped mac, change the device to cuda, cpu, or whatever suits your needs.**

```npm start```

- This will show the localhost port the server is running on, which you can visit using your browser.

#### Loading the existing network
- **If you're not using an apple silicon equipped mac, change the device to cuda, cpu, or whatever suits your needs.**

```python3 main.py --predict --image <path/to/28x28/json_array> --model <path/to/model>```

#### Training a new neural network
- **If you're not using an Apple Silicon equipped mac, change the device to cuda, cpu, or whatever suits your needs.**

```python3 main.py --train```

### Network
- Convolution 
- Maxpool 
- Convolutional 
- Maxpool 
- Fully connected 
- Fully connected 
- Softmax layer

### Advantages
- Very good translational and rotational invariance

### Disadvantages
- The model is a bit overfit and produces wrong results about 5% of the time

### Screenshots
![Screenshot 2023-01-01 at 5 38 04 PM](https://user-images.githubusercontent.com/119449399/210174830-5253f343-2507-4eec-b4d5-cf2e35affaa6.png)
![Screenshot 2023-01-01 at 5 38 16 PM](https://user-images.githubusercontent.com/119449399/210174833-ec334b67-b4bd-4a2d-8e43-14247e63e797.png)
![Screenshot 2023-01-01 at 5 38 27 PM](https://user-images.githubusercontent.com/119449399/210174835-79089a02-0c27-4e27-872a-e5d4c8cd765b.png)
![Screenshot 2023-01-01 at 5 38 39 PM](https://user-images.githubusercontent.com/119449399/210174837-78158d5b-2ee2-4d34-8add-07101fa9fbbb.png)


