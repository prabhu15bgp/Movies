import fresh_tomatoes
import media

toy_story=media.Movie("Toy Story",
                      "A Story of a boy and his toys that come to life",
                      "http://images5.fanpop.com/image/photos/30100000/Buzz-Lightyear-toy-story-2-30185761-1600-1200.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)
avatar=media.Movie("Avatar",
                    "A Story of space sip on another Planet",
                    "https://resizing.flixster.com/S5uksiCrVzEIio7HTEEX5Bem1rU=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDk5OzEyMDA7ODAwOzEyMDA",
                    "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print (avatar.storyline)
mersal=media.Movie("Mersal",
                    "A Story of Tamilan",
                    "http://img.nowrunning.com/content/movie/2017/vijay-19797/stills/Mersal-movie-02.jpg",
                    "https://www.youtube.com/watch?v=3XmrZaVVUpc")
#mersal.show_trailer()
movies=[toy_story,avatar,mersal]
fresh_tomatoes.open_movies_page(movies)
