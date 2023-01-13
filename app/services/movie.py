from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self, filters):
        if "director_id" in filters:
            return self.dao.get_by_director(filters.get("director_id"))
        if "genre_id" in filters:
            return self.dao.get_by_genre(filters.get("genre_id"))
        if "year" in filters:
            return self.dao.get_by_year(filters.get("year"))
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid, data):
        movie = self.get_one(mid)
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")
        self.dao.update(movie)

    def delete(self, mid):
        self.dao.delete(mid)