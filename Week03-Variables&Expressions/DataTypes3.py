song4 = "150"
song5 = 250.25
# Ints adn strings cannot be added togehter directly
# so we need to convert one of them first 
# an string and a float cannot be added toether directly
# so we need to convert one of them first to avoid an error
playlist = str(song4) + (song5)
print(f"The playlist is {playlist} seconds.")