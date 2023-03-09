"""
Some methods that move source files into place
"""
import shutil
import time
from jinja2 import Template
import os
from jinja2 import Environment, FileSystemLoader
from bs4 import BeautifulSoup
import datetime
class MoverShaker:

    def __init__(self,filename,title,video_url):

        self.filename = filename
        self.VID_DIR = f"transcripts/{filename}"
        self.video_url = video_url
        self.title = title
        self.graph_png_url =''
        self.transcript_url =''


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

        parts = html_dst_file.split('/')
        self.transcript_url = '/'.join(parts[-2:])
        """
        cleaning up the file name 
        """
        if self.transcript_url.endswith("_.html"):
            self.transcript_url = self.transcript_url[:-6] + ".html"
        print(self.transcript_url)

        """
        copy .png over
        """
        png_source_src_file = png_source
        print(png_source_src_file)
        png_dst_file = self.VID_DIR.lower() + '/' + self.filename[:-6].lower() + '.png'
        print(png_dst_file)
        shutil.copy(png_source_src_file, png_dst_file)

        parts = png_dst_file.split('/')
        self.graph_png_url = '/'.join(parts[-2:])

        if self.graph_png_url.endswith("_.png"):
            self.graph_png_url = self.graph_png_url[:-6] + ".png"
        print(self.graph_png_url)





    def table_a_updater(self):
        """
        Updates table on index.html
        """

        # Define the path to the templates directory
        template_dir = os.path.join(os.path.dirname(__file__), 'templates')

        # Create a Jinja2 environment object
        env = Environment(loader=FileSystemLoader(template_dir))

        # Define the data for each row
        data = [
            {'date': 'Apr 2022', 'title': "Andrew Tate's Final Message", 'transcript': 'transcripts/final_message.html',
             'video_link': 'https://www.youtube.com/watch?v=SK2tlXFg8tM&t=6s'},
            {'date': 'Dec 2018', 'title': 'PhD course', 'transcript': 'transcripts/andrew_tate_phd.html',
             'video_link': 'https://www.youtube.com/watch?v=htYdpp0LxOE&t=872s'},
            {'date': 'Apr 2020', 'title': 'Only Fans Elites FULL Course',
             'transcript': 'transcripts/only_fans_elites_full.html',
             'video_link': 'https://www.youtube.com/watch?v=y3n7HB03UK8&t=529s'},

            {'date': 'Nov 2022', 'title': 'Full Send Pod1',
             'transcript': 'transcripts/full_send_pod1.html',
             'video_link': 'https://www.youtube.com/watch?v=kJyTkLgW_KI&t=747s'},
        ]

        # Sort the rows by date in descending order
        data.sort(key=lambda x: datetime.datetime.strptime(x['date'], '%b %Y'), reverse=True)

        # Get the path to the original HTML file
        index_path = os.path.join(os.path.dirname(__file__), 'index.html')

        # Read the original HTML file
        with open(index_path) as f:
            html = f.read()

        # Create a BeautifulSoup object from the original HTML
        soup = BeautifulSoup(html, 'html.parser')

        # Find the table in the HTML
        table = soup.find('table')

        # Clear the table body
        tbody = table.find('tbody')
        tbody.clear()

        # Populate the table with the sorted rows
        for row in data:
            tr = soup.new_tag('tr')
            tbody.append(tr)

            td1 = soup.new_tag('td')
            td1.string = row['date']
            tr.append(td1)

            td2 = soup.new_tag('td')
            td2.string = row['title']
            tr.append(td2)

            td3 = soup.new_tag('td')
            a = soup.new_tag('a', href=row['transcript'])
            a.string = 'View Transcript'
            td3.append(a)
            tr.append(td3)

            td4 = soup.new_tag('td')
            a = soup.new_tag('a', href=row['video_link'])
            a.string = 'Watch Video'
            td4.append(a)
            tr.append(td4)

        # Write the updated HTML to a new file in the templates directory
        new_index_path = os.path.join(template_dir, 'index.html')

        with open(new_index_path, 'w') as f:
            f.write(soup.prettify())

        # Return the HTML as the response to the user's request
        return str(soup)




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
            'image_url': self.graph_png_url,
            'transcript_url': self.transcript_url
        }

        # Render the template with the data
        html = template.render(data)

        soup = BeautifulSoup(html, 'html.parser')

        # Write the HTML to a file
        with open(f'transcripts/{self.title[:-6].lower()}.html', 'w') as f:
            f.write(soup.prettify())








    def main(self):
        self.moves_files()
        #self.table_a_updater()
        self.transcript_page_template()




if __name__ == "__main__":
    a = MoverShaker(filename="April_Raid_Interview0",
                    title='April_Raid_Interview0',
                    video_url='https://www.youtube.com/embed/4PCK5NzAPUM',

                    )
    a.main()












