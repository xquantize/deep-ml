import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    try:
        img = np.array(image, dtype=float)
    except (ValueError, TypeError):
        return -1

    if img.ndim != 3 or img.shape[2] != 3 or img.shape[0] == 0 or img.shape[1] == 0:
        return -1

    if np.any(img < 0) or np.any(img > 255):
        return -1

    weights = np.array([0.299, 0.587, 0.114])
    gray = img @ weights

    return np.round(gray).astype(int).tolist()
