import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that comes to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://avatarblog.typepad.com/.a/6a0120a6b2c140970c012876c79e1a970c-800wi",
                        "https://www.youtube.com/watch?v=_i2RCBa3l-g")

#print (avatar.storyline)
#avatar.show_trailer()

transformers = media.Movie("Transformers",
                        "A alien transforms into automotives",
                        "http://cdn.collider.com/wp-content/uploads/T3-IMAX-One-Sheet-FINAL.jpg",
                        "https://www.youtube.com/watch?v=ejxQOv53lXs")

#transformers.show_trailer()

movies = [toy_story, avatar, transformers]
fresh_tomatoes.open_movies_page(movies)
