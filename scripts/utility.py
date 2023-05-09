import cv2
import albumentations as Alb


def applyTransformation(augStyle, img, transformCount, file, dir_aug_out):
    # Performs transformation using albumentation library
    # Stores the transformed image to the respective output directory

    transform = Alb.Compose([eval(augStyle)])

    transformed = transform(image=img)
    transformed_image = transformed['image']

    newImageName = str(transformCount) + '_' + str(file)
    cv2.imwrite(dir_aug_out+'/'+newImageName, transformed_image)


def utility(operationName, img, transformCount, file, dir_aug_out, imageCount):
    # Performs crop, flips, resize, and gaussian blur

    def Crop_operation():
        # Ask for parameters and sends them to the augmentation script
        # x_min is the minimum x value
        # y_min is the maximum y value
        # x_max is the minimum x value
        # y_max is the maximum y value
        # p is the probability of applying the transform. Default: 1.

        print('Provide information about image: '+ str(file))
        print('Note the image size is: '+ str(img.shape))

        x_min = int(input("x_min: ") or '0')
        y_min = int(input("y_min: ") or '0')
        x_max = int(input("x_max: ") or str(img.shape[1]))
        y_max = int(input("y_max: ") or str(img.shape[0]))

        augStyle = "Alb.Crop(x_min=" + str(int(x_min)) + ', y_min=' + str(int(y_min)) + ', x_max=' + str(int(x_max)) + ', y_max='+ str(int(y_max)) + ", always_apply=False, p=1.0)"
        applyTransformation(augStyle, img, transformCount, file, dir_aug_out)

    def HorizontalFlip():
        # Dont require any parameters.
        # Performs horizontal flip

        augStyle = "Alb.HorizontalFlip()"
        applyTransformation(augStyle, img, transformCount, file, dir_aug_out)

    def VerticalFlip():
        # Dont require any parameters.
        # Performs vertical flip

        augStyle = "Alb.VerticalFlip()"
        applyTransformation(augStyle, img, transformCount, file, dir_aug_out)

    def Resize():
        # It resizes the image as per the required height and width.
        # requires desired height and width
        # interpolation flag that is used to specify the interpolation algorithm. 
        # Should be one of: cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4. Default: cv2.INTER_LINEAR.
        # p is the probability of applying the transform. Default: 1.

        print('Provide information about image: '+ str(file))
        print('Note the image size is: '+ str(img.shape))

        height = int(input("height: ") or str(img.shape[0]))
        width = int(input("width: ") or str(img.shape[1]))
        interpolation = int(input("interpolation: ") or '1')

        augStyle = "Alb.Resize(height=" + str(int(height)) + ", width=" + str(int(width)) + ", interpolation=" + str(int(interpolation)) + ", always_apply=True, p=1)"
        applyTransformation(augStyle, img, transformCount, file, dir_aug_out)

    def GaussianBlur():
        # This function performs gaussian blur; 
        # Blur the input image using a Gaussian filter with a random kernel size.
        # blur_limit: maximum Gaussian kernel size for blurring the input image. Must be zero or odd and in range [0, inf). 
        # If set to 0 it will be computed from sigma as round(sigma * (3 if img.dtype == np.uint8 else 4) * 2 + 1) + 1. 
        # If set single value blur_limit will be in range (0, blur_limit). Default: (3, 7).
        # sigma_limit is the Gaussian kernel standard deviation. Must be in range [0, inf). If set single value sigma_limit will be in range (0, sigma_limit). 
        # If set to 0 sigma will be computed as sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8. Default: 0.
        # p is the probability of applying the transform. Default: 0.5.

        print('Provide information about image: '+ str(file))
        print('Note: The blur limits must be odd')

        lowerLimit = int(input("lowerLimit: ") or '3')
        upperLimit = int(input("upperLimit: ") or '7')
        sigma_limit = int(input("sigma_limit: ") or '0')

        augStyle = "Alb.GaussianBlur(blur_limit=(" + str(int(lowerLimit)) + ", " + str(int(upperLimit)) + "), sigma_limit=" + str(int(sigma_limit)) + ", always_apply=True, p=1)"
        applyTransformation(augStyle, img, transformCount, file, dir_aug_out)

    def Normalization():
        # Normalization is applied by the formula: img = (img - mean * max_pixel_value) / (std * max_pixel_value)
        # Mean is the mean values, should be a list of floats.
        # std is the std values, should be a list of floats.
        # max_pixel_value is the maximum possible pixel value.

        print('Provide information about image: '+ str(file))
        print('Note the mean and standard daviation should be in between 0 to 1')

        mean = (float(input("Mean value for 1st channel: ") or '0.485'), float(input("Mean value for 2nd channel: ") or '0.456'), float(input("Mean value for 3rd channel: ") or '0.406'))
        std = (float(input("Std value for 1st channel: ") or '0.229'), float(input("Std value for 2nd channel: ") or '0.224'), float(input("Std value for 3rd channel: ") or '0.225'))
        max_pixel_value = float(input("max pixel value: ") or '255.0')

        augStyle = "Alb.Normalize(mean=" + str(mean) + ", std=" + str(std) + ", max_pixel_value =" + str(max_pixel_value) + " , always_apply=True, p=1.0)"
        applyTransformation(augStyle, img, transformCount, file, dir_aug_out)
        
    def operations():
        # This function performs the operations as per the requirements.
        # Append more conditions for increasing the operation range.
        # Currently is supports crop, flips, resize, gaussian blur, and normalization of the input images

        if operationName == 'Crop':
            print('----------------------------------------')
            Crop_operation()
        elif operationName == 'HorizontalFlip':
            HorizontalFlip()
        elif operationName == 'VerticalFlip':
            VerticalFlip()
        elif operationName == 'Resize':
            print('----------------------------------------')
            Resize()
        elif operationName == 'GaussianBlur':
            print('----------------------------------------')
            GaussianBlur()
        elif operationName == 'Normalization':
            print('----------------------------------------')
            Normalization()

    operations()


def readAndtransform(methodType, file, root, multipleOperations, augTransforms, dir_aug_out, imageCount, operationName):
    # This function reads the image using opencv.
    # Further checks is the image is not corrupt, and then performs the desired operation.
    # It filters the method as per the arguments provided by the user.
    
    if file.endswith('.png'): # Specify the image format
        if methodType == 'single_image':
            img = cv2.imread(str(root))
        else:
            img = cv2.imread(str(root) + '/' + str(file))

        if img is None: # Image is either corrupt or the path is wrong
            result = "Image " + str(file) + " is either corrupt; empty or the path is wrong"
            print(result)
        else:                
            transformCount = 0

            # If the augmentation is to be performed for multiple images using the same transformations specified in Augmentations text file
            if multipleOperations == True: 
                for line in augTransforms:
                    transformCount+=1
                    augStyle = "Alb." + str(line.strip()) # Read each line in text file
                    applyTransformation(augStyle, img, transformCount, file, dir_aug_out)
            else:
                # If the augmentation is to be performed for multiple images using the same transformation with specific parameters
                utility(operationName, img, transformCount, file, dir_aug_out, imageCount)
            imageCount += 1 
        # cv2.waitKey(0)
    return imageCount