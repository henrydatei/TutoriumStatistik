from manim import *
import numpy as np

class Titel(Scene):
    def construct(self):
        title = Text("Übung 5, Statistik 2")
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

class Themen(Scene):
    def construct(self):
        ueberschrift = Title("Heutige Themen")
        list = BulletedList(r"Eigenschaften von Schätzern", r"Konfidenzintervalle").scale(0.7)
        list.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(list), run_time = 3)
        self.wait(2)
        self.play(FadeOut(ueberschrift), FadeOut(list))

class Aufgabe1(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 5.1")

        t1 = Tex(r"Eine Grundgesamtheit habe den Erwartungswert $\mu$ und die Varianz $\sigma^2$. Sei $(X_1, X_2, ..., X_n)$ eine einfache (theoretische) Zufallsstichprobe aus dieser Grundgesamtheit. Folgende fünf Schätzfunktionen für den Erwartungswert sind gegeben:", tex_environment = "flushleft").scale(0.7)
        formel = MathTex(r"\hat{\mu}_1 &= \frac{1}{n}\left(X_1 + X_2 + \dots + X_n\right) \notag \\ \hat{\mu}_2 &= \frac{1}{3}\left(2X_1 + X_3\right) \notag \\ \hat{\mu}_3 &= X_1 \notag \\ \hat{\mu}_4 &= \bar{X} + \frac{1000}{n} \notag \\ \hat{\mu}_5 &= \frac{n-1}{n}\bar{X}\notag").scale(0.7)
        t2 = Tex(r"Beantworten Sie die folgende Fragen und begründen Sie Ihre Antwort:", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Welche dieser Schätzfunktionen sind erwartungstreu?",
        r"Wie lautet jeweils der mittlere quadratische Fehler?",
        r"Welche Schätzfunktionen sind konsistent?",
        r"Welcher Schätzfunktion würden Sie nach dem Kriterium der Güte den Vorzug geben?").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        formel.next_to(t1, direction = DOWN)
        t2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 4)
        self.play(Write(formel), run_time = 4)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(formel))

        self.play(Write(t2), run_time = 1)
        self.play(Write(list), run_time = 4)
        self.wait(2)
        self.play(FadeOut(t2), FadeOut(list), FadeOut(ueberschrift))

class Aufgabe2(Scene):
    def construct(self):
        ueberschrift = Title("Aufgabe 5.2")

        t1 = Tex(r"Der mittlere Zeitaufwand $\mu$ der Studierenden für die Klausurvorbereitung einer Statistikklausur (in Stunden) in einer Grundgesamtheit von 150 Studierenden soll mittels einer Stichprobe $X = (X_1, X_2, ..., X_n)$ vom Umfang $n$ geschätzt werden. Man konstruiert dafür ein Konfidenzintervall. Aus langjähriger Erfahrung weiß man, dass die einzelnen Variablen $X_i$ normalverteilt ($X_i \sim \mathcal{N}(\mu, \sigma^2)$, mit $\sigma^2 = 64$), und unabhängig voneinander sind.", tex_environment = "flushleft").scale(0.7)
        list = BulletedList(r"Bei einer zufälligen Stichprobe von 9 Studierenden wurden die folgenden Werte ermittelt: $\bar{x}=85$, $s^2 =70$.").scale(0.7)
        list2 = BulletedList(r"Bestimmen Sie das Konfidenzintervall für $\mu$ zum Signifikanzniveau $\alpha = 0.1$.",
        r"Bestimmen Sie das Konfidenzintervall für $\mu$ zum Signifikanzniveau $\alpha = 0.05$.",
        r"Bestimmen Sie das Konfidenzintervall für $\mu$ zum Signifikanzniveau $\alpha = 0.05$ unter der Annahme, dass die Varianz unbekannt ist und durch $s^2$ geschätzt wird.",
        r"Bestimmen Sie das Konfidenzintervall für $\sigma^2$ zum Signifikanzniveau $\alpha = 0.05$.",
        r"Anhand einer anderen Stichprobe $Y$ vom Umfang 40 werden der neue Mittelwert und die Stichprobenvarianz ermittelt ($\bar{y} = 90$, $s^2_y = 75$). Bestimmen Sie das asymptotische Konfidenzintervall für $\mu$ ($\alpha = 0.05$).").scale(0.5)
        list3 = BulletedList(r"Wie groß muss der Stichprobenumfang sein, damit die Länge des 95\%-Konfidenzintervalls höchstens 5 Stunden beträgt?",
        r"Bei einer zufälligen Stichprobe von 9 Studierenden wurde der Wert $\bar{x} = 85$ ermittelt. Wählen Sie das Signifikanzniveau $\alpha$ so aus, dass $\mu = 78$ im Konfidenzinterval liegt.").scale(0.7)
        t1.arrange(DOWN, aligned_edge = LEFT)
        t1.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list.next_to(t1, direction = DOWN, aligned_edge = LEFT)
        list2.next_to(ueberschrift, direction = DOWN, aligned_edge = LEFT)
        list3.next_to(list2, direction = DOWN, aligned_edge = LEFT)

        self.play(Write(ueberschrift))
        self.wait(1)
        self.play(Write(t1), run_time = 6)
        self.play(Write(list), run_time = 2)
        self.wait(2)
        self.play(FadeOut(t1), FadeOut(list))

        self.play(Write(list2), run_time = 8)
        self.play(Write(list3), run_time = 5)
        self.wait(2)
        self.play(FadeOut(list2), FadeOut(list3), FadeOut(ueberschrift))

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
