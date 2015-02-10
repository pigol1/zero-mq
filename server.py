import zmq

COUNT=0

context = zmq.Context.instance()

sock = context.socket(zmq.REP)
sock.connect('tcp://localhost:8080')

def handle_message(message):
    print(str(message))
    global COUNT
    COUNT = COUNT + 1
    return str(COUNT)

while True:
    message = sock.recv()
    response = handle_message(message)
    sock.send_string(response)


