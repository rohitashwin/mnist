# MNIST Training with PyTorch

A simple program to train on mnist dataset with a good looking interface.

# Some info

### M1 GPU Training vs CPU Training

I expected a huge jump in performance by moving the training to the GPU, but the performance improvements have been relatively minor.

CPU avg: 3 min 10 sec / epoch (batch 64)
GPU avg: 1 min 23 sec / epoch (batch 64)

It looks like it's a little bit more than 2x faster than training on the CPU.
