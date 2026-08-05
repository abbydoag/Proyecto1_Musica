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

pitches4 = [FS2,E2,FS3,E3,D3,CS3,B3]
notes=len(pitches4)
duration4= [WN*2.0]*notes

pitches5 = [GS3,D4,GS4]
notes=len(pitches5)
duration5= [WN*2.1]*notes

pitches6 = [B2,E3,D3,E3,B2,E3,D3,E3,A2,D3,CS3,D3,A2,D3,CS3,D3,G2,D3,B2,D3,G2,D3,B2,D3,G2,D3,B2,D3,G2,D3,B2,D3]
notes = len(pitches6)
duration6 = [QN]*notes

pitches7 = [GS2,D3,B2,D3,GS2,D3,B2,D3,GS2,D3,B2,D3,FS2,D3,B2,D3,ES2,D3,B2,D3,D2,D3,B2,D3,CS2,ES2,CS3,GS2,CS3,GS2,CS3,ES3]
notes = len(pitches7)
duration7 = [QN]*notes

#partes inicio
phrase1 = Phrase(0.0)
phrase1.addNoteList(pitches1, duration1)

phrase2 = Phrase()
phrase2.addNoteList(pitches2, duration2)

phrase3 = Phrase()
phrase3.addNoteList(pitches3, duration3)

phrase6 = Phrase()
phrase6.addNoteList(pitches6, duration6)

phrase7 = Phrase()
phrase7.addNoteList(pitches7, duration7)

#duraciones
intro_duration = len(pitches1) + len(pitches2) + len(pitches3)
chorus_repetition = intro_duration + len(pitches4)
intro_chorus_duration = intro_duration*2

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
#melodía 2da parte
mainMelody2_phrase = Phrase(intro_chorus_duration)
mainMelody2_phrase.addNoteList(pitches6, duration6)
mainMelody2_phrase.addNoteList(pitches7, duration7)

mainMelody = Part("Main", PIANO, 0)

#intro
mainMelody.add(phrase1)
mainMelody.add(phrase2)
mainMelody.add(phrase3)
#coro-repeticion melodia
mainMelody.add(phrase1_chorus)
mainMelody.add(phrase2_chorus)
mainMelody.add(phrase3_chorus)
#outro
mainMelody2 = Part("Main2", CELLO, 2)
mainMelody2.add(mainMelody2_phrase)


chorusCompany = Part("Harmony", CHOIR, 1)
chorusCompany.add(chorusCompany_phrase)

theme = Score("GLACEIR",145)
theme.add(mainMelody)
theme.add(chorusCompany)
theme.add(mainMelody2)
Play.setVolume(90, 1)

Play.midi(theme)