from manim import *
import numpy as np
from scipy.stats import norm

def stepAddition(liste):
        zurueck = []
        for i in range(len(liste)):
            zurueck.append(sum(liste[0:i+1])/sum(liste))
        return zurueck

class Titel(Scene):
    def construct(self):
        title = Text("Übung 12, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Tests für Verteilungen", r"QQ-Plot").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 12.1")

        t1 = Tex(r"Um die Mindest-Grünzeit von Fußgängerampeln in Abhängigkeit der Straßenbreite festzulegen, werden zunächst die Geschwindigkeiten einer repräsentativen Stichprobe von Fußgängern ermittelt. Es ergaben sich folgende Geschwindigkeiten in Metern pro Sekunde: 1.45, 1.30, 1.31, 1.18, 1.20, 1.70, 1.22, 1.30, 1.26, 1.23, 0.95, 4.80, 1.28, 1.22, 1.22, 1.12, 1.46, 1.00, 1.51, 1.44", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Geben Sie die effizienten Schätzer $\hat{\mu}$ und $\hat{\sigma}$ für Erwartungswert bzw. Standardabweichung der Geschwindigkeiten an.",
        r"Testen Sie die Verteilung der Geschwindigkeiten $X$ mit dem Kolmogorov-Smirnov-Test auf die Nullhypothese $H_0$: $X \sim \mathcal{N}(\mu,\sigma^2)$ bei einer Fehlerwahrscheinlichkeit von 5\%. Ermitteln Sie dabei die Realisierung der Test-Statistik graphisch unter Verwendung folgender Abbildung.",
        r"In den Daten gibt es einen Ausreißer, der aber nicht auf Messfehlern beruht. Warum kann bzw. sollte man ihn trotzdem für die Ermittlung der Mindest-Freigabezeiten ignorieren?").scale(0.7)

        ax = Axes(x_range=[0, 6, 1], y_range=[0, 1, 0.1], y_length = 5.5).shift(0.5*DOWN)
        xlabel = ax.get_x_axis_label(Text("Geschwindigkeit").scale(0.5), edge = DOWN, direction = DOWN)
        graph = ax.get_graph(lambda x: norm.cdf(x,1.4575,0.805))
        xvalues = sorted([1.45, 1.30, 1.31, 1.18, 1.20, 1.70, 1.22, 1.30, 1.26, 1.23, 0.95, 4.80, 1.28, 1.22, 1.22, 1.12, 1.46, 1.00, 1.51, 1.44])
        yvalues = stepAddition(xvalues)
        allDots = []

        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.play(Write(list), run_time = 9)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list))

        self.play(Write(ax), Write(xlabel))
        self.play(Write(graph))
        for x, y in zip(xvalues,yvalues):
            point = ax.coords_to_point(x, y)
            dot = Dot(point, color = BLUE_D)
            allDots.append(dot)
            self.play(GrowFromCenter(dot), run_time = 0.1)
        self.wait(2)
        self.play(FadeOut(ax), FadeOut(xlabel), FadeOut(ueberschrift), FadeOut(VGroup(*allDots)), FadeOut(graph))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 12.2")

        list = BulletedList(r"Ein Student kommt jeden Tag an einem Einkaufszentrum vorbei. Er sieht dort vor allem viele Passanten im mittleren Alter, aber eher wenige junge und sehr alte Menschen. Nun möchte er wissen, ob das Alter $X$ der Passanten in dem Einkaufszentrum normalverteilt ist. Er fragt zufällig sieben Passanten und notiert sich folgende Tabelle.").scale(0.7)
        tabelle = IntegerTable([[1,2,3,4,5,6,7],[35,78,30,81,24,10,30]], row_labels = [Tex(r"$i$"), Tex(r"$x_i$")]).scale(0.7)
        t1 = Tex(r"Der Student berechnet den Mittelwert $\bar{x} = 41.14$ und die Standardabweichung $s = 27.38$ der Stichprobe. Zeichnen Sie für ihn einen QQ-Plot für normalverteilte Daten und diskutieren Sie diesen.", tex_environment = "flushleft").scale(0.7)

        list2 = BulletedList(r"(nicht klausurrelevant) Testen Sie mit Daten ($\alpha = 0.05$). Die Tabelle mit den dem Shapiro - Wilk Test auf Normalverteilung der kritischen Werten für $W_{\alpha}$ ist gegeben.",
        r"Nun findet der Student, dass ein Stichprobenumfang von $n = 7$ zu keinem aussagekräftigen Ergebnis führt. Also macht er sich noch einmal auf den Weg und fragt zusätzlich 500 Passanten nach ihrem Alter. Anschließend zeichnet er den QQ-Plot erneut und wiederholt den Test in dem Statistiktool R. Er erhält folgendes Ergebnis mit dem Output aus R (Befehl: shapiro.test()): $w = 0.97537$, $p$-value $= 1.862\cdot 10^{-7}$ Wie ist die Grafik zu interpretieren? Kann $H_0$ laut dem Testergebnis aus R abgelehnt werden ($\alpha = 0.05$)?").scale(0.7)

        list.next_to(ueberschrift, direction = DOWN)
        tabelle.next_to(list, direction = DOWN)
        t1.next_to(list, direction = 8 * DOWN, aligned_edge = LEFT)
        list2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 5)
        self.play(Write(tabelle), run_time = 2)
        self.play(Write(t1), run_time = 3)
        self.wait(2)
        self.play(FadeOut(list), FadeOut(tabelle), FadeOut(t1))

        self.play(Write(list2), run_time = 10)
        self.wait(2)
        self.play(FadeOut(list2), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 12.3")

        t1 = Tex(r"In der folgenden Häufigkeitstabelle finden Sie für eine Fußball–Saison die Torerfolge pro Spiel.", tex_environment = "flushleft").scale(0.7)
        tabelle = MathTable([["0","1","2","3","4","5","6","7","8","9",">9"],["18","24","56","63","61","39","26","6","5","2","0"]], row_labels = [Tex("Tore pro Spiel"), Tex("Häufigkeit")]).scale(0.5)
        t2 = Tex(r"Es soll nun mit einem statistischen Test untersucht werden, ob die Torerfolge pro Spiel einer Poissonverteilung mit $\lambda = 3.4$ folgen.", tex_environment = "flushleft").scale(0.7)

        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        tabelle.next_to(t1, direction = DOWN)
        t2.next_to(t1, direction = 7 * DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2)
        self.play(Write(tabelle), run_time = 2)
        self.play(Write(t2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(t1), FadeOut(t2), FadeOut(tabelle))

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
