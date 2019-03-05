import fresh_tomatoes
import media

# begin movie definitions here
matrix = media.Movie("The Matrix",
                     "Neo, searching to find out what \"the Matrix\" is," +
                     "searches for a man named Morpheus and falls down a " +
                     "dangerous rabbithole",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=vKQi3bBA1y8")

pacific_rim = media.Movie("Pacific Rim",
                          "When extra dimensional creatures known as Kaiju " +
                          "attack Earth, mankind builds the giant machines " +
                          "called Jaegers to fight them",
                          "https://upload.wikimedia.org/wikipedia/en/f/f3/Pacific_Rim_FilmPoster.jpeg",
                          "https://www.youtube.com/watch?v=5guMumPFBag")

alien = media.Movie("Alien (1979)",
                    "The crew of the mining ship Nostromo are awakened " +
                    "from cryo sleep to investigate a distress signal on" +
                    "an alien planet",
                    "https://upload.wikimedia.org/wikipedia/en/c/c3/Alien_movie_poster.jpg",
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

django = media.Movie("Django Unchained",
                     "Django, a runaway slave joins Dr. Schultz a German " +
                     "Civil War era bounty hunter, on a mission to hunt " +
                     "down wanted criminals",
                     "https://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                     "https://www.youtube.com/watch?v=eUdM9vrCbow")

the_prestige = media.Movie("The Prestige",
                           "Two rival magicians battling to create the " +
                           "ultimate illusion may inadvertently make the" +
                           "ultimate sacrifice.",
                           "https://upload.wikimedia.org/wikipedia/en/d/d2/Prestige_poster.jpg",
                           "https://www.youtube.com/watch?v=ObGVA1WOqyE")


ghost_in_the_shell = media.Movie("Ghost in the Shell (1995)",
                                 "Public security agent Motoko Kusinagi " +
                                 "hunts down the notorious super hacker " +
                                 "the Puppet Master.",
                                 "https://upload.wikimedia.org/wikipedia/en/c/ca/Ghostintheshellposter.jpg",
                                 "https://www.youtube.com/watch?v=p2MEaROKjaE")

# listify the movie instances for input into the page generation function
movies = [matrix, pacific_rim, alien, django, the_prestige, ghost_in_the_shell]

# generate the page
fresh_tomatoes.open_movies_page(movies)
