from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 1, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Wiederholung Verteilungen").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 1.1")

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
        ueberschrift = Title("Aufgabe 1.2")

        t1 = VGroup(Tex(r"Die Dauer von Telefongesprächen an der Information am Hauptbahnhof"), Tex(r"Dresden sei exponentialverteilt mit dem Parameter $\lambda=0.2$ min$^{-1}$.")).scale(0.7)
        list = BulletedList(r"Skizzieren Sie die Dichte und die Verteilungsfunktion der Dauer der Telefongespräche.",
        r"Wie groß ist die Wahrscheinlichkeit, dass ein Gespräch kürzer als 3 Minuten dauert?",
        r"Wie groß ist die Wahrscheinlichkeit, dass ein Gespräch länger als 3 Minuten dauert?",
        r"Wie groß ist die Wahrscheinlichkeit, dass ein Gespräch länger als 2 Minuten und kürzer als 3 Minuten dauert?",
        r"Berechnen Sie den Erwartungswert und die Varianz für die Dauer der Telefongespräche.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(list), run_time = 7.5)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 1.3")

        t1 = VGroup(Tex(r"Der Preis von Erdbeeren sei normalverteilt mit dem Erwartungswert $\mu = 1.50$"), Tex(r"Euro und der Standardabweichung $\sigma = 0.36$ Euro.")).scale(0.7)
        list = BulletedList(r"Skizzieren Sie die Dichte des Preises.",
        r"Zeichnen Sie jeweils die folgenden Wahrscheinlichkeiten als Fläche unter der Dichte ein, und berechnen Sie die Wahrscheinlichkeit, einen Preis zu erreichen, der kleiner als 1.60 Euro ist, kleiner als 1.40 Euro ist, größer als 1.40 Euro ist, nicht im Bereich von 1.14 Euro bis 1.90 Euro liegt, grösser als 1.75 Euro ist, kleiner als 2.00 Euro und größer als 1.30 Euro ist.",
        r"Bestimmen Sie den 10\%-Quantilswert, und fassen Sie in Worte, was er aussagt.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(list), run_time = 6)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

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
