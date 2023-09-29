import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
import logging
import csv

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler for output file
handler = logging.FileHandler('./data_files/log_files/app.log')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)

# Create an error file handler for error output file
error_handler = logging.FileHandler('./data_files/log_files/error.log')
error_handler.setFormatter(formatter)
error_handler.setLevel(logging.ERROR)

# Create a stream handler to print log messages to the console in real-time
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)  # Set the desired logging level for console here

# Add handlers to the logger
logger.addHandler(handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)

# files
json_file = "./data_files/resources_to_teach/common_vocabs.json"
text_file = "./data_files/resources_to_teach/common_vocabs.txt"
hiragana_file = "./data_files/resources_to_teach/hiragana.txt"
personal_csv_file = "./data_files/resources_to_teach/common_words_personal.csv"

class Extractor:
    def __init__(self, hiragana_file):
        self.hiragana_file = hiragana_file

    async def fetch_html(self, url, session):
        try:
            async with session.get(url) as res:
                if res.status != 200:
                    logger.warning(f"Non-200 response from {url}: {res.status}")
                logger.info(f"Received response from {url}")
                return await res.text()
        except Exception as e:
            logger.error(f"Failed to get response from {url}: {e}")
            return None

    async def find_level(self, word, session):
        try:
            async with session.get(f"https://jisho.org/search/{word}") as res:
                text_res = await res.text()
                soup = BeautifulSoup(text_res, "lxml")
                word_section = soup.find("div", "concept_light clearfix")
                jlpt_level = word_section.find("span", class_="concept_light-tag label").text
                return jlpt_level
        except Exception as e:
            logger.error("Error in find_level: ", e)

    async def find_words(self, soup, word_detail_list, session):
        try:
            words_div = soup.find_all("div", class_="concept_light-representation")
            for word_div in words_div:
                text = word_div.find("span", class_="text")
                kanji_word = text.text.strip()
                jlpt_level = await self.find_level(kanji_word, session)
                word_detail_list.append({"kanji": kanji_word, "jlpt_level": jlpt_level})
                print(f"Word: {kanji_word}")
        except Exception as e:
            logger.error("Error in find_words: ", e)

    async def fetch_words(self, url, session, semaphore):
        async with semaphore:
            try:
                html = await self.fetch_html(url, session)
                if html:
                    soup = BeautifulSoup(html, "lxml")
                    word_detail_list = []
                    await self.find_words(soup, word_detail_list, session)
                    return word_detail_list
            except Exception as e:
                logger.error(f"Failed to extract words from {url}: {e}")
                return []

    async def process_urls(self, url_list):
        logger.info(f"Starting to process {len(url_list)} URLs.")
        word_counts = {}
        async with aiohttp.ClientSession() as session:
            semaphore = asyncio.Semaphore(20)
            tasks = []
            for url in url_list:
                await asyncio.sleep(1)
                task = self.fetch_words(url, session, semaphore)
                tasks.append(task)
            result = await asyncio.gather(*tasks)
            for url, words in zip(url_list, result):
                word_counts[url] = len(words)
            flattened_result = [item for sublist in result for item in sublist]
            logger.info("Processing completed.")
            for url, count in word_counts.items():
                logger.info(f"Total words from {url}: {count}")
            return flattened_result

def json_to_text():
    with open(json_file, "r") as f:
        json_ = json.loads(f.read())
        list_ = [i["kanji"] for i in json_]
        with open(text_file, "a+") as g:
            counter = 1
            for i in list_:
                if counter % 20 == 0:
                    g.write(f"{i} \n")
                else:
                    g.write(f"{i} ")
                counter += 1

def sort_key(item):
    return ["JLPT N5", "JLPT N4", "JLPT N3", "JLPT N2", "JLPT N1"].index(item['jlpt_level'])

def filter_duplicates():
    with open(json_file, "r") as f:
        python_list = json.load(f)
        unique_list = [dict(t) for t in {tuple(obj.items()) for obj in python_list}]
        # Sort the deduplicated list
        sorted_unique_list = sorted(unique_list, key=sort_key)
        with open(json_file, "w") as g:
            g.write(json.dumps(sorted_unique_list, indent=4, ensure_ascii=False))
        
        print("Duplicates filtered and list sorted successfully.")


def merge_persona_file_with_scraped():
    with open(json_file, "r") as f:
        json_data = f.read()
        python_list = json.loads(json_data)
        with open(personal_csv_file, "r") as g:
            csv_reader = csv.reader(g)
            for row in csv_reader:
                data_format = {"kanji": row[0], "jlpt_level": "JLPT N5"}
                python_list.append(data_format)
        with open(json_file, "w") as h:
            h.write(json.dumps(python_list, indent=4, ensure_ascii=False))
        print("data merged successfully :)")

async def get_words_async():
    extractor = Extractor(hiragana_file=hiragana_file)
    urls = [f"https://jisho.org/search/%20%23common%20%23words?page={i + 1}" for i in range(50)]
    result = await extractor.process_urls(urls)
    logger.info(f"Total words: {len(result)}")
    with open(json_file, 'w') as outfile:
        try:
            outfile.write(json.dumps(result, indent=4, ensure_ascii=False))
        except Exception as e:
            logger.error(f"Failed to write data to file: {e}")

    logger.info("Data saved to common_vocabs.json.")

def get_words():
    asyncio.run(get_words_async())

if __name__ == "__main__":
    get_words()
    merge_persona_file_with_scraped()
    filter_duplicates()
    json_to_text()

"""
order to remember: 
first get json
then merge personal json file
then deduplicate the json file
then create a text file
"""