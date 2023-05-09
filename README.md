# Augmentation

Introduction:

    The repository provides preprocessing operations for input images through 3 methodologies, 
    expanding the augmentation strategies, including cropping, resizing, blurring, flipping, and normalization.
    The available methodologies are:
        1. multiple_operation: performs a set of operations on multiple images in a directory. (Recommended)
        2. single_operation: implements a specific transformation on multiple images in the directory with user-specified parameters.
        3. single_image: applies a single operation on a single image with user-specified parameters.

    File structure is as follows:
        scripts/main.py: contains main function which utilizes utility.py for operations.
        scripts/utility.py: file contains all required functions and operations.
        scripts/Augmentations: A text file containing a list of operations as per the albumentation library.
        sampled_results: folder presented the sampled transformed images.
        coding_task: Dataset folder provided by Finnos.
        
    Why Albumentation?

    Albumentations is an image augmentation library for deep learning that offers a diverse range of transformations for computer vision tasks. 
    It provides over 70 augmentations, making the most number of operations supported by any pipeline, that can be combined to create custom pipelines, 
    allowing data scientists to generate new variations of their input images to improve model performance.

    6 big libraries merged together to provide a vast range of transformations within one library named albumentations.

    One of the main advantages of Albumentations over other preprocessing libraries and tools is its speed. 
    It's optimized for high-performance and can process large datasets quickly, making it an ideal choice for machine learning pipelines. 
    Additionally, Albumentations is designed to work seamlessly with PyTorch and TensorFlow.

    Refer the link to check the quantity of transformation albumentation offers: https://albumentations.ai/docs/getting_started/transforms_and_targets/

Methodologies:

    1. multiple_operation :

        Arguments:
            --augmentation_file_path : Path to a file containing a list of albumentation transformations.
            --image_root_dir : Path to the directory containing the images.
            --dir_out : Path to a folder to save the augmented images.

        The preprocessing steps are defined using a text file that follows the structure of the transformations in the Albumentation library. 
        The script reads each line of the text file and applies the specified operations to all images in the input root directory. 
        The resulting transformed images are then saved in the specified output folder while maintaining the same folder structure.

        Advantages:
            1. The flexibility of defining the operations in a text file allows for easy customization and modification of the preprocessing pipeline.
            2. This approach offers a streamlined and scalable solution for applying multiple preprocessing operations to a large dataset of images.
            3. Very less code as we dont need to specify each transformation within code.
            4. Could be utilized for domain specific applications.
            5. User could also change the parameters, however, make sure that you follow albumentation transformation requirements.

    2. single_operation :

        Arguments:
            --image_root_dir : Path to the directory containing the images.
            --operation : choices=['Crop', 'HorizontalFlip', 'VerticalFlip', 'Resize', 'GaussianBlur', 'Normalization']
            --dir_out : Path to a folder to save the augmented images.

        The script performs a specified operation on all images in the directory, with specific inputs required for each image. 
        Users can choose to either provide their own input parameters or use default values by simply pressing enter.

        Advantages:
            1. Could be utilized if multiple images requires same operation with different parameters.
            2. User dont need to know the albumentation specific requirements for transformations.

    3. single_image

        Arguments:
            --image_path : Direct path to the images
            --operation : choices=['Crop', 'HorizontalFlip', 'VerticalFlip', 'Resize', 'GaussianBlur', 'Normalization']
            --dir_out : Path to a folder to save the augmented images.

        The script performs a user-specified operation on a single image at a time and prompts for specific inputs required for the operation. 
        If no parameters are provided, default values are used.

        Advantages:
            1. Could be used if a single image need to be tested for preprocessing within a large database.
            2. Could be used for demo purposes.

    Note: image20230123_103711_192330_Main_CCam2.png in 192330 is unreadable, thus a check is written in script to ignore it.

Dependencies:
    Python v3+
    OpenCV
    Albumentations
    argparse

Example CLI for each methodology:
    Basic commands:
        cd Assignment_Gaurang/scripts

    1. multiple_operation : (Recommended)
        python3 main.py multiple_operation --image_root ../coding_task/data --dir_out ../coding_task/output --augmentation_file_path Augmentations

    2. single_operation : 
        python3 main.py single_operation --image_root ../coding_task/data --dir_out ../coding_task/output --operation HorizontalFlip
    
    3. single_image : 
        python3 main.py single_image --image_path ../coding_task/data/192086/image20230123_102027_192086_Main_CCam1.png --dir_out ../coding_task/output --operation Crop

Multi-annotation transformations are possible with albumentation library.
For implementation please fork my github:
https://github.com/GaurangSharma18/Detection-Segmentation-and-Feature-estimation-pipeline.git

Two visualize results of the multi-annotation pipeline, please check my published dataset:
https://zenodo.org/record/7669593#.ZFPRRtJBxH4


A conference paper is submited addressing the novelty in multi-label pipeline, will share soon once it gets published.
