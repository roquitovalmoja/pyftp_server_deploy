# pyftp_server_deploy
For homelab deployment of FTP server

1. Create a folder in home directory pyftp_server
1. Create an .env file with the following variables:
    FTP_PORT=<port>
    FTP_USER=<username>
    FTP_PASSWORD=<password>
2. Open firewall port of server
3. Install Python interpreter, if you are using Linux, you probably already have it installed.
4. Create virtual environment (optional)
5. Refer to the requirements.txt for libraries to install
6. Navigate to src/. Initialization:
    python main.py "/home/<directory_name>"

