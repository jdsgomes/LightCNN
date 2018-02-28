import os
import argparse
from pathlib import Path
import dlib
from imutils import face_utils
from scipy.misc import imread, imsave
from aux import load_labeled_images_fpaths

parser = argparse.ArgumentParser(description='Dlib Face Detection')
parser.add_argument('--input_path', default='', type=str, metavar='PATH',
                    help='root path of face images (default: none).')
parser.add_argument('--save_path', default='', type=str, metavar='PATH',
                    help='save root path for features of face images.')


def main():
    global args
    args = parser.parse_args()
    input_dpath = Path(args.input_path)
    output_dpath = Path(args.save_path)
    labeled_images_fpaths = load_labeled_images_fpaths(input_dpath)
    face_detector = dlib.get_frontal_face_detector()
    for classname, imfpaths in labeled_images_fpaths.items():
        face_counter = 0
        class_outpath = output_dpath / classname
        class_outpath.mkdir(exist_ok=True)
        for imagefpath in imfpaths:
            image = imread(imagefpath, mode='L')
            im_h, im_w = image.shape[:2]
            rects = face_detector(image, 1)
            for rect in rects:
                (x, y, w, h) = face_utils.rect_to_bb(rect)
                x_start = max(0, x)
                x_end = min(w, x+im_w)
                y_start = max(0, y)
                y_end = min(h, y+im_h)
                face_image = image[y_start:y_end, x_start:x_end]
                if face_image.shape[0] != 0 and face_image.shape[1] != 0:
                    fname = '%d.png' % face_counter
                    save_path = class_outpath / fname
                    print(save_path)
                    print(face_image.shape)
                    imsave(save_path, face_image)
                    face_counter += 1


if __name__ == '__main__':
    main()
