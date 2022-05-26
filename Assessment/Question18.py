""" Define the Artist module in Artist.py with a constructor to initialize an artist's information. The constructor should by default initialize the artist's name to "None" and the years of birth and death to 0.

Define the Artwork module in Artwork.py with a constructor to initialize an artwork's information. The constructor should by default initialize the title to "None", the year created to 0, and the artist to use the Artist default constructor parameter values. Add an import statement to import the Artist module.

Add import statements to main.py to import the Artist and Artwork modules.

You may toggle between "main.py", "Artist.py", and "Artwork.py" by clicking the file name at the top of your coding module.

Ex: If the input is:

Pablo Picasso
1881
1973
Three Musicians
1921

the output is:

Artist: Pablo Picasso (1881-1973)
Title: Three Musicians, 1921

If the input is:

Brice Marden
1938
-1
Distant Muses 
2000

the output is:

Artist: Brice Marden, born 1938
Title: Distant Muses, 2000

 """
 # TODO: Import Artist from Artist.py and Artwork from Artwork.py

if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)
  
    new_artwork.print_info()