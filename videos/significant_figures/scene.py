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

        author.set_color(YELLOW)
        author.next_to(quote, DOWN, buff=0.5)

        self.play(Write(quote, run_time=2))
        self.wait(1)
        self.play(Write(author, run_time=4))

        self.wait()


class HistoricalContext(Scene):
    def construct(self):
        pass
