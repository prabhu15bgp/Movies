import webbrowser
class Movie():
    """This class provides a way to store movie related informations"""
    #google style guide for python
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_video):
        #initializes or creats space in memory
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_video
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
        
    
