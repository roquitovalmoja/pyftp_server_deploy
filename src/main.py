from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from dotenv import load_dotenv
import os
import argparse
import logging

load_dotenv()

# use argparse to get input for the directory to serve
parser = argparse.ArgumentParser(description='Serve a directory over FTP')
parser.add_argument('directory', type=str, help='The directory to serve')
args = parser.parse_args()
print(args.directory)

def main():
    # create a new authorizer
    authorizer = DummyAuthorizer()

    # add a user
    authorizer.add_user(os.getenv('FTP_USER'), os.getenv('FTP_PASSWORD'), args.directory, perm='elradfmwMT')

    # add anonymous user with read-only permissions
    authorizer.add_anonymous(os.getcwd())

    # create a handler object
    handler = FTPHandler
    handler.authorizer = authorizer

    # logging
    logging.basicConfig(filename='var/log/pyftp.log', level=logging.INFO) # change to DEBUG for verbose logging i.e. socket connections

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for passive connections.
    # Decomment in case you're behind a NAT.
    # handler.masquerade_address = os.getenv('FTP_MASQUERADE_ADDRESS')
    # handler.passive_ports = range(60000, 65535)

    # create a new server
    server = FTPServer("127.0.0.1", int(os.getenv('FTP_PORT')), handler)
    
    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5
    
    server.serve_forever()

if __name__ == "__main__":
    # main()
    pass
