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

        list = BulletedList(r"Wie viele Möglichkeiten gibt es, die Buchstaben des englischen Wortes TEA anzuordnen, wobei jeder einzelne nur einmal vorkommen darf?",
        r"Wie viele Möglichkeiten gibt es, die Buchstaben des deutschen Wortes TEE anzuordnen, wobei jeder einzelne nur einmal vorkommen darf?",
        r"Wie viele Möglichkeiten gibt es, die Buchstaben des Wortes STATISTIK anzuordnen, wobei jeder einzelne nur einmal vorkommen darf?").scale(0.7)

        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 4.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.2")

        list = BulletedList(r"Es werden zwei Würfel gleichzeitig geworfen. Wie viele verschiedene Augenpaare können auftreten?",
        r"Wie viele verschiedene Aufgaben enthält das kleine Einmaleins ($1 \times 1$ bis $9 \times 9$)?",
        r"Bestimmen Sie die Anzahl der Möglichkeiten für eine Lotto-Ziehung 6-aus-49.").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 4.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.3")

        t1 = Tex(r"Berechnen Sie, wie viele Möglichkeiten der Anordnung es für").scale(0.7)
        list = BulletedList(r"4 unterschiedlich farbige Kugeln gibt.", r"$m$ schwarze und 1 weiße Kugel gibt.").scale(0.7)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1))
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(list))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.4")

        t1 = VGroup(Tex(r"Eine Sparkassen-Bankkarte ist mit einem vierstelligen PIN gesichert."), Tex(r"Vorkommen können die Ziffern von 0 bis 9, jede Ziffer kann (im Prinzip)"), Tex(r"mehrfach auftreten. Wie viele mögliche Ziffernkombinationen gibt es,")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        list = BulletedList(r"wenn man sich an gar nichts mehr erinnern kann?", r"wenn man noch weiß, dass unter den richtigen Ziffern genau eine 3 war?", r"wenn man noch weiß, dass diese eine 3 definitiv an der dritten Stelle stand?").scale(0.7)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3*1.5)
        self.play(Write(list), run_time = 4.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(list))

class Aufgabe5(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.5")

        t1 = VGroup(Tex(r"Ein Zug besteht aus 4 Wagen der 1. Klasse, 7 Wagen der 2. Klasse,"), Tex(r"1 Speisewagen und 2 Gepäckwagen. Wie viele unterscheidbare Wagenfolgen"), Tex(r"sind möglich")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        list = BulletedList(r"wenn die Wagen beliebig eingereiht werden dürfen?", r"wenn die Wagen der 1. Klasse nicht getrennt werden dürfen?").scale(0.7)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3*1.5)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(list))

class Aufgabe6(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.6")

        t1 = VGroup(Tex(r"Wie viele unterschiedliche Möglichkeiten zur Bildung eines EDV-Passwortes"), Tex(r"gibt es, wenn es aus genau zwei, unterschiedlichen Buchstaben des Alphabets"), Tex(r"insgesamt 26 Buchstaben, Groß- und Kleinschreibung ohne Bedeutung) und"), Tex(r"anschließend einer Zahl bestehend aus mindestens 2, maximal 4 Ziffern (0 an"), Tex(r"erster Stelle möglich) bestehen soll?")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5*1.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))

class Aufgabe7(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.7")

        t1 = VGroup(Tex(r"Im \textit{Jahr des Buches} haben Sie vorsorglich zehn Bücher unterschiedlicher Titel"), Tex(r"als Geschenke gekauft. Fünf Geburtstage stehen bevor. Wie viele"), Tex(r"Verteilungsmöglichkeiten gibt es, wenn jedes Geburtstagskind nur ein Buch"), Tex(r"erhalten soll?")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4*1.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))

class Aufgabe8(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.8")

        t1 = VGroup(Tex(r"Auf wie viele Arten kann man 7 Hotelgäste in 10 freien Einzelzimmern"), Tex(r"unterbringen?")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2*1.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))

class Aufgabe9(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.9")

        t1 = VGroup(Tex(r"Für das Elfmeterschießen muss der Trainer 5 der 11 Spieler auswählen. Wie"), Tex(r"viele Möglichkeiten hat er bei")).scale(0.7)
        list = BulletedList(r"der Bestimmung der Kandidaten?", r"der Bestimmung der Reihenfolge der Schützen, nachdem die Kandidaten gewählt wurden?").scale(0.7)

        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2*1.5)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(list))

class Aufgabe10(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.10")

        t1 = VGroup(Tex(r"Bei einem regulären Würfel sind die Wahrscheinlichkeiten für die Augenzahlen"), Tex(r"1, 2,..., 6 gleich. Würfelt man mit zwei Würfeln gleichzeitig, so erhält man als"), Tex(r"Augensumme eine Zahl zwischen 2 und 12. Bspw. kann man die Summe 9"), Tex(r"mittels der Kombinationen 9 = 3 + 6 = 4 + 5 erhalten, während die 10 sich"), Tex(r"über 10 = 4 + 6 = 5 + 5 erzielen lässt. Wieso erhält man im Durchschnitt 9"), Tex(r"etwas häufiger als 10?")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 6*1.5)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1))
