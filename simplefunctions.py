# Write a function sum_numbers(n) that takes a positive integer n and returns the sum 
# of all numbers from 1 to n using a for loop.

# def sum_numbers(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total


# print(sum_numbers(5))  

# Write a function count_vowels(text) that takes a string and returns the number of vowels 
# in the string using a for loop.

# def count_vowels(text):
#     count = 0
#     vowels = "aeiouAEIOU"
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count


# print(count_vowels("Hello World")) 

# Write a function multiplication_table(n) that takes a positive integer n 
# and prints the multiplication table for n up to 10 using a for loop.

# def multiplication_table(n):
#     for i in range(1, 11):
#         print(f'{i} x {n} = {i*n}')
#         # print(i*n)


# multiplication_table(5)


# Write a function reverse_string(text) that takes a string and returns it reversed using a for loop.


# def reverse_string(text):
#     reversed_text = ""
#     for char in text:
#         reversed_text = char + reversed_text
#     return reversed_text


# print(reverse_string("Hello"))  

# Write a function count_words(sentence) that takes a string and 
# returns the number of words in the sentence using a for loop.

# def count_words(sentence):
#     words = sentence.split()
#     count = 0
#     for word in words:
#         count += 1
#     return count


# print(count_words("This is a simple sentence."))  



# Detailed Question for the Music Playlist Management Code:
# Scenario: You are tasked with creating a simple command-line program to manage a digital music playlist. The program should allow users to perform the following operations:

# Add a Song: Users should be able to add a new song to the playlist.
# Play a Song: Users should be able to "play" (i.e., select and view) a song from the playlist.
# Remove a Song: Users should be able to remove a song from the playlist.
# Show Playlist: Users should be able to view the current list of songs in the playlist.
# Exit: Users should be able to exit the program.
def add_song(song_name):
    """Add a song to the playlist."""
    playlist.append(song_name)
    print(f'Song "{song_name}" has been added to the playlist.')

def play_song(song_name):
    """Play a song from the playlist."""
    if song_name in playlist:
        print(f'Now playing: "{song_name}".')
    else:
        print(f'Sorry, "{song_name}" is not in the playlist.')

def remove_song(song_name):
    """Remove a song from the playlist."""
    if song_name in playlist:
        playlist.remove(song_name)
        print(f'Song "{song_name}" has been removed from the playlist.')
    else:
        print(f'Song "{song_name}" is not in the playlist.')

def show_playlist():
    """Display the list of songs in the playlist."""
    if playlist:
        print("Songs in your playlist:")
        for song in playlist:
            print(f"- {song}")
    else:
        print("Your playlist is empty.")

# Main program loop
playlist = []

while True:
    user_input = input("\nChoose an option: \n1. Add a Song \n2. Play a Song \n3. Remove a Song \n4. Show Playlist \n5. Exit\n")

    if user_input == '1':
        song = input("Enter the name of the song to add: ")
        add_song(song)

    elif user_input == '2':
        song = input("Enter the name of the song to play: ")
        play_song(song)

    elif user_input == '3':
        song = input("Enter the name of the song to remove: ")
        remove_song(song)

    elif user_input == '4':
        show_playlist()

    elif user_input == '5':
        print("Exiting the playlist manager. Enjoy your music!")
        break

    else:
        print("Invalid option. Please try again.")


