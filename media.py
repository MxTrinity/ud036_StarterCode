import webbrowser

class Movie():
	#initialize the method's instance vars on construction
	def __init__(self, movie_title, movie_storyline, poster_image,
 			  trailer_youtube):
 		self.title = movie_title
 		self.storyline =  movie_storyline
 		self.poster_image_url = poster_image
 		self.trailer_youtube_url = trailer_youtube

	#just run the trailer specified during construction
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)