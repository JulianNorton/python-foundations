import fresh_tomatoes
import media

toy_story = media.Movie(
                        'toy story',
                        'Toys come to life',
                        'https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg',
                        'https://www.youtube.com/watch?v=KYz2wyBy3kc')


avatar = media.Movie(
                    'Avatar',
                    'A marine on an alien planet',
                    'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg',
                    'https://youtu.be/5PSNL1qE6VY?t=11s',
                    )

there_will_be_blood = media.Movie(
                    'There Will Be Blood',
                    'A sprawling epic of family, faith, power and oil',
                    'https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg',
                    'https://www.youtube.com/watch?v=WbRnuwjicUU',
                    )

movies = [toy_story, avatar, there_will_be_blood]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
