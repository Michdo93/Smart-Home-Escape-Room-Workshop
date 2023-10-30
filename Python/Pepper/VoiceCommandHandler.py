# -*- coding: utf-8 -*-
import qi
from openhab import CRUD

class OpenHABVoiceCommandHandler(object):
    def __init__(self, session, openhab_address):
        self.session = session
        self.asr_service = session.service("ALSpeechRecognition")
        self.behavior_service = session.service("ALBehaviorManager")
        self.memory_service = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        self.subscriber = None
        self.crud = CRUD(openhab_address)

    def __on_speech_recognized(self, value):
        recognized_words = value[0]
        confidence = value[1]

        print("Erkannte Worte: {}".format(recognized_words))
        print("Vertrauen: {}".format(confidence))

        if confidence > 0.3:
            if "Pepper, schalte die Lampen in der Küche ein" in recognized_words:
                lampen = self.crud.read("iKueche_Hue_Lampen_Schalter")

                if lampen.get("state") == "ON":
                    self.tts.say("Die Lampen in der Küche sind bereits an")
                else:
                    self.crud.sendCommand("iKueche_Hue_Lampen_Schalter", "ON")
            elif "Pepper, schalte die Lampen in der Küche aus" in recognized_words:
                hue_lampen = self.crud.read("iKueche_Hue_Lampen_Schalter")

                if hue_lampen.get("state") == "OFF":
                    self.tts.say("Die Lampen in der Küche sind bereits aus")
                else:
                    self.crud.sendCommand("iKueche_Hue_Lampen_Schalter", "OFF")
            elif "Pepper, schalte die Lampen in der Küche auf rot" in recognized_words:
                self.crud.sendCommand("iKueche_Hue_Lampen_Farbe", (0, 100, 100))
                self.tts.say("Die Farben der Lampen in der Küche sind jetzt rot")
            elif "Pepper, schalte die Lampen in der Küche auf blau" in recognized_words:
                self.crud.sendCommand("iKueche_Hue_Lampen_Farbe", (240, 100, 100))
                self.tts.say("Die Farben der Lampen in der Küche sind jetzt blau")
            elif "Pepper, schalte die Lampen in der Küche auf grün" in recognized_words:
                self.crud.sendCommand("iKueche_Hue_Lampen_Farbe", (120, 100, 100))
                self.tts.say("Die Farben der Lampen in der Küche sind jetzt grün")
            elif "Pepper, schalte die Lampen im Bad ein" in recognized_words:
                lampen = self.crud.read("iBad_Hue_Lampen_Schalter")

                if lampen.get("state") == "ON":
                    self.tts.say("Die Lampen im Bad sind bereits an")
                else:
                    self.crud.sendCommand("iBad_Hue_Lampen_Schalter", "ON")
            elif "Pepper, schalte die Lampen im Bad aus" in recognized_words:
                lampen = self.crud.read("iBad_Hue_Lampen_Schalter")

                if lampen.get("state") == "OFF":
                    self.tts.say("Die Lampen im Bad sind bereits aus")
                else:
                    self.crud.sendCommand("iBad_Hue_Lampen_Schalter", "OFF")
            elif "Pepper, schalte die Lampen im Bad auf rot" in recognized_words:
                self.crud.sendCommand("iBad_Hue_Lampen_Farbe", (0, 100, 100))
                self.tts.say("Die Farben der Lampen im Bad sind jetzt rot")
            elif "Pepper, schalte die Lampen im Bad auf blau" in recognized_words:
                self.crud.sendCommand("iBad_Hue_Lampen_Farbe", (240, 100, 100))
                self.tts.say("Die Farben der Lampen im Bad sind jetzt blau")
            elif "Pepper, schalte die Lampen im Bad auf grün" in recognized_words:
                self.crud.sendCommand("iBad_Hue_Lampen_Farbe", (120, 100, 100))
                self.tts.say("Die Farben der Lampen im Bad sind jetzt grün")
            elif "Pepper, schalte die Lampen im Ei Oh Ti Raum ein" in recognized_words:
                lampen = self.crud.read("iIoT_Hue_Lampen_Schalter")

                if lampen.get("state") == "ON":
                    self.tts.say("Die Lampen im Ei Oh Ti Raum sind bereits an")
                else:
                    self.crud.sendCommand("iIoT_Hue_Lampen_Schalter", "ON")
            elif "Pepper, schalte die Lampen im Ei Oh Ti Raum aus" in recognized_words:
                lampen = self.crud.read("iIoT_Hue_Lampen_Schalter")

                if lampen.get("state") == "OFF":
                    self.tts.say("Die Lampen im Ei Oh Ti Raum sind bereits aus")
                else:
                    self.crud.sendCommand("iIoT_Hue_Lampen_Schalter", "OFF")
            elif "Pepper, schalte die Lampen im Ei Oh Ti Raum auf rot" in recognized_words:
                self.crud.sendCommand("iIoT_Hue_Lampen_Farbe", (0, 100, 100))
                self.tts.say("Die Farben der Lampen im Ei Oh Ti Raum sind jetzt rot")
            elif "Pepper, schalte die Lampen im Ei Oh Ti Raum auf blau" in recognized_words:
                self.crud.sendCommand("iIoT_Hue_Lampen_Farbe", (240, 100, 100))
                self.tts.say("Die Farben der Lampen im Ei Oh Ti Raum sind jetzt blau")
            elif "Pepper, schalte die Lampen im Ei Oh Ti Raum auf grün" in recognized_words:
                self.crud.sendCommand("iIoT_Hue_Lampen_Farbe", (120, 100, 100))
                self.tts.say("Die Farben der Lampen im Ei Oh Ti Raum sind jetzt grün")
            elif "Pepper, schalte die Lampen im Multimediaraum ein" in recognized_words:
                lampen = self.crud.read("iMultimedia_Hue_Lampen_Schalter")

                if lampen.get("state") == "ON":
                    self.tts.say("Die Lampen im Multimediaraum sind bereits an")
                else:
                    self.crud.sendCommand("iMultimedia_Hue_Lampen_Schalter", "ON")
            elif "Pepper, schalte die Lampen im Multimediaraum aus" in recognized_words:
                lampen = self.crud.read("iMultimedia_Hue_Lampen_Schalter")

                if lampen.get("state") == "OFF":
                    self.tts.say("Die Lampen im Multimediaraum sind bereits aus")
                else:
                    self.crud.sendCommand("iMultimedia_Hue_Lampen_Schalter", "OFF")
            elif "Pepper, schalte die Lampen im Multimediaraum auf rot" in recognized_words:
                self.crud.sendCommand("iMultimedia_Hue_Lampen_Farbe", (0, 100, 100))
                self.tts.say("Die Farben der Lampen im Multimediaraum sind jetzt rot")
            elif "Pepper, schalte die Lampen im Multimediaraum auf blau" in recognized_words:
                self.crud.sendCommand("iMultimedia_Hue_Lampen_Farbe", (240, 100, 100))
                self.tts.say("Die Farben der Lampen im Multimediaraum sind jetzt blau")
            elif "Pepper, schalte die Lampen im Multimediaraum auf grün" in recognized_words:
                self.crud.sendCommand("iMultimedia_Hue_Lampen_Farbe", (120, 100, 100))
                self.tts.say("Die Farben der Lampen im Multimediaraum sind jetzt grün")
            elif "Pepper, führe im Webradio des Konferenzraums SWR3 aus" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, beende das Webradio im Konferenzraum" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, schalte den Beamer ein" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, wechsel den Beamer auf Computer eins" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, wechsel den Beamer auf HDMI zwei" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, wechsel den Beamer auf HDMI eins" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, schalten den Beamer aus" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, stelle den Ausgangszustand des Smart Home Labors wieder her" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, starte die Morgenroutine" in recognized_words:
                print("Derzeit noch nicht implementiert")
            elif "Pepper, spiel Lieder von Linkin Park" in recognized_words:
                print("Derzeit noch nicht implementiert")

    def start(self):
        self.asr_service.setLanguage("German")

        self.asr_service.pause(True)  # ASR-Dienst anhalten
        vocabulary = [
            "Pepper, schalte die Lampen in der Küche ein",
            "Pepper, schalte die Lampen in der Küche aus",
            "Pepper, schalte die Lampen in der Küche auf rot",
            "Pepper, schalte die Lampen in der Küche auf blau",
            "Pepper, schalte die Lampen in der Küche auf grün",
            "Pepper, schalte die Lampen im Bad ein",
            "Pepper, schalte die Lampen im Bad aus",
            "Pepper, schalte die Lampen im Bad auf rot",
            "Pepper, schalte die Lampen im Bad auf blau",
            "Pepper, schalte die Lampen im Bad auf grün",
            "Pepper, schalte die Lampen im Ei Oh Ti Raum ein",
            "Pepper, schalte die Lampen im Ei Oh Ti Raum aus",
            "Pepper, schalte die Lampen im Ei Oh Ti Raum auf rot",
            "Pepper, schalte die Lampen im Ei Oh Ti Raum auf blau",
            "Pepper, schalte die Lampen im Ei Oh Ti Raum auf grün",
            "Pepper, schalte die Lampen im Multimediaraum ein",
            "Pepper, schalte die Lampen im Multimediaraum aus",
            "Pepper, schalte die Lampen im Multimediaraum auf rot",
            "Pepper, schalte die Lampen im Multimediaraum auf blau",
            "Pepper, schalte die Lampen im Multimediaraum auf grün",
            "Pepper, führe im Webradio des Konferenzraums SWR3 aus",
            "Pepper, beende das Webradio im Konferenzraum",
            "Pepper, schalte den Beamer ein",
            "Pepper, wechsel den Beamer auf Computer eins",
            "Pepper, wechsel den Beamer auf HDMI eins",
            "Pepper, wechsel den Beamer auf HDMI zwei",
            "Pepper, schalten den Beamer aus",
            "Pepper, stelle den Ausgangszustand des Smart Home Labors wieder her",
            "Pepper, starte die Morgenroutine",
            "Pepper, spiel Lieder von Linkin Park"
            ]

        self.asr_service.setVocabulary(vocabulary, False)
        self.asr_service.pause(False)  # ASR-Dienst fortsetzen

        self.subscriber = self.memory_service.subscriber("WordRecognized")
        self.subscriber.signal.connect(self.__on_speech_recognized)

        self.asr_service.subscribe("openHAB_ASR")

    def stop(self):
        self.asr_service.unsubscribe("openHAB_ASR")

if __name__ == "__main__":
    app = qi.Application(url="tcp://localhost:9559")
    app.start()
    session = app.session

    voice_handler = OpenHABVoiceCommandHandler(session, "http://192.168.0.5:8080")
    voice_handler.start()

    app.run()
    voice_handler.stop()

    app.stop()