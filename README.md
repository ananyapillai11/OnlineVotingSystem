
Online Voting System
This Online Voting System is an interactive and secure application designed to facilitate voting through a client-server architecture. The project demonstrates the use of Python's socket programming for real-time communication and a graphical user interface (GUI) for seamless voter interaction. Below is a detailed description of the project:

Features
Server-Side Functionality:

Manages the voting process, tallying votes in real-time for parties like BJP, Congress, AAP, and NOTA.
Ends the voting session and determines the winner once the voting is concluded.
Supports multiple concurrent connections using Python's threading module.
Ensures proper communication with clients while preventing invalid votes.
Client-Side GUI:

Developed using Tkinter for an intuitive user experience.
Voters input personal details such as name, age, and address to ensure eligibility.
Buttons with candidate logos allow voters to cast their vote.
Real-time acknowledgment and updates on the voting status are displayed.
Prevents underage voting and invalid candidate selection.
Ends voting after a preset limit or when the voting session is manually terminated.
Visual Enhancements:

Background image and graphical elements enhance the voting interface.
Images of party logos are displayed alongside corresponding voting buttons for clarity.
Technical Highlights
Server-Side Implementation:

Python Socket Programming enables real-time communication between the server and multiple clients.
Multi-threading allows handling multiple client connections simultaneously.
Client-Side Implementation:

Tkinter is used for building the GUI.
Pillow (PIL) library enables image resizing and rendering of candidate logos.
Voting Mechanism:

Votes are securely transmitted to the server, which tallies them dynamically.
Voting can be terminated either after a specific number of votes or manually by the admin.
How It Works
Server:

Listens for incoming connections from clients (voters) on a specified port.
Validates votes, tallies results, and determines the winner when voting ends.
Displays voter details and vote count in real-time.
Client:

Displays a GUI for the voter to input their details and cast a vote.
Sends the voter's information and vote to the server.
Displays responses from the server, such as vote acknowledgment or voting closure notification.
Tech Stack
Programming Language: Python
Libraries:
socket (real-time server-client communication)
threading (multi-threading for concurrent connections)
tkinter (GUI development)
Pillow (image processing for candidate logos)
Steps to Run the System
Start the server:

Execute the server.py file to initialize the voting server.
The server listens for incoming connections and manages votes.
Start the client:

Execute the client.py file to open the GUI.
Input voter details and cast a vote.
Voting Flow:

Voters interact with the GUI to cast votes.
Votes are sent to the server for tallying.
Results are dynamically updated on the server side.
End Voting:

The admin or the system ends the voting session.
The server announces the winner based on the highest votes.
Future Improvements
Encrypt voter-server communication for enhanced security.
Add a database to store voter details and voting history.
Enable mobile-friendly GUI for wider accessibility.
Introduce additional security measures, such as voter ID verification.
