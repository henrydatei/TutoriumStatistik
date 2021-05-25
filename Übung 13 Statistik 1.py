from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 13, Statistik 1")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"diskrete Verteilungen").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 13.1")

        t1 = VGroup(Tex(r"Nur 3\% der kontrollierten Fahrgäste der Dresdner Straßenbahnen besitzen"),
        Tex(r"keinen gültigen Fahrschein. Die Ergebnisse der Kontrolle seien unabhängig,"),
        Tex(r"d.h. es wird vereinfacht angenommen, dass nur Einzelpersonen kontrolliert"),
        Tex(r"werden.")).scale(0.7)
        list = BulletedList(r"Mit welcher Wahrscheinlichkeit wird bei der Kontrolle von 10 Personen wenigstens ein Schwarzfahrer erwischt?",
        r"Wie groß ist die Wahrscheinlichkeit, dass der Kontrolleur erst bei der zehnten Kontrolle den ersten Schwarzfahrer aufspürt?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.play(Write(list), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 13.2")

        t1 = VGroup(Tex(r"Von der Eiersorte sei bekannt, dass von einer Packung mit sechs Eiern zwei"),
        Tex(r"Eier faul sind. Aus dieser Packung werden zufällig drei Eier ausgewählt und"),
        Tex(r"auf ihre Güte überprüft, d.h. in die Pfanne geschlagen.")).scale(0.7)
        list = BulletedList(r"Wie groß ist die Wahrscheinlichkeit, dass genau ein Ei faul ist?",
        r"Wie groß ist die Wahrscheinlichkeit, dass höchstens ein Ei faul ist?",
        r"Wie groß ist die Wahrscheinlichkeit, dass mindestens zwei Eier faul sind?",
        r"Wie groß ist die Wahrscheinlichkeit, dass genau drei Eier faul sind?",
        r"Wie viele faule Eier sind zu erwarten?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(list), run_time = 6)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 13.3")

        t1 = VGroup(Tex(r"Zwischen 14 und 16 Uhr ist die durchschnittliche Anzahl der Telefongespräche,"),
        Tex(r"die die Vermittlung einer Firma pro Minute empfängt, gleich 2.5.")).scale(0.7)
        list = BulletedList(r"Wie ist die Zufallsvariable $X$ - \textit{Anzahl der in dieser Zeit empfangenen Telefonate pro Minute} verteilt?",
        r"Wie groß ist die Wahrscheinlichkeit, dass während einer bestimmten Minute in dieser Zeit kein, weniger als drei, vier oder mehr Telefonate empfangen werden?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2.5)
        self.play(Write(list), run_time = 3.5)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 13.4")

        t1 = VGroup(Tex(r"Es werden Familien mit vier Kindern betrachtet. Wir nehmen an, dass"),
        Tex(r"Jungen- und Mädchengeburten unabhängig voneinander und"),
        Tex(r"gleichwahrscheinlich sind. Mit $X$ bezeichnen wir die (zufällige) Anzahl der"),
        Tex(r"Jungen in einer Familie mit vier Kindern. Wie ist $X$ verteilt? Man berechne"),
        Tex(r"die Wahrscheinlichkeit dafür, dass")).scale(0.7)
        list = BulletedList(r"zwei Jungen und zwei Mädchen",
        r"drei Jungen und ein Mädchen",
        r"vier Jungen").scale(0.7)
        t2 = Tex(r"geboren werden.").scale(0.7)
        list2 = BulletedList(r"Man berechne auch die erwartete Anzahl der Jungen in einer Familie.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        t2.next_to(list, direction = DOWN, aligned_edge = LEFT)
        list2.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.play(Write(list), run_time = 2)
        self.play(Write(t2), run_time = 0.5)
        self.play(Write(list2))
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift), FadeOut(t2), FadeOut(list2))

class Ende(Scene):
    def construct(self):
        text = Text("Viel Erfolg!")
        subtext = Tex(r"Fragen $\to$ Forum").scale(0.7)
        subtext.next_to(text, direction = DOWN)

        self.play(Write(text))
        self.wait(1)
        self.play(Write(subtext))
        self.wait(2)
        self.play(FadeOut(text), FadeOut(subtext))

class Trenner(Scene):
    def construct(self):
        self.wait(0.5)
