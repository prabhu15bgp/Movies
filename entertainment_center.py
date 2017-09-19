import fresh_tomatoes
import media
Title=['Toy Story','Avatar','Mersal','Interstellar','Inception','X-men','Transformer']
StoryLine=["A Story of a boy and his toys that come to life",
           "A Story of space sip on another Planet","A Story of Tamilan against Corprates."]
Piclink=["http://images5.fanpop.com/image/photos/30100000/Buzz-Lightyear-toy-story-2-30185761-1600-1200.jpg",
            "https://resizing.flixster.com/S5uksiCrVzEIio7HTEEX5Bem1rU=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDk5OzEyMDA7ODAwOzEyMDA",
            "img/vijay.jpg"]
Vdolink=["https://www.youtube.com/watch?v=KYz2wyBy3kc",
         "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
         "https://www.youtube.com/watch?v=3XmrZaVVUpc"]
toy_story=media.Movie(Title[0],
                      StoryLine[0],
                      Piclink[0],
                      Vdolink[0])
#print (toy_story.storyline)
avatar=media.Movie(Title[1],
                    StoryLine[1],
                    Piclink[1],
                    Vdolink[1])
#print (avatar.storyline)
mersal=media.Movie(Title[2],
                    StoryLine[2],
                    Piclink[2],
                    Vdolink[2])
#mersal.show_trailer()
movies=[toy_story,avatar,mersal]
fresh_tomatoes.open_movies_page(movies)
