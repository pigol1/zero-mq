import zmq
context = zmq.Context.instance()

sock = context.socket(zmq.REQ)
sock.bind('tcp://*:8080')

sock.send(message)
response = sock.recv()

