from nose.tools import eq_, ok_, raises
import rssfeed_reader


def test_get_feed_episodes():
    episode_generator = rssfeed_reader.get_feed_episodes('file:///home/salil/Python/pypodcastr/tests/feed.rss')
    episode = next(episode_generator)
    eq_(episode, rssfeed_reader.Episode(title='Newshour: Finucane report shock: 12 Dec 12', link='http://downloads.bbc.co.uk/podcasts/worldservice/newshour/newshour_20121212-1400a.mp3'))


@raises(StopIteration)
def test_nonsense_url():
    episode_generator = rssfeed_reader.get_feed_episodes('http://timbuktunonsense.zumrigft.com')
    next(episode_generator)    
