from model import KMeans
from utils import get_image, show_image, save_image, error,plot_MSE_graph


def main():
    # get image
    original_image = get_image('image.jpg')
    img_shape = original_image.shape

    # reshape image
    image = original_image.reshape(original_image.shape[0] * original_image.shape[1], original_image.shape[2])
    errors = dict()
    for k in [2,5,10,20,25,50,75,100]:
        # create model
        num_clusters = k # CHANGE THIS
        kmeans = KMeans(num_clusters)

        # fit model
        kmeans.fit(image)

        # replace each pixel with its closest cluster center
        generated_image = kmeans.replace_with_cluster_centers(image)

        # reshape image
        image_clustered = generated_image.reshape(img_shape)

        # Print the error
        errors[k] = error(original_image, image_clustered)
        print('MSE:', errors[k])
        
        # show/save image
        # show_image(image)
        save_image(image_clustered, f'image_clustered_{num_clusters}.jpg')

    plot_MSE_graph(errors)

if __name__ == '__main__':
    main()
