from manim import *

class circle(Scene):
    def construct(self):
        circle = Circle(radius=1, color=RED)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()
