import numpy as np
from PIL import Image
import base64

def write_to_file(save_path, data):
  with open(save_path, "wb") as f:
    f.write(base64.b64decode(data))

def color_mask(array, r_lim, g_lim, b_lim):
    """
    array : m x n x 3 array of colors
    *_lim are 2-element tuples, where the first element is expected to be <= the second.
    """
    r_mask = ((array[..., 0] >= r_lim[0]) & (array[..., 0] <= r_lim[1]))
    g_mask = ((array[..., 1] >= g_lim[0]) & (array[..., 1] <= g_lim[1]))
    b_mask = ((array[..., 2] >= b_lim[0]) & (array[..., 2] <= b_lim[1]))
    return r_mask & g_mask & b_mask