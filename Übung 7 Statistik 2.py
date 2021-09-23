from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 7, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"statistische Tests").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 1)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.1")

        t1 = Tex(r"Der mittlere Zeitaufwand $\mu$ für die Klausurvorbereitung einer Statistikklausur (in Stunden) wird untersucht. Eine Dozentin behauptet, dass ein Student im Durchschnitt nur 83 Stunden Vorbereitungszeit braucht, um die Klausur mit einer guten Note zu bestehen: \textit{über ein Semester von 15 Wochen fünf Stunden pro Woche (1.5 (Vorlesung) + 1.5 (Übung) + 2 (selber Zuhause)) und jeweils vier Stunden an den zwei Tagen vor der Klausur.} Sie fragt neun zufällig ausgewählte Studierende nach der Vorbereitungszeit und erhält eine Stichprobe $X = (X_1, X_2, ..., X_9)$. Daraus ergibt sich ein mittlerer Wert $\bar{x} = 86$ Stunden. Aus langjähriger Erfahrung weiß man, dass die einzelnen Variablen $X_i$ normalverteilt sind: $X_i \sim \mathcal{N}(\mu, \sigma^2)$, mit $\sigma^2 = 64$ Stunden$^2$. Die $X_i$ sind unabhängig voneinander.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Führen Sie einen statistischen Test zum Signifikanzniveau $\alpha = 0.05$ durch, um die Behauptung der Dozentin zu prüfen.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 11)
        self.play(Write(list), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list))

        t2 = Tex(r"Nehmen Sie nachfolgend an, dass die Stichprobenvarianz $s^2 = 20$ Stunden$^2$ beträgt.", tex_environment = "flushleft").scale(0.7)
        list2 = BulletedList(r"Führen Sie unter der Annahme, dass die Varianz unbekannt ist, einen statistischen Test zum Signifikanzniveau $\alpha = 0.05$ durch, um die Behauptung der Dozentin zu prüfen.",
        r"Ein Student möchte anhand der o.g. Stichprobe zeigen, dass der mittlere Zeitaufwand größer als 83 Stunden ist ($\sigma^2$ ist unbekannt, $\alpha = 0.05$). Führen Sie einen geeigneten Test durch.",
        r"Ein anderer Student möchte dasselbe zum Niveau $\alpha = 0.02$ zeigen.",
        r"Testen Sie, ob die Varianz gleich 64 Stunden$^2$ ist.").scale(0.7)
        t2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list2.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(t2))
        self.play(Write(list2), run_time = 8)
        self.wait(2)
        self.play(FadeOut(t2), FadeOut(list2), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.2")

        t1 = Tex(r"Kurz vor einer wichtigen Wahl wird im Fernsehen folgendes Meinungsforschungsergebnis für den Stimmenanteil der Partei A bekannt gegeben: Unter 400 zufällig ausgewählten Befragten gaben 38 Prozent an, für die Partei A zu stimmen.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Führen Sie einen statistischen Test zum Signifikanzniveau $\alpha = 0.03$ durch, um zu prüfen, ob die Partei A bei der Wahl einen Stimmenanteil von mindestens 35\% bekommt.",
        r"Führen Sie den gleichen statistischen Test zu den Signifikanzniveaus $\alpha = 0.05$, $\alpha = 0.10$ und $\alpha = 0.15$ durch.",
        r"Bestimmen Sie den $p$-Wert des Tests.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.play(Write(list), run_time = 6)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe3(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.3")

        t1 = Tex(r"Ein Assistent am Lehrstuhl Statistik ärgert sich über die schlechte Qualität eines bestimmten Kopiergerätes. Von 100 zu zufälligen Zeitpunkten unternommenen Kopierversuchen an diesem Gerät waren nur 45 erfolgreich. In den restlichen Fällen war das Gerät defekt. Der Assistent geht davon aus, dass es sich somit um eine einfache Stichprobe vom Umfang $n = 100$ handelt und möchte dem Kopiergerätehersteller statistisch beweisen, dass das beschriebene Gerät in mehr als 50\% der Fälle nicht funktioniert. Führen Sie einen geeigneten Test zum Signifikanzniveau $\alpha = 0.2$ durch.", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 8)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(ueberschrift))

class Aufgabe4(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 7.4")

        t1 = Tex(r"Bei der Benzingewinnung für den Rennsport wird Nitromethan beigemischt, um ein besseres Laufverhalten des Motors zu erreichen. Bei der Abfüllung von Benzin in Tanks wird nun dieser Gehalt kontrolliert. Eine Stichprobe von $n = 116$ Kontrollmessungen ergab folgende Werte für den Gehalt an Nitromethan: Stichprobenmittelwert: 25.452 ml/l, Stichprobenvarianz: 0.850 (ml/l)$^2$. Testen Sie zum Niveau $\alpha = 0.04$, ob der wahre Anteil maximal 25.8 ml/l ist.", tex_environment = "flushleft").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 7)
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
