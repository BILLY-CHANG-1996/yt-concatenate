from pytube import YouTube
from .step import Step
import time
from .step import StepException
from yt_concate.settings import CAPTIONS_DIR
class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            if utils.caption_file_exist(url):
                print('found existing caption file')
                continue
            print(url)
            try:
                source = YouTube(url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption.generate_srt_captions()
            except (KeyError, AttributeError):
                print('Error when downloading caption for', url)
                continue

            #save the caption to a file named Outpust.txt
            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption.generate_srt_captions())
            text_file.close()

        end = time.time()
        print('took', end - start, 'seconds')

