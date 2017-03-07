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
import copy
import sdata as sd


class Scales:
    def __init__(self):
        self.data = sd.McData()
        self.octave_sequence = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.octave_sequence_rotated = []
        self.xref = {}

    @staticmethod
    def rotate(l, n):
        return l[n:] + l[:n]

    def rotate_octave_sequence(self, tonic_note):
        self.octave_sequence_rotated = copy.deepcopy(self.octave_sequence)
        x = self.octave_sequence_rotated.index(tonic_note[0])
        if x:
            self.octave_sequence_rotated = self.rotate(self.octave_sequence_rotated, x)

    @staticmethod
    def pairwise(thelist):
        """
            origin: http://code.activestate.com/recipes/409825-look-ahead-one-item-during-iteration/
             yield item i and item i+1 in thelist. e.g.
            (thelist[0], thelist[1]), (thelist[1], thelist[2]), ..., (thelist[-1], None)
        :param thelist:
        :return:
        """
        if not thelist:
            return
        for i in range(len(thelist) - 1):
            yield thelist[i], thelist[i + 1]
        yield thelist[-1], None

    @staticmethod
    def index_in_list(value, thelist, first_only=False):
        """
        Check list for value
        :param value: value to mind
        :param thelist:  Name of list to check
        :param first_only: If true, natch first character only
        :return: returns index of match
        """
        vidx = None
        for anote in thelist:
            if first_only:
                if anote[0] == value:
                    vidx = thelist.index(anote)
                    break
            else:
                if anote == value:
                    vidx = thelist.index(anote)
                    break
        return vidx

    @staticmethod
    def increment_index(rindex, rmax):
        xindex = rindex
        xindex += 1
        if xindex >= rmax:
            xindex = 0
        return xindex

    def check_scale_integrity(self, rscale):
        next_index = 1
        imax = len(self.octave_sequence_rotated)
        rscaleidx = 1
        found = False
        replacement = None

        for anote, nextnote in self.pairwise(rscale):
            if nextnote is None:
                break
            expected_nextnote = self.octave_sequence_rotated[next_index]
            if expected_nextnote not in nextnote:
                noteid = self.data.note[nextnote]['id']
                samenotes = list(self.data.id_xref[noteid])
                for replacement in samenotes:
                    if expected_nextnote in replacement:
                        found = True
                        break
            if found:
                break
            next_index = self.increment_index(next_index, imax)
            rscaleidx += 1

        if found:
            rscale[rscaleidx] = replacement

        return found, rscale

    def get_scale(self, tonic_note, intervals):
        self.rotate_octave_sequence(tonic_note)
        rscale = [tonic_note]
        current_note = tonic_note
        for rival in intervals:
            rinterval = int(rival)
            while rinterval:
                current_note = self.data.note[current_note]['next_note']
                rinterval -= 1
            rscale.append(current_note)
        notdone = True
        while notdone:
            notdone, rscale = self.check_scale_integrity(rscale)
        return rscale

    def get_intervals(self, category, scalename):
        scalename = self.get_scalename(category, scalename)
        intervals = self.data.newscaledata[scalename]['interval']
        return intervals

    def get_scalename(self, category, aliasname):
        return self.data.xref[category][aliasname]

    def get_intervals_from_aliasname(self, aname):
        for category in self.data.xref.keys():
            for aliasname in self.data.xref[category].keys():
                if aliasname == aname:
                    scalename = self.data.xref[category][aliasname]
                    return self.get_intervals(category, scalename)
        return None

    def get_scale_from_scalename(self, scalename, key):
        if scalename not in self.data.newscaledata:
            return None
        sdata = self.data.newscaledata[scalename]
        intervals = sdata['interval']
        scale = self.get_scale(key, intervals)
        return scale

    def get_major_scale(self, ckey):
        xkey = '{} major'.format(ckey)
        if xkey in self.data.major_scales:
            if 'str' in str(type(self.data.major_scales[xkey])):
                xkey = self.data.major_scales[xkey]
        return self.data.major_scales[xkey]


def main():
    sd = Scales()
    scale = sd.get_scale_from_scalename('Raga Bihag', 'F#')
    print('scale for Raga Bihaq {}'.format(scale))
    # Test get_major_scale
    scale = sd.get_major_scale('Db')
    print('Db major: {}'.format(scale))
    scale = sd.get_major_scale('A#')
    print('Bb major: {}'.format(scale))

if __name__ == '__main__':
    main()
