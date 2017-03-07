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
import chords
import sdata as sd
import scales
import utilities as ut
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tm
import tkinter.filedialog as tf
import os
import os.path
from PIL import ImageTk, Image
from subprocess import STDOUT, check_output as qx
import time
import shutil
import pdb


class McNote:
    def __init__(self, parent):
        self.parent = parent
        self.sc = scales.Scales()
        self.chord = chords.Chords()
        # self.cd = sd
        self.basedir = os.getcwd() + '\\'
        self.lilydir = '..\\lilypond\\'

        # print('basedir: {}'.format(self.basedir))
        self.version = '1.0.0'
        self.parent.title('McNote by Larz60+ - Scales and Chords of the world - Version 1.0.0')
        self.mainframe = ttk.Frame(self.parent)

        self.png_basename = 'ScaleForProg'
        self.data = sd.McData()
        self.util = ut.Utility()
        # self.fwidth = 800

        self.cwidth = 800
        self.cheight = 600
        self.cscrollregion = (0, 0, 1000, 1000)

        self.treeheight = 29
        self.fheight = 450

        self.category = None
        self.aliasname = None
        self.scalename = None
        self.scale_text = []
        self.interval_pattern = []
        self.png_files = []
        self.scale_selected = False
        self.lilyfile_name = ''

        self.enharmonic_spelling = tk.IntVar()
        self.enharmonic_spelling.set(2)

        self.chords_onoff = tk.BooleanVar()
        self.chords_onoff.set(True)

        self.current_canvas_page = 0
        self.num_canvas_pages = None

        self.frame = tk.Frame(self.mainframe, border=2, relief='sunken')
        self.subframe1 = tk.Frame(self.mainframe, relief='raised', border=2)
        self.subframe2 = tk.Frame(self.mainframe, relief='raised', border=2)

        self.statusbar = tk.Label(self.subframe2, border=2, relief='sunken')

        self.tree = ttk.Treeview(self.frame, height=self.treeheight)
        self.tree_yscroll = tk.Scrollbar(self.frame, orient='vertical',
                                         command=self.tree.yview)

        self.tree.heading('#0', text='Scale selector', anchor='w')
        self.tree.bind('<Double-1>', self.item_selected)

        self.canvas = tk.Canvas(self.frame, border=2,
                                width=self.cwidth, height=self.cheight,
                                scrollregion=self.cscrollregion)

        self.ybar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.hbar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)

        self.ybar.config(command=self.canvas.yview)
        self.hbar.config(command=self.canvas.xview)

        self.canvas.config(width=self.cwidth, height=self.cheight)
        self.canvas.config(xscrollcommand=self.hbar.set, yscrollcommand=self.ybar.set)

        self.pdfbutton = tk.Button(self.subframe1, border=2, text='Save as PDF',
                                   command=self.save_as_pdf)
        self.savescaletextbutton = tk.Button(self.subframe1, border=2,
                                             text='Save as Text',
                                             command=self.save_as_text)

        self.savescalepngbutton = tk.Button(self.subframe1, border=2,
                                            text='Save as png',
                                            command=self.save_as_png)

        self.dummy1 = tk.Button(self.subframe1, text='         ',
                                border=0, padx=0, pady=0)

        self.nav_forward = tk.Button(self.subframe1, text='Next Page',
                                     border=2, command=self.next_page)

        self.nav_back = tk.Button(self.subframe1, text='Prev Page',
                                  border=2, command=self.prev_page)

        self.dummy2 = tk.Button(self.subframe1, text='         ',
                                border=0, padx=0, pady=0)

        self.bbox1 = tk.Frame(self.subframe1, border=3, padx=2, pady=2,
                              relief='sunken')

        self.bbox1label = tk.Label(self.bbox1, padx=2, pady=2,
                                   text='Enharmonic Spelling')

        self.show_accidentials = tk.Radiobutton(self.bbox1,
                                                variable=self.enharmonic_spelling,
                                                padx=2, pady=2, text='Off',
                                                relief='raised', value=1)

        self.remove_accidentals = tk.Radiobutton(self.bbox1,
                                                 variable=self.enharmonic_spelling,
                                                 padx=2, pady=2, text='On',
                                                 relief='raised', value=2)

        self.dummy3 = tk.Button(self.subframe1, text='         ',
                                border=0, padx=0, pady=0)

        self.bbox2 = tk.Frame(self.subframe1, border=3, padx=2, pady=2,
                              relief='sunken')

        self.bbox2label = tk.Label(self.bbox2, padx=2, pady=2,
                                   text='Show chords')

        self.show_chords = tk.Radiobutton(self.bbox2, variable=self.chords_onoff,
                                          padx=2, pady=2, text='No',
                                          relief='raised', value=False)

        self.remove_chords = tk.Radiobutton(self.bbox2,
                                            variable=self.chords_onoff,
                                            padx=2, pady=2, text='Yes',
                                            relief='raised', value=True)

        self.exitbutton = tk.Button(self.subframe1, border=2, text='Exit',
                                    command=self.quit)

        self.mainframe.grid()
        self.frame.grid(column=0, row=0, rowspan=27, sticky='nsew')
        self.subframe1.grid(column=0, row=28, columnspan=6, rowspan=2, sticky='nsew')
        self.subframe2.grid(column=0, row=30, columnspan=6, rowspan=2, sticky='nsew')
        self.statusbar.grid(column=0, row=0, sticky='nsew')

        self.tree_yscroll.grid(column=1, row=0, rowspan=26, sticky='ns')
        self.tree.grid(column=0, row=0, rowspan=26)

        self.hbar.grid(column=2, row=26, rowspan=1, sticky='ew')
        self.ybar.grid(column=3, row=0, rowspan=25, sticky='ns')
        self.canvas.grid(column=2, row=0, rowspan=25, sticky='nsew')

        self.pdfbutton.grid(row=0, column=0)
        self.savescaletextbutton.grid(row=0, column=1)
        self.savescalepngbutton.grid(row=0, column=2)

        self.bbox1.grid(column=3, row=0, columnspan=3, sticky='nsew')
        self.bbox1label.grid(column=0, row=0, sticky='e')
        self.show_accidentials.grid(column=1, row=0)
        self.remove_accidentals.grid(column=2, row=0)

        self.bbox2.grid(column=6, row=0, columnspan=3, sticky='nsew')
        self.bbox2label.grid(column=0, row=0, sticky='e')
        self.show_chords.grid(column=1, row=0)
        self.remove_chords.grid(column=2, row=0)

        self.dummy1.grid(column=9, row=0, sticky='w')

        self.nav_back.grid(column=10, row=0, rowspan=1, sticky='w')
        self.nav_forward.grid(column=11, row=0, rowspan=1, sticky='w')

        self.dummy2.grid(column=12, row=0, sticky='w')

        self.exitbutton.grid(column=13, row=0)

        self.loadtree()

    def save_as_pdf(self):
        self.save_file('pdf')

    def save_as_png(self):
        self.save_file('png')

    def save_file(self, ft='pdf'):
        fsuffix = '.' + ft
        if self.scale_selected:
            # Step 1 - get file name from user
            iname = "".join(self.aliasname.split())
            initialfile = '{}{}'.format(iname, fsuffix)
            filetypes = [('{} files'.format(fsuffix), fsuffix)]
            initialdir = self.basedir + "SavedFiles{}".format('\\')
            # print('initialdir: {}\ninitialfile: {}'.format(initialdir, initialfile))
            pdb.set_trace()
            os.chdir(initialdir)
            f = tf.asksaveasfile(parent=self.parent, mode='w', initialfile=initialfile,
                                 filetypes=filetypes, initialdir=initialdir,
                                 title='Save McNote Scale text data')

            dirname, basename, baseroot, suffix = self.util.prepare_filename(f.name)
            fname = initialdir + baseroot + '.{}'.format(ft)
            # print('dirname: {}, basename: {}, baseroot: {}, suffix: {}'
            #       .format(dirname, basename, baseroot, suffix))
            f.close()

            # Step 2 - remove temporary file
            newfn = initialdir + baseroot + '.ly'
            os.remove(fname)

            # Step 3 - copy .ly file to supposed name
            lname = '../{}'.format(self.lilyfile_name)
            shutil.copy2(lname, newfn)

            # Step 4 - Create the file
            cmd = ["lilypond", "--{}".format(ft), baseroot]
            # print('cmd: {}'.format(cmd))

            ret_code = qx(cmd, stderr=STDOUT, timeout=10)

            # Step 5 - Verify success
            if b'compilation successfully completed' not in ret_code:
                msgs = list(ret_code.splitlines())
                newmsg = ['Error codes - Please report']
                for line in msgs:
                    newmsg.append(str(line))
                tm.showerror('Unable to compile music', newmsg)

            # Step 6 - Remove lilypond file
            # print('newfn: {}'.format(newfn))
            os.remove(newfn)
            os.chdir(self.basedir)
        else:
            tm.showerror('file_save - {}', 'Please select scale'.format(ft))

    def save_as_text(self):
        if self.scale_selected:
            # defaultextension = '.txt'
            initialfile = '{}.txt'.format(self.aliasname)
            filetypes = [('all files', '.*'), ('text files', '.txt')]
            initialdir = self.basedir + 'SavedFiles'

            f = tf.asksaveasfile(parent=self.parent, mode='w', initialfile=initialfile,
                                 filetypes=filetypes, initialdir=initialdir,
                                 title='Save McNote Scale text data')
            for line in self.scale_text:
                line += '\n\n'
                f.write(line)
            f.close()
        else:
            tm.showerror('save_as_text', 'Please select scale')

    def show_status(self, message=''):
        self.statusbar.configure(text=message)

    def item_selected(self, event):
        # self.remove_old_files()
        item = self.tree.selection()[0]
        self.show_status(message='')
        parentnode = self.tree.parent(item)
        if parentnode:
            self.category = self.tree.item(parentnode, "text")
            self.aliasname = self.tree.item(item, "text")
            self.scalename = self.data.xref[self.category][self.aliasname]
            self.interval_pattern = self.sc.get_intervals(self.category,
                                                          self.scalename)
            # print('self.category: {}\nself.aliasname: {}\nself.scalename: {}\nself.interval_pattern: {}'
            #       .format(self.category, self.aliasname,self.scalename, self.interval_pattern))
            self.createscale()
            self.showimages()

    def loadtree(self):
        # TODO use new utilities
        categories = self.util.categories
        for category in categories:
            parentnode = self.tree.insert('', 'end', text=category,
                                          open=False)
            nodes = self.util.get_scales_of_category(category)
            for item in nodes:
                self.tree.insert(parentnode, 'end', text=item,
                                 open=False)

    def showimages(self):
        self.canvas.delete("all")
        if self.num_canvas_pages is not None:
            # print('showimages, png_files: {}'.format(self.png_files))
            fn = self.png_files[self.current_canvas_page]
            # print('showimages, fn: {}'.format(fn))
            filename = self.basedir + fn
            print('Png Filename: {}'.format(filename))
            img = Image.open(os.path.join(self.basedir, filename), 'r')
            self.canvas.image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')

    def clearstatus(self):
        self.show_status(message='')

    def next_page(self):
        if self.scale_selected:
            print('self.current_canvas_page: {}, self.num_canvas_pages: {}'
                  ''.format(self.current_canvas_page, self.num_canvas_pages))
            if self.current_canvas_page < self.num_canvas_pages:
                self.current_canvas_page += 1
                self.showimages()
            else:
                self.show_status(message='You are on the last page')
                self.parent.after(10000, self.clearstatus)
        else:
            tm.showerror('Next Page', 'Please select scale')

    def prev_page(self):
        if self.scale_selected:
            if self.current_canvas_page > 0:
                self.current_canvas_page -= 1
                self.showimages()
            else:
                self.show_status(message='You are on the first page')
                self.parent.after(10000, self.clearstatus)
        else:
            tm.showerror('Next Page', 'Please select scale')

    def remove_old_files(self):
        rlist = self.util.find_files(self.basedir, self.png_basename)
        for filename in rlist:
            os.remove(filename)
        self.scale_selected = False

    def add_music_line(self, f, scale):
        # scale = self.data.get_scale(tonic, self.interval_pattern)
        stext = "music = \\relative c' { "
        for snote in scale:
            z = self.util.translate_note_to_lilypond(snote)
            stext += '{} '.format(z)
        stext += '\\bar "|." }\n'
        f.write(stext)

    def write_enharmonic_scale(self, tonic, f, scale):
        # By default (in this software, if enharmonc key is Theoretical
        stext = ''
        self.scale_text.append('Scale theoretical key of {} - {}'.format(tonic, scale))
        stext += '\n\\score {\n  \\new Staff {\n'
        snote = self.util.translate_note_to_lilypond(tonic)
        stext += '    \\naturalizeMusic\n    \\transpose c {} {{\n'.format(snote)
        stext += '      \\mark "                                             {} {}' \
                 ' - Theoretical Key"\n'.format(tonic, self.aliasname)
        stext += '      \\music\n    }\n  }\n'
        stext += '  \\layout { \\override NonMusicalPaperColumn.page-break-permission = ##f }\n'
        stext += '}\n'
        f.write(stext)

    def write_scale(self, tonic, f, scale):
        self.scale_text.append('Scale key of {} - {}'.format(tonic, scale))
        f.write("\n\\score {\n  \\relative c' { ")
        firstnote = True

        for snote in scale:
            z = self.util.translate_note_to_lilypond(snote)
            f.write("{} ".format(z))

            if firstnote:
                firstnote = False
                if self.util.is_theoretical(scale):
                    f.write('\\mark "{} {} - Theoretical Key" '.format(snote, self.aliasname))
                else:
                    f.write('\\mark "{} {}" '.format(snote, self.aliasname))
        f.write('\\bar "|." }\n}\n')

    def createscale(self):
        self.remove_old_files()
        ftime = '{}'.format(int(time.time()))
        self.lilyfile_name = self.png_basename + ftime + '.ly'
        print('self.png_basename: {}, self.lilyfile_name: {}'
              .format(self.png_basename, self.lilyfile_name))
        self.scale_text = []
        with open(os.path.join(self.basedir, self.lilyfile_name), 'w') as f:
            if self.enharmonic_spelling.get() == 1:
                # This code for no enharmonic modification
                self.write_standard_header(f)
                for tonic in self.data.nkeys:
                    scale = self.sc.get_scale(tonic, self.interval_pattern)
                    self.write_scale(tonic, f, scale)
            else:
                self.create_enharmonic_scale(f)

        # TODO - Add chord build routine here
        if self.chords_onoff:
            self.add_chords()

        self.create_png_files()
        self.scale_selected = True

    def add_chords(self):
        pass

    def create_enharmonic_scale(self, f):
        # This code for enharmonic modification
        print('In loop 2')

        self.write_enharmonic_header(f)
        firstscale = True
        for tonic in self.data.nkeys:
            scale = self.sc.get_scale(tonic, self.interval_pattern)

            if firstscale:
                self.add_music_line(f, scale)
                firstscale = False

            if self.util.is_theoretical(scale):
                self.write_enharmonic_scale(tonic, f, scale)
            else:
                self.write_scale(tonic, f, scale)

    def write_enharmonic_header(self, f):
        # head = None
        with open(os.path.join(self.lilydir, 'enharmonicHeader.ly'), 'r') as f1:
            head = f1.read()
        f.write(head)
        f.write('  title = "{} - {}'.format(self.category, self.aliasname))
        if self.aliasname != self.scalename:
            f.write('\n (alias for {})'.format(self.scalename))
        f.write('"\n  composer = "Created By McNote ver. {}"\n'.format(self.version))
        f.write('}\n\n')

    def write_standard_header(self, f):
        f.write('\\version "2.18.2"\n\n\\header {\n')
        f.write('  title = "{} - {}'.format(self.category, self.aliasname))
        if self.aliasname != self.scalename:
            f.write('\n (alias for {})'.format(self.scalename))
        f.write('"\n  composer = "Created By McNote ver. {}"\n'.format(self.version))
        f.write('}\n\n')

    def create_png_files(self):
        self.png_files = []

        cmd = ["lilypond", "--png", self.lilyfile_name]
        print('cmd: {}'.format(cmd))
        ret_code = qx(cmd, stderr=STDOUT, timeout=10)

        if b'compilation successfully completed' not in ret_code:
            msgs = list(ret_code.splitlines())
            newmsg = ['Error codes - Please report McNote@DimpleChad.com\n']
            for line in msgs:
                newmsg.append(str(line))
            tm.showerror('Unable to compile music', newmsg)

        # Create Index
        self.png_files = []
        self.png_files = self.util.find_files(self.basedir, self.png_basename,
                                              fsuffix='.png')
        self.num_canvas_pages = len(self.png_files) - 1
        if self.num_canvas_pages >= 0:
            self.current_canvas_page = 0
        else:
            self.current_canvas_page = None

            # print('png files: ')
            # for item in self.png_files:
            #     print('{}'.format(item))

    def quit(self):
        self.parent.after(100, self.parent.destroy())


if __name__ == '__main__':
    root = tk.Tk()
    McNote(root)
    root.mainloop()
