def load_labeled_images_fpaths(dpath):
    """Loads (recursively) all images found under dpath.

    Assumes that each top level sub-directory contains images
    of one class.

    Returs a dictionary where the keys are the class names
    and the values are a list of image paths"""
    labeled_images_fpaths = {}
    for subpath in dpath.iterdir():
        if subpath.is_dir():
            classname =subpath.parts[-1]
            labeled_images_fpaths[classname] = []
    for classname in labeled_images_fpaths:
        classdpath = dpath / classname
        for fname in classdpath.iterdir():
            labeled_images_fpaths[classname].append(fname)
    return labeled_images_fpaths
