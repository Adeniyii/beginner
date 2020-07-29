"""Intro to classes."""

class Song():

    def __init__(self, lyrics, composers):
        self.lyrics = lyrics
        self.composers = composers


    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        print("-"* 10)
        print(f"\tComposed by {self.composers}.")
        print("-"* 10)



    bread_n_butter = [
    """
    Bread and butter,
    baskelembe,
    ma boju mo,
    baskelembe.
    """
    ]




happy_bday = Song([
"""
    Happy birthday to you,
    I don't want to get sued,
    so i'll stop right here.
"""
], "Kendrick Lamar")

bulls_on_parade = Song([
"""
    They rally around the family,
    with pockets full of shells.
"""
], "Don Tolliver")

drizzy = Song([
"""
    Left foot up,
    right foot slide.
    Right foot up,
    left foot slide.
"""
], "Aubrey Graham")


for line in Song.bread_n_butter:
    print(line)


drizzy.sing_me_a_song()
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
