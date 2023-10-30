# -*- coding: utf-8 -*-
import qi

class EscapeRoomSpeakerHandler(object):
    def __init__(self, session):
        self.session = session
        self.animatedSpeechService = session.service("ALAnimatedSpeech")

    def start(self):
        try:
            self.animatedSpeechService.say("^start(animations/Stand/Gestures/Explain_1) Willkommen, liebe Teilnehmer, zu einem einzigartigen Escape Room Workshop im Herzen des futuristischen Smart Home Labors. ^wait(animations/Stand/Gestures/Explain_1)")
            self.animatedSpeechService.say("^start(animations/Stand/Gestures/Excited_1) Ich bin euer digitaler Begleiter und Assistent Pepper. ^wait(animations/Stand/Gestures/Excited_1)")
            self.animatedSpeechService.say("^start(animations/Stand/Waiting/Think_1) Heute werdet ihr Teil einer aufregenden Ermittlung, bei der es darum geht, den mysteriösen Mord an unserem hoch angesehenen Professor aufzuklären. ^wait(animations/Stand/Waiting/Think_1)")
            self.animatedSpeechService.say("^start(animations/Stand/Gestures/Explain_3) Ihr betretet eine Welt voller modernster Technologien, in der künstliche Intelligenz und automatisierte Systeme eine zentrale Rolle spielen. ^wait(animations/Stand/Gestures/Explain_3)")
            self.animatedSpeechService.say("^start(animations/Stand/Gestures/Explain_3 Das Smart Home Labor, in dem der Professor sein bahnbrechendes Werk vollendet hat, birgt zahlreiche Hinweise, versteckte Rätsel und tiefgehende Geheimnisse. ^wait(animations/Stand/Gestures/Explain_3)")
            self.animatedSpeechService.say("^start(animations/Stand/Gestures/Explain_5) Eure Mission ist klar: Findet heraus, wer den Professor getötet hat, indem ihr seine Forschungen, die Prototypen und die digitale Hinterlassenschaft durchsucht. ^wait(animations/Stand/Gestures/Explain_5)")
            self.animatedSpeechService.say("^start(animations/Stand/Gestures/Explain_7) Doch seid gewarnt, die Zeit arbeitet gegen euch! Ihr habt nur begrenzte Zeit, um den Fall zu lösen und den Mörder zu entlarven. ^wait(animations/Stand/Gestures/Explain_7)")
            self.animatedSpeechService.say("^start(animations/Stand/Gestures/Explain_1) Die Zeit ist gekommen, den Escape Room zu betreten und das Rätsel um den Tod des Professors zu lösen. ^wait(animations/Stand/Gestures/Explain_1)")
            self.animatedSpeechService.say("^start(animations/Stand/Emotions/Positive/Happy_4) Viel Glück, werte Ermittler, und möge die digitale Welt eure Wahrnehmung herausfordern! ^wait(animations/Stand/Emotions/Positive/Happy_4)")
        except Exception as e:
            print("Fehler: ", str(e))

    def stop(self):
        self.animatedSpeechService.unsubscribe("ALAnimatedSpeech")

if __name__ == "__main__":
    app = qi.Application(url="tcp://localhost:9559")
    app.start()
    session = app.session

    speaker_handler = EscapeRoomSpeakerHandler(session)
    speaker_handler.start()

    app.run()
    speaker_handler.stop()

    app.stop()