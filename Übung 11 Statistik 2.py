from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 11, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Tests für Verteilungen").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 11.1")

        t1 = Tex(r"Eine typische Annahme bei einer Modellierung von Ereignissen in einem bestimmten Zeitraum ist die Poisson-Verteilung. Z.B. ist die Anzahl der während einer Stunde an einer bestimmten Tankstelle tankenden PKW Poisson-verteilt. Während einer Studie erhält man eine Stichprobe:", tex_environment = "flushleft").scale(0.7)
        table = IntegerTable([[0,1,2,3,4,5],[10,30,25,20,10,4]], row_labels = [Tex("Anzahl pro Stunde"), Tex("Häufigkeit")]).scale(0.7)
        t2 = Tex(r"Bitte überprüfen Sie zu den unterschiedlichen Niveaus $\alpha = 0.01,0.05,0.1$, ob die Poisson-Verteilung hier gerechtfertigt ist.", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN)
        t2.next_to(t1, direction = 9 * DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.play(Write(table), run_time = 2)
        self.play(Write(t2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(table), FadeOut(t2), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 11.2")

        t1 = Tex(r"Die Beratung in einem Geschäft darf nicht länger als 15 Minuten und kürzer als 5 Minuten dauern. Während einer Studie werden die Beratungszeiten (Variable $X$) gemessen. Man teste, ob $X$ die unten gegebene Verteilungsfunktion besitzt:", tex_environment = "flushleft").scale(0.7)
        formel = MathTex(r"F(x) = \begin{cases}0 & \text{falls } x < 5 \\ \frac{1}{100}(x-5)^2 & \text{falls } 5 \le x < 15 \\ 1 & \text{falls } x\ge 15\end{cases}").scale(0.7)

        list = BulletedList(r"Eine der Größe nach geordnete Stichprobe von zehn Beobachtungen ist: 6, 8, 10, 11, 13, 13, 14, 15, 15, 15. Überprüfen Sie bitte mit Hilfe des Kolmogorov-Smirnov-Tests, ob die Annahme über die Verteilung statistisch zum Niveau $\alpha = 0.05$ nachgewiesen werden kann.",
        r"Die 150 Beobachtungen einer anderen Stichprobe verteilen sich wie folgt auf verschiedene Intervalle. Wenden Sie den $\chi^2$-Anpassungstest an, um die Annahme der Verteilung zu prüfen.").scale(0.7)
        table = MathTable([["[5;7.5]","(7.5;10]","(10;12.5]","(12.5;15]"],["33","41","40","36"]], row_labels = [Tex(r"Intervall $I_i$"), Tex(r"Häufigkeit $S_i$")]).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formel.next_to(t1, direction = DOWN)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(list, direction = DOWN)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.play(Write(formel), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(formel))

        self.play(Write(list), run_time = 7)
        self.play(Write(table), run_time = 2)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list), FadeOut(table))

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
