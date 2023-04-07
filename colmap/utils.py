import os

import numpy as np

def create_database(database_path):
    cmd = f"colmap database_creator --database_path {database_path}"
    os.system(cmd)

def feature_extraction(database_path, image_path, single_camera, camera_model):
    cmd = f"colmap feature_extractor \
            --database_path {database_path} \
            --image_path {image_path} \
            --ImageReader.single_camera {single_camera} \
            --ImageReader.camera_model {camera_model} \
            --SiftExtraction.use_gpu 0"
    os.system(cmd)

def feature_matching(database_path):
    cmd = f"colmap exhaustive_matcher --database_path {database_path} --SiftMatching.use_gpu 0"
    os.system(cmd)

def sparse_reconstruction(database_path, image_path, output_path):
    os.makedirs(output_path, exist_ok=True)
    cmd = f"colmap mapper \
            --database_path {database_path} \
            --image_path {image_path} \
            --output_path {output_path}"
    os.system(cmd)

def save_output_as_txt(input_path, output_path, output_type):
    os.makedirs(output_path, exist_ok=True)
    cmd = f"colmap model_converter \
            --input_path {input_path} \
            --output_path {output_path} \
            --output_type {output_type}"
    os.system(cmd)

def model_converter_to_ply(input_path, output_path, output_filename="points3D_undistort.ply"):
    output_file_path = os.path.join(output_path, output_filename)
    cmd = f"colmap model_converter \
            --input_path {input_path} \
            --output_path {output_file_path} \
            --output_type PLY"
    os.system(cmd)