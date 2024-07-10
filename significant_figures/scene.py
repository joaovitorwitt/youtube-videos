from manim import * # pylint: disable=unused-wildcard-import, wildcard-import

class OpeningQuote(Scene):

    def construct(self):
        quote = Text(
            "''Science cannot solve the ultimate mystery of nature because \nwe ourselves are a part of the mystery that we are trying to solve.''",
            font_size=30,
            
        )

        quote.to_edge(UP)

        for mob in quote.submobjects:
            mob.set_color(WHITE)

        author = Text(
            "— Max Planck"
        )

        author.set_color(BLUE)
        author.next_to(quote, DOWN, buff=0.5)

        self.play(Write(quote, run_time=2))
        self.play(Write(author, run_time=3))

        self.wait()


class HistoricalContext(Scene):
    def construct(self):
        pass


class CalculatingArea(Scene):
    def construct(self):
        rectangle = Rectangle(color=BLUE, fill_opacity=0.5, stroke_width=5)
        self.play(rectangle.animate.move_to(RIGHT * 3))
        self.play(rectangle.animate.scale(0.3))
        self.wait(1)


