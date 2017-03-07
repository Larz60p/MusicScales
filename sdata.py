#
# MIT License
#
# Copyright (c) 2017 Larz60+
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
#    A Huge amount of Credit goes to  Francesco Balena, http://www.saxopedia.com
#    for his tremendous work on the publication 'The Scale Omnibus' which was my major
#    source for Interval patterns of scales from around the world.
#
#    All scores were created using lilypond -LilyPond is a music engraving program,
#    devoted to producing the highest-quality sheet music possible. It brings the
#    aesthetics of traditionally engraved music to computer printouts. LilyPond is
#    free software and part of the GNU Project.
#    Available at: http://www.lilypond.org/
#
#    If you have new material, including scales which you have created, please send
#    that information to me and to Francesco, along with a publication release, and
#    I will try and add it to the next software release
#
import collections


class McData:
    def __init__(self):
        self.lilypond_conversion = {
            'C': 'c', 'C#': 'cis', 'Db': 'des', 'D': 'd', 'D#': 'dis',
            'Eb': 'ees', 'E': 'e', 'F': 'f', 'F#': 'fis', 'Gb': 'ges',
            'G': 'g', 'G#': 'gis', 'Ab': 'aes', 'A': 'a', 'A#': 'ais',
            'Bb': 'bes', 'B': 'b', 'B#': 'bis', 'Cb': 'ces'
        }

        self.note = {
            'C': dict(id=1, next_note='C#', prev_note='B', sharpen='C#', flatten='B'),
            'C#': dict(id=2, next_note='D', prev_note='C', sharpen='C##', flatten='C'),
            'C##': dict(id=3, next_note='D#', prev_note='C#', sharpen='C###', flatten='C#'),
            'C###': dict(id=4, next_note='E', prev_note='D', sharpen='E', flatten='C##'),
            'Dbbb': dict(id=12, next_note='C', prev_note='Bb', sharpen='C', flatten='Dbb'),
            'Dbb': dict(id=1, next_note='Db', prev_note='B', sharpen='Db', flatten='Dbbb'),
            'Db': dict(id=2, next_note='D', prev_note='C', sharpen='D', flatten='C'),
            'D': dict(id=3, next_note='D#', prev_note='C#', sharpen='D#', flatten='Db'),
            'D#': dict(id=4, next_note='E', prev_note='D', sharpen='D##', flatten='D'),
            'D##': dict(id=5, next_note='F', prev_note='D#', sharpen='D###', flatten='D#'),
            'D###': dict(id=6, next_note='F#', prev_note='E', sharpen='F#', flatten='D##'),
            'Ebbb': dict(id=2, next_note='D', prev_note='C', sharpen='D', flatten='Ebb'),
            'Ebb': dict(id=3, next_note='Eb', prev_note='Db', sharpen='Ebbb', flatten='Eb'),
            'Eb': dict(id=4, next_note='E', prev_note='D', sharpen='E', flatten='D'),
            'E': dict(id=5, next_note='F', prev_note='D#', sharpen='E#', flatten='Eb'),
            'E#': dict(id=6, next_note='F#', prev_note='E', sharpen='E##', flatten='E'),
            'E##': dict(id=7, next_note='G', prev_note='F', sharpen='E###', flatten='E#'),
            'E###': dict(id=8, next_note='G#', prev_note='F#', sharpen='G#', flatten='E##'),
            'Fbbb': dict(id=3, next_note='Eb', prev_note='Db', sharpen='Fbb', flatten='Db'),
            'Fbb': dict(id=4, next_note='E', prev_note='D', sharpen='Fb', flatten='Fbbb'),
            'Fb': dict(id=5, next_note='F', prev_note='Eb', sharpen='F', flatten='Fbb'),
            'F': dict(id=6, next_note='F#', prev_note='E', sharpen='F#', flatten='E'),
            'F#': dict(id=7, next_note='G', prev_note='F', sharpen='F##', flatten='F'),
            'F##': dict(id=8, next_note='G#', prev_note='F#', sharpen='F###', flatten='F#'),
            'F###': dict(id=9, next_note='A', prev_note='G', sharpen='A', flatten='F##'),
            'Gbbb': dict(id=5, next_note='F', prev_note='Eb', sharpen='Gbb', flatten='Eb'),
            'Gbb': dict(id=6, next_note='Gb', prev_note='E', sharpen='Gb', flatten='Gbbb'),
            'Gb': dict(id=7, next_note='G', prev_note='F', sharpen='G', flatten='F'),
            'G': dict(id=8, next_note='G#', prev_note='F#', sharpen='G#', flatten='Gb'),
            'G#': dict(id=9, next_note='A', prev_note='G', sharpen='G##', flatten='G'),
            'G##': dict(id=10, next_note='A#', prev_note='G#', sharpen='G###', flatten='G#'),
            'G###': dict(id=11, next_note='B', prev_note='A', sharpen='B', flatten='G##'),
            'Abbb': dict(id=7, next_note='G', prev_note='F', sharpen='Abb', flatten='F'),
            'Abb': dict(id=8, next_note='Ab', prev_note='Gb', sharpen='Ab', flatten='Abbb'),
            'Ab': dict(id=9, next_note='A', prev_note='G', sharpen='A', flatten='Abb'),
            'A': dict(id=10, next_note='A#', prev_note='G#', sharpen='A#', flatten='G#'),
            'A#': dict(id=11, next_note='B', prev_note='A', sharpen='A##', flatten='A'),
            'A##': dict(id=12, next_note='C', prev_note='A#', sharpen='A###', flatten='A#'),
            'A###': dict(id=1, next_note='C#', prev_note='B', sharpen='C#', flatten='A##'),
            'Bbbb': dict(id=9, next_note='A', prev_note='G', sharpen='Bbb', flatten='G'),
            'Bbb': dict(id=10, next_note='Bb', prev_note='Ab', sharpen='Bb', flatten='Bbbb'),
            'Bb': dict(id=11, next_note='B', prev_note='A', sharpen='B', flatten='Bbb'),
            'B': dict(id=12, next_note='C', prev_note='A#', sharpen='C', flatten='Bb'),
            'B#': dict(id=1, next_note='C#', prev_note='B', sharpen='B##', flatten='B'),
            'B##': dict(id=2, next_note='D', prev_note='C', sharpen='B###', flatten='B#'),
            'B###': dict(id=3, next_note='D#', prev_note='C#', sharpen='D#', flatten='B##'),
            'Cbbb': dict(id=10, next_note='Bb', prev_note='Ab', sharpen='Cbb', flatten='Ab'),
            'Cbb': dict(id=11, next_note='B', prev_note='A', sharpen='Cb', flatten='Cbbb'),
            'Cb': dict(id=12, next_note='C', prev_note='Bb', sharpen='C', flatten='Cbb')
        }

        # TODO This is named id_xref1 in sdata
        self.id_xref = {
            1: ['C', 'B#', 'A###', 'Dbb'],
            2: ['C#', 'Db', 'B##', 'Ebbb'],
            3: ['D', 'B###', 'C##', 'Ebb', 'Fbbb'],
            4: ['D#', 'C###', 'Eb', 'Fbb'],
            5: ['E', 'D##', 'Fb', 'Gbbb'],
            6: ['F', 'E#', 'D###', 'Gbb'],
            7: ['F#', 'E##', 'Gb', 'Abb'],
            8: ['G', 'E###', 'F##', 'Abb'],
            9: ['G#', 'F###', 'Ab', 'Bbbb'],
            10: ['A', 'G##', 'Bbb', 'Cbbb'],
            11: ['A#', 'G###', 'Bb', 'Cbb'],
            12: ['B', 'A##', 'Cb', 'Dbbb']
        }

        # TODO Generate this with code
        self.xref = {
            'Major and Minor Scales': {
                'Major': 'Major',
                'Ionian': 'Major',
                'Peruvian Major': 'Major',
                'Ghana Heptatonic': 'Major',
                'Ararai': 'Major',
                'Xin': 'Major',
                'Maqam Cargah': 'Major',
                'Ajam Ashiran': 'Major',
                'Dastgah-e Mahur': 'Major',
                'Dastgah-e Rastpanjah': 'Major',
                'Raga Bilaval That': 'Major',
                'Raga Arabhi Descending': 'Major',
                'Raga Bilahari Descending': 'Major',
                'Mela Shankarabharanam': 'Major',
                'Dorian': 'Dorian',
                'Gregorian 8': 'Dorian',
                'Mischung 5': 'Dorian',
                'Yu': 'Dorian',
                'Hyojo': 'Dorian',
                'Oshikicho': 'Dorian',
                'Nam': 'Dorian',
                'Raga Kafi That': 'Dorian',
                'Mela Kharaharapriya': 'Dorian',
                'Raga Bhairavi Ascending': 'Dorian',
                'Raga Kharapriya': 'Dorian',
                'Raga Shree Descending': 'Dorian',
                'Raga Bhimpalasi': 'Dorian',
                'Raga Nayaki Kanada': 'Dorian',
                'Raga Sri': 'Dorian',
                'Raga Ritigaula': 'Dorian',
                'Raga Huseni': 'Dorian',
                'Raga Kanara': 'Dorian',
                'Raga Bageshri': 'Dorian',
                'Phrygian': 'Phrygian',
                'Major Inverse': 'Phrygian',
                'Ousak': 'Phrygian',
                'Zokuso': 'Phrygian',
                'Maqam Kurd': 'Phrygian',
                'Raga Dhanyasi Descending': 'Phrygian',
                'Mela Hanumatodi': 'Phrygian',
                'Mela Bhairavi That': 'Phrygian',
                'Raga Bilashkhani Todi': 'Phrygian',
                'Raga Ghanta': 'Phrygian',
                'Lydian': 'Lydian',
                'Ping': 'Lydian',
                'Gu': 'Lydian',
                'Mela Mecakalyani': 'Lydian',
                'Raga Shuddh Kalyan': 'Lydian',
                'Raga Kalyan That': 'Lydian',
                'Mixolydian': 'Mixolydian',
                'Gregorian 2': 'Mixolydian',
                'Mischung 3': 'Mixolydian',
                'Shang': 'Mixolydian',
                'Mela Harikamboji': 'Mixolydian',
                'Raga Kambodhi Descending': 'Mixolydian',
                'Raga Khamaj That': 'Mixolydian',
                'Raga Janjhuti': 'Mixolydian',
                'Raga Harini': 'Mixolydian',
                'Raga Khambhavati': 'Mixolydian',
                'Raga Surati': 'Mixolydian',
                'Raga Balahamsa': 'Mixolydian',
                'Aeolian': 'Aeolian',
                'Peruvian Minor': 'Aeolian',
                'Cushak': 'Aeolian',
                'Ezel': 'Aeolian',
                'Geez': 'Aeolian',
                'Se': 'Aeolian',
                'Raga Bhairavi Descending': 'Aeolian',
                'Mela Natabhairavi': 'Aeolian',
                'Raga Jaunpuri': 'Aeolian',
                'Raga Adana': 'Aeolian',
                'Raga Jingla': 'Aeolian',
                'Raga Asavari That': 'Aeolian',
                'Locrian': 'Locrian',
                'Pien Chih': 'Locrian',
                'Makam Lami': 'Locrian',
                'Yishtabach': 'Locrian',
                'Melodic Minor': 'Melodic Minor',
                'Ascending Minor': 'Melodic Minor',
                'Mischung 1': 'Melodic Minor',
                'Mela Gaurimanohari': 'Melodic Minor',
                'Raga Patdip': 'Melodic Minor',
                'Raga Velavali': 'Melodic Minor',
                'Raga Deshi 2': 'Melodic Minor',
                'Dorian b2': 'Dorian b2',
                'Jazz Minor Inverse': 'Dorian b2',
                'Phrygian Natural 6': 'Dorian b2',
                'Phrygian Mixolydian': 'Dorian b2',
                'Javanese': 'Dorian b2',
                'Mela Natakapriya': 'Dorian b2',
                'Raga Natabharanam': 'Dorian b2',
                'Raga Ahiri Todi': 'Dorian b2',
                'Lydian Augmented': 'Lydian Augmented',
                'Lydian #5': 'Lydian Augmented',
                'Altered Lydian': 'Lydian Augmented',
                'Lydian Dominant': 'Lydian Dominant',
                'Lydian b7': 'Lydian Dominant',
                'Mixolydian #4': 'Lydian Dominant',
                'Bartok': 'Lydian Dominant',
                'Acoustic': 'Lydian Dominant',
                'Overtone': 'Lydian Dominant',
                'Mela Vacaspati': 'Lydian Dominant',
                'Raga Bhusavati': 'Lydian Dominant',
                'Bhusavali': 'Lydian Dominant',
                'Melodic Major': 'Melodic Major',
                'Mixolydian b6': 'Melodic Major',
                'Mixolydian b13': 'Melodic Major',
                'Aeolian Major': 'Melodic Major',
                'Major Minor': 'Melodic Major',
                'Mischung 6': 'Melodic Major',
                'Hindu': 'Melodic Major',
                'Maqam Ussak': 'Melodic Major',
                'Mela Carukesi': 'Melodic Major',
                'Raga Tarangini': 'Melodic Major',
                'Half Diminished': 'Half Diminished',
                'Semilocrian': 'Half Diminished',
                'Locrian Natural 2': 'Half Diminished',
                'Minor Locrian': 'Half Diminished',
                'Minor b5': 'Half Diminished',
                'Altered Diminished': 'Half Diminished',
                'Altered Dominant': 'Altered Dominant',
                'Altered': 'Altered Dominant',
                'Superlocrian': 'Altered Dominant',
                'Locrian b4': 'Altered Dominant',
                'Pomeroy': 'Altered Dominant',
                'Ravel': 'Altered Dominant',
                'Harmonic Minor': 'Harmonic Minor',
                'Mischung 4': 'Harmonic Minor',
                'Mohammedan': 'Harmonic Minor',
                'Maqam Bayat-e-Esfahan': 'Harmonic Minor',
                'Maqam Sultani Yakah': 'Harmonic Minor',
                'Sultani Yakah': 'Harmonic Minor',
                'Zhalibny Minor': 'Harmonic Minor',
                'Raga Pilu That': 'Harmonic Minor',
                'Mela Kiravani': 'Harmonic Minor',
                'Raga Kiranavali': 'Harmonic Minor',
                'Raga Kirvani': 'Harmonic Minor',
                'Raga Kalyana Vasantha': 'Harmonic Minor',
                'Raga Deshi 3': 'Harmonic Minor',
                'Locrian #6': 'Locrian #6',
                'Locrian Natural Maj6': 'Locrian #6',
                'Dorian b9': 'Locrian #6',
                'Ionian Augmented': 'Ionian Augmented',
                'Romanian Minor': 'Romanian Minor',
                'Dorian #4': 'Romanian Minor',
                'Gnossiennes': 'Romanian Minor',
                'Ukranian Dorian': 'Romanian Minor',
                'Tunisian': 'Romanian Minor',
                'Kaffa': 'Romanian Minor',
                'Maqam Hedjaz': 'Romanian Minor',
                'Maqam Nakriz': 'Romanian Minor',
                'Misheberekh': 'Romanian Minor',
                'Nigriz': 'Romanian Minor',
                'Peiraiotikos Minor': 'Romanian Minor',
                'Souzinak': 'Romanian Minor',
                'Ukrainian Minor': 'Romanian Minor',
                'Mela Hemavati': 'Romanian Minor',
                'Raga Desisimharavam': 'Romanian Minor',
                'Phrygian Dominant': 'Phrygian Dominant',
                'Phrygian Major': 'Phrygian Dominant',
                'Harmonic Major Inverse': 'Phrygian Dominant',
                'Spanish': 'Phrygian Dominant',
                'Spanish Gipsy': 'Phrygian Dominant',
                'Zilof': 'Phrygian Dominant',
                'Dorico Flamenco': 'Phrygian Dominant',
                'Jewish': 'Phrygian Dominant',
                'Avaha': 'Phrygian Dominant',
                'Ahava Rabba': 'Phrygian Dominant',
                'Freygish': 'Phrygian Dominant',
                'Fraigish': 'Phrygian Dominant',
                'Hitzaz': 'Phrygian Dominant',
                'Hijaz': 'Phrygian Dominant',
                'Alhijaz': 'Phrygian Dominant',
                'Maqam Humayun': 'Phrygian Dominant',
                'Maqam Zengule': 'Phrygian Dominant',
                'Maqam Hijaz-Nahawand': 'Phrygian Dominant',
                'Humayun': 'Phrygian Dominant',
                'Mela': 'Phrygian Dominant',
                'Vakulabharanam': 'Phrygian Dominant',
                'Raga Jogiya': 'Phrygian Dominant',
                'Raga Vativasanta': 'Phrygian Dominant',
                'Lydian #2': 'Lydian #2',
                'Mela Kosalam': 'Lydian #2',
                'Raga Kuksumakaram': 'Lydian #2',
                'Raga Kusumakaram': 'Lydian #2',
                'Ultralocrian': 'Ultralocrian',
                'Mixolydian #1': 'Ultralocrian'
            },
            'Symmetrical Scales': {
                'Whole-Tone': 'Whole-Tone',
                'Hexatonic': 'Whole-Tone',
                'Anhemitonic Hexatonic': 'Whole-Tone',
                'Messiaen 1 Mode': 'Whole-Tone',
                'Raga Sahera': 'Whole-Tone',
                'Raga Gopriya': 'Whole-Tone',
                'Augmented': 'Augmented',
                'Major Augmented': 'Augmented',
                'Messiaen Truncated 3 Mode Inverse': 'Augmented',
                'Genus Tertium': 'Augmented',
                'Raga Devamani': 'Augmented',
                'Inverted Augmented': 'Inverted Augmented',
                'Prometheus Liszt': 'Inverted Augmented',
                'Diminished': 'Diminished',
                'Octatonic': 'Diminished',
                'Whole-Tone Diminished': 'Diminished',
                'Messiaen 2nd Mode Inverse': 'Diminished',
                'Modus Conjunctus': 'Diminished',
                'Diminished Half-tone': 'Diminished Half-tone',
                'Messiaen 2nd Mode': 'Diminished Half-tone',
                'Chromatic': 'Chromatic',
                'Tritone': 'Tritone',
                'Petrushka chord': 'Tritone',
                'Raga Neelangi': 'Raga Neelangi',
                'Messiaen 2nd Mode Truncated': 'Messiaen 2nd Mode Truncated',
                'Messiaen 3rd Mode': 'Messiaen 3rd Mode',
                'Messiaen 4th Mode': 'Messiaen 4th Mode',
                'Messiaen 4th Mode Inverse': 'Messiaen 4th Mode Inverse',
                'Messiaen 5th Mode': 'Messiaen 5th Mode',
                'Messiaen 5th Mode Inverse': 'Messiaen 5th Mode Inverse',
                'Messiaen 6th Mode': 'Messiaen 6th Mode',
                'Messiaen 6th Mode Inverse': 'Messiaen 6th Mode Inverse',
                'Messiaen 7th Mode': 'Messiaen 7th Mode',
                'Messiaen 7th Mode Inverse': 'Messiaen 7th Mode Inverse',
                'Genus Chromaticum': 'Genus Chromaticum',
                'Messiaen 3rd Mode Inverse': 'Genus Chromaticum',
                'Tcherepnin': 'Genus Chromaticum',
                'Two-semitone Tritone': 'Two-semitone Tritone',
                'Symmetrical Decatonic': 'Symmetrical Decatonic',
                'Van Der Host': 'Van Der Host'
            },
            'Jazz Scales': {
                'Blues': 'Blues',
                'Blues Hexatonic': 'Blues', 'Raga Nileshwari': 'Blues',
                'Blues Heptatonic': 'Blues Heptatonic',
                'Dorian b5': 'Blues Heptatonic',
                'Kartzihiar': 'Blues Heptatonic',
                'Maqam Karcigar': 'Blues Heptatonic',
                'Maqam Nahawand Murassah': 'Blues Heptatonic',
                'Blues Heptatonic 2': 'Blues Heptatonic 2',
                'Blues Octatonic': 'Blues Octatonic',
                'Blues Enneatonic': 'Blues Enneatonic',
                'Major-Dorian Mixed': 'Blues Enneatonic',
                'Raga Malgunji': 'Blues Enneatonic',
                'Raga Ramdasi Malhar': 'Blues Enneatonic',
                'Blues Enneatonic 2': 'Blues Enneatonic 2',
                'Blues Dorian Hexatonic': 'Blues Dorian Hexatonic',
                'Blues Phrygian': 'Blues Phrygian',
                'Blues Minor Maj7': 'Blues Minor Maj7',
                'Blues Modified': 'Blues Modified',
                'Blues Mixed': 'Blues Mixed',
                'Blues Leading Tone': 'Blues Leading Tone',
                "Rock 'n Roll": "Rock 'n Roll",
                'Mela Vagadhisvari': "Rock 'n Roll",
                'Raga Bhogachayanata': "Rock 'n Roll",
                'Raga Ganavaridhi': "Rock 'n Roll",
                'Raga Chayanata': "Rock 'n Roll",
                'Raga Nandkauns': "Rock 'n Roll",
                'Bebop': 'Bebop',
                'Bebop Dominant': 'Bebop',
                'Bebop Mixolydian': 'Bebop',
                'Major Mixolydian': 'Bebop',
                'Gregorian 6': 'Bebop',
                'Genus Diatonicum': 'Bebop',
                'Chinese': 'Bebop',
                'Eight-Tone': 'Bebop',
                'Rast': 'Bebop',
                'Maqam Shawq Awir': 'Bebop',
                'Raga Khamaj': 'Bebop',
                'Raga Desh Malhar': 'Bebop',
                'Raga Alhaiya Bilaval': 'Bebop',
                'Raga': 'Bebop',
                'Bihagara': 'Bebop',
                'Raga Devagandhari': 'Bebop',
                'Bebop Major': 'Bebop Major',
                'Bebop Major Hexatonic': 'Bebop Major Hexatonic',
                'Bebop Major Heptatonic': 'Bebop Major Heptatonic',
                'Bebop Minor': 'Bebop Minor',
                'Banshikicho': 'Bebop Minor',
                'Bebop Dorian': 'Bebop Dorian',
                'Mixolydian Dorian': 'Bebop Dorian',
                'Raga Zilla': 'Bebop Dorian',
                'Bebop Melodic Minor': 'Bebop Melodic Minor',
                'Zirafkend': 'Bebop Melodic Minor',
                'Bebop Harmonic Minor': 'Bebop Harmonic Minor',
                'Bebop Natural Minor': 'Bebop Harmonic Minor',
                'Utility Minor': 'Bebop Harmonic Minor',
                'Gregorian 4': 'Bebop Harmonic Minor',
                'Maqam Nahawand': 'Bebop Harmonic Minor',
                'Maqam Farahfaza': 'Bebop Harmonic Minor',
                'Raga Suha Kanada': 'Bebop Harmonic Minor',
                'Bebop Half-diminished': 'Bebop Half-diminished',
                'Bebop Locrian': 'Bebop Locrian',
                'Phrygian Locrian': 'Bebop Locrian',
                'Bebop Chromatic': 'Bebop Chromatic'
            },
            'Pentatonic Scales': {
                'Major Pentatonic': 'Major Pentatonic',
                'Ryosen': 'Major Pentatonic',
                'Yona Nuki Major': 'Major Pentatonic',
                'Man Jue': 'Major Pentatonic',
                'Gong': 'Major Pentatonic',
                'Peruvian Major': 'Major Pentatonic',
                'Pentatonic': 'Major Pentatonic',
                'Ghana Pentatonic 2': 'Major Pentatonic',
                'Tezeta Major': 'Major Pentatonic',
                'Raga Bilahari Ascending': 'Major Pentatonic',
                'Raga Mohanam': 'Major Pentatonic',
                'Raga Bhopali': 'Major Pentatonic',
                'Raga Deskar': 'Major Pentatonic',
                'Raga Kokila': 'Major Pentatonic',
                'Raga Jait Kalyan': 'Major Pentatonic',
                'Raga Bhup': 'Major Pentatonic',
                'Suspended Pentatonic': 'Suspended Pentatonic',
                'Egyptian': 'Suspended Pentatonic',
                'Shang-Diao': 'Suspended Pentatonic',
                'Jin-Yu': 'Suspended Pentatonic',
                'Quin-Yu': 'Suspended Pentatonic',
                'Rui Bin': 'Suspended Pentatonic',
                'Raga Madhmat Sarang': 'Suspended Pentatonic',
                'Raga Madhyamavati': 'Suspended Pentatonic',
                'Man Gong': 'Man Gong',
                'Blues Minor': 'Man Gong',
                'Minyo': 'Man Gong',
                'Jiao': 'Man Gong',
                'Quan Ming': 'Man Gong',
                'Yi Ze': 'Man Gong',
                'Raga Hindolam': 'Man Gong',
                'Ritusen': 'Ritusen',
                'Blues Major': 'Ritusen',
                'Scottish Pentatonic': 'Ritusen',
                'Yo': 'Ritusen',
                'Ritsu Gagaku': 'Ritusen',
                'Ujo': 'Ritusen', 'Zhi': 'Ritusen',
                'Zheng': 'Ritusen',
                'Bac': 'Ritusen',
                'Lai Soutsanaen': 'Ritusen',
                'Lai Po Sai': 'Ritusen',
                'Lai Soi': 'Ritusen',
                'Raga Arabhi Ascending': 'Ritusen',
                'Raga Devakriya': 'Ritusen',
                'Raga Shree Ascending': 'Ritusen',
                'Raga Yadukua Kambodhi Ascending': 'Ritusen',
                'Raga Suddha Saveri': 'Ritusen',
                'Minor Pentatonic': 'Minor Pentatonic',
                'Blues Minor Pentatonic': 'Minor Pentatonic',
                'Peruvian Minor Pentatonic': 'Minor Pentatonic',
                'Bati': 'Minor Pentatonic',
                'Qing Shang': 'Minor Pentatonic',
                'Gu Xian': 'Minor Pentatonic',
                'Jia Zhong': 'Minor Pentatonic',
                'Yu 2': 'Minor Pentatonic',
                "P'yongjo-kyemyonjo": 'Minor Pentatonic',
                'Lai Yai': 'Minor Pentatonic',
                'Lai Noi': 'Minor Pentatonic',
                'Raga Dhani': 'Minor Pentatonic',
                'Raga Abheri': 'Minor Pentatonic',
                'Raga Dhaanyasi Ascending': 'Minor Pentatonic',
                'Raga Udhayaravi': 'Minor Pentatonic',
                'Dorian Pentatonic': 'Dorian Pentatonic',
                'Kumoi': 'Dorian Pentatonic',
                'Kokin-Choshi': 'Kokin-Choshi',
                'Ian Iwato': 'Kokin-Choshi',
                'Miyakobushi': 'Kokin-Choshi',
                'Insen Pentatonic': 'Kokin-Choshi',
                'Soft Ascend': 'Kokin-Choshi',
                'Raga Bairagi': 'Kokin-Choshi',
                'Raga Baira': 'Kokin-Choshi',
                'Raga Lasaki': 'Kokin-Choshi',
                'Raga Ribhavari': 'Kokin-Choshi',
                'Raga Revati': 'Kokin-Choshi',
                'Raga Hindol': 'Raga Hindol',
                'Raga Sunada Vinodini': 'Raga Hindol',
                'Raga Sanjk Ka Hindol': 'Raga Hindol',
                'Han-Kumoi': 'Han-Kumoi',
                'Raga Shobhavari': 'Han-Kumoi',
                'Raga Sutradhari': 'Han-Kumoi',
                'Minor Pentatonic 7 b5': 'Minor Pentatonic 7 b5',
                'Raga Jayakauns': 'Minor Pentatonic 7 b5',
                'Ionian Pentatonic': 'Ionian Pentatonic',
                'Ryukyu': 'Ionian Pentatonic',
                'Pelog Degung Modern': 'Ionian Pentatonic',
                'Melog Selisir': 'Ionian Pentatonic',
                'Raga Jaganmohini Ascending': 'Ionian Pentatonic',
                'Raga Gambhiranata': 'Ionian Pentatonic',
                'Pelog Pentatonic': 'Pelog Pentatonic',
                'Belinese': 'Pelog Pentatonic',
                'Phrygian Pentatonic': 'Pelog Pentatonic',
                'Madenda Modern': 'Pelog Pentatonic',
                'Tezeta Minor': 'Pelog Pentatonic',
                'Raga Bhupalam': 'Pelog Pentatonic',
                'Raga Ramkali 2': 'Pelog Pentatonic',
                'Raga Hamsanada': 'Raga Hamsanada',
                'Raga Vaijayanti': 'Raga Hamsanada',
                'Raga Khamaji Durga': 'Raga Khamaji Durga',
                'Dominant Pentatonic': 'Dominant Pentatonic',
                'Chaio': 'Chaio',
                'Chin': 'Chin', 'Raga Harikauns': 'Chin',
                'Kyemyonjo': 'Kyemyonjo',
                'Minor 6th Added': 'Kyemyonjo',
                'Hybrid Pentatonic': 'Kyemyonjo',
                'Kung': 'Kung',
                'In': 'In',
                'Sakura': 'In',
                'Naka Zora': 'In', 'Soft Descend': 'In',
                'Ambassel': 'In', 'Olympos Enharmonic': 'In',
                'Raga Saveri Ascending': 'In',
                'Raga Gunkali': 'In', 'Raga Kunakri': 'In',
                'Raga Latantapryia': 'In',
                'Raga Salanganata': 'In',
                'Hirajoshi': 'Hirajoshi',
                'Lydian Pentatonic': 'Hirajoshi',
                'Chinese': 'Hirajoshi',
                'Ching': 'Hirajoshi',
                'Raga Amrtavarshini': 'Hirajoshi',
                'Raga Malashri': 'Hirajoshi',
                'Raga Shilangi': 'Hirajoshi',
                'Ake-Bono': 'Ake-Bono',
                'Aeolian Pentatonic': 'Ake-Bono',
                'Kata-Kumoi': 'Ake-Bono',
                'Yona Nuki Minor': 'Ake-Bono',
                'Iwato': 'Iwato',
                'Aeolian Harmonic': 'Iwato',
                'Zokuso Pentatonic': 'Iwato',
                'Hon-Kumoi-Joshi': 'Iwato',
                'Major Pentatonic b2': 'Major Pentatonic b2',
                'Scriabin': 'Major Pentatonic b2',
                'Raga Bibhas': 'Major Pentatonic b2',
                'Raga Rasika Ranjani': 'Major Pentatonic b2',
                'Major Pentatonic b2 b5': 'Major Pentatonic b2 b5',
                'Major Pentatonic b3': 'Major Pentatonic b3',
                'Major Pentatonic b6': 'Major Pentatonic b6',
                'Raga Bhupeshwari': 'Major Pentatonic b6',
                'Raga Janasammodini': 'Major Pentatonic b6',
                'Major Pentatonic b7 #9': 'Major Pentatonic b7 #9',
                'Diminished Pentatonic': 'Diminished Pentatonic',
                'Mixolydian Pentatonic': 'Mixolydian Pentatonic',
                'Jog': 'Mixolydian Pentatonic',
                'Raga Savethri': 'Mixolydian Pentatonic',
                'Tcherepnin Major Pentatonic': 'Tcherepnin Major Pentatonic',
                'Raga Desh': 'Tcherepnin Major Pentatonic',
                'Altered Pentatonic': 'Altered Pentatonic',
                'Raga Manaranjani 2': 'Altered Pentatonic',
                'Altered Major Pentatonic': 'Altered Major Pentatonic',
                'Locrian Pentatonic': 'Locrian Pentatonic',
                'Pentatonic Whole-Tone': 'Pentatonic Whole-Tone',
                'Augmented Pentatonic': 'Augmented Pentatonic',
                'Augmented Pentatonic 2': 'Augmented Pentatonic 2',
                'Center-Cluster PentaMirror': 'Center-Cluster PentaMirror',
                'Raga Nagaswaravali': 'Raga Nagaswaravali',
                'Raga Mand': 'Raga Nagaswaravali',
                'Raga Chitthakarshini': 'Raga Chitthakarshini',
                'Raga Hamsadhvani 2': 'Raga Hamsadhvani 2',
                'Pyeong Jo': 'Pyeong Jo',
                'Raga Guhamanohari': 'Pyeong Jo',
                'Raga Shailaja': 'Raga Shailaja',
                'Raga Varini': 'Raga Shailaja',
                'Pygmy': 'Pygmy',
                'Raga Mamata': 'Raga Mamata',
                'Raga Kokil Pancham': 'Raga Kokil Pancham',
                'Romanian Bacovia': 'Romanian Bacovia',
                'Raga Girija': 'Romanian Bacovia',
                'Greek Arkaik': 'Greek Arkaik',
                'Syrian Pentatonic': 'Syrian Pentatonic',
                'Raga Megharanjani': 'Syrian Pentatonic'
            },
            'Modal Scales': {
                'Ionian b5': 'Ionian b5',
                'Ionian #5': 'Ionian #5',
                'Ionian Augmented #2': 'Ionian Augmented #2',
                'Ionian Augmented b9': 'Ionian Augmented b9',
                'Minor Hexatonic': 'Minor Hexatonic',
                'Raga Manirangu': 'Minor Hexatonic',
                'Raga Nayaki': 'Minor Hexatonic',
                'Raga Palasi': 'Minor Hexatonic',
                'Raga Pushpalithika': 'Minor Hexatonic',
                'Raga Suha Sughrai': 'Minor Hexatonic',
                'Major Locrian': 'Major Locrian',
                'Jazz Minor #5': 'Jazz Minor #5',
                'Full Minor All Flats': 'Full Minor All Flats',
                'Raga Pilu': 'Full Minor All Flats',
                'Dorian Aeolian': 'Dorian Aeolian',
                'Gregorian 1': 'Dorian Aeolian',
                'Raga Anandabhairavi': 'Dorian Aeolian',
                'Raga Deshi': 'Dorian Aeolian',
                'Raga Mukhari': 'Dorian Aeolian',
                'Raga Manji': 'Dorian Aeolian',
                'Dorian b2 b4': 'Dorian b2 b4',
                'Dorian b2 Maj7': 'Dorian b2 Maj7',
                'Dorian b9 #11': 'Dorian b9 #11',
                'Todi b7': 'Dorian b9 #11',
                'Hindi b2 b3': 'Dorian b9 #11',
                'b7': 'Dorian b9 #11',
                'Raga Sthavarajam': 'Dorian b9 #11',
                'Raga Tivravahini': 'Dorian b9 #11',
                'Mela Sadvidhmargini': 'Dorian b9 #11',
                'Phrygian Hexatonic': 'Phrygian Hexatonic',
                'Raga Desya Todi': 'Phrygian Hexatonic',
                'Raga Gopikavasantam': 'Phrygian Hexatonic',
                'Phrygian Aeolian b4': 'Phrygian Aeolian b4',
                'Phrygian Aeolian Mixed': 'Phrygian Aeolian b4',
                'Phrygian b4': 'Phrygian b4',
                'Maqam Huzzam': 'Phrygian b4',
                'Maqam Saba Zamzam': 'Phrygian b4',
                'Phrygian b4 Maj7': 'Phrygian b4 Maj7',
                'Double Phrygian': 'Double Phrygian',
                'Ultraphrygian': 'Ultraphrygian',
                'Lydian Hexatonic': 'Lydian Hexatonic',
                'Raga Kumud': 'Lydian Hexatonic',
                'Raga Sankara': 'Lydian Hexatonic',
                'Raga Shankara': 'Lydian Hexatonic',
                'Raga Prabhati': 'Lydian Hexatonic',
                'Lydian #2 Hexatonic': 'Lydian #2 Hexatonic',
                'Lydian #2 #6': 'Lydian #2 #6',
                'Mela Rasikapriya': 'Lydian #2 #6',
                'Raga Hamsagiri': 'Lydian #2 #6',
                'Raga Rasamanjari': 'Lydian #2 #6',
                'Lydian Dominant b6': 'Lydian Dominant b6',
                'Lydian Minor': 'Lydian Dominant b6',
                'Raga Rishabapriya': 'Lydian Dominant b6',
                'Raga Ratipriya': 'Lydian Dominant b6',
                'Lydian Mixolydian': 'Lydian Mixolydian',
                'Taishikicho': 'Lydian Mixolydian',
                'Ryo': 'Lydian Mixolydian',
                'Lydian Diminished': 'Lydian Diminished',
                'Lydian b3': 'Lydian Diminished',
                'Melodic Minor #4': 'Lydian Diminished',
                'Mela Dharmavati': 'Lydian Diminished',
                'Raga Ambika': 'Lydian Diminished',
                'Raga Arunajualita': 'Lydian Diminished',
                'Raga Dumyaraga': 'Lydian Diminished',
                'Raga Madhuvanti': 'Lydian Diminished',
                'Lydian #6': 'Lydian #6',
                'Mela Citrambari': 'Lydian #6',
                'Raga Chaturangini': 'Lydian #6',
                'Lydian Augmented Dominant': 'Lydian Augmented Dominant',
                'Synthetic Mixture #5': 'Lydian Augmented Dominant',
                'Mixolydian Hexatonic': 'Mixolydian Hexatonic',
                "P'Yongjo": 'Mixolydian Hexatonic',
                'Yosen': 'Mixolydian Hexatonic',
                'Raga Devamanohari': 'Mixolydian Hexatonic',
                'Raga Andolika': 'Mixolydian Hexatonic',
                'Raga Darbar': 'Mixolydian Hexatonic',
                'Raga Gorakh': 'Mixolydian Hexatonic',
                'Raga Narayani': 'Mixolydian Hexatonic',
                'Raga Suposhini': 'Mixolydian Hexatonic',
                'Mixolydian Hexatonic 2': 'Mixolydian Hexatonic 2',
                'Mixolydian b5': 'Mixolydian b5',
                'Mixolydian Augmented': 'Mixolydian Augmented',
                'Mixolydian Augmented Maj9': 'Mixolydian Augmented Maj9',
                'Aeolian b1': 'Aeolian b1',
                'Lydian Augmented #2': 'Aeolian b1',
                'Locrian Dominant': 'Locrian Dominant',
                'Rahawi': 'Locrian Dominant',
                'Locrian bb7': 'Locrian bb7',
                'Locrian bb3 bb7': 'Locrian bb3 bb7',
                'Locrian Maj7': 'Locrian Maj7',
                'Semilocrian b4': 'Semilocrian b4',
                'Superlocrian bb3': 'Superlocrian bb3',
                'Leading Whole-Tone Inverse': 'Superlocrian bb3',
                'Superlocrian Maj7': 'Superlocrian Maj7',
                'Superlocrian bb6 bb7': 'Superlocrian bb6 bb7',
                'Superlocrian #6': 'Superlocrian #6',
                'Ultralocrian bb3': 'Ultralocrian bb3',
                'Harmonic Major': 'Harmonic Major',
                'Segiah': 'Harmonic Major',
                'Tabahaniotiko': 'Harmonic Major',
                'Mischung 2': 'Harmonic Major',
                'Mela Sarasangi': 'Harmonic Major',
                'Raga Haripriya': 'Harmonic Major',
                'Harmonic Major 2': 'Harmonic Major 2',
                'Harmonic Minor b5': 'Harmonic Minor b5',
                'Harmonic Minor Inverse': 'Harmonic Minor Inverse',
                'Mixolydian b2': 'Harmonic Minor Inverse',
                'Mixolydian b9': 'Harmonic Minor Inverse',
                'Maqam Hicaz': 'Harmonic Minor Inverse',
                'Maqam Zanjaran': 'Harmonic Minor Inverse',
                'Mela Cakravka': 'Harmonic Minor Inverse',
                'Raga Ahir Bhairav': 'Harmonic Minor Inverse',
                'Raga Bindumalini': 'Harmonic Minor Inverse',
                'Raga Chakravakam': 'Harmonic Minor Inverse',
                'Raga Vagadeeshwari': 'Harmonic Minor Inverse',
                'Raga Vegavahini Descending': 'Harmonic Minor Inverse',
                'Double Harmonic': 'Double Harmonic',
                'Double Harmonic Major': 'Double Harmonic',
                'Major Phrygian': 'Double Harmonic',
                'Byzantine': 'Double Harmonic',
                'Byzantine Liturgical Chromatic': 'Double Harmonic',
                'Major Gipsy': 'Double Harmonic',
                'Hungarian Folk': 'Double Harmonic',
                'Hitzazkiar': 'Double Harmonic',
                'Hijazskiar': 'Double Harmonic',
                'Maqam Hijaz Kar': 'Double Harmonic',
                'Maqam Suzidil': 'Double Harmonic',
                'Hijaz Kar': 'Double Harmonic',
                'Arabic': 'Double Harmonic',
                'Mela Mayamalavagowla': 'Double Harmonic',
                'Raga Saveri Descending': 'Double Harmonic',
                'Raga Kalingada': 'Double Harmonic',
                'Raga Paraj': 'Double Harmonic',
                'Raga Bhairav That': 'Double Harmonic',
                'Raga Gaulipantu': 'Double Harmonic',
                'Raga Lalita Panchami': 'Double Harmonic',
                'Chromatic Dorian': 'Chromatic Dorian',
                'Mela Kanakangi': 'Chromatic Dorian',
                'Raga Kanakambari': 'Chromatic Dorian',
                'Chromatic Dorian Inverse': 'Chromatic Dorian Inverse',
                'Raga None': 'Chromatic Dorian Inverse',
                'Chromatic Diatonic Dorian': 'Chromatic Diatonic Dorian',
                'Chromatic Phrygian': 'Chromatic Phrygian',
                'Chromatic Phrygian Inverse': 'Chromatic Phrygian Inverse',
                'Chromatic Lydian': 'Chromatic Lydian',
                'Raga Lalit': 'Chromatic Lydian',
                'Raga Bhankar': 'Chromatic Lydian',
                'Chromatic Lydian Inverse': 'Chromatic Lydian Inverse',
                'Maqam Athar Kurd': 'Chromatic Lydian Inverse',
                'Mela Shubhapanturavali': 'Chromatic Lydian Inverse',
                'Raga Gamakasamantam': 'Chromatic Lydian Inverse',
                'Raga Multani': 'Chromatic Lydian Inverse',
                'Chromatic Mixolydian': 'Chromatic Mixolydian',
                'Chromatic Mixolydian 2': 'Chromatic Mixolydian 2',
                'Chromatic Mixolydian Inverse': 'Chromatic Mixolydian Inverse',
                'Chromatic Hypodorian': 'Chromatic Hypodorian',
                'Relative Blues': 'Chromatic Hypodorian',
                'Raga Dvigandharabushini': 'Chromatic Hypodorian',
                'Chromatic Hypodorian Inverse': 'Chromatic Hypodorian Inverse',
                'Chromatic Hypolydian': 'Chromatic Hypolydian',
                'Puravi b6': 'Chromatic Hypolydian',
                'Pireotikos': 'Chromatic Hypolydian',
                'Raga Pantuvarali': 'Chromatic Hypolydian',
                'Raga Purvi': 'Chromatic Hypolydian',
                'Mela Kamavardhani': 'Chromatic Hypolydian',
                'Raga Basant': 'Chromatic Hypolydian',
                'Raga Dhipaka': 'Chromatic Hypolydian',
                'Raga Kasiramakryia': 'Chromatic Hypolydian',
                'Raga Puriya Dhanashri': 'Chromatic Hypolydian',
                'Raga Shri': 'Chromatic Hypolydian',
                'Raga Suddha Ramakriya': 'Chromatic Hypolydian',
                'Chromatic Hypophrygian Inverse': 'Chromatic Hypophrygian Inverse',
                'Chromatic Permutated Diatonic Dorian': 'Chromatic Permutated Diatonic Dorian',
                'Major Minor Mixed': 'Major Minor Mixed',
                'Minor Pentatonic with Leading Tones': 'Minor Pentatonic with Leading Tones',
                'Leading Whole-Tone': 'Leading Whole-Tone'
            },
            'European Scales': {
                'Adonai Malakh': 'Adonai Malakh',
                'Enigmatic Ascending': 'Enigmatic Ascending',
                'Enigmatic Descending': 'Enigmatic Descending',
                'Enigmatic Minor': 'Enigmatic Minor',
                'Enigmatic Mixed': 'Enigmatic Mixed',
                'Flamenco': 'Flamenco',
                'Spanish Phrygian': 'Flamenco',
                'Gypsy': 'Gypsy',
                'Hungarian Gypsy': 'Gypsy',
                'Damian Emmanuel': 'Gypsy',
                'Mela Sanmukhapriya': 'Gypsy',
                'Raga Simmendramadhyamam': 'Gypsy',
                'Raga Camara': 'Gypsy',
                'Gypsy Hexatonic': 'Gypsy Hexatonic',
                'Raga Kalakanthi': 'Gypsy Hexatonic',
                'Gypsy Inverse': 'Gypsy Inverse',
                'Mela Suryakanta': 'Gypsy Inverse',
                'Raga Bhairubahar': 'Gypsy Inverse',
                'Raga Sowrashtram': 'Gypsy Inverse',
                'Raga Supradhipam': 'Gypsy Inverse',
                'Gypsy Minor': 'Gypsy Minor',
                'Double Harmonic Minor': 'Gypsy Minor',
                'Harmonic Minor #4': 'Gypsy Minor',
                'Hungarian Minor': 'Gypsy Minor',
                'Niavent': 'Gypsy Minor',
                'Maqam Hisar': 'Gypsy Minor',
                'Maqam Nawa Athar': 'Gypsy Minor',
                'Niaventi Minor': 'Gypsy Minor',
                'Mela Simhendramadhyama': 'Gypsy Minor',
                'Raga Madhava Manohari': 'Gypsy Minor',
                'Hijaz Major': 'Hijaz Major',
                'Houseini': 'Houseini',
                'Houzam': 'Houzam',
                'Huzam': 'Houzam',
                'Ionian #2': 'Houzam',
                'Mela Sulini': 'Houzam',
                'Raga Sailadesakshi': 'Houzam',
                'Raga Trishuli': 'Houzam',
                'Hungarian Major': 'Hungarian Major',
                'Mela Nasikabhusani': 'Hungarian Major',
                'Raga Nasamani': 'Hungarian Major',
                'Hungarian Major Inverse': 'Hungarian Major Inverse',
                'Hungarian Minor b2': 'Hungarian Minor b2',
                'Istrian': 'Istrian',
                'Jeths': 'Jeths',
                'Zangula': 'Jeths',
                'Kiourdi': 'Kiourdi',
                'Magen Abot': 'Magen Abot',
                'Moorish Phrygian': 'Moorish Phrygian',
                'Neapolitan Major': 'Neapolitan Major',
                'Neapolitan': 'Neapolitan Major',
                'Mela Kokilapriya': 'Neapolitan Major',
                'Raga Kokilaravam': 'Neapolitan Major',
                'Neapolitan Major b4': 'Neapolitan Major b4',
                'Neapolitan Major b5': 'Neapolitan Major b5',
                'Neapolitan Minor': 'Neapolitan Minor',
                'Hungarian Gipsy': 'Neapolitan Minor',
                'Maqam Shahnaz': 'Neapolitan Minor',
                'Maqam Shahnaz Kurdi': 'Neapolitan Minor',
                'Mela Dhenuka': 'Neapolitan Minor',
                'Mela Senavati': 'Neapolitan Minor',
                'Raga Dhunibinnashadjam': 'Neapolitan Minor',
                'Raga Bhinnasadjam': 'Neapolitan Minor',
                'Harmonic Neapolitan Minor': 'Harmonic Neapolitan Minor',
                'Neveseri': 'Neveseri',
                'Prokofiev': 'Prokofiev',
                'Prometheus': 'Prometheus',
                'Raga Barbara': 'Prometheus',
                'Prometheus Neapolitan': 'Prometheus Neapolitan',
                'Romanian Major': 'Romanian Major',
                'Mela Ramapriya': 'Romanian Major',
                'Raga Nasikabhushani': 'Romanian Major',
                'Raga Ramamahohari': 'Romanian Major',
                'Sabach': 'Sabach',
                'Sabach Maj7': 'Sabach Maj7',
                'Scottish Hexatonic': 'Scottish Hexatonic',
                'Arezzo Major Diatonic Hexachord': 'Scottish Hexatonic',
                'Raga Kambodhi Ascending': 'Scottish Hexatonic',
                'Raga Yadukua Kambodhi Descending': 'Scottish Hexatonic',
                'Raga Devarangini 2': 'Scottish Hexatonic',
                'Raga Kambhoji': 'Scottish Hexatonic',
                'Sengiach': 'Sengiach',
                'Sengah ': 'Sengiach',
                'Gypsy Hexatonic Inverse': 'Sengiach',
                'Mela Gangeyabhusani': 'Sengiach',
                'Shostakovich': 'Shostakovich',
                'Spanish Heptatonic': 'Spanish Heptatonic',
                'Spanish Octatonic': 'Spanish Octatonic',
                'Espla': 'Spanish Octatonic',
                'Ahava Rabba': 'Spanish Octatonic'
            },
            'Asian Scales': {
                'Honkoshi': 'Honkoshi',
                'Ichikotsucho': 'Ichikotsucho',
                'Major-Lydian Mixed': 'Ichikotsucho',
                'Gregorian 5': 'Ichikotsucho',
                'Genus Diatonicum Veterum Correctum': 'Ichikotsucho',
                'Kubilai': 'Ichikotsucho',
                'Ishikotsucho': 'Ichikotsucho',
                'Raga Bihag': 'Ichikotsucho',
                'Raga Gaud Sarang': 'Ichikotsucho',
                'Raga Hamir Kalyani': 'Ichikotsucho',
                'Raga Kedar': 'Ichikotsucho',
                'Raga Yaman Kalyan': 'Ichikotsucho',
                'Raga': 'Ichikotsucho',
                'Insen': 'Insen',
                'Niagari': 'Insen',
                'Raga Phenadyuti 2': 'Insen',
                "Maqam Shadd'araban": "Maqam Shadd'araban",
                'Maqam Hijaz': 'Maqam Hijaz',
                'Maqam Shawq Afza': 'Maqam Shawq Afza',
                'Maqam Tarzanuyn': 'Maqam Tarzanuyn',
                'Nando-Kyemyonjo': 'Nando-Kyemyonjo',
                'Ghana Pentatonic': 'Nando-Kyemyonjo',
                'Chad Gadyo': 'Nando-Kyemyonjo',
                'Raga Purnanalita': 'Nando-Kyemyonjo',
                'Noh': 'Noh',
                'Nohkan': 'Nohkan',
                'Lydian Augmented #3': 'Nohkan',
                'Oriental': 'Oriental',
                'Minor Gypsy Inverse': 'Oriental',
                'Hungarian Minor Inverse': 'Oriental',
                'Tsinganikos': 'Oriental',
                'Raga Ahira Lalita': 'Oriental',
                'Oriental 2': 'Oriental 2',
                'Pelog': 'Pelog',
                'Mela Latangi': 'Pelog',
                'Raga Gitapriya': 'Pelog',
                'Raga Hamsalata': 'Pelog',
                'Persian': 'Persian',
                'Chromatic Hypolydian Inverse': 'Persian',
                'Raga Suddha Pancama': 'Persian',
                'Ritzu': 'Ritzu',
                'Raga Suddha Todi': 'Ritzu',
                'Sho': 'Sho',
                'Raga Gauri Velavali': 'Sho',
                'Raga Suddha Bangala': 'Sho',
                'Sho #2': 'Sho #2',
                'Takemitzu Tree 1': 'Takemitzu Tree 1',
                'Takemitzu Tree 2': 'Takemitzu Tree 2',
                'Youlan': 'Youlan'
            },
            'Indian Scales': {
                'Mela Bhavapriya': 'Mela Bhavapriya',
                'Raga Bhavani': 'Mela Bhavapriya',
                'Raga Kalamurti': 'Mela Bhavapriya',
                'Mela Calanata': 'Mela Calanata',
                'Raga Bhanumanjari': 'Mela Calanata',
                'Raga Jog': 'Mela Calanata',
                'Mela Dhavalambari': 'Mela Dhavalambari',
                "John Fould's Mantra of Will": 'Mela Dhavalambari',
                'Mela Dhatuvardhani': 'Mela Dhatuvardhani',
                'Raga Devarashtra': 'Mela Dhatuvardhani',
                'Raga Dhauta Pancama': 'Mela Dhatuvardhani',
                'Mela Divyamani': 'Mela Divyamani',
                'Raga Vamsavathi': 'Mela Divyamani',
                'Mela Ganamurti': 'Mela Ganamurti',
                'Raga Ganasamavarali': 'Mela Ganamurti',
                'Mela Gavambodhi': 'Mela Gavambodhi',
                'Raga Girvani': 'Mela Gavambodhi',
                'Mela Gayakapriya': 'Mela Gayakapriya',
                'Mela Hatakambari': 'Mela Hatakambari',
                'Raga Jeyasuddhamalavi': 'Mela Hatakambari',
                'Mela Jalarnava': 'Mela Jalarnava',
                'Mela Jhalavarli': 'Mela Jhalavarli',
                'Raga Jinavali': 'Mela Jhalavarli',
                'Raga Varali': 'Mela Jhalavarli',
                'Mela Jhankaradhvani': 'Mela Jhankaradhvani',
                'Raga Jhankara Bhramavi': 'Mela Jhankaradhvani',
                'Mela Jyotisvarupini': 'Mela Jyotisvarupini',
                'Raga Jotismatti': 'Mela Jyotisvarupini',
                'Mela Kantamani': 'Mela Kantamani',
                'Raga Kuntala': 'Mela Kantamani',
                'Raga Srutiranjani': 'Mela Kantamani',
                'Mela Manavati': 'Mela Manavati',
                'Raga Manoranjani': 'Mela Manavati',
                'Mela Naganandini': 'Mela Naganandini',
                'Raga Nagabharanam': 'Mela Naganandini',
                'Raga Samanta': 'Mela Naganandini',
                'Mela Namanarayani': 'Mela Namanarayani',
                'Raga Purvi Thaat': 'Mela Namanarayani',
                'Raga Narmada': 'Mela Namanarayani',
                'Raga Pratapa': 'Mela Namanarayani',
                'Mela Navanitam': 'Mela Navanitam',
                'Mela Nitimati': 'Mela Nitimati',
                'Raga Kaikavasi': 'Mela Nitimati',
                'Raga Nisada': 'Mela Nitimati',
                'Mela Pavani': 'Mela Pavani',
                'Raga Kunbhini': 'Mela Pavani',
                'Mela Ragavardhani': 'Mela Ragavardhani',
                'Raga Cudamani': 'Mela Ragavardhani',
                'Mela Raghupriya': 'Mela Raghupriya',
                'Raga Ghandarva': 'Mela Raghupriya',
                'Raga Ravikriya': 'Mela Raghupriya',
                'Mela Ratnangi': 'Mela Ratnangi',
                'Raga Phenadyuti': 'Mela Ratnangi',
                'Mela Rupavati': 'Mela Rupavati',
                'Mela Salaga': 'Mela Salaga',
                'Mela Syamalangi': 'Mela Syamalangi',
                'Raga Shyamalam': 'Mela Syamalangi',
                'Mela Suvarnangi': 'Mela Suvarnangi',
                'Raga Sauviram': 'Mela Suvarnangi',
                'Mela Tenarupi': 'Mela Tenarupi',
                'Raga Tanukirti': 'Mela Tenarupi',
                'Mela Venaspati': 'Mela Venaspati',
                'Raga Bhanumati': 'Mela Venaspati',
                'Mela Varunapriya': 'Mela Varunapriya',
                'Raga Viravasantham': 'Mela Varunapriya',
                'Mela Visvambhari': 'Mela Visvambhari',
                'Mela Yagapriya': 'Mela Yagapriya',
                'Raga Kalahamsa': 'Mela Yagapriya',
                'Raga Abhogi': 'Raga Abhogi',
                'Raga Airavati': 'Raga Airavati',
                'Ancient Chinese': 'Raga Airavati',
                'Raga Kalyani': 'Raga Airavati',
                'Raga Yamuna Kalyani': 'Raga Airavati',
                'Raga Kalyani Keseri': 'Raga Airavati',
                'Raga Amarasenapriya': 'Raga Amarasenapriya',
                'Raga Audav Tukhari': 'Raga Audav Tukhari',
                'Raga Bhatiyar': 'Raga Bhatiyar',
                'Buzurg': 'Raga Bhatiyar',
                'Raga Bhinna Pancama': 'Raga Bhinna Pancama',
                'Raga Brindabani': 'Raga Brindabani',
                'Raga Brindabani Sarang': 'Raga Brindabani',
                'Raga Megh': 'Raga Brindabani',
                'Megh Malhar': 'Raga Brindabani',
                'Raga Bowli Ascending': 'Raga Bowli Ascending',
                'Raga Reva': 'Raga Bowli Ascending',
                'Raga Revagupti': 'Raga Bowli Ascending',
                'Raga Vibhas': 'Raga Bowli Ascending',
                'Raga Bowli Descending': 'Raga Bowli Descending',
                'Raga Bauli': 'Raga Bowli Descending',
                'Raga Budhamanohari': 'Raga Budhamanohari',
                'Raga Chandrajyoti': 'Raga Chandrajyoti',
                'Raga Chandrakauns Kafi': 'Raga Chandrakauns Kafi',
                'Raga Surya': 'Raga Chandrakauns Kafi',
                'Raga Varamu': 'Raga Chandrakauns Kafi',
                'Raga Chandrakauns Kiravani': 'Raga Chandrakauns Kiravani',
                'Raga Chandrakauns Modern': 'Raga Chandrakauns Modern',
                'Raga Marga Hindola': 'Raga Chandrakauns Modern',
                'Raga Rajeshwari': 'Raga Chandrakauns Modern',
                'Raga Chaya Todi': 'Raga Chaya Todi',
                'Raga Chinthamani': 'Raga Chinthamani',
                'Raga Deshgaur': 'Raga Deshgaur',
                'Raga Devaranjani': 'Raga Devaranjani',
                'Raga Devaranji': 'Raga Devaranjani',
                'Raga Dhavalangam': 'Raga Dhavalangam',
                'Raga Indupriya': 'Raga Dhavalangam',
                'Raga Dhavalashri': 'Raga Dhavalashri',
                'Raga Dipak': 'Raga Dipak',
                'Raga Gamakakriya': 'Raga Gamakakriya',
                'Raga Hamsanarayami': 'Raga Gamakakriya',
                'Raga Mandari': 'Raga Gamakakriya',
                'Raga Gandharavam': 'Raga Gandharavam',
                'Raga Gangatarangini': 'Raga Gangatarangini',
                'Raga Gaula': 'Raga Gaula',
                'Raga Gaurikriya': 'Raga Gaurikriya',
                'Raga Jivantini': 'Raga Gaurikriya',
                'Raga Ghantana': 'Raga Ghantana',
                'Raga Kaishikiranjani': 'Raga Ghantana',
                'Raga Kaushiranjani': 'Raga Ghantana',
                'Raga Gopikatilaka': 'Raga Gopikatilaka',
                'Raga Simharava': 'Raga Gopikatilaka',
                'Raga Gowla Ascending': 'Raga Gowla Ascending',
                'Raga Gauri': 'Raga Gowla Ascending',
                'Raga Gowla': 'Raga Gowla Ascending',
                'Raga Gowla Dscending': 'Raga Gowla Descending',
                'Raga Gurjari Todi': 'Raga Gurjari Todi',
                'Raga Hamsadhvani': 'Raga Hamsadhvani',
                'Raga Hamsanandi': 'Raga Hamsanandi',
                'Raga Pancama': 'Raga Hamsanandi',
                'Raga Puriya 2': 'Raga Hamsanandi',
                'Raga Marva': 'Raga Hamsanandi',
                'Raga Sohni': 'Raga Hamsanandi',
                'Raga Hamsa Vinodini': 'Raga Hamsa Vinodini',
                'Raga Hari Nata': 'Raga Hari Nata',
                'Genus Secundum': 'Raga Hari Nata',
                'Raga Hejjajji': 'Raga Hejjajji',
                'Raga Jaganmohanam': 'Raga Jaganmohanam',
                'Raga Jivantika': 'Raga Jivantika',
                'Raga Jyoti': 'Raga Jyoti',
                'Raga Kalagada': 'Raga Kalagada',
                'Raga Kalakanthi 2': 'Raga Kalakanthi 2',
                'Raga Kalavati': 'Raga Kalavati',
                'Raga Ragamalini': 'Raga Kalavati',
                'Raga Kamalamanohari 2': 'Raga Kamalamanohari 2',
                'Raga Kashyapi': 'Raga Kashyapi',
                'Raga Kedaram Ascending': 'Raga Kedaram Ascending',
                'Raga Neelambari': 'Raga Kedaram Ascending',
                'Raga Nalinakanti': 'Raga Kedaram Ascending',
                'Raga Kedaram Descending': 'Raga Kedaram Descending',
                'Raga Vilasini': 'Raga Kedaram Descending',
                'Raga Khamach Ascending': 'Raga Khamach Ascending',
                'Raga Madhuri': 'Raga Khamach Ascending',
                'Raga Khamach Descending': 'Raga Khamach Descending',
                'Raga Kshanika': 'Raga Kshanika',
                'Raga Kumarapriya': 'Raga Kumarapriya',
                'Raga Kumurdaki': 'Raga Kumurdaki',
                'Raga Kumudki': 'Raga Kumurdaki',
                'Raga Kuntvarali': 'Raga Kuntvarali',
                'Raga Kuntalavarali': 'Raga Kuntvarali',
                'Raga Lalita': 'Raga Lalita',
                'Raga Sohini': 'Raga Lalita',
                'Raga Lalita Bhairav': 'Raga Lalita Bhairav',
                'Raga Vasantha': 'Raga Lalita Bhairav',
                'Raga Latika': 'Raga Latika',
                'Raga Madhukauns': 'Raga Madhukauns',
                'Raga Malarani': 'Raga Malarani',
                'Raga Malayamarutam': 'Raga Malayamarutam',
                'Raga Malahari Ascending': 'Raga Malahari Ascending',
                'In': 'Raga Malahari Ascending',
                'Raga Geyahejjajji': 'Raga Malahari Ascending',
                'Raga Kannadabangala': 'Raga Malahari Ascending',
                'Raga Malahari Descending': 'Raga Malahari Descending',
                'Raga Purna Pancama': 'Raga Malahari Descending',
                'Raga Malkauns': 'Raga Malkauns',
                'Raga Malini': 'Raga Malini',
                'Raga Senagrani': 'Raga Malini',
                'Raga Manaranjani': 'Raga Manaranjani',
                'Raga Manavi': 'Raga Manavi',
                'Raga Manohari': 'Raga Manohari',
                'Raga Malavasri': 'Raga Manohari',
                'Raga Marwa Thaat': 'Raga Marwa Thaat',
                'Peiraiotikos': 'Raga Marwa Thaat',
                'Mela Gamanasrama': 'Raga Marwa Thaat',
                'Raga Partiravan': 'Raga Marwa Thaat',
                'Raga Puriya': 'Raga Marwa Thaat',
                'Raga Puriya Kalyan': 'Raga Marwa Thaat',
                'Raga Purvikalyani': 'Raga Marwa Thaat',
                'Raga Sohani': 'Raga Marwa Thaat',
                'Raga Bairari': 'Raga Marwa Thaat',
                'Raga Matha Kokila': 'Raga Matha Kokila',
                'Raga Matkokil': 'Raga Matha Kokila',
                'Raga Megharanji': 'Raga Megharanji',
                'Raga Mian Ki Malhar': 'Raga Mian Ki Malhar',
                'Raga Bahar': 'Raga Mian Ki Malhar',
                'Raga Sindhura': 'Raga Mian Ki Malhar',
                'Raga Mohanangi': 'Raga Mohanangi',
                'Raga Mruganandana': 'Raga Mruganandana',
                'Raga Multani 2': 'Raga Multani 2',
                'Raga Nabhomani': 'Raga Nabhomani',
                'Raga Nagagandhari': 'Raga Nagagandhari',
                'Raga Nattai Ascending': 'Raga Nattai Ascending',
                'Raga Madhuranjani': 'Raga Nattai Ascending',
                'Raga Nata': 'Raga Nattai Ascending',
                'Raga Nattai Descending': 'Raga Nattai Descending',
                'Raga Udayaravicandrika': 'Raga Nattai Descending',
                'Raga Nattaikurinji': 'Raga Nattaikurinji',
                'Raga Rageshri 1': 'Raga Nattaikurinji',
                'Raga Rageshwari': 'Raga Nattaikurinji',
                'Raga Navamanohari': 'Raga Navamanohari',
                'Raga Neroshta': 'Raga Neroshta',
                'Raga Nishadi': 'Raga Nishadi',
                'Raga Padi': 'Raga Padi',
                'Raga Pahadi': 'Raga Pahadi',
                'Raga Paras Ascending': 'Raga Paras Ascending',
                'Raga Pharas': 'Raga Paras Ascending',
                'Raga Paraju': 'Raga Paras Ascending',
                'Raga Kamalamanohari': 'Raga Paras Ascending',
                'Raga Ramamanohari 2': 'Raga Paras Ascending',
                'Raga Simhavahini': 'Raga Paras Ascending',
                'Raga Sindhu Ramakriya': 'Raga Paras Ascending',
                'Raga Paras Descending': 'Raga Paras Descending',
                'Raga Priyadharshini': 'Raga Priyadharshini',
                'Raga Puruhutika': 'Raga Puruhutika',
                'Raga Purvaholica': 'Raga Puruhutika',
                'Raga Putrika': 'Raga Putrika',
                'Raga Rageshri': 'Raga Rageshri',
                'Raga Ramkali': 'Raga Ramkali',
                'Raga Ramakri': 'Raga Ramkali',
                'Raga Rangini': 'Raga Rangini',
                'Raga Ranjani': 'Raga Rangini',
                'Raga Rasamanjari 2': 'Raga Rasamanjari 2',
                'Raga Rasavali': 'Raga Rasavali',
                'Raga Rasranjani': 'Raga Rasranjani',
                'Raga Ratnakanthi': 'Raga Ratnakanthi',
                'Raga Chaturangini 2': 'Raga Ratnakanthi',
                'Raga Rudra Pancama': 'Raga Rudra Pancama',
                'Raga Rukmangi': 'Raga Rukmangi',
                'Raga Salagavarali': 'Raga Salagavarali',
                'Raga Samudhra Priya': 'Raga Samudhra Priya',
                'Raga Santanamanjari': 'Raga Santanamanjari',
                'Mela Sucaritra': 'Raga Santanamanjari',
                'Raga Sarasanana': 'Raga Sarasanana',
                'Raga Sarasvati': 'Raga Sarasvati',
                'Raga Saravati': 'Raga Saravati',
                'Raga Saugandhini': 'Raga Saugandhini',
                'Raga Yashranjani': 'Raga Saugandhini',
                'Raga Saurashtra': 'Raga Saurashtra',
                'Raga Shreeranjani': 'Raga Shreeranjani',
                'Raga Shee Ranjani': 'Raga Shreeranjani',
                'Raga Sriranjiani': 'Raga Shreeranjani',
                'Raga Kapijingla': 'Raga Shreeranjani',
                'Raga Bageshri 2': 'Raga Shreeranjani',
                'Raga Jayamanohari': 'Raga Shreeranjani',
                'Raga Shri Kalyan': 'Raga Shri Kalyan',
                'Raga Shubravarni': 'Raga Shubravarni',
                'Raga Sindhura Kafi': 'Raga Sindhura Kafi',
                'Raga Sindhi-Bhairavi': 'Raga Sindhi-Bhairavi',
                'Raga Siva Kambhoji': 'Raga Siva Kambhoji',
                'Raga Vivardhini': 'Raga Siva Kambhoji',
                'Raga Andhali': 'Raga Siva Kambhoji',
                'Raga Sorati': 'Raga Sorati',
                'Raga Sur Malhar': 'Raga Sorati',
                'Raga Suddha Mukhari': 'Raga Suddha Mukhari',
                'Raga Suddha Simantini': 'Raga Suddha Simantini',
                'Raga Syamalam': 'Raga Syamalam',
                'Raga Takka': 'Raga Takka',
                'Raga Tilang': 'Raga Tilang',
                'Raga Bridabani Tilang': 'Raga Tilang',
                'Raga Savitri': 'Raga Tilang',
                'Raga Trimurti': 'Raga Trimurti',
                'Raga Valaji': 'Raga Valaji',
                'Raga Vasanta Ascending': 'Raga Vasanta Ascending',
                'Raga Bhinna Shadj': 'Raga Vasanta Ascending',
                'Raga Hindolita': 'Raga Vasanta Ascending',
                'Raga Kaushikdhvani': 'Raga Vasanta Ascending',
                'Raga Vasanta Descending': 'Raga Vasanta Descending',
                'Raga Chaya Vati': 'Raga Vasanta Descending',
                'Raga Vegavahini Ascending': 'Raga Vegavahini Ascending',
                'Raga Khamas': 'Raga Vegavahini Ascending',
                'Raga Desya Khamas': 'Raga Vegavahini Ascending',
                'Raga Bahudari': 'Raga Vegavahini Ascending',
                'Raga Vijayanagari': 'Raga Vijayanagari',
                'Raga Vijayasri': 'Raga Vijayasri',
                'Raga Vijayavasanta': 'Raga Vijayavasanta',
                'Raga Viyogavarali': 'Raga Viyogavarali',
                'Raga Vutari': 'Raga Vutari',
                'Raga Zilaf': 'Raga Zilaf'
            },
            'Miscellaneous Scales': {
                'Algerian Octatonic': 'Algerian Octatonic',
                'Algerian': 'Algerian',
                'Eskimo Hexatonic': 'Eskimo Hexatonic',
                'Eskimo Hexatonic 2': 'Eskimo Hexatonic 2',
                'Hamel': 'Hamel',
                'Gregorian 3': 'Hamel',
                'Hawaiian': 'Hawaiian',
                'LG Octatonic': 'LG Octatonic',
                'Pyramid Hexatonic': 'Pyramid Hexatonic',
                'Nonatonic 2': 'Nonatonic 2',
                'Symmetrical Nonatonic': 'Symmetrical Nonatonic'
            }
        }

        self.newscaledata = {
            'Raga Vativasanta': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'formula': ['1', 'b2', '3', '4', '5', 'b6', 'b7', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'alternate names': [
                    'Phrygian Major', 'Harmonic Major inverse',
                    'Spanish or Spanish Gipsy', 'Zilof (Spain)',
                    'Dorico Flamenco (Spain)', 'Jewish',
                    'Avaha or Ahava Rabba (Jewish)',
                    'Freygish (or Fraigish)',
                    'Hitzaz (or Hijaz, Greece)',
                    'Alhijaz (Saudi Arabian)',
                    'Maqam Humayun (Iraq)', 'Maqam Zengule (Iraq)',
                    'Maqam Hijaz-Nahawand (Iraq)', 'Humayun (Iraq)',
                    'Mela Vakulabharanam', 'Raga Jogiya'
                ],
                'mode': 'mode V of Harmonic Minor scale (C Phrygian'
                        'Dominant = F Harmonic Minor)',
                'chords': ['7', '7b9', '7b13'],
                'description': 'The Phrygian Dominant scale can be found '
                               'in jazz compositions by Charles Mingus '
                               '(Ysabel�s Table Dance, Don�t Let It Happen '
                               'Here, The Black Saint and The Sinner Lady).'
                               ' It was used in classical music by Franz '
                               'Liszt (B-minor Sonata, closing bars).',
                'page': 27
            },
            'Raga Ramakri': {
                'category': 'Indian Scales',
                # c d  e f g a b
                # 1 2  3 4 5 6 7
                # c db e f f# g ab b
                'interval': ['1', '3', '1', '1', '1', '1', '3', '1'],
                'formula': ['1', 'b2', '3', '4', '#4', '5', 'b6', '7'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Raga Ramkali',
                'alternate names': ['Raga Ramakri'],
                'mode': 'mode VI of Hungarian Minor b2 scale (C Raga '
                        'Ramkali = F Hungarian Minor b2)',
                'chords': ['maj7', 'b9'],
                'page': 360
            },
            'Messiaen 6th Mode': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '2', '1', '1', '2', '2', '1', '1'],
                'formula': ['1', '2', '3', '4', '#4', '#5', '#6', '7'],
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G#', 'A#', 'B'],
                'mode': 'Messiaen 6th Mode Inverse (III)',
                'chords': ['7#5', '7#5#11'],
                'description': 'It should be noted that this scale contains'
                               ' the first 4 notes of the Major scale, '
                               'followed by the first 4 notes of of the '
                               'Major scale built a tritone above.',
                'page': 44
            },
            'Raga Bahar': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'A#', 'B'],
                'primary scale': 'Raga Miam Ki Malhar',
                'page': 342
            },
            'Superlocrian #6': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '2', '3', '1', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'A', 'Bb'],
                'page': 165
            },
            'Raga Jhankara Bhramavi': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A'],
                'primary scale': 'Mela Jhankaradhvani',
                'page': 258
            },
            'Augmented': {
                'category': 'Symmetrical Scales',
                'interval': ['3', '1', '3', '1', '3', '1'],
                'scale': ['C', 'D#', 'E', 'G', 'Ab', 'B'],
                'page': 31
            },
            'Kung': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '2', '3', '3'],
                'scale': ['C', 'D', 'E', 'Gb', 'A'],
                'page': 94
            },
            'Mela Citrambari': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Lydian #6',
                'page': 149
            },
            'Raga Girija': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G#', 'B'],
                'primary scale': 'Romanian Bacovia',
                'page': 122
            },
            'Raga Paras Ascending': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Ab', 'B'],
                'page': 355
            },
            'Chin': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '3', '2', '2', '2'],
                'scale': ['C', 'Eb', 'Gb', 'Ab', 'Bb'],
                'page': 92
            },
            'Romanian Major': {
                'category': 'European Scales',
                'interval': ['1', '3', '2', '1', '2', '1', '2'],
                'origin': 'Romania',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'Bb'],
                'page': 219
            },
            'Bebop Dorian': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '1', '2', '2', '1', '2'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'page': 70
            },
            'Raga Ambika': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian Diminished',
                'page': 148
            },
            'Raga Vaijayanti': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '4', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F#', 'G', 'B'],
                'primary scale': 'Raga Hamsanada',
                'page': 88
            },
            'Mela Shankarabharanam': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Major',
                'page': 9
            },
            'Zirafkend': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '2', '1'],
                'origin': 'Arabia',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'B'],
                'primary scale': 'Bebop Melodic Minor',
                'page': 71
            },
            'Harmonic Neapolitan Minor': {
                'category': 'European Scales',
                'interval': ['1', '1', '1', '2', '2', '1', '3', '1'],
                'origin': 'Italy',
                'scale': ['C', 'C#', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'page': 214
            },
            'Inverted Augmented': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '3', '1', '3', '1', '3'],
                'scale': ['C', 'Db', 'E', 'F', 'G#', 'A'],
                'page': 32
            },
            'Raga Samanta': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Mela Naganandini',
                'page': 262
            },
            'Chinese': {
                'category': 'Jazz Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'origin': 'China',
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Hirajoshi',
                'page': 96
            },
            'Chinese1': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'origin': 'China',
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Hirajoshi',
                'page': 96
            },
            'Double Phrygian': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '2', '1', '3', '3'],
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'A'],
                'page': 141
            },
            'Major Mixolydian': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Raga Ritigaula': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Shang-Diao': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'D', 'G', 'G', 'Bb'],
                'primary scale': 'Suspended Pentatonic',
                'page': 77
            },
            'Romanian Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'page': 26
            },
            'Raga Dhavalashri': {
                'category': 'Indian Scales',
                'interval': ['4', '2', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'E', 'F#', 'G', 'A'],
                'page': 297
            },
            'Ichikotsucho': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'page': 228
            },
            'Rast': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Chromatic Hypodorian': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '1', '3', '1', '1', '3'],
                'scale': ['C', 'D', 'D#', 'E', 'G', 'G#', 'A'],
                'page': 182
            },
            'Symmetrical Decatonic': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '1', '2', '1', '1', '1', '1', '2', '1', '1'],
                'scale': ['C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'G#', 'A#', 'B'],
                'page': 50
            },
            'Raga Saurashtra': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '1', '1', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'G#', 'A', 'B'],
                'page': 375
            },
            'Chromatic Dorian Inverse': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '1', '2', '3', '1', '1'],
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Bb', 'B'],
                'page': 173
            },
            'Ghana Pentatonic 2': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'Ghana',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Raga Sur Malhar': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'A#', 'B'],
                'primary scale': 'Raga Sorati',
                'page': 382
            },
            'Raga Asavari That': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Raga Salanganata': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'In',
                'page': 95
            },
            'Mela Nitimati': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A#', 'B'],
                'page': 265
            },
            'Locrian Maj7': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '2', '1', '2', '3', '1'],
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'B'],
                'page': 160
            },
            'Ionian Augmented': {
                'category': 'Major and Minor Scales',
                'interval': ['3', '1', '1', '3', '1', '2', '1'],
                'scale': ['C', 'D#', 'E', 'F', 'G#', 'A', 'B'],
                'page': 127
            },
            'Peruvian Major': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'Peru',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Major',
                'page': 9
            },
            'Peruvian Major1': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'Peru',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Major',
                'page': 9
            },
            'Raga Nalinakanti': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'B'],
                'primary scale': 'Raga Kedaram asc',
                'page': 321
            },
            'Chromatic': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
                'scale': ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B'],
                'page': 35
            },
            'Raga Bairagi': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Minor Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'page': 80
            },
            'Locrian Natural Maj6': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '1', '3', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Locrian #6',
                'page': 24
            },
            'Raga Manoranjani': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'A', 'B'],
                'primary scale': 'Mela Manavati',
                'page': 261
            },
            'Raga Manaranjani 2': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'A'],
                'primary scale': 'Altered Pentatonic',
                'page': 107
            },
            'Mela Kanakangi': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '3', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'G#', 'A'],
                'primary scale': 'Chromatic Dorian',
                'page': 172
            },
            'Kubilai': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'origin': 'Mongolia',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Pyramid Hexatonic': {
                'category': 'Miscellaneous Scales',
                'interval': [2, 1, 2, 1, 3, 3],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'A'],
                'page': 405
            },
            'Scottish Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'Scotland',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Bebop Major': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '1', '1', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'G#', 'A', 'B'],
                'page': 66
            },
            'Raga Deshgaur': {
                'category': 'Indian Scales',
                'interval': ['1', '6', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'G', 'Ab', 'B'],
                'page': 294
            },
            'Raga Malini': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '2', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'G#', 'A'],
                'page': 335
            },
            'Raga Viravasantham': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Mela Varunapriya',
                'page': 276
            },
            'Locrian bb3 bb7': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '3', '1', '2', '1', '3'],
                'scale': ['C', 'C#', 'D', 'F', 'F#', 'G#', 'A'],
                'page': 159
            },
            'Ghana Heptatonic': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'Ghana',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Major',
                'page': 9
            },
            'Raga Sohani': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Marwa Thaat',
                'page': 339
            },
            'Maqam Humayun': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Raga Sri': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Raga Srutiranjani': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'G#', 'A'],
                'primary scale': 'Mela Kantamani',
                'page': 260
            },
            'Houseini': {
                'category': 'European Scales',
                'interval': ['2', '1', '1', '1', '2', '1', '1', '1', '2'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'G#', 'A', 'Bb'],
                'page': 200
            },
            'Gypsy Hexatonic': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '1', '1', '3'],
                'origin': 'Hungary',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'G#', 'A'],
                'page': 196
            },
            'Yona Nuki Minor': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '1', '4', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'G', 'Ab'],
                'primary scale': 'Ake-Bono',
                'page': 97
            },
            'Mela Gamanasrama': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Marwa Thaat',
                'page': 339
            },
            'Raga Matkokil': {
                'category': 'Indian Scales',
                'interval': ['2', '5', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'G', 'A', 'Bb'],
                'primary scale': 'Raga Matha Kokila',
                'page': 340
            },
            'Neapolitan Major': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '2', '2', '1'],
                'origin': 'Italy',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'B'],
                'page': 210
            },
            'Raga Surya': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'A', 'Bb'],
                'primary scale': 'Raga Chandrakauns Kafi',
                'page': 289
            },
            'Raga Shilangi': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Hirajoshi',
                'page': 96
            },
            'Raga Vilasini': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'B'],
                'primary scale': 'Raga Kedaram desc',
                'page': 321
            },
            'Mela Suvarnangi': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A', 'B'],
                'page': 273
            },
            'Han-Kumoi': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '1', '4'],
                'scale': ['C', 'D', 'F', 'G', 'Ab'],
                'page': 84
            },
            'Messiaen 7th Mode': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '1', '1', '2', '1', '1', '1', '1', '2', '1'],
                'scale': ['C', 'C#', 'D', 'Eb', 'F', 'F#', 'G', 'G#', 'A', 'B'],
                'page': 46
            },
            'Raga Malashri': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Hirajoshi',
                'page': 96
            },
            'Souzinak': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Raga Kuntalavarali': {
                'category': 'Indian Scales',
                'interval': ['5', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'F', 'G', 'A', 'Bb'],
                'page': 326
            },
            'Lydian b7': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Lydian Dominant',
                'page': 19
            },
            'Chromatic Phrygian Inverse': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '2', '3', '1', '1', '3'],
                'scale': ['C', 'C#', 'D', 'E', 'G', 'G#', 'A'],
                'page': 176
            },
            'Genus Chromaticum': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '2', '1', '1', '2', '1', '1', '2', '1'],
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'G', 'G#', 'A', 'B'],
                'page': 48
            },
            'Raga Malayamarutam': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'A', 'Bb'],
                'page': 332
            },
            'Acoustic': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Lydian Dominant',
                'page': 19
            },
            'Raga Camara': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Gypsy',
                'page': 195
            },
            'Mela Dharmavati': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian Diminished',
                'page': 148
            },
            'Moorish Phrygian': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '1', '2', '1', '2', '1', '1'],
                'origin': 'Spain',
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'G', 'G#', 'A#', 'B'],
                'page': 209
            },
            'Raga Nishadi': {
                'category': 'Indian Scales',
                'interval': ['2', '4', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F#', 'G', 'A', 'B'],
                'page': 352
            },
            'Raga Kaushikdhvani': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'A', 'B'],
                'primary scale': 'Raga Vasanta asc',
                'page': 390
            },
            'Minor Gypsy Inverse': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '3', '1', '2'],
                'origin': 'Hungary',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Oriental',
                'page': 237
            },
            'Yi Ze': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '3', '2', '2'],
                'origin': 'China',
                'scale': ['C', 'Eb', 'F', 'Ab', 'Bb'],
                'primary scale': 'Man Gong',
                'page': 78
            },
            'Mela Carukesi': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Tritone': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '3', '2', '1', '3', '2'],
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Bb'],
                'primary scale': 'Tritone',
                'page': 36
            },
            'Maqam Shawq Awir': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Raga Jait Kalyan': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Mela Cakravka': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Raga Rasika Ranjani': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '3', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic b2',
                'page': 99
            },
            'Lydian b3': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian Diminished',
                'page': 148
            },
            'Overtone': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Lydian Dominant',
                'page': 19
            },
            'Houzam': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '2', '2', '1'],
                'origin': 'Greece',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'B'],
                'page': 201
            },
            'Hamel': {
                'category': 'Miscellaneous Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '1', '1'],
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'G#', 'A#', 'B'],
                'page': 402
            },
            'Raga Deshi': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb'],
                'primary scale': 'Dorian Aeolian',
                'page': 133
            },
            'Spanish': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Spain',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Prometheus': {
                'category': 'European Scales',
                'interval': ['2', '2', '2', '3', '1', '2'],
                'scale': ['C', 'D', 'E', 'Gb', 'A', 'Bb'],
                'page': 217
            },
            'Raga Bhairubahar': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Gypsy Inverse',
                'page': 197
            },
            'Raga Nattaikurinji': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'A', 'Bb'],
                'page': 349
            },
            'Lai Soutsanaen': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'Laos',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Raga Kaishikiranjani': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G#', 'B'],
                'primary scale': 'Raga Ghantana',
                'page': 304
            },
            'Maqam Hicaz': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Raga Suddha Simantini': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '2', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab'],
                'page': 384
            },
            'Raga Devamani': {
                'category': 'Symmetrical Scales',
                'interval': ['3', '1', '3', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'G', 'Ab', 'B'],
                'primary scale': 'Augmented',
                'page': 31
            },
            'Genus Diatonicum': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Raga Sutradhari': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'Ab'],
                'primary scale': 'Han-Kumoi',
                'page': 84
            },
            'Raga Surati': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Raga Purna Pancama': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab'],
                'primary scale': 'Raga Malahari desc',
                'page': 333
            },
            'Madenda Modern': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '4', '1', '4'],
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab'],
                'primary scale': 'Pelog Pentatonic',
                'page': 87
            },
            'Raga Gaud Sarang': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Raga Nasamani': {
                'category': 'European Scales',
                'interval': ['3', '1', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Hungarian Major',
                'page': 202
            },
            'Ambassel': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'Ethiopia',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'In',
                'page': 95
            },
            'Takemitzu Tree 2': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '3', '2', '2', '2'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'Gb', 'Ab', 'Bb'],
                'page': 245
            },
            'Raga Paras Descending': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'B', 'Ab', 'G', 'F', 'E', 'Db'],
                'page': 355
            },
            'Bati': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'Ethiopia',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Maqam Karcigar': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '1', '3', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Blues Heptatonic',
                'page': 53
            },
            'Maqam Saba Zamzam': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '3', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'C#', 'D#', 'E', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian b4',
                'page': 139
            },
            'Raga Hamsanada': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '4', '1', '4', '1'],
                'scale': ['C', 'D', 'F#', 'G', 'B'],
                'page': 88
            },
            'Raga Huseni': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Ararai': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'Ethiopia',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Majo',
                'page': 9
            },
            'Raga Kalakanthi': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'G#', 'A'],
                'primary scale': 'Gypsy Hexatonic',
                'page': 196
            },
            'Chromatic Phrygian': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '1', '3', '2', '1', '1'],
                'scale': ['C', 'D#', 'E', 'F', 'G#', 'Bb', 'B'],
                'page': 175
            },
            'Genus Diatonicum Veterum Correctum': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Harmonic Major': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'B'],
                'page': 167
            },
            'Raga Shuddh Kalyan': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian',
                'page': 12
            },
            'Raga Girvani': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'G#', 'A'],
                'primary scale': 'Mela Gavambodhi',
                'page': 253
            },
            'Enigmatic Ascending': {
                'category': 'European Scales',
                'interval': ['1', '3', '2', '2', '2', '1', '1'],
                'scale': ['C', 'Db', 'E', 'F#', 'G#', 'Bb', 'B'],
                'page': 191
            },
            'Raga Devaranji': {
                'category': 'Indian Scales',
                'interval': ['5', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'F', 'G', 'Ab', 'B'],
                'page': 295
            },
            'Chromatic Mixolydian': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '3', '1', '1', '3', '2'],
                'scale': ['C', 'C#', 'D', 'F', 'F#', 'G', 'Bb'],
                'page': 179
            },
            'Raga Kumarapriya': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '6', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'G#', 'B'],
                'page': 324
            },
            'Raga Nattai Ascending': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A#', 'B'],
                'page': 348
            },
            'Raga Sindhu Ramakriya': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Raga Paras desc',
                'page': 355
            },
            'Raga Devamanohari': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian Hexatonic',
                'page': 151
            },
            'Raga Latika': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '3', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'Ab', 'B'],
                'page': 329
            },
            'Raga Malgunji': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '1', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Blues Enneatonic',
                'page': 56
            },
            'Raga Shobhavari': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'Ab'],
                'primary scale': 'Han-Kumoi',
                'page': 84
            },
            'Spanish Octatonic': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '1', '1', '2', '2', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'Gb', 'Ab', 'Bb'],
                'page': 226
            },
            'Raga Puriya Dhanashri': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Raga Bowli Ascending': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '1', '5'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'Ab'],
                'page': 286
            },
            'Hyojo': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Raga Hamsa Vinodini': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'A', 'B'],
                'page': 310
            },
            'Raga Devakriya': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Raga Mukhari': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb'],
                'primary scale': 'Dorian Aeolian',
                'page': 133
            },
            'Zangula': {
                'category': 'European Scales',
                'interval': ['2', '1', '2', '1', '3', '2', '1'],
                'origin': 'Nigeria',
                'scale': ['C', 'E', 'Eb', 'F', 'Gb', 'A', 'B'],
                'primary scale': 'Jeths',
                'page': 206
            },
            'Qing Shang': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Mixolydian b2': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Phrygian Hexatonic': {
                'category': 'Modal Scales',
                'interval': ['3', '2', '2', '1', '2', '2'],
                'scale': ['C', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'page': 137
            },
            'Raga Yaman Kalyan': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Kyemyonjo': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '2', '3'],
                'scale': ['C', 'Eb', 'F', 'G', 'A'],
                'page': 93
            },
            'Major-Lydian Mixed': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Mela Hatakambari': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A#', 'B'],
                'page': 255
            },
            'Raga Nandkauns': {
                'category': 'Jazz Scales',
                'interval': ['3', '1', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': "Rock 'n Roll",
                'page': 64
            },
            'Raga Natabharanam': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b2',
                'page': 17
            },
            'Mela Jyotisvarupini': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'page': 259
            },
            'Mela Varunapriya': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A#', 'B'],
                'page': 276
            },
            'Iwato': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '1', '4', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'Gb', 'Bb'],
                'page': 98
            },
            'Niavent': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'origin': 'Egypt',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Nonatonic 2': {
                'category': 'Miscellaneous Scales',
                'interval': ['1', '2', '1', '1', '1', '1', '2', '1', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'F#', 'G', 'A', 'Bb'],
                'page': 406
            },
            'Mixolydian #4': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Lydian Dominant',
                'page': 19
            },
            'Hungarian Minor b2': {
                'category': 'European Scales',
                'interval': ['1', '1', '1', '3', '1', '1', '3', '1'],
                'origin': 'Hungary',
                'scale': ['C', 'C#', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'page': 204
            },
            'Altered Lydian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Lydian Augmented',
                'page': 18
            },
            'Raga Chaturangini 2': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Raga Ratnakanthi',
                'page': 365
            },
            'Raga Desh Malhar': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Jin-Yu': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'D', 'G', 'G', 'Bb'],
                'primary scale': 'Suspended Pentatonic',
                'page': 77
            },
            'Raga Nagabharanam': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Mela Naganandini',
                'page': 262
            },
            'Ezel': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'Ethiopia',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Raga Kunakri': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'In',
                'page': 95
            },
            'Nigriz': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Aeolian Harmonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '1', '2', '1', '2', '2', '1'],
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian #2',
                'page': 28
            },
            'Messiaen 2nd Mode': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '2', '1', '2', '1', '2', '1', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Diminished Half-tone',
                'page': 34
            },
            'Relative Blues': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '1', '3', '1', '1', '3'],
                'scale': ['C', 'D', 'D#', 'E', 'G', 'G#', 'A'],
                'primary scale': 'Chromatic Hypodorian',
                'page': 182
            },
            'Raga Gandharavam': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Bb'],
                'page': 300
            },
            'Raga Hamsanarayami': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Raga Gamakakriya',
                'page': 299
            },
            'Shang': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'China',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Mischung 6': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'origin': 'Germany',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Algerian': {
                'category': 'Miscellaneous Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1', '2', '1', '2'],
                'origin': 'Tunisia',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B', 'C', 'D', 'Eb', 'F'],
                'page': 399
            },
            'Bebop': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'page': 65
            },
            'Rahawi': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '1', '2', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Locrian Dominant',
                'page': 157
            },
            'Hijaz': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Mela Suryakanta': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Gypsy Inverse',
                'page': 197
            },
            'Raga Kalavati': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A'],
                'page': 318
            },
            'Chromatic Dorian': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '3', '2', '1', '1', '3'],
                'scale': ['C', 'C#', 'D', 'F', 'G', 'G#', 'A'],
                'page': 172
            },
            'LG Octatonic': {
                'category': 'Miscellaneous Scales',
                'interval': ['1', '2', '1', '1', '2', '2', '1', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'page': 404
            },
            'Kata-Kumoi': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '1', '4', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'G', 'Ab'],
                'primary scale': 'Ake-Bono',
                'page': 97
            },
            'Raga Purnanalita': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '2', '2', '5'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G'],
                'primary scale': 'Nando-Kyemyonjo',
                'page': 234
            },
            'Raga Arunajualita': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian Diminished',
                'page': 148
            },
            'Mischung 4': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'origin': 'Germany',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Maqam Suzidil': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Mela Shubhapanturavali': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Lydian Inv.',
                'page': 178
            },
            'Raga Hamir Kalyani': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Raga Kalakanthi 2': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'G#', 'A'],
                'page': 317
            },
            'Scriabin': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '3', '2', '3'],
                'scale': ['C', 'Eb', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic b2',
                'page': 99
            },
            'Messiaen 4th Mode': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '1', '3', '1', '1', '1', '3', '1'],
                'scale': ['C', 'C#', 'D', 'F', 'F#', 'G', 'Ab', 'B'],
                'page': 40
            },
            'Raga Pahadi': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '1', '1', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'G#', 'A', 'A#', 'B'],
                'page': 354
            },
            'Maqam Hijaz Kar': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Chaya Vati': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Raga Vasanta desc',
                'page': 391
            },
            'Raga Vasantha': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '3', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Ab', 'Bb'],
                'primary scale': 'Raga Lalita Bhairav',
                'page': 328
            },
            'Locrian b4': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '2', '2'],
                'scale': ['C', 'Eb', 'Eb', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Altered Dominant',
                'page': 22
            },
            'Raga Vasanta Descending': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'B', 'A', 'F', 'E', 'Db'],
                'page': 390
            },
            'Mixolydian Hexatonic': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '2', '2', '1', '2'],
                'scale': ['C', 'D', 'F', 'G', 'A', 'Bb'],
                'page': 151
            },
            'Spanish Phrygian': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '1', '2', '1', '2', '2'],
                'origin': 'Spain',
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Flamenco',
                'page': 194
            },
            'Mixolydian b13': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Raga Rasranjani': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'A', 'B'],
                'page': 364
            },
            'Raga Pantuvarali': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Puravi b6': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Raga Khamach Descending': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Bb', 'A', 'G', 'F', 'E', 'D'],
                'page': 322
            },
            'Raga Dhunibinnashadjam': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Neapolitan Minor',
                'page': 213
            },
            'Hawaiian': {
                'category': 'Miscellaneous Scales',
                'interval': ['2', '1', '4', '2', '2', '1'],
                'origin': 'Hawaii',
                'scale': ['C', 'D', 'Eb', 'G', 'A', 'B'],
                'page': 403
            },
            'Humayun': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Raga Kokil Pancham': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G', 'Ab'],
                'page': 121
            },
            'Maqam Nakriz': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Noh': {
                'category': 'Asian Scales',
                'interval': ['2', '3', '2', '1', '1', '2', '1'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'F', 'G', 'G#', 'A', 'B'],
                'page': 235
            },
            'Rui Bin': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'D', 'G', 'G', 'Bb'],
                'primary scale': 'Suspended Pentatonic',
                'page': 77
            },
            'Mela Mecakalyani': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian',
                'page': 12
            },
            'Blues Hexatonic': {
                'category': 'Jazz Scales',
                'interval': ['3', '2', '1', '1', '3', '2'],
                'scale': ['C', 'Eb', 'F', 'F#', 'G', 'Bb'],
                'page': 52
            },
            'Messiaen 3rd Mode Inverse': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '2', '1', '1', '2', '1', '1', '2', '1'],
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'G', 'G#', 'A', 'B'],
                'primary scale': 'Genus Chromaticum',
                'page': 48
            },
            'Raga Rageshri': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '4', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'A', 'A#', 'B'],
                'page': 359
            },
            'Raga Shee Ranjani': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'A', 'Bb'],
                'page': 376
            },
            'Raga Senagrani': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '2', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'G#', 'A'],
                'primary scale': 'Raga Malini',
                'page': 335
            },
            'Ancient Chinese': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '2', '3'],
                'origin': 'China',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A'],
                'primary scale': 'Raga Aivarati',
                'page': 280
            },
            'Niagari': {
                'category': 'Asian Scales',
                'interval': ['1', '4', '2', '1', '2', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Insen',
                'page': 229
            },
            'Raga Gauri Velavali': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '2', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A'],
                'primary scale': 'Sho',
                'page': 242
            },
            'Ultralocrian bb3': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '2', '2', '2', '1', '3'],
                'scale': ['C', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
                'page': 166
            },
            'Phrygian Aeolian b4': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '1', '2', '2', '1', '2', '2'],
                'scale': ['C', 'C#', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'page': 138
            },
            'Phrygian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '4', '1', '4'],
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab'],
                'primary scale': 'Pelog Pentatonic',
                'page': 87
            },
            'Ryosen': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Blues Major': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Raga Kamalamanohari': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Raga Paras asc',
                'page': 355
            },
            'Raga Suddha Mukhari': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '3', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G#', 'A'],
                'page': 383
            },
            'Nando-Kyemyonjo': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '2', '2', '5'],
                'origin': 'Korea',
                'scale': ['C', 'D', 'Eb', 'F', 'G'],
                'page': 234
            },
            'Zokuso': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Dorian Aeolian': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb'],
                'page': 133
            },
            'Peiraiotikos': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Marwa Thaat',
                'page': 339
            },
            'Raga Ratnakanthi': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'B'],
                'page': 365
            },
            'Raga Kshanika': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'Ab', 'B'],
                'page': 323
            },
            'Raga Puruhutika': {
                'category': 'Indian Scales',
                'interval': ['5', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'F', 'G', 'A', 'B'],
                'page': 357
            },
            'Raga Kanakambari': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '3', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'G#', 'A'],
                'primary scale': 'Chromatic Dorian',
                'page': 172
            },
            'Locrian bb7': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '2', '1', '2', '1', '3'],
                'scale': ['C', 'Db', 'Eb', 'F', 'F#', 'G#', 'A'],
                'page': 158
            },
            'Raga Megharanji': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '6', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'B'],
                'page': 341
            },
            'Major Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Adonai Malakh': {
                'category': 'European Scales',
                'interval': ['1', '1', '1', '2', '2', '2', '1', '2'],
                'scale': ['C', 'C#', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'page': 190
            },
            'Misheberekh': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Jewish',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Dorian b9 #11': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '2', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A', 'Bb'],
                'page': 136
            },
            'Phrygian Aeolian Mixed': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '1', '2', '2', '1', '2', '2'],
                'scale': ['C', 'C#', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Aeolian b4',
                'page': 138
            },
            'Raga Hindol': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '3', '2', '1'],
                'scale': ['C', 'E', 'Gb', 'A', 'B'],
                'page': 83
            },
            'Raga Gowla Ascending': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'B'],
                'page': 306
            },
            'Raga Multani': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Lydian Inv.',
                'page': 178
            },
            'Raga Suha Sughrai': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Hexatonic',
                'page': 129
            },
            'Raga Prabhati': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '3', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'A', 'B'],
                'primary scale': 'Lydian Hexatonic',
                'page': 143
            },
            'Raga Purvi Thaat': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Namanarayani',
                'page': 263
            },
            'Minor Hexatonic': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '3', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Bb'],
                'page': 129
            },
            'Raga Takka': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G', 'Ab', 'B'],
                'page': 386
            },
            'Ching': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'origin': 'China',
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Hirajoshi',
                'page': 96
            },
            'Mixolydian b9': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Phrygian Major': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Raga Kannadabangala': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'Raga Malahari asc',
                'page': 333
            },
            'Gnossiennes': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Raga Jingla': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Mela Natabhairavi': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Melodic Major': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'page': 20
            },
            'Scottish Hexatonic': {
                'category': 'European Scales',
                'interval': ['2', '2', '1', '2', '2', '3'],
                'origin': 'Scotland',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A'],
                'page': 222
            },
            'Raga Sanjk Ka Hindol': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'Gb', 'A', 'B'],
                'primary scale': 'Raga Hindol',
                'page': 83
            },
            'Raga Vibhas': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '1', '5'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'Ab'],
                'primary scale': 'Raga Bowli asc',
                'page': 286
            },
            'Raga Nileshwari': {
                'category': 'Jazz Scales',
                'interval': ['3', '2', '1', '1', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'F#', 'G', 'Bb'],
                'primary scale': 'Blues',
                'page': 52
            },
            'Bebop Chromatic': {
                'category': 'Jazz Scales',
                'interval': ['1', '1', '2', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'C#', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'page': 75
            },
            'Major Pentatonic b7 #9': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '1', '3', '3', '2'],
                'scale': ['C', 'D#', 'E', 'G', 'Bb'],
                'page': 103
            },
            'Diminished': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '2', '1', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G#', 'A', 'B'],
                'page': 33
            },
            'Raga Shankara': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '3', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'A', 'B'],
                'primary scale': 'Lydian Hexatonic',
                'page': 143
            },
            'Altered Dominant': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '2', '2'],
                'scale': ['C', 'Eb', 'Eb', 'E', 'F#', 'G#', 'Bb'],
                'page': 22
            },
            'Raga Chandrakauns Kafi': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'A', 'Bb'],
                'page': 289
            },
            'Bebop Mixolydian': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Ritzu': {
                'category': 'Asian Scales',
                'interval': ['1', '2', '2', '3', '2', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'Eb', 'F', 'G#', 'Bb'],
                'page': 241
            },
            'Kartzihiar': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '1', '3', '1', '2'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Blues Heptatonic',
                'page': 53
            },
            'Aeolian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'page': 14
            },
            'Raga Sindhi-Bhairavi': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '1', '1', '1', '2', '1', '2', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'D#', 'E', 'F', 'G', 'G#', 'A#', 'B'],
                'page': 380
            },
            'Raga Malkauns': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '3', '2', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G#', 'A#', 'B'],
                'page': 334
            },
            'Dorian b9': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '1', '3', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Locrian #6',
                'page': 24
            },
            'Eskimo Hexatonic 2': {
                'category': 'Miscellaneous Scales',
                'interval': ['2', '2', '2', '2', '3', '1'],
                'origin': 'Alaska',
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'B'],
                'page': 401
            },
            'Raga Varamu': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'A', 'Bb'],
                'primary scale': 'Raga Chandrakauns Kafi',
                'page': 289
            },
            'Mixolydian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '3', '2'],
                'scale': ['C', 'E', 'F', 'G', 'Bb'],
                'page': 104
            },
            'Dorian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'page': 10
            },
            'Gypsy Minor': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'origin': 'Hungary',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'page': 198
            },
            'Raga Narmada': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Namanarayani',
                'page': 263
            },
            'Raga Gamakakriya': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'B'],
                'page': 299
            },
            'Blues Minor': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '3', '2', '2'],
                'scale': ['C', 'Eb', 'F', 'Ab', 'Bb'],
                'primary scale': 'Man Gong',
                'page': 78
            },
            'Superlocrian bb3': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '2', '2', '2', '2', '2'],
                'scale': ['C', 'C#', 'D', 'E', 'F#', 'G#', 'Bb'],
                'page': 162
            },
            'Raga Chakravakam': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Raga Supradhipam': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Gypsy Inverse',
                'page': 197
            },
            'Soft Descend': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'In',
                'page': 95
            },
            'Raga Chitthakarshini': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '2', '3', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'Ab'],
                'page': 115
            },
            'Lydian Hexatonic': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '3', '2', '2', '1'],
                'scale': ['C', 'D', 'E', 'G', 'A', 'B'],
                'page': 143
            },
            'Spanish Heptatonic': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '1', '2', '2', '2'],
                'origin': 'Spain',
                'scale': ['C', 'D#', 'E', 'F', 'Gb', 'Ab', 'Bb'],
                'page': 225
            },
            'Chromatic Mixolydian 2': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '2', '2', '1', '3', '2'],
                'scale': ['C', 'C#', 'D', 'E', 'F#', 'G', 'Bb'],
                'page': 180
            },
            'Raga Manji': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb'],
                'primary scale': 'Dorian Aeolian',
                'page': 133
            },
            'Harmonic Minor #4': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Mela Dhavalambari': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'G#', 'A'],
                'page': 249
            },
            'Raga Mruganandana': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'A', 'B'],
                'page': 344
            },
            'Raga Chandrajyoti': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'A'],
                'page': 288
            },
            'Major Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'page': 76
            },
            'Mela Rupavati': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '2', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A#', 'B'],
                'page': 270
            },
            'Mixolydian Augmented': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '3', '1', '1', '2'],
                'scale': ['C', 'D', 'E', 'F', 'G#', 'A', 'Bb'],
                'page': 154
            },
            'Raga Suddha Todi': {
                'category': 'Asian Scales',
                'interval': ['1', '2', '2', '3', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G#', 'Bb'],
                'primary scale': 'Ritzu',
                'page': 241
            },
            'Raga Mian Ki Malhar': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'A#', 'B'],
                'page': 342
            },
            'Semilocrian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '1', '2', '2', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Half Diminished',
                'page': 21
            },
            'Raga Varali': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Mela Jhalavarli',
                'page': 257
            },
            'Raga Santanamanjari': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '2', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'G#', 'A'],
                'page': 370
            },
            'Diminished Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '3', '2', '3', '1'],
                'scale': ['C', 'Eb', 'F#', 'G#', 'B'],
                'page': 104
            },
            'Whole-Tone Diminished': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '2', '1', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Diminished',
                'page': 33
            },
            'Raga Phenadyuti 2': {
                'category': 'Asian Scales',
                'interval': ['1', '4', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Insen',
                'page': 229
            },
            'Raga Khamaj That': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Messiaen 5th Mode': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '4', '1', '1', '4', '1'],
                'scale': ['C', 'Db', 'F', 'F#', 'G', 'B'],
                'page': 42
            },
            'Maqam Hijaz-Nahawand': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Raga Nayaki': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Hexatonic',
                'page': 129
            },
            "Rock 'n Roll": {
                'category': 'Jazz Scales',
                'interval': ['3', '1', '1', '2', '2', '1', '2'],
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'page': 64
            },
            'Lydian Augmented #3': {
                'category': 'Asian Scales',
                'interval': ['2', '3', '1', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'F', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Nohkan',
                'page': 236
            },
            'Petrushka chord': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '3', '2', '1', '3', '2'],
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Bb'],
                'page': 36
            },
            'Augmented Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '1', '3', '1', '4'],
                'scale': ['C', 'D#', 'E', 'G', 'Ab'],
                'page': 111
            },
            'Van Der Host': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '2', '2', '1', '1', '2', '2', '1'],
                'scale': ['C', 'Db', 'Eb', 'F', 'F#', 'G', 'A', 'B'],
                'page': 51
            },
            'Neapolitan Major b4': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '3', '2', '2', '1'],
                'origin': 'Italy',
                'scale': ['C', 'Db', 'Eb', 'E', 'G', 'A', 'B'],
                'page': 211
            },
            'Lydian Augmented #2': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '2', '2', '1', '2', '1'],
                'scale': ['C', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Aeolian b1',
                'page': 156
            },
            'Bartok': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Lydian Dominant',
                'page': 19
            },
            'Suspended Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'scale': ['C', 'D', 'G', 'G', 'Bb'],
                'page': 77
            },
            'Raga Dhipaka': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Bebop Locrian': {
                'category': 'Jazz Scales',
                'interval': ['1', '2', '2', '1', '1', '1', '2', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'F#', 'G', 'Ab', 'Bb'],
                'page': 74
            },
            'Center-Cluster PentaMirror': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '1', '1', '3', '4'],
                'scale': ['C', 'D#', 'E', 'F', 'Ab'],
                'page': 111
            },
            'Raga Suddha Saveri': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Phrygian b4': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '3', '1', '2', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'G', 'Ab', 'Bb'],
                'page': 139
            },
            'Raga Bowli Descending': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '1', '3', '1', ''],
                'origin': 'India',
                'scale': ['C', 'B', 'Ab', 'G', 'E', 'Db'],
                'page': 286
            },
            'Mela Venaspati': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'A', 'Bb'],
                'page': 275
            },
            'Leading Whole-Tone': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '2', '2', '1', '1'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'A#', 'B'],
                'page': 189
            },
            'Hungarian Folk': {
                'category': 'Modal Scales',
                'interval': ['[1', '3', '1', '2', '1', '3', '1'],
                'origin': 'Hungary',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Jotismatti': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Jyotisvarupini',
                'page': 259
            },
            'Ryukyu': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '4', '1'],
                'origin': 'Japan',
                'scale': ['C', 'E', 'F', 'G', 'B'],
                'primary scale': 'Ionian Pentatonic',
                'page': 86
            },
            'Hungarian Minor': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'origin': 'Hungary',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Chromatic Mixolydian Inverse': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '1', '1', '3', '1', '1'],
                'scale': ['C', 'D', 'F', 'F#', 'G', 'Bb', 'B'],
                'page': 181
            },
            'Raga Rasamanjari 2': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'B'],
                'page': 362
            },
            'Lydian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Hirajoshi',
                'page': 96
            },
            'Raga Dvigandharabushini': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '1', '3', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'D#', 'E', 'G', 'G#', 'A'],
                'page': 182
            },
            'Lydian #2': {
                'category': 'Major and Minor Scales',
                'interval': ['3', '1', '2', '1', '2', '2', '1'],
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A', 'B'],
                'page': 28
            },
            'Maqam Hedjaz': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Lydian Mixolydian': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'Bb', 'B'],
                'page': 147
            },
            'Blues Minor Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Mixolydian b6': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Messiaen 7th Mode Inverse': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '1', '1', '1', '2', '1', '1', '1', '1'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'F#', 'G#', 'A', 'Bb', 'B'],
                'page': 47
            },
            'Raga Tivravahini': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b9 #11',
                'page': 136
            },
            'Mela Sarasangi': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Major',
                'page': 167
            },
            'Raga Mand': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A'],
                'primary scale': 'Raga Nagaswaravali',
                'page': 114
            },
            'Raga Mandari': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Raga Gamakakriya',
                'page': 299
            },
            'Neapolitan Minor': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '1', '3', '1'],
                'origin': 'Italy',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B'],
                'page': 213
            },
            'Yishtabach': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '1', '2', '2', '2'],
                'origin': 'Jewish',
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Locrian',
                'page': 15
            },
            'Maqam Tarzanuyn': {
                'category': 'Asian Scales',
                'interval': ['1', '2', '1', '1', '1', '1', '1', '1', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb'],
                'page': 233
            },
            'Raga Shyamalam': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'G#', 'A'],
                'primary scale': 'Mela Syamalangi',
                'page': 272
            },
            'Maqam Farahfaza': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '1', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'B'],
                'primary scale': 'Bebop Harmonic Minor',
                'page': 72
            },
            'Neapolitan Major b5': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '1', '3', '2', '1'],
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'A', 'B'],
                'page': 212
            },
            'Chromatic Hypodorian Inverse': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '1', '3', '1', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G#', 'A', 'Bb'],
                'page': 183
            },
            'Raga Nata': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Raga Nattai asc',
                'page': 348
            },
            'Cushak': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'Armenia',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Raga Gauri': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'B'],
                'primary scale': 'Raga Gowla asc',
                'page': 306
            },
            'Gu': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '2', '1'],
                'origin': 'China',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian',
                'page': 12
            },
            'Hungarian Gypsy': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '2', '2'],
                'origin': 'Hungary',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Gypsy',
                'page': 195
            },
            'Hirajoshi': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'origin': 'Japan',
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'page': 96
            },
            'Raga Puriya': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Marwa Thaat',
                'page': 339
            },
            'Bebop Natural Minor': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '1', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'B'],
                'primary scale': 'Bebop Harmonic Minor',
                'page': 72
            },
            'Sakura': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Ab', 'In'],
                'page': 95
            },
            'Shostakovich': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '2', '1', '2', '2', '1'],
                'origin': 'Russia',
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'G', 'A', 'B'],
                'page': 224
            },
            'Raga Revati': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Raga Jivantini': {
                'category': 'Indian Scales',
                'interval': ['3', '3', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Raga Gaurikriya',
                'page': 303
            },
            'Mixolydian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'page': 13
            },
            'Raga Vegavahini Ascending': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A', 'Bb'],
                'page': 392
            },
            'Raga Kafi That': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Lydian #5': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Lydian Augmented',
                'page': 18
            },
            'Raga Gaulipantu': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Bhupeshwari': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'Ab'],
                'primary scale': 'Major Pentatonic b6',
                'page': 102
            },
            'Raga Jinavali': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Mela Jhalavarli',
                'page': 257
            },
            'Raga Dhavalangam': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab'],
                'page': 296
            },
            'Raga Revagupti': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '1', '5'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'Ab'],
                'primary scale': 'Raga Bowli asc',
                'page': 286
            },
            'Mela Latangi': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Pelog',
                'page': 239
            },
            'Mela Yagapriya': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'G#', 'A'],
                'page': 278
            },
            'Raga Ramkali 2': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '4', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab'],
                'primary scale': 'Pelog Pentatonic',
                'page': 87
            },
            'Raga Kumurdaki': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '5', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'B'],
                'page': 325
            },
            'Raga Bhanumati': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mela Venaspati',
                'page': 275
            },
            'Minor Pentatonic with Leading Tones': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '1', '1', '1', '1', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'F#', 'G', 'A', 'A#', 'B'],
                'page': 188
            },
            'Mela Harikamboji': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Raga Khamas': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Raga Vegavahini asc',
                'page': 392
            },
            'Oriental': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '3', '1', '2'],
                'origin': 'China',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'Bb'],
                'page': 237
            },
            'Raga Kalingada': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Gambhiranata': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'B'],
                'primary scale': 'Ionian Pentatonic',
                'page': 86
            },
            'Raga Palasi': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Hexatonic',
                'page': 129
            },
            'Major Locrian': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '1', '2', '2', '2'],
                'scale': ['C', 'D', 'E', 'F', 'Gb', 'Ab', 'Bb'],
                'page': 130
            },
            'Raga Sailadesakshi': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Houzam',
                'page': 201
            },
            'Raga Deskar': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Raga Gopikatilaka': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Bb'],
                'page': 305
            },
            'Raga Gurjari Todi': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '2', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'Gb', 'Ab', 'Bb'],
                'page': 307
            },
            'Aeolian Major': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Maqam Huzzam': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '3', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'C#', 'D#', 'E', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian b4',
                'page': 139
            },
            'Raga Velavali': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Melodic Minor',
                'page': 16
            },
            'Mischung 5': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'Germany',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Mela Raghupriya': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'A#', 'B'],
                'page': 268
            },
            'Lydian Dominant b6': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '1', '1', '2', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'page': 146
            },
            'Mela Calanata': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Bb'],
                'page': 248
            },
            'Raga Siva Kambhoji': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Bb'],
                'page': 381
            },
            'Lai Yai': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'Laos',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Maqam Nahawand': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '1', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'B'],
                'primary scale': 'Bebop Harmonic Minor',
                'page': 72
            },
            'Raga Vegavahini Descending': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Bb', 'A', 'G', 'F', 'E', 'Db'],
                'page': 392
            },
            'Lydian Minor': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '1', '1', '2', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Lydian Dominant b6',
                'page': 146
            },
            'Major-Dorian Mixed': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Blues Enneatonic',
                'page': 56
            },
            'Maqam Athar Kurd': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Lydian Inv.',
                'page': 178
            },
            'Ultraphrygian': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '3', '1', '1', '3'],
                'scale': ['C', 'C#', 'D#', 'E', 'G', 'G#', 'A'],
                'page': 142
            },
            'Raga Dumyaraga': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian Diminished',
                'page': 148
            },
            'Bebop Harmonic Minor': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '1', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'B'],
                'page': 72
            },
            'Kumoi': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '1', '4', '2', '3'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'G', 'A'],
                'primary scale': 'Dorian Pentatonic',
                'page': 81
            },
            'Ravel': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '2', '2'],
                'scale': ['C', 'Eb', 'Eb', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Altered Dominant',
                'page': 22
            },
            'Major Pentatonic b6': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '1', '4'],
                'scale': ['C', 'D', 'E', 'G', 'Ab'],
                'page': 102
            },
            'Raga Kuntvarali': {
                'category': 'Indian Scales',
                'interval': ['5', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'F', 'G', 'A', 'Bb'],
                'page': 326
            },
            'Mela Kiravani': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Raga Lalit': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '1', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'B'],
                'primary scale': 'Chromatic Lydian',
                'page': 177
            },
            'Raga Mohanam': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Raga Bhatiyar': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '1', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'page': 283
            },
            'Raga Ragamalini': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A'],
                'primary scale': 'Raga Kalavati',
                'page': 318
            },
            'Hijaz Kar': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'Arabia',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Chromatic Lydian': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '1', '3', '2', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'B'],
                'page': 177
            },
            'Ryo': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '1', '1', '1'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Lydian Mixolydian',
                'page': 147
            },
            'Mela Hemavati': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Raga Manaranjani': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'Bb'],
                'page': 336
            },
            'Mela Namanarayani': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'page': 263
            },
            'Raga Chayanata': {
                'category': 'Jazz Scales',
                'interval': ['3', '1', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': "Rock 'n Roll",
                'page': 64
            },
            'Dorian #4': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Byzantine Liturgical Chromatic': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Shri': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Blues Enneatonic 2': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '1', '1', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'F#', 'G', 'A', 'Bb'],
                'page': 57
            },
            'Raga Manavi': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '4', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'G', 'A', 'Bb'],
                'page': 337
            },
            'Raga Chandrakauns Kiravani': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G#', 'B'],
                'page': 290
            },
            'Zhalibny Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Raga Kuksumakaram': {
                'category': 'Major and Minor Scales',
                'interval': ['3', '1', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian #2',
                'page': 28
            },
            'Zilof': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Spain',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Ghana Pentatonic': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '2', '2', '5'],
                'origin': 'Ghana',
                'scale': ['C', 'D', 'Eb', 'F', 'G'],
                'primary scale': 'Nando-Kyemyonjo',
                'page': 234
            },
            'Mischung 1': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '2', '1'],
                'origin': 'Germany',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Melodic Minor',
                'page': 16
            },
            'Aeolian b1': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '2', '2', '1', '2', '1'],
                'scale': ['C', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
                'page': 156
            },
            'Yona Nuki Major': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Raga Gamakasamantam': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Lydian Inv.',
                'page': 178
            },
            'Blues Phrygian': {
                'category': 'Jazz Scales',
                'interval': ['1', '2', '2', '1', '1', '3', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'F#', 'G', 'Bb'],
                'page': 59
            },
            'Raga Bhankar': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '1', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'B'],
                'primary scale': 'Chromatic Lydian',
                'page': 177
            },
            'Damian Emmanuel': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '2', '2'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Gypsy',
                'page': 195
            },
            'Messiaen 2nd Mode Truncated': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '2', '3', '1', '2', '3'],
                'scale': ['C', 'Eb', 'Eb', 'F#', 'G', 'A'],
                'page': 38
            },
            'Messiaen 3rd Mode': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '1', '2', '1', '1', '2', '1', '1'],
                'scale': ['C', 'D', 'D#', 'E', 'F#', 'G', 'G#', 'Bb', 'B'],
                'page': 39
            },
            'Raga Ghantana': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G#', 'B'],
                'page': 304
            },
            'Raga Kumudki': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '5', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'B'],
                'primary scale': 'Raga Kumurdaki',
                'page': 325
            },
            'Raga Pilu': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb', 'B'],
                'page': 132
            },
            'Raga Madhuvanti': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian Diminished',
                'page': 148
            },
            'Raga Kharapriya': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Mela Manavati': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'A', 'B'],
                'page': 261
            },
            'Raga Sindhura Kafi': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'B'],
                'page': 379
            },
            'Raga Rasamanjari': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '2', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Lydian #2 #6',
                'page': 145
            },
            'Pomeroy': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '2', '2'],
                'scale': ['C', 'Eb', 'Eb', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Altered Dominant',
                'page': 22
            },
            'Mela Gayakapriya': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'G#', 'A'],
                'page': 254
            },
            'Pireotikos': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Mela Ganamurti': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'Ab', 'B'],
                'page': 252
            },
            'Raga Navamanohari': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'Ab', 'Bb'],
                'page': 350
            },
            'Raga Khamaj': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Synthetic Mixture #5': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '2', '1', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'A', 'Bb'],
                'primary scale': 'Lydian Aug. Dominant',
                'page': 150
            },
            'Maqam Hisar': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Altered Major Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '1', '3', '4'],
                'scale': ['C', 'D', 'E', 'F', 'Ab'],
                'page': 108
            },
            'Raga Lasaki': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Raga Saravati': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'G#', 'A'],
                'page': 373
            },
            'Raga Madhukauns': {
                'category': 'Indian Scales',
                'interval': ['3', '3', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F#', 'G', 'A', 'Bb'],
                'page': 330
            },
            'Raga Marga Hindola': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'A', 'B'],
                'primary scale': 'Raga Chandrakauns M.',
                'page': 291
            },
            'Maqam Nawa Athar': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Lai Noi': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'Laos',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Leading Whole-Tone Inverse': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '2', '2', '2', '2', '2'],
                'scale': ['C', 'C#', 'D', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Superlocrian bb3',
                'page': 162
            },
            'Nam': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'Vietnam',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Insen Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Raga Airavati': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A'],
                'page': 280
            },
            'Superlocrian': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '2', '2'],
                'scale': ['C', 'Eb', 'Eb', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Altered Dominant',
                'page': 22
            },
            'Raga Bhimpalasi': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Raga Harikauns': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '3', '2', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Chin',
                'page': 92
            },
            'Quin-Yu': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'D', 'G', 'G', 'Bb'],
                'primary scale': 'Suspended Pentatonic',
                'page': 77
            },
            'Raga Bhavani': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Bhavapriya',
                'page': 247
            },
            'Two-semitone Tritone': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '1', '4', '1', '1', '4'],
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'Ab'],
                'page': 49
            },
            'Neapolitan': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '2', '2', '1'],
                'origin': 'Italy',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'B'],
                'page': 210
            },
            'Raga Neelangi': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '3', '2', '1', '3'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G#', 'A'],
                'page': 37
            },
            'Raga Kedaram Ascending': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'B'],
                'page': 321
            },
            'Ukrainian Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Ukraine',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Raga Trimurti': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '4', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'G', 'Ab', 'Bb'],
                'page': 388
            },
            'Mixolydian #1': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '1', '3'],
                'scale': ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A'],
                'primary scale': 'Ultralocrian',
                'page': 29
            },
            'Minor b5': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '1', '2', '2', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Half Diminished',
                'page': 21
            },
            'Chromatic Permutated Diatonic Dorian': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '2', '1', '2', '1', '1', '2', '1'],
                'scale': ['C', 'C#', 'D', 'E', 'F', 'G', 'G#', 'A', 'B'],
                'page': 186
            },
            'Mela Navanitam': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'A', 'Bb'],
                'page': 264
            },
            'Raga Kiranavali': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Superlocrian bb6 bb7': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '2', '1', '2', '3'],
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'G', 'A'],
                'page': 164
            },
            'Raga Dhauta Pancama': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Mela Dhatuvardhani',
                'page': 250
            },
            'Bebop Melodic Minor': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'B'],
                'page': 71
            },
            'Insen': {
                'category': 'Asian Scales',
                'interval': ['1', '4', '2', '1', '2', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Ab', 'Bb'],
                'page': 229
            },
            'Raga Suddha Pancama': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '2', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'Ab', 'B'],
                'primary scale': 'Persian',
                'page': 240
            },
            'Mela Salaga': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'G#', 'A'],
                'page': 271
            },
            'Phrygian': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'page': 11
            },
            'Sabach': {
                'category': 'European Scales',
                'interval': ['2', '1', '1', '3', '1', '2', '2'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'D#', 'E', 'G', 'Ab', 'Bb'],
                'page': 220
            },
            'Raga None': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '1', '2', '3', '1', '1'],
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Bb', 'B'],
                'primary scale': 'Chromatic Dorian Inverted',
                'page': 173
            },
            'Pelog Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '4', '1', '4'],
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab'],
                'page': 87
            },
            'Raga Sthavarajam': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b9 #11',
                'page': 136
            },
            'Freygish': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Mela Senavati': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Neapolitan Minor',
                'page': 213
            },
            'Major Pentatonic b2 b5': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '3', '3'],
                'scale': ['C', 'Db', 'E', 'Gb', 'A'],
                'page': 100
            },
            'Bebop Half-diminished': {
                'category': 'Jazz Scales',
                'interval': ['1', '2', '2', '1', '1', '1', '3', '1'],
                'scale': ['C', 'Db', 'Eb', 'F', 'F#', 'G', 'Ab', 'B'],
                'page': 73
            },
            'Raga Bauli': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'Ab', 'B'],
                'primary scale': 'Raga Bowli desc',
                'page': 286
            },
            'Hungarian Minor Inverse': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '3', '1', '2'],
                'origin': 'Hungary',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Oriental',
                'page': 237
            },
            'Oriental 2': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '3', '1', '1', '1'],
                'origin': 'China',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'A#', 'B'],
                'page': 238
            },
            'Raga Sahera': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '2', '2', '2', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Whole-Tone',
                'page': 30
            },
            'Locrian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '1', '2', '4', '2'],
                'scale': ['C', 'D#', 'E', 'Gb', 'Bb'],
                'page': 108
            },
            'Mela Sanmukhapriya': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Gypsy',
                'page': 195
            },
            'Raga Madhyamavati': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'G', 'G', 'Bb'],
                'primary scale': 'Suspended Pentatonic',
                'page': 77
            },
            'Tezeta Minor': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '4', '1', '4'],
                'origin': 'Ethiopia',
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab'],
                'primary scale': 'Pelog Pentatonic',
                'page': 87
            },
            'Tezeta Major': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'Ethiopia',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Ukranian Dorian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Ukraine',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Kaffa': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Ethiopia',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Half Diminished': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '1', '2', '2', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'page': 21
            },
            'Raga Nisada': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Mela Nitimati',
                'page': 265
            },
            'Raga Shreeranjani': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'A', 'Bb'],
                'page': 376
            },
            'Maqam Cargah': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Major',
                'page': 9
            },
            'Raga Sankara': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '3', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'A', 'B'],
                'primary scale': 'Lydian Hexatonic',
                'page': 143
            },
            'Raga Janasammodini': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'Ab'],
                'primary scale': 'Major Pentatonic b6',
                'page': 102
            },
            'Raga Shri Kalyan': {
                'category': 'Indian Scales',
                'interval': ['2', '4', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'F#', 'G', 'A'],
                'page': 377
            },
            'Miyakobushi': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Raga Nattai Descending': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'B', 'G', 'F', 'D#'],
                'page': 348
            },
            'Pentatonic Whole-Tone': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '2', '2', '2'],
                'scale': ['C', 'E', 'F#', 'G#', 'Bb'],
                'page': 110
            },
            'Raga Ratipriya': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Lydian Dominant b6',
                'page': 146
            },
            'Jeths': {
                'category': 'European Scales',
                'interval': ['2', '1', '2', '1', '3', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'A', 'B'],
                'page': 206
            },
            'Hitzaz': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Mela Tenarupi': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'A#', 'B'],
                'page': 274
            },
            'Ionian b5': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '1', '3', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'Gb', 'A', 'B'],
                'page': 125
            },
            'Raga Hari Nata': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A', 'B'],
                'page': 311
            },
            'Raga Rishabapriya': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Lydian Dominant b6',
                'page': 146
            },
            'Dorian b2': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '2', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'Bb'],
                'page': 17
            },
            'Raga Jog': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Bb'],
                'primary scale': 'Mela Calanata',
                'page': 248
            },
            'Ionian #5': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '3', '1', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G#', 'A', 'B'],
                'page': 126
            },
            'Mela Hanumatodi': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Sho': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '2', '2', '2', '3'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A'],
                'page': 242
            },
            'Raga Deshi 2': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Melodic Minor',
                'page': 16
            },
            'Raga Ganavaridhi': {
                'category': 'Jazz Scales',
                'interval': ['3', '1', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': "Rock 'n Roll",
                'page': 64
            },
            'Gypsy Hexatonic Inverse': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '1', '3', '1'],
                'origin': 'Hungary',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Sengiach',
                'page': 223
            },
            'Raga Nabhomani': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '5'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G'],
                'page': 346
            },
            'Xin': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'China',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Major',
                'page': 9
            },
            'Raga Desya Khamas': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Raga Vegavahini asc',
                'page': 392
            },
            'Geez': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'Ethiopia',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Altered Diminished': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '1', '2', '2', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Half Diminished',
                'page': 21
            },
            'Raga Viyogavarali': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '2', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'Ab', 'B'],
                'page': 395
            },
            'Raga Kuntala': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'G#', 'A'],
                'primary scale': 'Mela Kantamani',
                'page': 260
            },
            'Raga Rukmangi': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '4', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'G', 'Bb'],
                'page': 367
            },
            'Mixolydian Augmented Maj9': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '3', '1', '1', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G#', 'A', 'Bb'],
                'page': 155
            },
            'In': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'page': 95
            },
            'In1': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'page': 95
            },
            'Raga Bairari': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Marwa Thaat',
                'page': 339
            },
            'Raga Malahari Descending': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Ab', 'G', 'F', 'E', 'Db'],
                'page': 333
            },
            'Mela Vagadhisvari': {
                'category': 'Jazz Scales',
                'interval': ['3', '1', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': "Rock 'n Roll",
                'page': 64
            },
            'Locrian': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '1', '2', '2', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'page': 15
            },
            'Raga Vijayanagari': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A'],
                'page': 392
            },
            'Espla': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '1', '1', '2', '2', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Spanish Octatonic',
                'page': 226
            },
            'Raga Suddha Ramakriya': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Raga Purvi': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Raga Devarangini 2': {
                'category': 'European Scales',
                'interval': ['2', '2', '1', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A'],
                'primary scale': 'Scottish Hexatonic',
                'page': 222
            },
            'Messiaen 6th Mode Inverse': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '1', '2', '2', '1', '1', '2', '2'],
                'scale': ['C', 'C#', 'D', 'F', 'F#', 'G', 'Ab', 'Bb'],
                'page': 45
            },
            'Ujo': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'Korea',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Raga Bibhas': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '3', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic b2',
                'page': 99
            },
            'Raga Kalahamsa': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'G#', 'A'],
                'primary scale': 'Mela Yagapriya',
                'page': 278
            },
            'Ultralocrian': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '1', '3'],
                'scale': ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A'],
                'page': 29
            },
            'Symmetrical Nonatonic': {
                'category': 'Miscellaneous Scales',
                'interval': ['1', '1', '2', '2', '1', '1', '2', '1', '1'],
                'scale': ['C', 'C#', 'D', 'E', 'F#', 'G', 'G#', 'A#', 'B'],
                'page': 407
            },
            'Blues Octatonic': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '1', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G', 'A', 'Bb'],
                'page': 55
            },
            'Mela Rasikapriya': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '2', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Lydian #2 #6',
                'page': 145
            },
            'Minor Locrian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '1', '2', '2', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Half Diminished',
                'page': 21
            },
            'Hon-Kumoi-Joshi': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '1', '4', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'Gb', 'Bb'],
                'primary scale': 'Iwato',
                'page': 98
            },
            'Raga Bhinnasadjam': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Neapolitan Minor',
                'page': 213
            },
            'Raga Reva': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '1', '5'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'Ab'],
                'primary scale': 'Raga Bowli asc',
                'page': 286
            },
            'Mela Visvambhari': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A#', 'B'],
                'page': 277
            },
            'Raga Bindumalini': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Gypsy Inverse': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '2', '2', '1'],
                'origin': 'Hungary',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'B'],
                'page': 197
            },
            'Minor 6th Added': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '2', '3'],
                'scale': ['C', 'Eb', 'F', 'G', 'A'],
                'primary scale': 'Kyemyonjo',
                'page': 93
            },
            'Mela Ramapriya': {
                'category': 'European Scales',
                'interval': ['1', '3', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Romanian Major',
                'page': 219
            },
            'Raga Pratapa': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Namanarayani',
                'page': 263
            },
            'Semilocrian b4': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '1', '2', '2', '2', '2'],
                'scale': ['C', 'D', 'D#', 'E', 'F#', 'G#', 'Bb'],
                'page': 161
            },
            'Raga Simhavahini': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Raga Paras asc',
                'page': 355
            },
            'Raga Shubravarni': {
                'category': 'Indian Scales',
                'interval': ['2', '4', '3', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F#', 'A', 'Bb'],
                'page': 378
            },
            'Raga Darbar': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian Hexatonic',
                'page': 151
            },
            'Chromatic Hypolydian': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'page': 184
            },
            'Blues Heptatonic 2': {
                'category': 'Jazz Scales',
                'interval': ['3', '2', '1', '1', '2', '1', '2'],
                'scale': ['C', 'Eb', 'F', 'F#', 'G', 'A', 'Bb'],
                'page': 54
            },
            'Blues Heptatonic': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '1', '3', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'page': 53
            },
            'Raga Basant': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Raga Yamuna Kalyani': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A'],
                'primary scale': 'Raga Aivarati',
                'page': 280
            },
            'Raga Jyoti': {
                'category': 'Indian Scales',
                'interval': ['4', '2', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F#', 'G', 'Ab', 'Bb'],
                'page': 315
            },
            'Raga Rangini': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'Gb', 'A', 'B'],
                'page': 361
            },
            'Maqam Zanjaran': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Nohkan': {
                'category': 'Asian Scales',
                'interval': ['2', '3', '1', '2', '1', '2', '1'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'F', 'F#', 'G#', 'A', 'B'],
                'page': 236
            },
            'Raga Madhava Manohari': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Mela Syamalangi': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'G#', 'A'],
                'page': 272
            },
            'Ahava Rabba': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Jewish',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Ahava Rabba1': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Jewish',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Jia Zhong': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Raga Tarangini': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Raga Bahudari': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Raga Vegavahini asc',
                'page': 392
            },
            'Phrygian Locrian': {
                'category': 'Jazz Scales',
                'interval': ['1', '2', '2', '1', '1', '1', '2', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Bebop Locrian',
                'page': 74
            },
            'Mela Bhavapriya': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'page': 247
            },
            'Magen Abot': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '2', '2', '1', '2', '1'],
                'origin': 'Jewish',
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'G#', 'A', 'B'],
                'page': 208
            },
            'Raga Vamsavathi': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Mela Divyamani',
                'page': 251
            },
            'Raga Gangatarangini': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '1', '2', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'Gb', 'Ab', 'B'],
                'page': 301
            },
            'Harmonic Minor Inverse': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'page': 170
            },
            'Raga Malarani': {
                'category': 'Indian Scales',
                'interval': ['2', '4', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F#', 'G', 'A#', 'B'],
                'page': 331
            },
            'Raga Lalita Panchami': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Mela Kokilapriya': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Neapolitan Major',
                'page': 210
            },
            'Maqam Ussak': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Quan Ming': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '3', '2', '2'],
                'origin': 'China',
                'scale': ['C', 'Eb', 'F', 'Ab', 'Bb'],
                'primary scale': 'Man Gong',
                'page': 78
            },
            'Raga Bhinna Pancama': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'Ab', 'B'],
                'page': 284
            },
            'Modus Conjunctus': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '2', '1', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Diminished',
                'page': 33
            },
            'Mela Kantamani': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'G#', 'A'],
                'page': 260
            },
            'Raga Multani 2': {
                'category': 'Indian Scales',
                'interval': ['3', '3', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F#', 'G', 'B'],
                'page': 345
            },
            'Mela Bhairavi That': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Raga Padi': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab', 'B'],
                'page': 353
            },
            'Raga Kalyana Vasantha': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Raga Devagandhari': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Blues Mixed': {
                'category': 'Jazz Scales',
                'interval': ['3', '1', '1', '1', '1', '3', '2'],
                'scale': ['C', 'D#', 'E', 'F', 'F#', 'G', 'Bb'],
                'page': 62
            },
            'Takemitzu Tree 1': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '3', '2', '3', '1'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'Gb', 'Ab', 'B'],
                'page': 244
            },
            'Flamenco': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '1', '2', '1', '2', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'G', 'Ab', 'Bb'],
                'page': 194
            },
            'Pyeong Jo': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '4', '1', '2'],
                'origin': 'Korea',
                'scale': ['C', 'D', 'F', 'A', 'Bb'],
                'page': 117
            },
            'Raga Ribhavari': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Tcherepnin Major Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '4', '1'],
                'origin': 'Russia',
                'scale': ['C', 'D', 'F', 'G', 'B'],
                'page': 106
            },
            'Ionian Augmented #2': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '1', '3', '1', '2', '1'],
                'scale': ['C', 'D#', 'E', 'F', 'G#', 'A', 'B'],
                'page': 127
            },
            'Raga Trishuli': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Houzam',
                'page': 201
            },
            'Raga Suposhini': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian Hexatonic',
                'page': 151
            },
            'Phrygian Mixolydian': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '2', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b2',
                'page': 17
            },
            'Mela Divyamani': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A#', 'B'],
                'page': 251
            },
            'Raga Sauviram': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Mela Suvarnangi',
                'page': 273
            },
            'Raga Dhani': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Sengiach': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '1', '3', '1'],
                'origin': 'Greece',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Ab', 'B'],
                'page': 223
            },
            'Raga Hamsagiri': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '2', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Lydian #2 #6',
                'page': 145
            },
            'Blues Minor Maj7': {
                'category': 'Jazz Scales',
                'interval': ['3', '2', '1', '1', '4', '1'],
                'scale': ['C', 'Eb', 'F', 'F#', 'G', 'B'],
                'page': 60
            },
            'Double Harmonic Minor': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Raga Sunada Vinodini': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'Gb', 'A', 'B'],
                'primary scale': 'Raga Hindol',
                'page': 83
            },
            'Raga Phenadyuti': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Ratnangi',
                'page': 269
            },
            'Naka Zora': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'In',
                'page': 10
            },
            'Maqam Sultani Yakah': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Raga Hindolita': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'A', 'B'],
                'primary scale': 'Raga Vasanta asc',
                'page': 390
            },
            'Raga Nagaswaravali': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A'],
                'page': 114
            },
            'Mela Nasikabhusani': {
                'category': 'European Scales',
                'interval': ['3', '1', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Hungarian Major',
                'page': 202
            },
            'Yu 2': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Raga Matha Kokila': {
                'category': 'Indian Scales',
                'interval': ['2', '5', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'G', 'A', 'Bb'],
                'page': 340
            },
            'Raga Megh': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Raga Brindabani',
                'page': 285
            },
            'Niaventi Minor': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '3', '1'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Gypsy Minor',
                'page': 198
            },
            'Prometheus Liszt': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '3', '1', '3', '1', '3'],
                'scale': ['C', 'Db', 'E', 'F', 'G#', 'A'],
                'primary scale': 'Inverted Augmented',
                'page': 32
            },
            'Dorian b5': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '1', '3', '1', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Blues Heptatonic',
                'page': 53
            },
            'Double Harmonic': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'page': 171
            },
            'Lydian #6': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '1', '3', '1', '1'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A#', 'B'],
                'page': 149
            },
            'Mela Jalarnava': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'Ab', 'Bb'],
                'page': 256
            },
            'Ionian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '4', '1'],
                'scale': ['C', 'E', 'F', 'G', 'B'],
                'page': 86
            },
            'Raga Devarashtra': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Mela Dhatuvardhani',
                'page': 250
            },
            'Raga Gaurikriya': {
                'category': 'Indian Scales',
                'interval': ['3', '3', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F#', 'G', 'A#', 'B'],
                'page': 303
            },
            'Ousak': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Raga Pancama': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'A', 'B'],
                'primary scale': 'Raga Hansanandi',
                'page': 309
            },
            'Raga Khamach Ascending': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A', 'A#', 'B'],
                'page': 322
            },
            'Raga Ahir Bhairav': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Harmonic Minor Inverse',
                'page': 170
            },
            'Raga Ganasamavarali': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Mela Ganamurti',
                'page': 252
            },
            'Raga Savitri': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Raga Tilang',
                'page': 387
            },
            'Raga Jaganmohanam': {
                'category': 'Indian Scales',
                'interval': ['2', '4', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F#', 'G', 'Ab', 'Bb'],
                'page': 313
            },
            'Sabach Maj7': {
                'category': 'European Scales',
                'interval': ['2', '1', '1', '3', '1', '3', '1'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'D#', 'E', 'G', 'Ab', 'B'],
                'page': 221
            },
            'Raga Bhairav That': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Gunkali': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'In',
                'page': 95
            },
            'Man Gong': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '3', '2', '2'],
                'scale': ['C', 'Eb', 'F', 'Ab', 'Bb'],
                'page': 78
            },
            'Mela Jhalavarli': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'Ab', 'B'],
                'page': 257
            },
            'Raga Kirvani': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Raga Neroshta': {
                'category': 'Indian Scales',
                'interval': ['3', '3', '5', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'A', 'B'],
                'page': 351
            },
            'Mela Natakapriya': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b2',
                'page': 17
            },
            'Raga Gopriya': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '2', '2', '2', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Whole-Tone',
                'page': 30
            },
            'Raga Sorati': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'A#', 'B'],
                'page': 382
            },
            'Minor Pentatonic 7 b5': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '1', '4', '2'],
                'scale': ['C', 'Bb', 'F', 'Gb', 'Bb'],
                'page': 85
            },
            'Ian Iwato': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Sho #2': {
                'category': 'Asian Scales',
                'interval': ['1', '2', '1', '2', '4', '2'],
                'origin': 'Japan',
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'Bb'],
                'page': 243
            },
            'Anhemitonic Hexatonic': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '2', '2', '2', '2', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Whole-Tone',
                'page': 30
            },
            'Javanese': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '2', '1', '2'],
                'origin': 'Java',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b2',
                'page': 17
            },
            'Raga Purvikalyani': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Marwa Thaat',
                'page': 339
            },
            'Blues Enneatonic': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'page': 56
            },
            'Raga Kanara': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Maqam Shahnaz Kurdi': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Neapolitan Minor',
                'page': 213
            },
            'Raga Nayaki Kanada': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Pien Chih': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '1', '2', '2', '2'],
                'origin': 'China',
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Locrian',
                'page': 15
            },
            'Raga Purvaholica': {
                'category': 'Indian Scales',
                'interval': ['5', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'F', 'G', 'A', 'B'],
                'primary scale': 'Raga Puruhutika',
                'page': 357
            },
            'Raga Jayamanohari': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'A', 'Bb'],
                'primary scale': 'Raga Shreeranjani',
                'page': 376
            },
            'Raga Rasavali': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'A', 'Bb'],
                'page': 363
            },
            'Raga Ahiri Todi': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b2',
                'page': 17
            },
            'Raga Kalagada': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '3', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'G', 'G#', 'A'],
                'page': 316
            },
            'Raga Rudra Pancama': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'A', 'Bb'],
                'page': 366
            },
            'Mela Sulini': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Houzam',
                'page': 201
            },
            'Raga Manohari': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G', 'A', 'Bb'],
                'page': 338
            },
            'Mixolydian Hexatonic 2': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '3', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'G', 'A', 'Bb'],
                'page': 152
            },
            'Raga Bhup': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Buzurg': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '1', '1', '2', '2', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Bhatiyar',
                'page': 283
            },
            'Mela Dhenuka': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Neapolitan Minor',
                'page': 213
            },
            'Raga Bilashkhani Todi': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Melog Selisir': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '4', '1'],
                'scale': ['C', 'E', 'F', 'G', 'B'],
                'primary scale': 'Ionian Pentatonic',
                'page': 86
            },
            'Minyo': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '3', '2', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Eb', 'F', 'Ab', 'Bb'],
                'primary scale': 'Man Gong',
                'page': 78
            },
            'Mela Jhankaradhvani': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A'],
                'page': 258
            },
            'Mela Kharaharapriya': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Kokin-Choshi': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'page': 82
            },
            'Yosen': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '2', '2', '1', '2'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian Hexatonic',
                'page': 151
            },
            'Raga Mohanangi': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '3', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'G', 'A'],
                'page': 343
            },
            'Eskimo Hexatonic': {
                'category': 'Miscellaneous Scales',
                'interval': ['2', '2', '2', '2', '1', '3'],
                'origin': 'Alaska',
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'A'],
                'page': 400
            },
            'Bebop Dominant': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'page': 65
            },
            'Raga Kunbhini': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Mela Pavani',
                'page': 266
            },
            'Hungarian Major': {
                'category': 'European Scales',
                'interval': ['3', '1', '2', '1', '2', '1', '2'],
                'origin': 'Hungary',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A', 'Bb'],
                'page': 202
            },
            'Pelog': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '2', '1', '1', '3', '1'],
                'origin': 'Bali',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'B'],
                'page': 239
            },
            'Raga Zilla': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Bebop Dorian',
                'page': 70
            },
            'Peruvian Minor Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'Peru',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Raga Megharanjani': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '1', '3', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Ab'],
                'primary scale': 'Syrian Pentatonic',
                'page': 123
            },
            'Raga Kalyani': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A'],
                'primary scale': 'Raga Aivarati',
                'page': 280
            },
            'Full Minor All Flats': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '1', '1', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb', 'B'],
                'page': 132
            },
            'Mischung 2': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '2', '1', '3', '1'],
                'origin': 'Germany',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Major',
                'page': 167
            },
            'Major Inverse': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Enigmatic Minor': {
                'category': 'European Scales',
                'interval': ['1', '2', '3', '2', '2', '1', '1'],
                'scale': ['C', 'Db', 'Eb', 'F#', 'G#', 'Bb', 'B'],
                'page': 192
            },
            'Raga Hamsalata': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Pelog',
                'page': 239
            },
            'Lydian Diminished': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'page': 148
            },
            'Raga Ghanta': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Raga Baira': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Raga Adana': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Major Pentatonic b3': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '3', '3', '3'],
                'scale': ['C', 'Db', 'Eb', 'F#', 'A'],
                'page': 101
            },
            'Raga Madhmat Sarang': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'G', 'G', 'Bb'],
                'primary scale': 'Suspended Pentatonic',
                'page': 77
            },
            'Chaio': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '3', '2', '2'],
                'scale': ['C', 'D', 'F', 'G#', 'Bb'],
                'page': 91
            },
            'Bebop Major Hexatonic': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '3', '1', '1', '3'],
                'scale': ['C', 'D', 'E', 'G', 'G#', 'A'],
                'page': 67
            },
            'Raga Bhopali': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Ping': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '2', '1'],
                'origin': 'China',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian',
                'page': 12
            },
            'Raga Nagagandhari': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'B'],
                'page': 347
            },
            'Man Jue': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'China',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Ritusen': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'page': 79
            },
            'Mela Gaurimanohari': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Melodic Minor',
                'page': 16
            },
            'Raga Sowrashtram': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Gypsy Inverse',
                'page': 197
            },
            'Raga Kedaram Descending': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'B', 'G', 'F', 'E', 'D'],
                'page': 321
            },
            'Lydian Augmented Dominant': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '2', '1', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'A', 'Bb'],
                'page': 150
            },
            'Raga Bhinna Shadj': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'A', 'B'],
                'primary scale': 'Raga Vasanta asc',
                'page': 390
            },
            'Zheng': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'China',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Raga Kedar': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Major': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'page': 9
            },
            'Arezzo Major Diatonic Hexachord': {
                'category': 'European Scales',
                'interval': ['2', '2', '1', '2', '2', '3'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'A'],
                'primary scale': 'Scottish Hexatonic',
                'page': 222
            },
            'Harmonic Minor b5': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '1', '2', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'B'],
                'page': 169
            },
            'Raga Suha Kanada': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'B'],
                'primary scale': 'Bebop Harmonic Minor',
                'page': 72
            },
            'Mela Sadvidhmargini': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b9 #11',
                'page': 136
            },
            'Raga Gaula': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Bb'],
                'page': 302
            },
            'Raga Khambhavati': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Genus Secundum': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '2', '1'],
                'scale': ['C', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Raga Hari Nata',
                'page': 311
            },
            'Dorian b2 Maj7': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '2', '3', '2', '1'],
                'scale': ['C', 'Db', 'Eb', 'E', 'Gb', 'A', 'B'],
                'page': 135
            },
            'Maqam Zengule': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Raga Hindolam': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '3', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'Ab', 'Bb'],
                'primary scale': 'Man Gong',
                'page': 78
            },
            'Raga Kashyapi': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '4', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab', 'Bb'],
                'page': 320
            },
            'Honkoshi': {
                'category': 'Asian Scales',
                'interval': ['1', '2', '2', '1', '4', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'Db', 'F', 'Gb', 'Bb'],
                'page': 227
            },
            'Raga Tilang': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Raga Tilang',
                'page': 387
            },
            'Raga Ravikriya': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Mela Raghupriya',
                'page': 268
            },
            'Raga Sohini': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Ab', 'B'],
                'primary scale': 'Raga Lalita',
                'page': 327
            },
            'Raga Hamsadhvani': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '4', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'G', 'B'],
                'page': 308
            },
            'Raga Puriya 2': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'A', 'B'],
                'primary scale': 'Raga Hansanandi',
                'page': 309
            },
            'Hindu': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Melodic Major',
                'page': 20
            },
            'Lydian #2 #6': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '2', '1', '3', '1', '1'],
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A#', 'B'],
                'page': 145
            },
            'Raga Syamalam': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab'],
                'page': 385
            },
            'Prokofiev': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '1', '2', '2', '1', '1'],
                'origin': 'Russia',
                'scale': ['C', 'Db', 'Eb', 'F', 'F#', 'G#', 'A#', 'B'],
                'page': 216
            },
            'Raga Abheri': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Tcherepnin': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '2', '1', '1', '2', '1', '1', '2', '1'],
                'origin': 'Russia',
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'G', 'G#', 'A', 'B'],
                'primary scale': 'Genus Chromaticum',
                'page': 48
            },
            'Octatonic': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '2', '1', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Diminished',
                'page': 33
            },
            'Greek Arkaik': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '1', '1', '6'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F', 'Gb'],
                'page': 123
            },
            'Utility Minor': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '1', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb', 'B'],
                'primary scale': 'Bebop Harmonic Minor',
                'page': 72
            },
            'Locrian Dominant': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '1', '2', '2', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'Ab', 'Bb'],
                'page': 157
            },
            'Raga Chaturangini': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '2', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Lydian #6',
                'page': 149
            },
            'Raga Anandabhairavi': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '1', '1', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb'],
                'primary scale': 'Dorian Aeolian',
                'page': 133
            },
            'Tabahaniotiko': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '2', '1', '3', '1'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Major',
                'page': 167
            },
            'Harmonic Major 2': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '3', '1', '2', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G#', 'A', 'B'],
                'page': 168
            },
            'Melodic Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
                'page': 16
            },
            'Raga Sarasvati': {
                'category': 'Indian Scales',
                'interval': ['2', '4', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F#', 'G', 'A', 'Bb'],
                'page': 372
            },
            'Mohammedan': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Major Augmented': {
                'category': 'Symmetrical Scales',
                'interval': ['3', '1', '3', '1', '3', '1'],
                'scale': ['C', 'D#', 'E', 'G', 'Ab', 'B'],
                'primary scale': 'Augmented',
                'page': 31
            },
            'Olympos Enharmonic': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '2', '1', '4'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'In',
                'page': 95
            },
            'Melodic Minor #4': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '3', '1', '2', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian Diminished',
                'page': 148
            },
            'Blues Dorian Hexatonic': {
                'category': 'Jazz Scales',
                'interval': ['1', '2', '1', '3', '2', '3'],
                'scale': ['C', 'C#', 'D#', 'E', 'G', 'A'],
                'page': 58
            },
            'Algerian Octatonic': {
                'category': 'Miscellaneous Scales',
                'interval': ['2', '1', '2', '1', '1', '1', '3', '1'],
                'origin': 'Tunisia',
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G', 'Ab', 'B'],
                'page': 398
            },
            'Raga Bilaval That': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '1', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Major',
                'page': 9
            },
            'Persian': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '2', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'Ab', 'B'],
                'page': 240
            },
            'Todi b7': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '2', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b9 #11',
                'page': 136
            },
            'Yo': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Makam Lami': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '1', '2', '2', '2'],
                'origin': 'Jewish',
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb'],
                'primary scale': 'Locrian',
                'page': 15
            },
            'Banshikicho': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '3', '2', '1', '2'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'D#', 'E', 'G', 'A', 'Bb'],
                'primary scale': 'Bebop Minor',
                'page': 69
            },
            'Raga Lalita': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Ab', 'B'],
                'page': 327
            },
            'Raga Indupriya': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab'],
                'primary scale': 'Raga Dhavalangam',
                'page': 296
            },
            'Raga Desh': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'B'],
                'primary scale': 'Tcherepnin Major Pent.',
                'page': 106
            },
            'Jiao': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '3', '2', '2'],
                'origin': 'China',
                'scale': ['C', 'Eb', 'F', 'Ab', 'Bb'],
                'primary scale': 'Man Gong',
                'page': 78
            },
            'Maqam Hijaz': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '1', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'G#', 'A#', 'B'],
                'page': 231
            },
            'Mischung 3': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'Germany',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Ionian #2': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '2', '2', '1'],
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'B'],
                'primary scale': 'Houzam',
                'page': 201
            },
            'Raga Ramkali': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '1', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'F#', 'G', 'Ab', 'B'],
                'page': 360
            },
            'Raga Ramamahohari': {
                'category': 'European Scales',
                'interval': ['1', '3', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Romanian Major',
                'page': 219
            },
            'Raga Simharava': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Bb'],
                'primary scale': 'Raga Gopikatilaka',
                'page': 305
            },
            'Harmonic Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'page': 23
            },
            'Raga Desya Todi': {
                'category': 'Modal Scales',
                'interval': ['3', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Hexatonic',
                'page': 137
            },
            'Mela Kosalam': {
                'category': 'Major and Minor Scales',
                'interval': ['3', '1', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian #2',
                'page': 28
            },
            'Ake-Bono': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '1', '4', '1', '4'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'G', 'Ab'],
                'page': 97
            },
            'Raga Deshi 3': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Pygmy': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '1', '4', '3', '2'],
                'scale': ['C', 'D', 'Eb', 'G', 'Bb'],
                'page': 119
            },
            'Raga Jeyasuddhamalavi': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Mela Hatakambari',
                'page': 255
            },
            'Phrygian Dominant': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'page': 27
            },
            'Raga Kalyan That': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Lydian',
                'page': 12
            },
            'Maqam Kurd': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '1', '2', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian',
                'page': 11
            },
            'Raga Bhupalam': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '4', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab'],
                'primary scale': 'Pelog Pentatonic',
                'page': 87
            },
            'Raga Haripriya': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Major',
                'page': 167
            },
            'Harmonic Major Inverse': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Raga Amrtavarshini': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F#', 'G', 'B'],
                'primary scale': 'Hirajoshi',
                'page': 96
            },
            'Raga Audav Tukhari': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '3', '4'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'Ab'],
                'page': 282
            },
            'Raga Jayakauns': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '1', '4', '2'],
                'origin': 'India',
                'scale': ['C', 'Bb', 'F', 'Gb', 'Bb'],
                'primary scale': 'Minor Pentatonic 7 b5',
                'page': 85
            },
            'Raga Salagavarali': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '4', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'G', 'A', 'Bb'],
                'page': 368
            },
            'Raga Chinthamani': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '1', '1', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'G#', 'A', 'Bb'],
                'page': 293
            },
            'Raga Ahira Lalita': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '3', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Oriental',
                'page': 237
            },
            'Raga Samudhra Priya': {
                'category': 'Indian Scales',
                'interval': ['3', '3', '1', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F#', 'G', 'Bb'],
                'page': 369
            },
            'Raga Vijayasri': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'B'],
                'page': 393
            },
            'Istrian': {
                'category': 'European Scales',
                'interval': ['1', '2', '1', '2', '1', '5'],
                'origin': 'Croatia',
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'G'],
                'page': 205
            },
            'Ionian Augmented b9': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '3', '1', '2', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'G#', 'A', 'B'],
                'page': 128
            },
            'Messiaen 5th Mode Inverse': {
                'category': 'Symmetrical Scales',
                'interval': ['4', '1', '1', '4', '1', '1'],
                'scale': ['C', 'E', 'F', 'Gb', 'Bb', 'B'],
                'page': 43
            },
            'Byzantine': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Gorakh': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian Hexatonic',
                'page': 151
            },
            'Tunisian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '3', '1', '2', '1', '2'],
                'origin': 'Tunisia',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Romanian Minor',
                'page': 26
            },
            'Se': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'SAeolian',
                'page': 14
            },
            'Raga Jogiya': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Messiaen 4th Mode Inverse': {
                'category': 'Symmetrical Scales',
                'interval': ['3', '1', '1', '1', '3', '1', '1', '1'],
                'scale': ['C', 'D#', 'E', 'F', 'Gb', 'A', 'Bb', 'B'],
                'page': 41
            },
            'Neveseri': {
                'category': 'European Scales',
                'interval': ['1', '2', '3', '1', '1', '2', '1', '1'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'Bb', 'B'],
                'page': 215
            },
            'Hitzazkiar': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Jaunpuri': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Raga Gitapriya': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Pelog',
                'page': 239
            },
            'Mela Pavani': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'A', 'B'],
                'page': 266
            },
            'Zokuso Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '1', '4', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'Gb', 'Bb'],
                'primary scale': 'Iwato',
                'page': 98
            },
            'Prometheus Neapolitan': {
                'category': 'European Scales',
                'interval': ['1', '3', '2', '3', '1', '2'],
                'origin': 'Italy',
                'scale': ['C', 'Db', 'E', 'Gb', 'A', 'Bb'],
                'page': 218
            },
            'Chromatic Diatonic Dorian': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '1', '2', '2', '1', '1', '1', '2'],
                'scale': ['C', 'C#', 'D', 'Eb', 'F', 'G', 'G#', 'A', 'Bb'],
                'page': 174
            },
            'Blues Leading Tone': {
                'category': 'Jazz Scales',
                'interval': ['3', '2', '1', '1', '3', '1', '1'],
                'scale': ['C', 'Eb', 'F', 'F#', 'G', 'A#', 'B'],
                'page': 62
            },
            'Raga Vijayavasanta': {
                'category': 'Indian Scales',
                'interval': ['4', '2', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F#', 'G', 'A#', 'B'],
                'page': 394
            },
            'Raga Sarasanana': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'Ab', 'B'],
                'page': 371
            },
            'Soft Ascend': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '3', '2'],
                'origin': 'Japan',
                'scale': ['C', 'Db', 'F', 'G', 'Bb'],
                'primary scale': 'Kokin-Choshi',
                'page': 82
            },
            'Lydian': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '2', '1'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'B'],
                'page': 12
            },
            'Raga Vivardhini': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Bb'],
                'primary scale': 'Raga Siva Kambhoji',
                'page': 381
            },
            'Raga Patdip': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Melodic Minor',
                'page': 16
            },
            'Belinese': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '2', '4', '1', '4'],
                'origin': 'Bali',
                'scale': ['C', 'Db', 'Eb', 'G', 'Ab'],
                'primary scale': 'Pelog Pentatonic',
                'page': 87
            },
            'Egyptian': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '3', '2'],
                'origin': 'Egypt',
                'scale': ['C', 'D', 'G', 'GBb'],
                'primary scale': 'Suspended Pentatonic',
                'page': 77
            },
            'Chad Gadyo': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '2', '2', '5'],
                'origin': 'Jewish',
                'scale': ['C', 'D', 'Eb', 'F', 'G'],
                'primary scale': 'Nando-Kyemyonjo',
                'page': 234
            },
            'Syrian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '1', '3', '4'],
                'origin': 'Syria',
                'scale': ['C', 'Db', 'E', 'F', 'Ab'],
                'page': 123
            },
            'Altered': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '1', '2', '2', '2', '2'],
                'scale': ['C', 'Eb', 'Eb', 'E', 'F#', 'G#', 'Bb'],
                'page': 22
            },
            'Hybrid Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '2', '3'],
                'scale': ['C', 'Eb', 'F', 'G', 'A'],
                'primary scale': 'Kyemyonjo',
                'page': 93
            },
            'Mixolydian Dorian': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '1', '2', '2', '1', '2'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Bebop Dorian',
                'page': 70
            },
            'Raga Bihag': {
                'category': 'Asian Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Ichikotsucho',
                'page': 228
            },
            'Raga Barbara': {
                'category': 'European Scales',
                'interval': ['2', '2', '2', '3', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'Gb', 'A', 'Bb'],
                'primary scale': 'Prometheus',
                'page': 217
            },
            'Dorico Flamenco': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Spain',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Segiah': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Major',
                'page': 167
            },
            'Mela Dhatuvardhani': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F#', 'G', 'Ab', 'B'],
                'page': 250
            },
            'Lai Po Sai': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'Laos',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Raga Chaya Todi': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '2', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'Gb', 'Ab'],
                'page': 292
            },
            'Enigmatic Mixed': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '1', '2', '2', '1', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'F#', 'G#', 'A#', 'B'],
                'page': 193
            },
            'Mixolydian b5': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '1', '3', '1', '2'],
                'scale': ['C', 'D', 'E', 'F', 'Gb', 'A', 'Bb'],
                'page': 152
            },
            'Mela Ratnangi': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'Ab', 'Bb'],
                'page': 269
            },
            'Raga Rageshwari': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'A', 'Bb'],
                'primary scale': 'Raga Nattaikurinji',
                'page': 349
            },
            'Mela Vacaspati': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Lydian Dominant',
                'page': 19
            },
            'Raga Simmendramadhyamam': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Gypsy',
                'page': 195
            },
            'Raga Zilaf': {
                'category': 'Indian Scales',
                'interval': ['4', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Ab'],
                'page': 397
            },
            'Alhijaz': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'origin': 'Arabia',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Raga Bhogachayanata': {
                'category': 'Jazz Scales',
                'interval': ['3', '1', '1', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': "Rock 'n Roll",
                'page': 64
            },
            'Aeolian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '1', '4', '1', '4'],
                'scale': ['C', 'D', 'Eb', 'G', 'Ab'],
                'primary scale': 'Ake-Bono',
                'page': 97
            },
            'Raga Paraj': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Lydian Dominant': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'page': 19
            },
            'Blues Modified': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '1', '1', '3', '2'],
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G', 'Bb'],
                'page': 61
            },
            'Tsinganikos': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '3', '1', '2'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Oriental',
                'page': 237
            },
            'Raga Budhamanohari': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '5'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G'],
                'page': 287
            },
            'Dominant Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '3', '2'],
                'scale': ['C', 'D', 'E', 'G', 'Bb'],
                'page': 90
            },
            'Gypsy': {
                'category': 'European Scales',
                'interval': ['2', '1', '3', '1', '1', '2', '2'],
                'origin': 'Hungary',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'page': 195
            },
            'Hijaz Major': {
                'category': 'European Scales',
                'interval': ['1', '4', '1', '2', '1', '1', '2'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'F', 'F#', 'G#', 'A', 'Bb'],
                'page': 199
            },
            'Hexatonic': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '2', '2', '2', '2', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'Bb'],
                'primary scale': 'Whole-Tone',
                'page': 30
            },
            'Raga Hamsadhvani 2': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'G', 'B'],
                'page': 116
            },
            'Jazz Minor Inverse': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '2', '2', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian b2',
                'page': 17
            },
            'Raga Kokila': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Yu': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'China',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Jog': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Bb'],
                'primary scale': 'Mixolydian Pentatonic',
                'page': 104
            },
            'Lydian Augmented': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'A', 'B'],
                'page': 18
            },
            'Raga Marva': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'A', 'B'],
                'primary scale': 'Raga Hansanandi',
                'page': 309
            },
            'Raga Kaushiranjani': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G#', 'B'],
                'primary scale': 'Raga Ghantana',
                'page': 304
            },
            'Hijazskiar': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'Greece',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Udhayaravi': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Jazz Minor #5': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '3', '1', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G#', 'A', 'B'],
                'page': 131
            },
            'Raga Balahamsa': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Bebop Major Heptatonic': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '1', '1', '3'],
                'scale': ['C', 'D', 'E', 'F', 'G', 'G#', 'A'],
                'page': 68
            },
            'Enigmatic Descending': {
                'category': 'European Scales',
                'interval': ['1', '3', '1', '3', '2', '1', '1'],
                'scale': ['C', 'B', 'Bb', 'Gb', 'F', 'E', 'Db'],
                'page': 191
            },
            'Kiourdi': {
                'category': 'European Scales',
                'interval': ['2', '1', '2', '1', '1', '1', '1', '1', '2'],
                'origin': 'Greece',
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G', 'G#', 'A', 'Bb'],
                'page': 207
            },
            'Raga Dipak': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '1', '1', '5'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G'],
                'page': 298
            },
            'Raga Valaji': {
                'category': 'Indian Scales',
                'interval': ['4', '3', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'G', 'A', 'Bb'],
                'page': 389
            },
            'Raga Andhali': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'Bb'],
                'primary scale': 'Raga Siva Kambhoji',
                'page': 381
            },
            'Blues': {
                'category': 'Jazz Scales',
                'interval': ['3', '2', '1', '1', '3', '2'],
                'scale': ['C', 'Eb', 'F', 'F#', 'G', 'Bb'],
                'page': 52
            },
            'Genus Tertium': {
                'category': 'Symmetrical Scales',
                'interval': ['3', '1', '3', '1', '3', '1'],
                'scale': ['C', 'D#', 'E', 'G', 'Ab', 'B'],
                'primary scale': 'Augmented',
                'page': 31
            },
            'Oshikicho': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Dorian',
                'page': 10
            },
            'Raga Kokilaravam': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Neapolitan Major',
                'page': 210
            },
            'Raga Kalyani Keseri': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '2', '1', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A'],
                'primary scale': 'Raga Aivarati',
                'page': 280
            },
            'Mela Ragavardhani': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Ab', 'Bb'],
                'page': 267
            },
            'Major Phrygian': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Dorian Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '1', '4', '2', '3'],
                'scale': ['C', 'D', 'Eb', 'G', 'A'],
                'page': 81
            },
            'Mela Gangeyabhusani': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Sengiach',
                'page': 223
            },
            'Raga Lalita Bhairav': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '1', '3', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'Ab', 'Bb'],
                'page': 328
            },
            'Raga Madhuranjani': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Raga Nattai asc',
                'page': 348
            },
            'Raga Pilu That': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Chromatic Hypolydian Inverse': {
                'category': 'Asian Scales',
                'interval': ['1', '3', '1', '1', '2', '3', '1'],
                'scale': ['C', 'Db', 'E', 'F', 'Gb', 'Ab', 'B'],
                'primary scale': 'Persian',
                'page': 240
            },
            'Raga Marwa Thaat': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'page': 339
            },
            'Raga Kalamurti': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Bhavapriya',
                'page': 247
            },
            'Maqam Shawq Afza': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '1', '1', '1', '1', '1', '1', '2', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B'],
                'page': 232
            },
            'Raga Alhaiya Bilaval': {
                'category': 'Jazz Scales',
                'interval': ['2', '2', '1', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Bebop',
                'page': 65
            },
            'Raga Madhuri': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'A', 'A#', 'B'],
                'primary scale': 'Raga Khamach asc',
                'page': 322
            },
            'Ascending Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'B'],
                'primary scale': 'Melodic Minor',
                'page': 16
            },
            'Raga Hamsanandi': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '3', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'A', 'B'],
                'page': 309
            },
            'Raga Saugandhini': {
                'category': 'Indian Scales',
                'interval': ['1', '5', '1', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F#', 'G', 'Ab'],
                'page': 374
            },
            'Augmented Pentatonic 2': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '2', '2', '3', '1'],
                'scale': ['C', 'E', 'F#', 'G#', 'B'],
                'page': 112
            },
            'Fraigish': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '3', '1', '2', '1', '2', '2'],
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Phrygian Dominant',
                'page': 27
            },
            'Locrian #6': {
                'category': 'Major and Minor Scales',
                'interval': ['1', '2', '2', '1', '3', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'page': 24
            },
            'Gong': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '2', '3', '2', '3'],
                'origin': 'China',
                'scale': ['C', 'D', 'E', 'G', 'A'],
                'primary scale': 'Major Pentatonic',
                'page': 76
            },
            'Lydian #2 Hexatonic': {
                'category': 'Modal Scales',
                'interval': ['3', '1', '3', '2', '2', '1'],
                'scale': ['C', 'D#', 'E', 'G', 'A', 'B'],
                'page': 144
            },
            'Taishikicho': {
                'category': 'Modal Scales',
                'interval': ['2', '2', '1', '1', '1', '2', '1', '1', '1'],
                'origin': 'Japan',
                'scale': ['C', 'D', 'E', 'F', 'F#', 'G', 'A', 'Bb', 'B'],
                'primary scale': 'Lydian Mixolydian',
                'page': 147
            },
            'Hungarian Major Inverse': {
                'category': 'European Scales',
                'interval': ['2', '1', '2', '1', '2', '1', '3'],
                'origin': 'Hungary',
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G#', 'A'],
                'page': 203
            },
            'Raga Jivantika': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'A', 'B'],
                'page': 314
            },
            'Peruvian Minor': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '2', '2'],
                'origin': 'Peru',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Aeolian',
                'page': 14
            },
            'Mela Naganandini': {
                'category': 'Indian Scales',
                'interval': ['2', '2', '1', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A#', 'B'],
                'page': 262
            },
            'Mela Mayamalavagowla': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Ghandarva': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '4', '1', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F#', 'G', 'A#', 'B'],
                'primary scale': 'Mela Raghupriya',
                'page': 268
            },
            'Raga Savethri': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Bb'],
                'primary scale': 'Mixolydian Pentatonic',
                'page': 104
            },
            'Raga Manirangu': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '2', '2', '3', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Hexatonic',
                'page': 129
            },
            'Romanian Bacovia': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '3', '3', '1'],
                'origin': 'Romania',
                'scale': ['C', 'E', 'F', 'G#', 'B'],
                'page': 122
            },
            'Raga Ramamanohari 2': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Raga Paras asc',
                'page': 355
            },
            'Raga Cudamani': {
                'category': 'Indian Scales',
                'interval': ['3', '1', '1', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'Ab', 'Bb'],
                'primary scale': 'Mela Ragavardhani',
                'page': 267
            },
            'Raga Priyadharshini': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '3', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G#', 'B'],
                'page': 356
            },
            'Major Pentatonic b2': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '3', '3', '2', '3'],
                'scale': ['C', 'Eb', 'E', 'G', 'A'],
                'page': 99
            },
            'Raga Vasanta Ascending': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'A', 'B'],
                'page': 390
            },
            'Mela Kamavardhani': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Maqam Nahawand Murassah': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '2', '1', '3', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'D', 'Eb', 'F', 'Gb', 'A', 'Bb'],
                'primary scale': 'Blues Heptatonic',
                'page': 53
            },
            'Raga Amarasenapriya': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '3', '1', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'B'],
                'page': 281
            },
            'Gu Xian': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '2', '2', '3', '2'],
                'origin': 'China',
                'scale': ['C', 'Eb', 'F', 'G', 'Bb'],
                'primary scale': 'Minor Pentatonic',
                'page': 80
            },
            'Diminished Half-tone': {
                'category': 'Symmetrical Scales',
                'interval': ['1', '2', '1', '2', '1', '2', '1', '2'],
                'scale': ['C', 'C#', 'D#', 'E', 'F#', 'G', 'A', 'Bb'],
                'page': 34
            },
            'Raga Bhusavati': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '2', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F#', 'G', 'A', 'Bb'],
                'primary scale': 'Lydian Dominant',
                'page': 19
            },
            'Youlan': {
                'category': 'Asian Scales',
                'interval': ['1', '1', '2', '1', '1', '1', '2', '1', '2'],
                'origin': 'China',
                'scale': ['C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'A', 'Bb'],
                'page': 246
            },
            'Whole-Tone': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '2', '2', '2', '2', '2'],
                'scale': ['C', 'D', 'E', 'F#', 'G#', 'Bb'],
                'page': 30
            },
            'Phrygian b4 Maj7': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '3', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'page': 140
            },
            'Raga Putrika': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '6', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'G#', 'A'],
                'page': 358
            },
            'Huzam': {
                'category': 'European Scales',
                'interval': ['3', '1', '1', '2', '2', '2', '1'],
                'origin': 'Greece',
                'scale': ['C', 'D#', 'E', 'F', 'G', 'A', 'B'],
                'page': 201
            },
            'Raga Kambhoji': {
                'category': 'European Scales',
                'interval': ['2', '2', '1', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A'],
                'primary scale': 'Scottish Hexatonic',
                'page': 222
            },
            'Raga Kamalamanohari 2': {
                'category': 'Indian Scales',
                'interval': ['4', '1', '2', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F', 'G', 'Ab', 'Bb'],
                'page': 319
            },
            'Sultani Yakah': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Altered Pentatonic': {
                'category': 'Pentatonic Scales',
                'interval': ['1', '4', '2', '2', '3'],
                'scale': ['C', 'Db', 'F', 'G', 'A'],
                'page': 107
            },
            'Raga Khamaji Durga': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '1', '4', '1', '2'],
                'scale': ['C', 'E', 'F', 'A', 'Bb'],
                'page': 89
            },
            'Maqam Shahnaz': {
                'category': 'European Scales',
                'interval': ['1', '2', '2', '2', '1', '3', '1'],
                'origin': 'Iraq',
                'scale': ['C', 'Db', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Neapolitan Minor',
                'page': 213
            },
            'Raga Andolika': {
                'category': 'Modal Scales',
                'interval': ['2', '3', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian Hexatonic',
                'page': 151
            },
            'Maqam Bayat-e-Esfahan': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '1', '3', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Harmonic Minor',
                'page': 23
            },
            'Raga Varini': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '4', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'G', 'Ab', 'Bb'],
                'primary scale': 'Raga Shailaja',
                'page': 118
            },
            'Raga Brindabani': {
                'category': 'Indian Scales',
                'interval': ['2', '3', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'G', 'A#', 'B'],
                'page': 285
            },
            'Raga Udayaravicandrika': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '2', '4', '1'],
                'origin': 'India',
                'scale': ['C', 'D#', 'F', 'G', 'B'],
                'primary scale': 'Raga Nattai desc',
                'page': 348
            },
            'Raga Mamata': {
                'category': 'Pentatonic Scales',
                'interval': ['4', '3', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'E', 'G', 'A', 'B'],
                'page': 120
            },
            'Raga Vutari': {
                'category': 'Indian Scales',
                'interval': ['4', '2', '1', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'E', 'F#', 'G', 'A', 'Bb'],
                'page': 396
            },
            'Zhi': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '2', '2', '3'],
                'origin': 'China',
                'scale': ['C', 'D', 'F', 'G', 'A'],
                'primary scale': 'Ritusen',
                'page': 79
            },
            'Raga Guhamanohari': {
                'category': 'Pentatonic Scales',
                'interval': ['2', '3', '4', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'F', 'A', 'Bb'],
                'primary scale': 'Pyeong Jo',
                'page': 117
            },
            'Major Minor Mixed': {
                'category': 'Modal Scales',
                'interval': ['2', '1', '1', '1', '2', '1', '1', '1', '1', '1'],
                'scale': ['C', 'D', 'D#', 'E', 'F', 'G', 'G#', 'A', 'A#', 'B'],
                'page': 187
            },
            'Chromatic Lydian Inverse': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '3', '1', '1', '3', '1'],
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'Ab', 'B'],
                'page': 178
            },
            'Messiaen 2nd Mode Inverse': {
                'category': 'Symmetrical Scales',
                'interval': ['2', '1', '2', '1', '2', '1', '2', '1'],
                'scale': ['C', 'D', 'Eb', 'F', 'F#', 'G#', 'A', 'B'],
                'primary scale': 'Diminished',
                'page': 33
            },
            'Raga Puriya Kalyan': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '1', '2', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'A', 'B'],
                'primary scale': 'Raga Marwa Thaat',
                'page': 339
            },
            'Chromatic Hypophrygian Inverse': {
                'category': 'Modal Scales',
                'interval': ['1', '1', '3', '1', '1', '2', '3'],
                'scale': ['C', 'C#', 'D', 'F', 'F#', 'G', 'A'],
                'page': 185
            },
            "Maqam Shadd'araban": {
                'category': 'Asian Scales',
                'interval': ['1', '2', '1', '1', '1', '3', '1', '2'],
                'origin': 'Iraq',
                'scale': ['C', 'C#', 'D#', 'E', 'F', 'Gb', 'A', 'Bb'],
                'page': 230
            },
            'Raga Shailaja': {
                'category': 'Pentatonic Scales',
                'interval': ['3', '4', '1', '2', '2'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'G', 'Ab', 'Bb'],
                'page': 118
            },
            'Raga Hejjajji': {
                'category': 'Indian Scales',
                'interval': ['1', '3', '2', '2', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G#', 'A'],
                'page': 312
            },
            'Raga Geyahejjajji': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'primary scale': 'Raga Malahari asc',
                'page': 333
            },
            'Dorian b2 b4': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '3', '2', '1', '2'],
                'scale': ['C', 'Db', 'Eb', 'E', 'G', 'A', 'Bb'],
                'page': 134
            },
            'Raga Abhogi': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '4', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'A'],
                'page': 279
            },
            'Raga Harini': {
                'category': 'Major and Minor Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '2'],
                'origin': 'India',
                'scale': ['C', 'D', 'E', 'F', 'G', 'A', 'Bb'],
                'primary scale': 'Mixolydian',
                'page': 13
            },
            'Raga Malahari Ascending': {
                'category': 'Indian Scales',
                'interval': ['1', '4', '2', '1', '4'],
                'origin': 'India',
                'scale': ['C', 'Db', 'F', 'G', 'Ab'],
                'page': 333
            },
            'Superlocrian Maj7': {
                'category': 'Modal Scales',
                'interval': ['1', '2', '1', '2', '2', '3', '1'],
                'scale': ['C', 'Db', 'Eb', 'E', 'Gb', 'Ab', 'B'],
                'page': 163
            },
            'Raga Chandrakauns Modern': {
                'category': 'Indian Scales',
                'interval': ['3', '2', '4', '2', '1'],
                'origin': 'India',
                'scale': ['C', 'Eb', 'F', 'A', 'B'],
                'page': 291
            },
            'Bebop Minor': {
                'category': 'Jazz Scales',
                'interval': ['2', '1', '1', '3', '2', '1', '2'],
                'scale': ['C', 'D', 'D#', 'E', 'G', 'A', 'Bb'],
                'page': 69
            },
            'Raga Kasiramakryia': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '2', '1', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'Db', 'E', 'F#', 'G', 'Ab', 'B'],
                'primary scale': 'Chromatic Hypolydian',
                'page': 184
            },
            'Raga Suddha Bangala': {
                'category': 'Asian Scales',
                'interval': ['2', '1', '2', '2', '2', '3'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A'],
                'primary scale': 'Sho',
                'page': 242
            },
            'Raga Sindhura': {
                'category': 'Indian Scales',
                'interval': ['2', '1', '2', '2', '2', '1', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'D', 'Eb', 'F', 'G', 'A', 'A#', 'B'],
                'primary scale': 'Raga Miam Ki Malhar',
                'page': 342
            },
            'Raga Tanukirti': {
                'category': 'Indian Scales',
                'interval': ['1', '1', '3', '2', '3', '1', '1'],
                'origin': 'India',
                'scale': ['C', 'C#', 'D', 'F', 'G', 'A#', 'B'],
                'primary scale': 'Mela Tenarupi',
                'page': 274
            },
            'Arabic': {
                'category': 'Modal Scales',
                'interval': ['1', '3', '1', '2', '1', '3', '1'],
                'origin': 'Arabia',
                'scale': ['C', 'Db', 'E', 'F', 'G', 'Ab', 'B'],
                'primary scale': 'Double Harmonic',
                'page': 171
            },
            'Raga Devaranjani': {
                'category': 'Indian Scales',
                'interval': ['5', '2', '1', '3', '1'],
                'origin': 'India',
                'scale': ['C', 'F', 'G', 'Ab', 'B'],
                'page': 295
            },
            'Mela Gavambodhi': {
                'category': 'Indian Scales',
                'interval': ['1', '2', '3', '1', '1', '1', '3'],
                'origin': 'India',
                'scale': ['C', 'Db', 'Eb', 'F#', 'G', 'G#', 'A'],
                'page': 253
            }
        }

        self.nkeys = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#',
                      'Fb', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A',
                      'A#', 'Bb', 'B', 'B#', 'Cb']

        self.category = ['Major and Minor Scales', 'Symmetrical Scales',
                         'Jazz Scales', 'Pentatonic Scales', 'Modal Scales',
                         'European Scales', 'Asian Scales', 'Indian Scales',
                         'Miscellaneous Scales'
                         ]

        self.interval_names = {
            'P1': [0, 'Perfect unison', [None]],
            'd2': [0, 'Diminished second', [None]],
            'm2': [1, 'Minor second', ['semitone', 'half tone', 'half step']],
            'A1': [1, 'Augmented unison', ['semitone', 'half tone', 'half step']],
            'S': [1, 'Semitone', ['half tone', 'half step']],
            'M2': [2, 'Major second', ['Tone']],
            'd3': [2, 'Diminished third', ['Tone']],
            'T': [2, 'Tone', ['Whole', 'Diminished third', 'Major second']],
            'W': [2, 'Whole', ['Tone', 'Diminished third', 'Major second']],
            'm3': [3, 'Minor third', [None]],
            'A2': [3, 'Augmented second', [None]],
            'M3': [4, 'Major third', [None]],
            'd4': [4, 'Diminshed fourth', [None]],
            'P4': [5, 'Perfect fourth', [None]],
            'A3': [5, 'Augmented third', [None]],
            'd5': [6, 'Diminished fifth', ['Tritone']],
            'A4': [6, 'Augmented fourth', ['Tritone']],
            'TT': [6, 'Tritone', ['Augmented fourth', 'Diminished fifth']],
            'P5': [7, 'Perfect fifth', [None]],
            'd6': [7, 'Diminished sixth', [None]],
            'm6': [8, 'Minor sixth', [None]],
            'A5': [8, 'Augmented fifth', [None]],
            'M6': [9, 'Major sixth', [None]],
            'd7': [9, 'Diminished seventh', [None]],
            'm7': [10, 'Minor seventh', [None]],
            'A6': [10, 'Augmented sixth', [None]],
            'M7': [11, 'Major seventh', [None]],
            'd8': [11, 'Diminished octave', [None]],
            'P8': [12, 'Perfect octave', [None]],
            'A7': [12, 'Augmented seventh', [None]],
            'd9': [12, 'Diminished ninth', [None]],
            'm9': [13, 'Minor ninth', [None]],
            'A8': [13, 'Augmented eighth', [None]],
            'M9': [14, 'Major ninth', [None]],
            'd10': [14, 'Diminished tenth', [None]],
            'm10': [15, 'Minor tenth', [None]],
            'A9': [15, 'Augmented ninth', [None]],
            'M10': [16, 'Major tenth', [None]],
            'd11': [16, 'Diminished eleventh', [None]],
            'P11': [17, 'Perfect eleventh', [None]],
            'A10': [17, 'Augmented tenth', [None]],
            'd12': [18, 'Diminished twelfth', [None]],
            'A11': [18, 'Augmented eleventh', [None]],
            'P12': [19, 'Perfect twelfth', [None]],
            'd13': [19, 'Diminished thirteenth', [None]],
            'm13': [20, 'Minor thirteenth', [None]],
            'A12': [20, 'Augmented twelfth', [None]],
            'M13': [21, 'Major thirteenth', [None]],
            'd14': [21, 'Diminished fourteenth', [None]],
            'm14': [22, 'Minor fourteenth', [None]],
            'A13': [22, 'Augmented thirteenth', [None]],
            'M14': [23, 'Major fourteenth', [None]],
            'd15': [23, 'Diminished fifteenth', [None]],
            'P15': [24, 'Perfect fifteenth', [None]],
            'A14': [24, 'Augmented fourteenth', [None]],
            'A15': [25, 'Augmented fifteenth', [None]]
        }

        # 'Asian Scales': {
        #     'Honkoshi': 'Honkoshi',
        #     'Ichikotsucho': 'Ichikotsucho',
        #     'Major-Lydian Mixed': 'Ichikotsucho',

        # for chord building
        self.major_scales = {
            'A major': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#', 'A'],
            'Bb major': ['Bb', 'C', 'D', 'Eb', 'F', 'G', 'A', 'Bb'],
            'B major': ['B', 'C#', 'D#', 'E', 'F#', 'G#', 'A#', 'B'],
            'C major': ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C'],
            'Db major': ['Db', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'C', 'Db'],
            'D major': ['D', 'E', 'F#', 'G', 'A', 'B', 'C#', 'D'],
            'Eb major': ['Eb', 'F', 'G', 'Ab', 'Bb', 'C', 'D', 'Eb'],
            'E major': ['E', 'F#', 'G#', 'A', 'B', 'C#', 'D#', 'E'],
            'F major': ['F', 'G', 'A', 'Bb', 'C', 'D', 'E', 'F'],
            'Gb major': ['Gb', 'Ab', 'Bb', 'Cb', 'Db', 'Eb', 'F', 'Gb'],
            'G major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G'],
            'Ab major': ['Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'G', 'Ab'],
            'A# major': 'Bb major',
            'C# major': 'Db major',
            'D# major': 'Eb major',
            'F# major': 'Gb major',
            'G# major': 'Ab major'
        }

        self.chord_formulas = collections.OrderedDict()
        self.chord_formulas['Triad'] = collections.OrderedDict()
        self.chord_formulas['Triad']['Major'] = \
            [['1', '3', '5'], ['Major third', 'Minor third'], 'Maj']
        self.chord_formulas['Triad']['Minor'] = \
            [['1', '2', '5'], ['Minor third', 'Major third'], 'm']
        self.chord_formulas['Triad']['Diminished'] = \
            [['1', '2', '4'], ['Minor third', 'Minor third'], 'dim']
        self.chord_formulas['Triad']['Augmented'] = \
            [['1', '3', '6'], ['Major third', 'Major third'], 'aug']
        self.chord_formulas['Seventh'] = collections.OrderedDict()
        self.chord_formulas['Seventh']['Major'] = \
            self.chord_formulas['Seventh']['Minor'] = \
            self.chord_formulas['Seventh']['Diminished'] = \
            self.chord_formulas['Seventh']['Augmented'] = \
            [['1', '3', '#5', 'b7'], ['Major third', 'Major third',
                                      'Diminished third'], 'aug7']
        self.chord_formulas['Seventh']['Augmented Major'] = \
            [['1', '3', '#5', '7'], ['Major third', 'Major third',
                                     'Minor third'], 'maj7(?5)']
        self.chord_formulas['Seventh']['Half-Diminshed'] = \
            [['1', 'b3', 'b5', 'b7'], ['Minor third', 'Minor third',
                                       'Major third'], '7(?5)',
             ['aka', 'Dominant Seventh Flat Five']]
        self.chord_formulas['Seventh']['Dominant'] = \
            [['1', '3', '5', 'b7'], ['Major third', 'Minor third',
                                     'Minor third'], '7']
        self.chord_formulas['Seventh']['Minor-major'] = \
            [['1', 'b3', '5', '7'], ['Minor third', 'Major third',
                                     'Major third'], 'mM7']
        self.chord_formulas['Ninth'] = collections.OrderedDict()
        self.chord_formulas['Ninth']['Major'] = \
            [['1', '3', '5', '7', '9'], ['Major third', 'Perfect fifth',
                                         'Major seventh', 'Major Ninth'],
             'maj9']
        self.chord_formulas['Ninth']['Minor'] = \
            [['1', 'b3', '5', 'b7', '9'], [], 'm9']
        self.chord_formulas['Ninth']['Dominant'] = \
            [['1', '3', '5', 'b7', '9'], ['Major third', 'Perfect fifth',
                                          'Minor seventh', 'Major ninth'],
             'dim9']
        self.chord_formulas['Ninth']['Dominant Minor'] = \
            [['1', '3', '5', 'b7', '9'], ['Major third', 'Perfect fifth',
                                          'Minor seventh', 'Minor ninth'],
             '7b9']

        self.chromatic_sharps = {
            'C': 'C#', 'C#': 'D', 'D': 'D#', 'D#': 'E', 'E': 'F', 'F': 'F#',
            'F#': 'G', 'G': 'G#', 'G#': 'A', 'A': 'A#', 'A#': 'B', 'B': 'C'
        }

        self.chromatic_flats = {
            'C': 'Db', 'Db': 'D', 'D': 'Eb', 'Eb': 'E', 'E': 'F', 'F': 'Gb',
            'Gb': 'G', 'G': 'Ab', 'Ab': 'A', 'A': 'Bb', 'Bb': 'B', 'B': 'C'
        }
