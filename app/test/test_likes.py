import unittest
from src.models import Like  # Replace 'your_module' with the actual module name

class TestLikeModel(unittest.TestCase):
    """
    Test cases for the Like model.
    """

    def test_like(self):
        """
        Test case for a'like'
        """
        like = Like(user_id=1, movieId=100, like_value=1)
        self.assertEqual(repr(like), "1 liked 100")

    def test_dislike(self):
        """
        Test case for 'dislike'.
        """
        like = Like(user_id=2, movieId=200, like_value=-1)
        self.assertEqual(repr(like), "2 disliked 200")

    def test_neutral(self):
        """
        Test case for 'neutral' entry.
        """
        like = Like(user_id=3, movieId=300, like_value=0)
        self.assertEqual(repr(like), "3 disliked 300")  

    def test_foreign_user_id(self):
        """
        Test case for foreign `user_id`.
        """
        like = Like(user_id=999, movieId=400, like_value=1)  
        self.assertEqual(like.user_id, 999)

    def test_foreign_movie_id(self):
        """
        Test case for ensuring foreign  `movieId`.
        """
        like = Like(user_id=4, movieId=888, like_value=-1)  
        self.assertEqual(like.movieId, 888)

    def test_string_like(self):
        """
        Test case for string representation of 'like'.
        """
        like = Like(user_id=10, movieId=120, like_value=1)
        self.assertEqual(repr(like), "10 liked 120")

    def test_string_dislike(self):
        """
        Test case for string representation of 'dislike'.
        """
        like = Like(user_id=15, movieId=125, like_value=-1)
        self.assertEqual(repr(like), "15 disliked 125")

    def test_string_neutral(self):
        """
        Test case for string representation of 'neutral'.
        """
        like = Like(user_id=20, movieId=130, like_value=0)
        self.assertEqual(repr(like), "20 disliked 130")  

    def test_multiple_likes(self):
        """
        Test case for a user liking multiple movies.
        """
        like1 = Like(user_id=5, movieId=201, like_value=1)
        like2 = Like(user_id=5, movieId=202, like_value=1)
        self.assertEqual(like1.user_id, like2.user_id)
        self.assertNotEqual(like1.movieId, like2.movieId)

    def test_multiple_users_same_movie(self):
        """
        Test case for multiple users liking the same movie.
        """
        like1 = Like(user_id=50, movieId=300, like_value=1)
        like2 = Like(user_id=51, movieId=300, like_value=-1)
        self.assertEqual(like1.movieId, like2.movieId)
        self.assertNotEqual(like1.user_id, like2.user_id)

    def test_unexpected_attribute_access(self):
        """
        Test case for accessing an attribute that does not exist.
        """
        like = Like(user_id=1, movieId=100, like_value=1)
        with self.assertRaises(AttributeError):
            _ = like.non_existent_attribute

    def test_mutability_of_instance(self):
        """
        Test case to ensure mutability of attributes is allowed, or behaves as expected.
        """
        like = Like(user_id=1, movieId=100, like_value=1)
        like.user_id = 2
        like.movieId = 200
        like.like_value = -1

        self.assertEqual(like.user_id, 2)
        self.assertEqual(like.movieId, 200)
        self.assertEqual(like.like_value, -1)

    def test_repr_method_edge_case(self):
        """
        Test case to verify the `repr` method handles unexpected modifications gracefully.
        """
        like = Like(user_id=1, movieId=100, like_value=1)

        like.like_value = "unexpected_value" 
        repr_output = repr(like)

        self.assertTrue(repr_output.startswith("1 "), "Repr output did not start with expected user_id")
        self.assertTrue(
            "100" in repr_output,
            "Repr output did not include the expected movieId even with unexpected like_value",
        )

    def test_large_user_id_and_movie_id(self):
        """
        Test case for very large values of `user_id` and `movieId`.
        """
        large_value = 2**31 - 1  
        like = Like(user_id=large_value, movieId=large_value, like_value=1)
        self.assertEqual(like.user_id, large_value)
        self.assertEqual(like.movieId, large_value)
        self.assertEqual(repr(like), f"{large_value} liked {large_value}")

    def test_empty_like_instance(self):
        """
        Test case for creating an empty Like instance without setting attributes.
        """
        like = Like()  
        self.assertIsNone(getattr(like, 'user_id', None))
        self.assertIsNone(getattr(like, 'movieId', None))
        self.assertIsNone(getattr(like, 'like_value', None))


    def test_switch_from_like_to_dislike(self):
        """
        Test case for a user switching from a like to a dislike for the same movie.
        """
        like = Like(user_id=1, movieId=100, like_value=1)
        like.like_value = -1  
        self.assertEqual(like.like_value, -1)
        self.assertEqual(repr(like), "1 disliked 100")

    def test_neutral_like_value(self):
        """
        Test case for a user setting a neutral `like_value` after initially liking or disliking.
        """
        like = Like(user_id=1, movieId=100, like_value=1)
        like.like_value = 0  
        self.assertEqual(like.like_value, 0)
        self.assertEqual(repr(like), "1 disliked 100")  

    def test_multiple_reactions_to_same_movie(self):
        """
        Test case for a user reacting multiple times to the same movie.
        """
        like1 = Like(user_id=1, movieId=100, like_value=1)
        like2 = Like(user_id=1, movieId=100, like_value=-1)
    
        self.assertEqual(like1.user_id, like2.user_id)
        self.assertEqual(like1.movieId, like2.movieId)
        self.assertNotEqual(like1.like_value, like2.like_value)
        self.assertEqual(repr(like1), "1 liked 100")
        self.assertEqual(repr(like2), "1 disliked 100")

    def test_invalid_reaction_sequence(self):
        """
        Test case for an invalid sequence of reactions.
        """
        like = Like(user_id=1, movieId=100, like_value=1)

        like.like_value = -999

        self.assertEqual(like.like_value, -999)
        repr_output = repr(like)
        self.assertEqual(repr_output, "1 disliked 100")

    def test_negative_user_id_and_movie_id(self):
        """
        Test case for negative values of `user_id` and `movieId`.
        """
        like = Like(user_id=-1, movieId=-100, like_value=1)
        self.assertEqual(like.user_id, -1)
        self.assertEqual(like.movieId, -100)
        self.assertEqual(repr(like), "-1 liked -100")

if __name__ == "__main__":
    unittest.main()
