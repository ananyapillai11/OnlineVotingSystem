import tkinter as tk
import socket
import threading
from PIL import Image, ImageTk

####################################################################


SERVER_IP = socket.gethostname()#'192.168.62.34'
port = 6666

total_votes = 0  # Variable to track the total number of votes
voting_ended = False  # Flag to track if voting has ended

def vote(choice):
    global total_votes

    if voting_ended:
        result_label.configure(text="Voting has ended. Your vote will not be counted.")
        return

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_IP, port))

        # Send the voter's details to the server
        details = f"{name_entry.get()},{age_entry.get()},{address_entry.get()}"
        client_socket.send(details.encode())

        # Send the voter's choice to the server
        client_socket.send(choice.encode())

        # Receive acknowledgment from the server
        response = client_socket.recv(1024).decode()
        print(response)

        total_votes += 1  # Increment the total votes

        if total_votes >= 10:
            end_voting()  # Terminate the program if 10 votes have been received

        # Clear input fields for the next voter
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.configure(state=tk.NORMAL)  # Enable the name entry field
        age_entry.configure(state=tk.NORMAL)   # Enable the age entry field
        address_entry.configure(state=tk.NORMAL)  # Enable the address entry field

    except ConnectionResetError:
        result_label.configure(text="Connection lost. Please try again later.")

    except socket.timeout:
        result_label.configure(text="Connection timed out. Please try again later.")

    finally:
        client_socket.close()

def cast_vote(candidate):
    if not voting_ended:
        # Create a new thread for voting
        vote_thread = threading.Thread(target=vote, args=(candidate,))
        vote_thread.start()
        result_label.configure(text="Vote cast for " + candidate)

def validate_and_start_gui():
    global voting_ended

    # Get the voter's details
    name = name_entry.get()
    age = age_entry.get()
    address = address_entry.get()

    if int(age) < 18:
        result_label.configure(text="Sorry, you are not eligible to vote.")
    else:
        voting_ended = False
        start_button.configure(state=tk.DISABLED)
        cast_vote_frame.pack(pady=20)

def end_voting():
    global voting_ended
    cast_vote('end vote')
    voting_ended = True
    start_button.configure(state=tk.NORMAL)
    cast_vote_frame.pack_forget()

# Create the main window
window = tk.Tk()
window.title("Online Voting System")
window.state('zoomed')  # Maximize the window

# Set the background image
bg_image = tk.PhotoImage(file="download.png")
background_label = tk.Label(window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Configure font settings
font_style = ("Arial", 12, "bold")
heading_font_style = ("Arial", 16, "bold")

# Create a bold heading
heading_label = tk.Label(window, text="ONLINE VOTING SYSTEM", font=heading_font_style)
heading_label.pack(pady=10)

# Create voter details input fields
details_frame = tk.Frame(window)
details_frame.pack(pady=20)

name_label = tk.Label(details_frame, text="Name:", font=font_style)
name_label.grid(row=0, column=0)
name_entry = tk.Entry(details_frame, font=font_style)
name_entry.grid(row=0, column=1)

age_label = tk.Label(details_frame, text="Age:", font=font_style)
age_label.grid(row=1, column=0)
age_entry = tk.Entry(details_frame, font=font_style)
age_entry.grid(row=1, column=1)

address_label = tk.Label(details_frame, text="Address:", font=font_style)
address_label.grid(row=2, column=0)
address_entry = tk.Entry(details_frame, font=font_style)
address_entry.grid(row=2, column=1)

start_button = tk.Button(details_frame, text="Start Voting", command=validate_and_start_gui, bg="light green", fg="white", font=font_style)
start_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create candidate selection buttons
cast_vote_frame = tk.Frame(window)

# Set the BJP button
btn_candidate_a = tk.Button(cast_vote_frame, text="BJP", command=lambda: cast_vote("BJP"), bg="orange", fg="white", font=font_style)
btn_candidate_a.grid(row=0, column=0, padx=10)

bjp_image = Image.open("bjp.png")
bjp_image = bjp_image.resize((60, 60), Image.LANCZOS)  # Resize the image while maintaining aspect ratio
bjp_photo = ImageTk.PhotoImage(bjp_image)
bjp_label = tk.Label(window, image=bjp_photo)
bjp_label.place(relx=0.37, rely=0.7)  # Adjust the values of relx and rely to position the image
btn_candidate_a.image = bjp_photo  # Store a reference to the image to prevent garbage collection


# Set the CONGRESS button
btn_candidate_b = tk.Button(cast_vote_frame, text="CONGRESS", command=lambda: cast_vote("CONGRESS"), bg="blue", fg="white", font=font_style)
btn_candidate_b.grid(row=0, column=1, padx=10)

congress_image = Image.open("congress.png")
congress_image = congress_image.resize((60, 60), Image.LANCZOS)  # Resize the image while maintaining aspect ratio
congress_photo = ImageTk.PhotoImage(congress_image)
congress_label = tk.Label(window, image=congress_photo)
congress_label.place(relx=0.44, rely=0.7)  # Adjust
btn_candidate_b.image = congress_photo  # Store a reference to the image to prevent garbage collection


# Set the AAP button
btn_candidate_c = tk.Button(cast_vote_frame, text="AAP", command=lambda: cast_vote("AAP"), bg="green", fg="white", font=font_style)
btn_candidate_c.grid(row=0, column=2, padx=10)

aap_image = Image.open("aap.jpeg")
aap_image = aap_image.resize((60, 60), Image.LANCZOS)  # Resize the image while maintaining aspect ratio
aap_photo = ImageTk.PhotoImage(aap_image)
aap_label = tk.Label(window, image=aap_photo)
aap_label.place(relx=0.51, rely=0.7)  # Adjust the values of relx and rely to position the image
btn_candidate_c.image = aap_photo  # Store a reference to the image to prevent garbage collection


# Set the NOTA button
btn_candidate_d = tk.Button(cast_vote_frame, text="NOTA", command=lambda: cast_vote("NOTA"), bg="black", fg="white", font=font_style)
btn_candidate_d.grid(row=0, column=3, padx=10)

nota_image = Image.open("nota.jpeg")
nota_image = nota_image.resize((60, 60), Image.LANCZOS)  # Resize the image while maintaining aspect ratio
nota_photo = ImageTk.PhotoImage(nota_image)
nota_label = tk.Label(window, image=nota_photo)
nota_label.place(relx=0.58, rely=0.7)  # Adjust the values of relx and rely to position the image
btn_candidate_d.image = nota_photo  # Store a reference to the image to prevent garbage collection


# Create label for displaying result
result_label = tk.Label(window, text="", font=font_style, fg="blue")
result_label.pack(pady=10)

# Create button to end voting
end_voting_button = tk.Button(window, text="End Voting", command=end_voting, bg="red", fg="white", font=font_style)
end_voting_button.pack(pady=10)

# Create a footer label
footer_label_text = "Online Voting System - Developed by Ananya, Vishwa, Suba, and Akshit"
footer_label = tk.Label(window, text=footer_label_text, font=("Arial", 8), fg="gray")
footer_label.pack(side=tk.BOTTOM, pady=5)

# Set focus to the name entry field at startup
name_entry.focus()

# Start the GUI event loop
window.mainloop()
