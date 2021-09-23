from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 6, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Konfidenzintervalle").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 6.1")

        t1 = Tex(r"Bei der Benzingewinnung für den Rennsport wird Nitromethan beigemischt, um ein besseres Laufverhalten des Motors zu erreichen. Bei der Abfüllung von Benzin in Tanks wird nun dieser Gehalt kontrolliert. Eine Stichprobe von $n = 116$ Kontrollmessungen ergab folgende Werte für den Gehalt an Nitromethan: Stichprobenmittelwert: 25.452 ml/l, Stichprobenvarianz: 0.850 (ml/l)$^2$. Berechnen Sie das 96\%-Konfidenzintervall für den erwarteten Nitromethangehalt in der Produktion.", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 7)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 6.2")

        t1 = Tex(r"Von 100 befragten Personen einer Großstadt haben 70 einen Pkw (im Bekannten- oder Freundeskreis) verfügbar.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"In welchem Bereich liegt die \textit{wahre} Pkw-Verfügbarkeit mit einer maximalen Irrtumswahrscheinlichkeit von $\alpha = 0.1$?",
        r"Wie viele Personen müsste man befragen, um das Konfidenzintervall (bei gleichem $\alpha$) auf $\pm 5\%$ eingrenzen zu können?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 2)
        self.play(Write(list), run_time = 4)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 6.3")

        t1 = Tex(r"Kurz vor einer wichtigen Wahl wird im Fernsehen folgendes Meinungsforschungsergebnis für den Wähleranteil der Partei A bekannt gegeben: Unter 400 zufällig ausgewählten Befragten gaben 38 Prozent an, für die Partei A zu stimmen.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Bestimmen Sie das 97\%-Konfidenzintervall für den Anteil der Wähler*innen der Partei A zu diesem Zeitpunkt in der Gesamtbevölkerung.",
        r"Zu welchem Signifikanzniveau wird die 35\%-Barriere für den Anteil der Wähler*innen der Partei A zu diesem Zeitpunkt in der Gesamtbevölkerung überschritten?",
        r"Bei welchem Stichprobenumfang $n$ würde die Befragung mit dem Ergebnis \textit{38\% der Befragten haben zugestimmt} sichern, dass die 35\%-Barriere zum Signifikanzniveau $\alpha = 0.06$ überschritten wird?",).scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.play(Write(list), run_time = 8)
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
