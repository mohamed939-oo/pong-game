import unittest
from unittest.mock import patch
from io import StringIO
import pong_game  

class TestPongGame(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout):
        pong_game.main()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('turtle.Turtle.ycor')
    def test_left_paddle_up(self, mock_ycor):
        mock_ycor.return_value = 0
        pong_game.leftpaddleup()
        self.assertEqual(pong_game.leftpaddle.ycor(), 20)

    @patch('turtle.Turtle.ycor')
    def test_left_paddle_down(self, mock_ycor):
        mock_ycor.return_value = 0
        pong_game.leftpaddledown()
        self.assertEqual(pong_game.leftpaddle.ycor(), -20)

    @patch('turtle.Turtle.ycor')
    def test_right_paddle_up(self, mock_ycor):
        mock_ycor.return_value = 0
        pong_game.rightpaddleup()
        self.assertEqual(pong_game.rightpaddle.ycor(), 20)

    @patch('turtle.Turtle.ycor')
    def test_right_paddle_down(self, mock_ycor):
        mock_ycor.return_value = 0
        pong_game.rightpaddledown()
        self.assertEqual(pong_game.rightpaddle.ycor(), -20)

    def test_check_collision_left_paddle(self):
        pong_game.ball.xcor.return_value = -345
        pong_game.ball.ycor.return_value = 0
        pong_game.check_collision()
        self.assertEqual(pong_game.ballxdirection, 0.2)

    def test_check_collision_right_paddle(self):
        pong_game.ball.xcor.return_value = 345
        pong_game.ball.ycor.return_value = 0
        pong_game.check_collision()
        self.assertEqual(pong_game.ballxdirection, -0.2)

    def test_check_collision_reset_ball(self):
        pong_game.ball.xcor.return_value = 0
        pong_game.ball.ycor.return_value = 0
        pong_game.check_collision()
        self.assertEqual(pong_game.ball.x, 400)

if __name__ == '__main__':
    unittest.main()
