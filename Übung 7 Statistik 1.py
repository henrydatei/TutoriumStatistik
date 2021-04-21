from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 7, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        t1 = Text("Kombinatorik").scale(0.75)
        t1.to_edge(LEFT).shift(UP).shift(0.5*RIGHT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.1")
        t1 = Text("(a) Wie viele Möglichkeiten gibt es, die Buchstaben des englischen Wortes TEA anzuordnen, wobei jeder einzelne nur einmal vorkommen darf?").set(width = 12)
        t2 = Text("(b) Wie viele Möglichkeiten gibt es, die Buchstaben des deutschen Wortes TEE anzuordnen, wobei jeder einzelne nur einmal vorkommen darf?").set(width = 12)
        t3 = Text("(c) Wie viele Möglichkeiten gibt es, die Buchstaben des Wortes STATISTIK anzuordnen, wobei jeder einzelne nur einmal vorkommen darf?").set(width = 12)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        t2.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        t3.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(t2))
        self.play(Write(t3))
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(t2), FadeOut(t3))
