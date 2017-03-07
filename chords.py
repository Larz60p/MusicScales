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
import sdata as sd
import scales


class Chords:
    def __init__(self):
        self.sc = scales.Scales()
        self.data = sd.McData()

    def show_chord_formula_table(self):
        for chtype in self.data.chord_formulas:
            for chname in self.data.chord_formulas[chtype]:
                print('chordtype:{} chordname: {}'.format(chtype, chname))
                for n in range(len(self.data.chord_formulas[chtype][chname])):
                    if n == 0:
                        print('    formula: ', end='')
                    elif n == 1:
                        print('    intervals: ', end='')
                    elif n == 2:
                        print('    chord name: ', end='')
                    elif n == 3:
                        print('    AKA: ', end='')
                    else:
                        print('    ?? - {} '.format(n), end='')
                    print('    {}'.format(self.data.chord_formulas[chtype][chname][n]))
                print()

    def splitformula(self, formula_part):
        # print('interval: {}'.format(formula_part))
        if len(formula_part) == 1:
            accidental = None
            note = int(formula_part)
        else:
            note = int(formula_part[1])
            accidental = formula_part[0]
        note -= 1
        return accidental, note

    def get_chord(self, chname, chtype, ckey):
        chord = []
        pscale = self.sc.get_major_scale(ckey)
        formula = self.data.chord_formulas[chtype][chname][0]

        # print('scale: {}\nformula: {}'.format(pscale, formula))
        for n in range(len(formula)):
            accidental, note = self.splitformula(formula[n])
            if note >= len(pscale):
                note = note - len(pscale) + 1
            noteletter = pscale[note]
            if accidental == 'b':
                noteletter = self.data.note[noteletter]['flatten']
            elif accidental == '#':
                noteletter = self.data.note[noteletter]['sharpen']
            chord.append(noteletter)
        return chord


def main():
    cd = Chords()
    # cd.show_chord_formula_table()

    ckeys = ['C', 'G', 'D', 'A', 'E', 'B', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F']

    # print('ckeys: {}'.format(ckeys))
    for chordtype in cd.data.chord_formulas.keys():
        # print(chordtype)
        for chordname in cd.data.chord_formulas[chordtype].keys():
            # print('    {}'.format(chordname))
            # print('    {}'.format(cd.data.chord_formulas[chordtype][chordname]))
            for ckey in ckeys:
                # print('key: {}'.format(ckey))
                chord = cd.get_chord(chordname, chordtype, ckey)
                print('{} {} chord in key of {} = {}'.format(chordname, chordtype, ckey, chord))


if __name__ == '__main__':
    main()
