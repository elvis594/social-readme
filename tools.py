import datetime
import re

import feedparser
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

import logging

DOUBAN_RATING = {
    '<p>推荐: 很差</p>': '🌟☆☆☆☆ 很差',
    '<p>推荐: 较差</p>': '🌟🌟☆☆☆ 较差',
    '<p>推荐: 还行</p>': '🌟🌟🌟☆☆ 还行',
    '<p>推荐: 推荐</p>': '🌟🌟🌟🌟☆ 推荐',
    '<p>推荐: 力荐</p>': '🌟🌟🌟🌟🌟 力荐'
}

def generate_new_readme(start_comment: str, end_comment: str, content: str, readme: str) -> str:
    """Generate a new Readme.md"""
    pattern = f"{start_comment}[\\s\\S]+{end_comment}"
    repl = f"{start_comment}\n{content}\n{end_comment}"
    if re.search(pattern, readme) is None:
        print(f"can not find section in your readme, please check it, it should be {start_comment} and {end_comment}")

    return re.sub(pattern, repl, readme)


def format_time(timestamp) -> datetime:
    gmt_format = '%a, %d %b %Y %H:%M:%S GMT'
    date_str = datetime.datetime.strptime(timestamp, gmt_format) + datetime.timedelta(hours=8)
    return date_str.date()


def generate_entries(rss_hub_link,route,params) -> str:
    #add retry and timeout
    return fetch_feed_with_retries_and_timeout(rss_hub_link + route + params, timeout=5, max_retries=2)

def fetch_feed_with_retries_and_timeout(url, timeout, max_retries):
    print(f"Fetching RSS feed from {url}")
    session = requests.Session()
    retries = Retry(total=max_retries, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    try:
        response = session.get(url, timeout=timeout)
        response.raise_for_status()  # 检查响应状态
        return feedparser.parse(response.content)["entries"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the RSS feed: {e}")
        return None
    
def generate_rating_star(desc) -> str:
    pattern = re.compile(r'<p>推荐: [\S\S]+</p>')
    matches = re.findall(pattern, desc)
    if len(matches) > 0:
        return DOUBAN_RATING[matches[0]]
    return ''