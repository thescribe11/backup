import numpy as np
import cv2

def shift_image(img, dx, dy):

    img = np.roll(img, dy, axis=0)

    img = np.roll(img, dx, axis=1)

    if dy>0:

        img[:dy, :] = 0

    elif dy<0:

        img[dy:, :] = 0

    if dx>0:

        img[:, :dx] = 0

    elif dx<0:

        img[:, dx:] = 0

    return img

import random

def hologram_effect(img):

    # add a blue tint

    holo = cv2.applyColorMap(img, cv2.COLORMAP_WINTER)

    # add a halftone effect

    bandLength, bandGap = 2, 3

    for y in range(holo.shape[0]):

        if y % (bandLength+bandGap) < bandLength:

            holo[y,:,:] = holo[y,:,:] * np.random.uniform(0.1, 0.3)

    # add some ghosting

    holo_blur = cv2.addWeighted(holo, 0.2, shift_image(holo.copy(), 5, 5), 0.8, 0)

    holo_blur = cv2.addWeighted(holo_blur, 0.4, shift_image(holo.copy(), -5, -5), 0.6, 0)

    # combine with the original color, oversaturated

    out = cv2.addWeighted(img, 0.5, holo_blur, 0.6, 0)

    return out


def get_frame(cap, background_scaled):

    _, frame = cap.read()

    # fetch the mask with retries (the app needs to warmup and we're lazy)

    # e v e n t u a l l y c o n s i s t e n t

    
    frame = hologram_effect(frame)

    return frame