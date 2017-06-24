class Movie():
    """Initializing properties of a movie """
    def __init__(self, movie_title, movie_time,
                 movie_actors, movie_storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.mtime = movie_time
        self.actors = movie_actors
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
