import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = list()
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(str(key))

    def draw(self, count, selection=None):  # Draw a number of random balls from hat
        balls = list()

        if selection is None:  # Specify which list to draw from
            selection = self.contents

        if count > len(selection):  # Return all balls if attempting to draw more than possible
            return selection

        for i in range(count):
            index = random.randrange(len(selection))
            ball = selection.pop(index)
            balls.append(ball)
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for i in range(num_experiments):
        balls = copy.copy(hat.contents)
        drawn = hat.draw(num_balls_drawn, balls)
        drawn_no_dupes = set(drawn)
        sorted_drawn = dict()

        for color in drawn_no_dupes:
            sorted_drawn[color] = drawn.count(color)
            if color in expected_balls:
                if sorted_drawn[color] >= expected_balls[color]:
                    sorted_drawn[color] = expected_balls[color]
            else:
                del sorted_drawn[color]

        if sorted_drawn == expected_balls:
            counter += 1

    possibility = counter / num_experiments
    return possibility
