from manim import *


class InitialQuote(Scene):
    def construct(self):
        text = Text("""
            The more I think about language, the more it amazes
            me that people ever understand each other at all.
            """, font_size=30)



        author = Text("— Kurt Gödel")
        author.next_to(text, DOWN)

        self.play(
            Write(text, run_time=3),
        )
        self.wait(3)
        self.play(Write(author, run_time=5))
        
        