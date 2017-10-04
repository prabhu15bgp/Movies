import fresh_tomatoes
import media
#List To store the data Contents 
title = [ 'Toy Story', 'Avatar', 'Mersal', 
		  'Interstellar', 'Inception', 'X-men', 'Transformer']

storyLine=["A Story of a boy and his toys that come to life",
           "A Story of space sip on another Planet",
           "A Story of Tamilan against Corprates.",
           "A stroy of Space exploration ",
           "A story of Dream ",
           "A story of Mutants",
           "A stroy of bots @ aliens"]

piclink=["http://images5.fanpop.com/image/photos/30100000/Buzz-Lightyear-toy-story-2-30185761-1600-1200.jpg", 
         "https://resizing.flixster.com/S5uksiCrVzEIio7HTEEX5Bem1rU=/206x305/v1.bTsxMTE3Njc5MjtqOzE3NDk5OzEyMDA7ODAwOzEyMDA", # NOQA 
         "img/vijay.jpg", 
         "img/interstellar.jpg", 
         "img/inception.jpg", 
         "img/xmen.jpg", 
         "img/transformer.jpg"]

vdolink=["https://www.youtube.com/watch?v=KYz2wyBy3kc", 
         "https://www.youtube.com/watch?v=cRdxXPV9GNQ", 
         "https://www.youtube.com/watch?v=3XmrZaVVUpc", 
         "https://www.youtube.com/watch?v=zSWdZVtXT7E", 
         "https://www.youtube.com/watch?v=8hP9D6kZseM", 
         "https://www.youtube.com/watch?v=x_EZZrIErDI", 
         "https://www.youtube.com/watch?v=6Vtf0MszgP8"]

toy_story=media.Movie(title[0], 
                      storyLine[0], 
                      piclink[0], 
                      vdolink[0] )

avatar=media.Movie( title[1], 
                    storyLine[1], 
                    piclink[1], 
                    vdolink[1]) 

mersal=media.Movie( title[2],
                    storyLine[2],
                    piclink[2],
                    vdolink[2])

interstellar=media.Movie(title[3],
                         storyLine[3],
                         piclink[3],
                         vdolink[3])

inception=media.Movie(title[4], 
                      storyLine[4],  
                      piclink[4], 
                      vdolink[4])

xmen=media.Movie(title[5],
                 storyLine[5],
                 piclink[5],
                 vdolink[5])

transformer=media.Movie(title[6],
                        storyLine[6],
                        piclink[6],
                        vdolink[6])


movies=[toy_story,avatar,mersal,interstellar,inception,xmen,transformer]
fresh_tomatoes.open_movies_page(movies)
