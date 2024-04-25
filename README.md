# Snake Segmentation in Image Processing

This project implements snake-based segmentation algorithms for image processing tasks. Snakes, also known as active contours, are curve-based techniques used for delineating object boundaries in images.

## Overview

Snake segmentation involves iteratively deforming a contour or curve to minimize an energy function, which is typically defined based on image properties such as gradients, edges, and region homogeneity. This process allows the contour to adapt to the features of interest in the image.

This project aims to find the outline of an object on an image. Normally for this we often use the gradient. However, this method is not very precise. Here we will use snakes segmentation. It is a technique that consists in stretching a coarse contour of the image towards its true contour. The method is based on the minimization of the Snake energy, explained in the file `snake.pdf`.

## Prerequisites

Before running the code, ensure you have the required Python modules installed. You can install them using pip:
```bash
pip install numpy matplotlib scipy
```

## Usage

1. Clone this repository to your local machine.
2. Install the prerequisite modules as mentioned above.
3. Run the main Python script to execute the snake segmentation algorithm on your desired images.

## Examples

__*For an image of water drop :*__

![goutteCercle](https://github.com/Lxvxo/Snake-Segmentation-in-Image-Processing/assets/113984090/3d4c4343-ce9a-4fea-8383-e63c8c6b087a)

__*Gradient :*__

![gr](https://github.com/Lxvxo/Snake-Segmentation-in-Image-Processing/assets/113984090/803deebc-a3f8-4ec1-bd95-1f54fe3395e1)

__*Evolution of the snake during the algorithm :*__

![cgoutte](https://github.com/Lxvxo/Snake-Segmentation-in-Image-Processing/assets/113984090/6d2fe000-481e-43f8-82f7-85b7cf083205)


> [!TIP]
> For a great result, you have to choose the good parameters for $\alpha$, $\beta$ et $\gamma$ and always check that the starting circle serving as rough outline contains the whole object
