import zmq
context = zmq.Context.instance()

sock = context.socket(zmq.REQ)
sock.bind('tcp://*:8080')

for i in xrange(1, 10000):
    sock.send("hello world :" + str(i))
    response = sock.recv()
    print("Response: " + str(response))
