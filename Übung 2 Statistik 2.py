from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 2, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Ungleichung von \textsc{Tschebyscheff}", r"Zentraler Grenzwertsatz", r"Binomial- und Normalverteilung").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 2.1")

        t1 = VGroup(Tex(r"Eine Zufallsvariable $X$ habe den Erwartungswert $\mathbb{E}(X) = 10$ und die Varianz"), Tex(r"$\text{Var}(X) = 4$.")).scale(0.7)
        list = BulletedList(r"Welche Aussage kann über die Wahrscheinlichkeit des Ereignisses $7 < X < 13$ gemacht werden?",
        r"Welche Aussage kann über die Wahrscheinlichkeit dieses Ereignisses gemacht werden, wenn man weiß, dass $X$ normalverteilt ist?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2)
        self.play(Write(list), run_time = 4)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 2.2")

        t1 = VGroup(Tex(r"An einer Klausur haben 100 Studierende teilgenommen. Die Zufallsvariable $X_i$"), Tex(r"(mit dem Erwartungswert von 45 Minuten und der Standardabweichung von"), Tex(r"10 Minuten, dabei sind alle $X_i$ unabhängig voneinander) beschreibe die für die"), Tex(r"Korrektur der $i$–ten Klausur benötigte Zeit. Wie groß ist die"), Tex(r"Wahrscheinlichkeit, dass für die Korrektur höchstens 10 Arbeitstage"), Tex(r"(achtstündig) benötigt werden?")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 8)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 2.3")

        t1 = VGroup(Tex(r"Eine Näherei, die Oberhemden herstellt, bezieht die benötigten Knöpfe von"), Tex(r"einer Fremdfirma. Aus langjähriger Erfahrung weiß man, dass ein Knopf mit"), Tex(r"einer Wahrscheinlichkeit von 0.12 einen Defekt aufweist, d.h. zur Verarbeitung"), Tex(r"nicht verwendet werden kann. Die Knöpfe sind unabhängig voneinander.")).scale(0.7)
        list = BulletedList(r"In einem bestimmten Monat werden 4500 Knöpfe geliefert. Wie groß ist die (approximative) Wahrscheinlichkeit, dass sich darunter mindestens 4000 Knöpfe ohne Defekt befinden?",
        r"Wie viele Knöpfe müssen geordert werden, damit mit 95\%–iger Sicherheit mehr als 4500 Knöpfe verarbeitet werden können?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5.5)
        self.play(Write(list), run_time = 5)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 2.4")

        t1 = Tex(r"Die Ergebnisse eines Leistungstests seien normalverteilt mit $\mu = 150$, $\sigma = 36.$").scale(0.7)
        list = BulletedList(r"Berechnen Sie die Wahrscheinlichkeit, Werte zu erreichen, die kleiner als 140 sind.",
        r"Der Leistungstest wird nun an 49 Personen unabhängig voneinander durchgeführt. Wie wahrscheinlich ist es, einen Mittelwert kleiner als 140 zu beobachten? Vergleichen Sie Ihr Ergebnis mit dem aus (a). Wie erklären Sie sich den Unterschied?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 1.5)
        self.play(Write(list), run_time = 5)
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
