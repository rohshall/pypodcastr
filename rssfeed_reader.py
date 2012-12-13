#!/usr/bin/env python3
from collections import namedtuple
from urllib.request import urlretrieve
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


def get_feeds():
    for feedUrl in open('feeds.txt'):
        episodes = get_feed_episodes(feedUrl)
        download_episodes(episodes)


if __name__ == '__main__':
    try:
        get_feeds()
    except KeyboardInterrupt:
        pass
