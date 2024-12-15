import numpy as np
import pydicom
from pydicom.pixel_data_handlers.util import apply_voi_lut
import cv2
import matplotlib.pyplot as plt

def read_xray(path, voi_lut=True, fix_monochrome=True, apply_clahe=True, clipLimit=2.0, tileGridSize=(8, 8)):
    dicom = pydicom.read_file(path)

    # VOI LUT (if available by DICOM device) is used to transform raw DICOM data to "human-friendly" view
    if voi_lut:
        data = apply_voi_lut(dicom.pixel_array, dicom)
    else:
        data = dicom.pixel_array

    # depending on this value, X-ray may look inverted - fix that:
    if fix_monochrome and dicom.PhotometricInterpretation == "MONOCHROME1":
        data = np.amax(data) - data

    data = data - np.min(data)
    data = data / np.max(data)
    #     data = data.astype(np.float32)
    #     data = (data * 255.0).astype(np.float32) # no need for this I think

    if apply_clahe:
        data = apply_clahe_to_image(data, clipLimit=clipLimit, tileGridSize=tileGridSize)

    return data


def apply_clahe_to_image(image, clipLimit=2.0, tileGridSize=(8, 8)):
    # Convert image to uint16
    image = (image * 65535).astype(np.uint16)

    # Create a CLAHE object
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)

    # Apply CLAHE
    clahe_image = clahe.apply(image)

    # Convert image back to float32 in range [0, 1]
    clahe_image = clahe_image.astype(np.float32) / 65535.0

    return clahe_image

def plot_images(images, titles, rows, cols):
    fig, axes = plt.subplots(rows, cols, figsize=(9, 9))
    for i, (image, title) in enumerate(zip(images, titles)):
        ax = axes[i // cols, i % cols]
        ax.imshow(image, cmap='gray')
        ax.set_title(title)
        ax.axis('off')
    plt.show()

# path = 'src/Chest_Xray_Abnormality_Detection/data/raw/00087195a35bb9948323aa89ccb2a860.dicom'
# # path = '/kaggle/input/vinbigdata-chest-xray-abnormalities-detection/train/0007d316f756b3fa0baea2ff514ce945.dicom'
# # path = '/kaggle/input/vinbigdata-chest-xray-abnormalities-detection/train/003cfe5ce5c0ec5163138eb3b740e328.dicom'
# # path = '/kaggle/input/vinbigdata-chest-xray-abnormalities-detection/train/0076d6a1e3139927fd62459c54276c3c.dicom'
# # path = '/kaggle/input/vinbigdata-chest-xray-abnormalities-detection/train/0101ad90f31ddb8fb24e9935a3dac9db.dicom'
#
# clipLimits = [2.0, 3.0]
# tileGridSizes = [(6, 6), (8, 8)]
# images = []
# titles = []
#
# for clipLimit in clipLimits:
#     for tileSize in tileGridSizes:
#         images.append(read_xray(path, clipLimit=clipLimit, tileGridSize=tileSize))
#         titles.append(f"clipLimit={clipLimit}, tileGridSize={tileSize}")
#
# titles = [f"CL={clipLimit}, GS={tileSize}" for clipLimit in clipLimits for tileSize in tileGridSizes]
