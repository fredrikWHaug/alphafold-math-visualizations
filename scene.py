from manim import *


class SimpleCircle(Scene):
    def construct(self):
        # Create a simple circle
        circle = Circle(radius=1, color=BLUE)

        # Create text
        text = Text("Hello Manim!")

        # Animate the circle appearing
        self.play(Create(circle))

        # Move text above the circle
        text.next_to(circle, UP)

        # Animate text appearing
        self.play(Write(text))

        # Wait for 2 seconds
        self.wait(2)
