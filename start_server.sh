#starts python server on localhost 8888
#!/bin/bash

# this starts a new instance of a local python server on the pwd
#python3 -m http.server 8888

#this starts a python server from the specified file
python3 server.py --dir public
