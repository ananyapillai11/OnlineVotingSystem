# 🗳️ Online Voting System

The **Online Voting System** is an interactive and secure application designed to facilitate voting through a client-server architecture. This project uses Python's socket programming for real-time communication and a user-friendly GUI built with Tkinter for seamless voter interaction.

---

## 🎯 Features

### Server-Side Functionality
- **Real-Time Voting Management**: Tally votes dynamically for candidates such as BJP, Congress, AAP, and NOTA.
- **Concurrent Connections**: Handles multiple client connections using Python's threading module.
- **Vote Validation**: Ensures only valid votes are counted and prevents duplicate or invalid entries.
- **Voting Termination**: Ends the session and calculates the winner once voting concludes.

### Client-Side Functionality
- **Graphical User Interface (GUI)**:
  - Developed using Tkinter for intuitive user interaction.
  - Voters input their details (name, age, address) to validate eligibility.
  - Buttons with candidate logos allow voters to cast votes effortlessly.
- **Real-Time Updates**:
  - Displays voting status, errors, and acknowledgments in real-time.
  - Prevents underage voters from participating.
- **Termination Control**:
  - Voting ends after a preset limit or manual termination by the admin.

### Visual Enhancements
- Background image for a professional look.
- Party logos displayed alongside voting buttons for better user clarity.

---

## 🛠️ Tech Stack

- **Programming Language**: Python  
- **Libraries**:
  - `socket`: For real-time server-client communication.
  - `threading`: To handle multiple client connections concurrently.
  - `tkinter`: For building the GUI.
  - `Pillow (PIL)`: For processing and resizing candidate logos.

---

## 🚀 How It Works

### Server
1. Starts on a specified port and listens for incoming connections.
2. Validates and tallies votes in real-time.
3. Displays voter details and vote count dynamically.
4. Determines and announces the winner once voting concludes.

### Client
1. Provides a GUI for voters to:
   - Input personal details (name, age, address).
   - Cast their votes by selecting a candidate.
2. Sends voter details and selected vote to the server.
3. Receives real-time responses from the server, including acknowledgments or voting closure messages.

---

## 📋 Steps to Run the System

1. **Start the Server**:
   - Run the `server.py` file to initialize the voting server.
   - The server listens for connections and manages the voting process.

2. **Start the Client**:
   - Run the `client.py` file to launch the GUI.
   - Input voter details and cast your vote.

3. **Voting Flow**:
   - Voters interact with the GUI to submit their votes.
   - Votes are transmitted to the server for validation and counting.

4. **End Voting**:
   - The server concludes voting either automatically or manually by the admin.
   - The winner is announced based on the highest votes received.

---

## 📈 Future Enhancements
- **Enhanced Security**: Encrypt server-client communication.
- **Database Integration**: Store voter details and voting history securely.
- **Mobile-Friendly Interface**: Develop a responsive GUI for mobile devices.
- **Advanced Verification**: Implement voter ID validation for added security.

---

## 🏗️ Project Structure

