from matplotlib import pyplot as plt
import numpy as np

def get_image(image_path):
    image = plt.imread(image_path)
    return image/255.0


def show_image(image):
    plt.imshow(image)
    plt.show()

def save_image(image, image_path):
    plt.imsave(image_path, image)

def plot_MSE_graph(errors):
    MEANS = list(errors.keys())
    ERROR = list(errors.values())
    filename = "plot_MSError.png"
    fig, ax = plt.subplots()
    ax.plot(MEANS, ERROR, 'o-')
    ax.set_xlabel('Number Of Cluster')
    ax.set_ylabel('Mean Squared Error')
    ax.set_title('Number Of Clusters Vs MSE for K-Means Algorithm')
    plt.savefig(filename)


def error(original_image: np.ndarray, clustered_image: np.ndarray) -> float:
    # Returns the Mean Squared Error between the original image and the clustered image
    # original_image = original_image.reshape(original_image.shape[0]*original_image.shape[1],original_image.shape[2])
    # clustered_image = clustered_image.reshape(clustered_image.shape[0]*clustered_image.shape[1],clustered_image.shape[2])
    return (np.square(original_image - clustered_image)).mean()