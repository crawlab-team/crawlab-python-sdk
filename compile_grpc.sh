#!/bin/bash

# proto_path_root is the path to the directory containing the proto files
proto_path_root=${CRAWLAB_PROTO_PATH}

# check if proto_path_root is empty
if [ -z "$proto_path_root" ]; then
    echo "Please set the CRAWLAB_PROTO_PATH environment variable to the path containing the proto files."
    exit 1
fi

# check if proto_path_root exists
if [ ! -d "$proto_path_root" ]; then
    echo "The directory specified by CRAWLAB_PROTO_PATH does not exist."
    exit 1
fi

# output_path is the path to the directory where the generated Python code will be saved
output_path=./crawlab/grpc

# Remove the output directory if it exists
if [ -d ${output_path} ]; then
    rm -rf ${output_path}
fi

# Create the output directory
mkdir -p ${output_path}

# Generate the Python code from the proto files
python -m grpc_tools.protoc \
    -I ${proto_path_root} \
    --python_out=${output_path} \
    --grpc_python_out=${output_path} \
    ${proto_path_root}/**/*.proto

# Convert imports to absolute paths
sed -i 's/from \([a-zA-Z0-9_]*\) import \([a-zA-Z0-9_]*\)_pb2/from crawlab.grpc.\1 import \2_pb2/g' ${output_path}/**/*.py