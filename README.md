# gRPC example in python

## gRPC = Google Remote Procedure Call

## Step for build and test project

#### Step 1: Install all requirements from requirements.txt files

#### Step 2: create proto file

```
    EX file location =  server/protos/users.proto
```

#### Step 3: Generate python Class and methods from proto file

```
    python -m grpc_tools.protoc -I<protos folder location> --python_out=. --pyi_out=. --grpc_python_out=. <protos file path>

    Ex command = python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/users.proto
```

#### Now communication between the microservices through gRPC protocol buffers

```
cd server
python app.py

cd client
python app.py
```
