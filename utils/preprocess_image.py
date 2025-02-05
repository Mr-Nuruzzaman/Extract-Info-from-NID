import cv2


def preprocess_image(image_path):
    image = cv2.imread(image_path)

    # Apply Gaussian blur to reduce noise (mild)
    denoised = cv2.GaussianBlur(image, (5, 5), 0)

    processed_path = "processed_" + image_path
    cv2.imwrite(processed_path, denoised)

    return processed_path
