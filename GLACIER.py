from music import *

#notas
pitches1 = [FS2,CS3,B2,CS3,FS2,CS3,B2,CS3,E2,CS3,B2,CS3,E2,CS3,B2,CS3,D2,CS3,B2,CS3,D2,CS3,B2,CS3,CS2,CS3,B2,CS3,FS3,CS3,B2,CS3]
notes = len(pitches1)
duration1 = [QN]*notes

pitches2 = [B1,E3,D3,E3,FS2,E3,D3,E3,A2,D3,CS3,D3,E2,D3,CS3,D3,GS2,D3,B2,D3,GS2,D3,B2,D3,GS2,D3,B2,D3,FS2,D3,B2,D3,ES2,D3,B2,D3,D2,D3,B2,D3]
notes = len(pitches2)
duration2 = [QN]*notes

pitches3 = [CS2,ES2,CS3,GS2,ES2,GS2,CS3,ES3]
notes = len(pitches3)
duration3 = [QN]*notes

pitches4 = [FS2,E2,FS4,E4,D4,D4,CS3]
notes=len(pitches4)
duration4= [WN*2.2]*notes

pitches5 = [GS4,GS4]
notes=len(pitches5)
duration5= [WN*2.3]*notes

#partes inicio
phrase1 = Phrase(0.0)
phrase1.addNoteList(pitches1, duration1)

phrase2 = Phrase()
phrase2.addNoteList(pitches2, duration2)

phrase3 = Phrase()
phrase3.addNoteList(pitches3, duration3)

phrase4 = Phrase()
phrase4.addNoteList(pitches4, duration4)

#duraciones
intro_duration = len(pitches1) + len(pitches2) + len(pitches3)
chorus_repetition = intro_duration + len(pitches4)

#repeticion melodia principal para coro
phrase1_chorus = Phrase(intro_duration)
phrase1_chorus.addNoteList(pitches1, duration1)

phrase2_chorus = Phrase()
phrase2_chorus.addNoteList(pitches2, duration2)

phrase3_chorus = Phrase()
phrase3_chorus.addNoteList(pitches3, duration3)
#inicio coro
chorusCompany_phrase = Phrase(intro_duration)
chorusCompany_phrase.addNoteList(pitches4, duration4)
chorusCompany_phrase.addNoteList(pitches5, duration5)

mainMelody = Part("Main", PIANO, 0)
#intro
mainMelody.add(phrase1)
mainMelody.add(phrase2)
mainMelody.add(phrase3)
#coro-repeticion melodia
mainMelody.add(phrase1_chorus)
mainMelody.add(phrase2_chorus)
mainMelody.add(phrase3_chorus)

chorusCompany = Part("Harmony", CELLO, 1)
chorusCompany.add(chorusCompany_phrase)

theme = Score("GLACEIR",145)
theme.add(mainMelody)
theme.add(chorusCompany)
Play.setVolume(70, 1)

Play.midi(theme)