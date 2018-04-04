import media
import fresh_tomatoes

memoirs_story = media.Movie ("Memoirs of a geisha",
                             "In the 1920s, 9-year-old Chiyo gets sold to a geisha house. Beautiful and eager to please, yet too distant to really learn much from and ultimately little more than a beautiful, well-crafted object to be appreciated.",
                             "http://www.movieposter.com/posters/archive/main/91/MPW-45564",
                             "https://www.youtube.com/watch?v=4L-xlmakQvc",
                             "https://www.goodreads.com/book/show/929.Memoirs_of_a_Geisha")

omen_story = media.Movie ("The Omen",
                          "American diplomat Robert adopts Damien when his wife, Katherine , delivers a stillborn child. As more people around Damien die, Robert investigates Damien's background and realizes his adopted son may be the Antichrist.",
                          "https://ia.media-imdb.com/images/M/MV5BZmNjZDcwNTMtMjQxMy00ZTY5LTg4M2YtYjA5NDliNjNhYzQ3XkEyXkFqcGdeQXVyNjc1NTYyMjg@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=V7CEbd7ffNw",
                          "https://www.telegraph.co.uk/culture/film/filmreviews/11301178/the-omen-review.html")


movies = [memoirs_story, omen_story]

fresh_tomatoes.open_movies_page(movies)