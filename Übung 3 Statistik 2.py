from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 3, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Maximum-Likelihood-Schätzung").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 3.1")

        t1 = VGroup(Tex(r"Gegeben sei eine unabhängige Zufallsstichprobe $X_1, X_2, ..., X_n$. Es sei"), Tex(r"$X_i \sim \mathcal{N}(\mu, \sigma^2)$. Welche Schätzfunktion ergibt sich nach dem"), Tex(r"Maximum-Likelihood-Prinzip für den Erwartungswert $\mu$? Gehen Sie davon"), Tex(r"aus, dass $\sigma^2$ bekannt ist.")).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 3.2")

        t1 = Tex(r"Man möchte online einen Sitzplatz für einen Flug reservieren. Es gibt je drei Plätze links und rechts vom Gang. Es wird angenommen, dass man einen Platz zufällig zugewiesen bekommt, dabei ist die Wahrscheinlichkeit für einen bestimmten Sitzplatz auf jedem Flug gleich und unabhängig von den vorher zugewiesenen Sitzplätzen. Ein Manager ist im letzten Monat zehn Mal geflogen, davon vier Mal am Fenster, fünf Mal am Gang und ein Mal in der Mitte.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Wie schätzt der Manager aufgrund seiner Erfahrung die Wahrscheinlichkeiten am Fenster/am Gang/in der Mitte zu sitzen?",
        r"Laut den Regeln der Flugfirma ist die Wahrscheinlichkeit, einen Fensterplatz zu ergattern, gleich der Wahrscheinlichkeit einen Platz am Gang zu bekommen, und beträgt $p$. Die Wahrscheinlichkeit in der Mitte zu sitzen, ist demnach $1-2p$. Ermitteln Sie anhand der Erfahrung des Managers den ML–Schätzwert für $p$!").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 7)
        self.play(Write(list), run_time = 6)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 3.3")

        t1 = Tex(r"Die Anzahl an technischen Defekten alter Autos pro 10 000 km sei iid. Poisson-verteilt, $X \sim \mathcal{P}o(\lambda)$. Ein Automechaniker hat folgende Beobachtung von 15 Fahrzeugen während der letzten 10 000 km notiert:", tex_environment = "flushleft").scale(0.7)
        table = IntegerTable([[3,2,8,2],[1,4,5,7]], row_labels = [Tex(r"Fahrzeugzahl $n(x_i)$"), Tex(r"Pannenzahl $x_i$")]).scale(0.7)
        list = BulletedList(r"Leiten Sie allgemein den ML-Schätzer für den Verteilungsparameter $\lambda$ her.",
        r"Schätzen Sie die Wahrscheinlichkeit dafür ab, dass solch ein Fahrzeug in den nächsten 10 000 km keine Panne haben wird.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        table.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        list.next_to(table, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 3)
        self.play(Write(table), run_time = 3)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(table), FadeOut(ueberschrift))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 3.4")

        t1 = Tex(r"Am Bahnhof wurden die Wartezeiten (in Minuten) gemessen, die die Kund*innen vor der Kasse bis zur Bezahlung verbringen mussten: $x = (10, 8, 9, 5, 4, 7, 9, 5)$. Es wird angenommen, dass die Wartezeit iid. exponential verteilt ist; $X \sim \mathcal{E}xp(\lambda)$. Schätzen Sie den Parameter $\lambda$!", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 5)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

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
