import socket # Used for creating socket connections
import threading # Used to handle multiple client connections concurrently
# thread - an entity within a process that can be scheduled for execution

# Dictionary to store the votes
votes = {
    'BJP': 0,
    'CONGRESS': 0,
    'AAP': 0,
    'NOTA':0
}

total_votes = 0  # Variable to track total votes received
voting_ended = False  # Flag to indicate if voting has ended

def handle_client(client_socket):
    global total_votes, voting_ended  # Access the global variables, can be accessed and modified anywhere in diff functions in the code

    # Receive the voter's details
    details = client_socket.recv(1024).decode().split(",")
    name, age, address = details

    # To print details in the client GUI
    if voting_ended: #True
        response = "Voting has ended. Your vote will not be counted."
    else:
        # Receive the voter's choice
        choice = client_socket.recv(1024).decode()

        if choice == 'end vote':
            voting_ended = True
            response = "Voting ended. Thank you for voting!"
            determine_winner()  # Calculate and print the winner immediately
        else:
            if choice in votes:
                votes[choice] += 1 # choice represents the party
                total_votes += 1
                response = f"Vote received for {choice}. Thank you for voting!"
            else:
                response = "Invalid candidate. Please choose from BJP, CONGRESS, AAP or NOTA."

    client_socket.send(response.encode())
    client_socket.close()

    # Print the voter's details on the server side if available
    if name and age and address:
        print("Vote received from:", name)
        print("Age:", age)
        print("Address:", address)
        print("Current Vote Tally:")
        print(votes)

# This function is responsible for starting the server and listening for incoming client connections.
def start_server():
    # 1 -  Specifies the address family for the socket (IPv4)
    # 2 -  Specifies the socket type or protocol (TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind(('0.0.0.0', 6666))  # Bind to all available network interfaces
    # server_socket - refers to the socket object that was created earlier using socket.socket() to represent the server's socket.
    # listen() - called on the server_socket object to enable it to accept incoming connections.
    server_socket.listen(5) # 5 specifies the max number of queued conn that the server can handle.
    print("Server started. Listening on port 6666...")

    while True:
        # accept() - called on server_socket to accept an incoming client conn
        # client_socket, addr - returned value from accept()
        # client_socket -  new socket object specific to the client connection
        # addr - contains client's address information
        
        # In summary, client_socket, addr = server_socket.accept() waits for an incoming client connection, 
        # accepts it when received, and assigns the client socket object and client address to the variables 'client_socket, 
        # and 'addr', respectively. This allows the server to establish communication with the client using the returned socket object.
        client_socket, addr = server_socket.accept()
        print("Connection established from:", addr)

        if voting_ended:
            response = "Voting has ended. Your vote will not be counted."
            client_socket.send(response.encode())
            client_socket.close()
        else:
            # used to start and create a new thread that will handle comm with a specific client
            
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            # creates a new Thread obj
            # target parameter specifies the func will be executed in new thread which in case is 'handle_client'
            # args parameter contains the arguments to be passed to the 'handle_client' function.  
            
            client_handler.start()
            # line starts execution of new thread by calling the 'start' method on 'client_handler' object
            # start method is called - new thread is spawned and the handle_client func is exe in that thread with the main thread
            

def determine_winner():
    max_votes = max(votes.values())
    winners = [candidate for candidate, vote_count in votes.items() if vote_count == max_votes]

    print("Voting has ended.")
    print("Total Votes:", total_votes)
    for candidate, vote_count in votes.items():
        print(f"{candidate}: {vote_count}")
    print("Winners:", ", ".join(winners))

start_server()
