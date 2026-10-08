# Phase 5: Deep Learning

> Learning from data with multi-layer neural networks.

## Overview

| | |
|---|---|
| **Focus** | Neural networks and their main architectures |
| **Prerequisites** | Phase 1 (calculus, linear algebra), Phase 4 (gradient descent, loss, regularization) |
| **Frameworks** | PyTorch, TensorFlow and Keras |
| **Projects** | 3 |
| **Folder** | `07-Deep-Learning/` |
| **Next phase** | Phase 6: MLOps & Deployment |

## Neural Networks

| Topic | Meaning |
|---|---|
| **Perceptron** | The simplest neuron: weighted sum plus an activation |
| **Multi-Layer Perceptron (MLP)** | Layers of neurons stacked together |
| **Activation Functions** | Add non-linearity so networks can learn complex patterns |
| **Forward Propagation** | Passing input through the layers to get a prediction |
| **Loss Functions** | Measuring how wrong the network is |
| **Backpropagation (What, How, Why)** | Computing the gradients used to update every weight |
| **Optimizers** | Methods that update weights using gradients |
| **Dropout & Regularization** | Reducing overfitting in networks |

## Frameworks

| Framework | Use |
|---|---|
| **PyTorch** | Flexible, widely used for research and production |
| **TensorFlow & Keras** | High-level API for building and training networks quickly |

## Architectures

| Architecture | Best for | Notes |
|---|---|---|
| **ANN** | Tabular and general data | Fully connected layers |
| **CNN** | Images | CNN vs ANN, backpropagation in CNN, data augmentation, visualizing filters and feature maps, transfer learning |
| **RNN** | Sequences | Passes information from step to step |
| **LSTM** | Long sequences | Gates to remember and forget |
| **GRU** | Sequences | A simpler gated alternative to LSTM |
| **Transformers** | Language and beyond | Attention-based, the basis of modern LLMs |

## Projects

| Project | Architecture | Skills practiced |
|---|---|---|
| **Image Classification** | CNN | Data augmentation, transfer learning |
| **Handwritten Digit Recognition** | ANN / CNN | Training and evaluating a network |
| **Sentiment Analysis (RNN)** | RNN / LSTM | Text sequences |

## Outcome

By the end of this phase, you can:

- Explain forward propagation and backpropagation.
- Build and train ANN, CNN and RNN models.
- Reduce overfitting with dropout and data augmentation.
- Use transfer learning on image tasks.