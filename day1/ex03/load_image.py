from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """loads an image, prints its format, and its pixels\
        content in RGB format."""
    try:
        if not isinstance(path, str):
            raise TypeError("Path must be a string")

        img = Image.open(path)

        if img.format not in ("JPEG", "JPG"):
            raise ValueError("Unsupported image format")

        img = img.convert("RGB")
        pixels = np.array(img)

        print(f"The shape of image is: {pixels.shape}")
        return pixels

    except FileNotFoundError:
        print("Error: file not found")
    except PermissionError:
        print("Error: permission denied")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
