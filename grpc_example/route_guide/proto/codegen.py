# Run this scripts in project root path

from grpc_tools import protoc

protoc.main((
    '',
    '--proto_path=.',
    '--python_out=.',
    '--grpc_python_out=.',
    './grpc_example/route_guide/proto/route_guide.proto',
))
