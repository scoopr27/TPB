from tpb import TPB
from tpb import CATEGORIES, ORDERS

t = TPB('https://thepiratebay.org') # create a TPB object with default domain

# search for 'public domain' in 'movies' category
search = t.search('public domain', category=CATEGORIES.VIDEO.MOVIES)

# return listings from page 2 of this search
search.page(2)

# sort this search by count of seeders, and return a multipage result
search.order(ORDERS.SEEDERS.ASC).multipage()

# search, order by seeders and return page 3 results
t.search('python').order(ORDERS.SEEDERS.ASC).page(3)

# multipage beginning on page 4
t.search('recipe book').page(4).multipage()

# search, in a category and return multipage results
t.search('something').category(CATEGORIES.OTHER.OTHER).multipage()

# get page 3 of recent torrents
t.recent().page(3)

# get top torrents in Movies category
t.top().category(CATEGORIES.VIDEO.MOVIES)

# print all torrent descriptions
for torrent in t.search('public domain'):
    print(torrent.info)

# print all torrent files and their sizes
for torrent in t.search('public domain'):
    print(torrent.files)
