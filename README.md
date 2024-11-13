File Transfer with Socket
This project provides a simple file transfer mechanism using Python sockets. It includes two main scripts:

Sender: Sends a large file to the server in chunks.
Receiver: Receives the file on the server and reassembles it.
Requirements
Make sure Python is installed on both client and server machines. Install the required packages with:

bash
Copy code
pip install -r requirements.txt
The required packages are:

tqdm for progress display.
Setup and Usage
Step 1: Set up the Receiver on the Server
Edit the receiver.py script to set the correct SAVE_PATH, SERVER_IP, and SERVER_PORT values.

SAVE_PATH: Directory where the file will be saved.
SERVER_IP: Set to 0.0.0.0 to listen on all network interfaces.
SERVER_PORT: The port the server listens on.
Run the receiver script:

bash
Copy code
python receiver.py
The server is now ready to receive files.

Step 2: Configure and Run the Sender
Edit the sender.py script to set SERVER_IP, SERVER_PORT, and FILE_PATH values.

SERVER_IP: Server's IP address.
SERVER_PORT: The port the server listens on.
FILE_PATH: Path to the file you want to transfer.
Run the sender script:

bash
Copy code
python sender.py
The file will now be sent in chunks to the server.

Notes
Ensure that both client and server are on the same network or have internet access to each other.
Adjust the CHUNK_SIZE and NUM_THREADS in both scripts if necessary to optimize transfer speed.
