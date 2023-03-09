"""
Some methods that move source files into place
"""
import shutil
import os
import time
from jinja2 import Template

class MoverShaker:

    def __init__(self,filename,title,video_url,image_url,transcript_url):

        self.filename = filename
        self.VID_DIR = f"transcripts/{filename}"
        self.video_url = video_url
        self.image_url = image_url
        self.transcript_url = transcript_url
        self.title = title

    def moves_files(self):
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

    def transcript_page_template(self):


        # Define the template with placeholders
        template = Template('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ title }}</title>
            <meta charset="UTF-8">
            <style>
                .back-button {
                    position: absolute;
                    top: 0;
                    right: 0;
                    padding: 10px;
                    background-color: #f00;
                    color: #fff;
                    text-decoration: none;
                }
                .video-container {
                    margin-top: 20px;
                    display: flex;
                    flex-wrap: wrap;
                    align-items: center;
                }
                .video {
                    flex: 1;
                    margin-right: 20px;
                }
                .image-container {
                    flex: 1;
                    max-width: 700px;
                    margin-top: 20px;
                }
                .image-container img {
                    max-width: 100%;
                    height: auto;

                }
            </style>
        </head>
        <body>
            <a href="#" class="back-button">Back</a>
            <div class="video-container">
                <div class="video">
                    <iframe width="420" height="345" src="{{ video_url }}"></iframe>
                </div>
                <div class="image-container">
                    <img src="{{ image_url }}" alt="Image">
                </div>
            </div>
            <h1>Transcript</h1>
            <p></p>
            <iframe src="{{ transcript_url }}" width="100%" height="500px"></iframe>
        </body>
        </html>
        ''')

        # Define the data to fill in the placeholders
        data = {
            'title': self.title,
            'video_url': self.video_url,
            'image_url': self.image_url,
            'transcript_url': self.transcript_url
        }

        # Render the template with the data
        html = template.render(data)

        # Write the HTML to a file
        with open('transcripts/my_page.html', 'w') as f:
            f.write(html)






    def main(self):

        self.moves_files()
        #self.transcript_page_template()


if __name__ == "__main__":
    a = MoverShaker(filename="Andrew_Tate_PhD_Course",
                    title='Andrew_Tate_PhD_Course',
                    video_url='',
                    image_url='',
                    transcript_url='')
    a.main()
