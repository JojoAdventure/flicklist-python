import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles

        movlist = ('End of Evangelion', 'Akira', 'Lupin III: The Castle of Cagliostro', 'Jin-Roh', 'Ghost in the Shell')

        # TODO: randomly choose one of the movies, and return it

        return random.choice(movlist)

    def get(self):
        movie = self.getRandomMovie()
        tmovie = self.getRandomMovie()
        while movie == tmovie:
            tmovie = self.getRandomMovie()

        # build the response string
        response = "<h1>Movie of the Day</h1>"
        response += "<ul><li>" + movie + "</li></ul>"

        response += "<h2>Tomorrow's Movie</h2>"
        response += "<ul><li>" + tmovie + "</li></ul>"
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
