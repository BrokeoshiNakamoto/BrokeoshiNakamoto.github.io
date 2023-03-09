"""
Some methods that move source files into place
"""
import shutil
import os
import time


class MoverShaker:

    def __init__(self,filename):

        self.filename = filename
        self.VID_DIR = f"transcripts/{filename}"

    def moves_files(self,src_file,dst_file,type):
        """
        check if dir exists
        if not create it
        """
        if not os.path.exists(self.VID_DIR.lower()):
            os.makedirs(self.VID_DIR.lower())
            print(f"Created directory: {self.VID_DIR.lower()}")

        else:
            print(f"Directory already exists: {self.VID_DIR}")

        self.SOURCE_DIR = f"/home/prime/PycharmProjects/auris/output/html/"
        html_source = self.SOURCE_DIR+self.filename+"_html.html"

        self.SOURCE_DIR = f"/home/prime/PycharmProjects/auris/output/graphs/"
        png_source = self.SOURCE_DIR+self.filename+"_graph.png"
        print(html_source)
        print(png_source)

        """
        copy copy.html
        """
        html_src_file = html_source
        print(src_file)
        html_dst_file = self.VID_DIR.lower()+'/'+self.filename[:-6].lower()+'.html'
        print(html_dst_file)
        shutil.copy(html_src_file, html_dst_file)
        """
        copy .png over
        """
        png_source_src_file = png_source
        print(png_source_src_file)
        png_dst_file = self.VID_DIR.lower() + '/' + self.filename[:-6].lower() + '.png'
        print(html_dst_file)
        shutil.copy(png_source_src_file, png_dst_file)



    def main(self):

        self.moves_files(src_file='/home/prime/PycharmProjects/auris/output/',dst_file='efdfd',type='html')


if __name__ == "__main__":
    a = MoverShaker(filename="Andrew_Tate_Final_Message")
    a.main()
