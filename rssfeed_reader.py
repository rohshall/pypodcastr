#!/usr/bin/env python3
from collections import namedtuple
from urllib.request import urlretrieve
import multiprocessing
import feedparser

Episode = namedtuple('Episode', ['title', 'link'])

def get_feed_episodes(feedUrl):
    feed = feedparser.parse(feedUrl)
    for item in feed["items"]:
        yield Episode(item["title"], item["link"])


def download_episodes(episodes):
    for episode in episodes:
        print("Downloading ", episode.title)
        localfilename = episode.link.rpartition('/')[2]
        urlretrieve(episode.link, localfilename)


def download_feed(feedUrl):
    episodes = get_feed_episodes(feedUrl)
    download_episodes(episodes)


def get_feeds():
    jobs = []
    for feedUrl in open('feeds.txt'):
        job = multiprocessing.Process(name=feedUrl, target=download_feed, args=(feedUrl,))
        jobs.append(job)
        job.start()
    for job in jobs:
        job.join()


if __name__ == '__main__':
    try:
        get_feeds()
    except KeyboardInterrupt:
        pass
