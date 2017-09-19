import fresh_tomatoes
import media

Title=['Toy Story','Avatar','Mersal','Interstellar','Inception','X-men','Transformer']

StoryLine=["A Story of a boy and his toys that come to life",
           "A Story of space sip on another Planet",
           "A Story of Tamilan against Corprates.",
           "A stroy of Space exploration ",
           "A story of Dream ",
           "A story of Mutants",
           "A stroy of bots @ aliens"]

Piclink=["http://images5.fanpop.com/image/photos/30100000/Buzz-Lightyear-toy-story-2-30185761-1600-1200.jpg",
         "https://resizing.flixster.com/S5uksiCrVzEIio7HTEEX5Bem1rU=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDk5OzEyMDA7ODAwOzEyMDA",
         "img/vijay.jpg",
         "img/interstallar.jpg",
         "img/inception.jpg",
         "img/xmen.jpg",
         "img/transformers.jpg"]

Vdolink=["https://www.youtube.com/watch?v=KYz2wyBy3kc",
         "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
         "https://www.youtube.com/watch?v=3XmrZaVVUpc",
         "https://www.youtube.com/watch?v=zSWdZVtXT7E",
         "https://www.youtube.com/watch?v=8hP9D6kZseM",
         "https://www.youtube.com/watch?v=x_EZZrIErDI",
         "https://www.youtube.com/watch?v=6Vtf0MszgP8"]

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

interstellar=media.Movie(Title[3],
                        StoryLine[3],
                        Piclink[3],
                        Vdolink[3])

inception=media.Movie(Title[4],
                        StoryLine[4],
                        Piclink[4],
                        Vdolink[4])

xmen=media.Movie(Title[5],
                    StoryLine[5],
                    Piclink[5],
                    Vdolink[5])

transformer=media.Movie(Title[6],
                        StoryLine[6],
                        Piclink[6],
                        Vdolink[6])


movies=[toy_story,avatar,mersal,interstellar,inception,xmen,transformer]
fresh_tomatoes.open_movies_page(movies)
