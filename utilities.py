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
import os
import os.path


class Utility:
    def __init__(self):
        self.data = sd.McData()
        self.categories = {}
        self.get_categories()

    def get_categories(self):
        for scalename in self.data.newscaledata.keys():
            category = self.data.newscaledata[scalename]['category']
            if category not in self.categories:
                self.categories[category] = category

    def get_scales_of_category(self, category):
        scalelist = []
        for scalename in self.data.newscaledata.keys():
            if self.data.newscaledata[scalename]['category'] == category:
                scalelist.append(scalename)
        return scalelist

    def dump_categories(self):
        for category in self.categories.keys():
            print('{}'.format(category))
            scalelist = self.get_scales_of_category(category)
            scalelist.sort()

            for scale in scalelist:
                print('    {}'.format(scale))

    def convert_to_lilypond(self, notes):
        notestr = ''
        for note in notes:
            notestr += '{} '.format(self.data.lilypond_conversion[note])
        return notestr

    def prepare_filename(self, name):
        # xbaseroot = None
        xdirname, xbasename = os.path.split(name)
        sidx = None
        try:
            sidx = xbasename.index('.')
            xsuffix = None
            xbaseroot = None
        except ValueError:
            xsuffix = None
            xbaseroot = xbasename
        if sidx is not None:
            xsuffix = xbasename[sidx:]
            xbaseroot = xbasename[0:sidx]
            xbaseroot = "".join(xbaseroot.split())
            xbasename = xbaseroot + xsuffix
        return xdirname, xbasename, xbaseroot, xsuffix

    def translate_note_to_lilypond(self, snote):
        if '##' in snote:
            z = '{}isis'.format(snote[0].lower())
        elif '#' in snote:
            z = '{}is'.format(snote[0].lower())
        elif 'bb' in snote:
            z = '{}eses'.format(snote[0].lower())
        elif 'b' in snote:
            z = '{}es'.format(snote[0].lower())
        else:
            z = '{}'.format(snote[0].lower())
        return z

    def find_files(self, directory, pattern, fsuffix=None, removesuffix=False):
        print('In find_files')
        files = [f for f in os.listdir(directory) if os.path.isfile(f)]
        flist = []
        for f in files:
            if pattern in f:
                fn = os.path.splitext(f)
                if fsuffix:
                    if fn[1] == fsuffix:
                        if removesuffix:
                            flist.append(fn[0])
                        else:
                            flist.append(f)
                    continue
                if removesuffix:
                    flist.append(fn[0])
                else:
                    flist.append(f)
        return flist

    def is_theoretical(self, scale):
        for item in scale:
            if ('##' in item) or ('bb' in item):
                return True
        return False


if __name__ == '__main__':
    import os

    u = Utility()
    # cdir =  os.getcwd() + '\\' + 'wally Winslow.txt'
    cdir = os.getcwd() + '\\'
    pdirname, pbasename, baseroot, suffix = u.prepare_filename(cdir)
    print('pdirname: {}, pbasename: {}, suffix: {}, baseroot: {}'
          .format(pdirname, pbasename, suffix, baseroot))
    print('{}'.format(u.convert_to_lilypond(['C', 'D#', 'Eb', 'F#', 'G'])))
    u.dump_categories()
