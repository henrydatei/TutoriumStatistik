from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 1, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))
        
class Themen(Scene):
    def construct(self):
        ueberschrift = Text("Heutige Themen")
        ueberschrift.to_edge(UP)
        t1 = Text("Mittelwert").scale(0.75)
        t1.to_edge(LEFT).shift(UP)
        t2 = Text("Populationsvarainz").scale(0.75)
        t2.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        t3 = Text("empirische Varianz").scale(0.75)
        t3.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), Write(t2), Write(t3))
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(t2), FadeOut(t3))
