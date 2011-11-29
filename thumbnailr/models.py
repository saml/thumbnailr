import os

from thumbnailr.settings import IMG_DIR, PREFIX_ORIGINAL



class ImagePath(object):
    def __init__(self, img_path,
            img_dir=IMG_DIR,
            prefix_original=PREFIX_ORIGINAL):
        '''image path.

        >>> img = ImagePath('foo/bar.jpg', img_dir='/tmp/imgs', prefix_original='original')
        >>> img.ext == '.jpg'
        True
        >>> img.path == '/tmp/imgs/foo/bar.jpg'
        True
        >>> img.original == '/tmp/imgs/foo/bar.jpg/original.jpg'
        True
        '''

        _,self.ext = os.path.splitext(img_path)
        self.path = os.path.join(img_dir, img_path)
        self.original = os.path.join(self.path, prefix_original + self.ext)

def crop_info(width, height, target_width, target_height):
    'given original dimension and target dimension, returns crop (x, y, crop width, crop height)'

    if target_width is None or target_height is None:
        #don't crop
        return (0, 0, width, height)

    #try to fit width
    w = width
    h = w * target_height / target_width
    if h <= height:
        return (0, (height - h) / 2, w, h)

    #try to fit height
    h = height
    w = h * target_width / target_height
    if w <= width:
        return ((width - w) /  2, 0, w, h)
