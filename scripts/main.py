import os
import argparse
from utility import readAndtransform

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Augmentation Operations')
    subparser = parser.add_subparsers(dest='command')

    multiple_operation = subparser.add_parser('multiple_operation')
    single_operation = subparser.add_parser('single_operation')
    single_image = subparser.add_parser('single_image')

    multiple_operation.add_argument("--augmentation_file_path", help="Path to a file containing a list of albumentation augmmentations.", type=str)
    multiple_operation.add_argument("--image_root_dir", help="Path to the directory containing the images.", type=str)
    multiple_operation.add_argument("--dir_out", help="Path to a folder to save the augmented images.", type=str)

    single_operation.add_argument("--image_root_dir", help="Path to the directory containing the images.", type=str)
    single_operation.add_argument('--operation', choices=['Crop', 'HorizontalFlip', 'VerticalFlip', 'Resize', 'GaussianBlur', 'Normalization'])
    single_operation.add_argument("--dir_out", help="Path to a folder to save the augmented images.", type=str)

    single_image.add_argument("--image_path", help="Direct path to the images.", type=str)
    single_image.add_argument('--operation', choices=['Crop', 'HorizontalFlip', 'VerticalFlip', 'Resize', 'GaussianBlur', 'Normalization'])
    single_image.add_argument("--dir_out", help="Path to a folder to save the augmented images.", type=str)

    args = parser.parse_args()

    dir_out = args.dir_out + '/'
    imageCount = 0

    # Check is the output directory already exists
    if not os.path.exists(dir_out):
        os.mkdir(dir_out)
    
    if args.command == 'multiple_operation': 
        # If the augmentation is to be performed for multiple images using the same transformations specified in Augmentations text file
        multipleOperations = True
        operationName = 'All'
        dir_src = args.image_root_dir

        augmentation_file_path = args.augmentation_file_path
        augFile = open(augmentation_file_path, 'r')
        augTransforms = augFile.readlines()

    elif args.command == 'single_operation':
        # If the augmentation is to be performed for multiple images using the same transformation with specific parameters
        multipleOperations = False
        augTransforms = ''
        operationName = args.operation
        dir_src = args.image_root_dir

    elif args.command == 'single_image':
        # If the augmentation is to be performed for multiple images using the same transformation with specific parameters
        multipleOperations = False
        augTransforms = ''
        operationName = args.operation
        dir_aug_out = dir_out
        root = args.image_path
        file = str(root.rsplit('/', 1)[-1])

        imageCount = readAndtransform(args.command, file, root, multipleOperations, augTransforms, dir_aug_out, imageCount, operationName)
    
    if args.command != 'single_image':
        # Go through each directory and get images
        for root, _, files in os.walk(dir_src):

            # Setup folders as per the dataset folder structure
            if len(root.split("/")) > 3: # Change this number as per the directory structure
                dir_aug_out = dir_out + str(root.rsplit('/', 1)[-1])
                if not os.path.exists(dir_aug_out):
                    os.mkdir(dir_aug_out)

            for file in files:
                imageCount = readAndtransform(args.command, file, root, multipleOperations, augTransforms, dir_aug_out, imageCount, operationName)

    # cv2.destroyAllWindows()
    print('Execution ends!')
    print('Results are saved in the output directory specified in the arguments!')