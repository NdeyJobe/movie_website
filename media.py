import webbrowser

class Movie () :

    """ This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, movie_reviews):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.reviews_url = movie_reviews

    def show_trailer (self) :
        webbrowser.open(self.trailer_youtube_url)

    def show_reviews(self):
        webbrowser.open(self.reviews_url)
