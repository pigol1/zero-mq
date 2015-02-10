import zmq
context = zmq.Context.instance()

sock = context.socket(zmq.REP)
sock.connect('tcp://localhost:8080')

while True:
    message = sock.recv()
    response = handle_message(message)
    sock.send(response)



