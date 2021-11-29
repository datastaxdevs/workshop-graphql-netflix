#!/bin/env python3
# starting from https://github.com/csplinter/datasets/blob/master/netflix/netflixdata-clean.csv

import sys
import csv
from collections import Counter

THUMBNAIL_PLACEHOLDER = 'https://i.imgur.com/V6WMXYx.mp4'

# genres handling
baseGenres = {
    'Action',
    'Anime',
    'Award-Winning',
    'Children & Family',
    'Comedies',
    'Documentaries',
    'Dramas',
    'Fantasy',
    'French',
    'Horror',
    'Independent',
    'Music & Musicals',
    'Romance',
    'Sci-Fi',
    'Thriller',
}
genreMapping = { # source-csv to our genres
    'Dramas'                        : 'Dramas',             # 1077
    'Comedies'                      : 'Comedies',           # 803
    'Documentaries'                 : 'Documentaries',      # 644
    'Action & Adventure'            : 'Action',             # 597
    'International TV Shows'        : 'International',      # 570
    'Children & Family Movies'      : 'Children & Family',  # 358
    'Crime TV Shows'                : 'Crime',              # 309
    'Kids TV'                       : 'Children & Family',  # 288
    'Stand-Up Comedy'               : 'Comedies',           # 273
    'British TV Shows'              : 'International',      # 210
    'Horror Movies'                 : 'Horror',             # 205
    'Docuseries'                    : 'Documentaries',      # 148
    'Anime Series'                  : 'Anime',              # 117
    'TV Comedies'                   : 'Comedies',           # 89
    'International Movies'          : 'International',      # 85
    'Reality TV'                    : 'Reality TV',         # 63
    'Classic Movies'                : 'Classic',            # 62
    'Movies'                        : 'Action',             # 56
    'TV Dramas'                     : 'Dramas',             # 56
    'Thrillers'                     : 'Thriller',           # 40
    'TV Action & Adventure'         : 'Action',             # 30
    'Stand-Up Comedy & Talk Shows'  : 'Comedies',           # 28
    'Romantic TV Shows'             : 'Romance',            # 21
    'Classic & Cult TV'             : 'Cult',               # 19
    'Independent Movies'            : 'Independent',        # 18
    'Anime Features'                : 'Anime',              # 12
    'Music & Musicals'              : 'Music & Musicals',   # 12
    'Cult Movies'                   : 'Cult',               # 10
    'Sci-Fi & Fantasy'              : 'Sci-Fi',             # 10
    'TV Shows'                      : 'TV Show',            # 10
    'TV Horror'                     : 'Horror',             # 9
    'Romantic Movies'               : 'Romance',            # 2
    'Spanish-Language TV Shows'     : 'International',      # 1
    'Sports Movies'                 : 'Action',             # 1
    'TV Sci-Fi & Fantasy'           : 'Fantasy',            # 1
}    

def _mConvert(rawM):
    newM = {k: v for k, v in rawM.items()}
    # we brutally reduce a movie to a single genre here.
    # And also 'eval' is bad to use. Meh.
    newM['listed_in'] = eval(rawM['listed_in'])[0]
    return newM


if __name__ == '__main__':
    inFile = open(sys.argv[1])
    args = sys.argv[2:]

    # read csv
    reader = csv.reader(inFile)
    allRows = list(reader)
    headers = allRows[0]
    movies = [
        _mConvert(
            {
                t: v
                for t, v in zip(headers, row)
            }
        )
        for row in allRows[1:]
    ]
    print('Loaded %i entries' % len(movies))

    # The following flags I used in sequence to create the mapping
    if '-g' in args:
        # survey of genres
        # and printing a draft for the conversion map!
        genres = Counter(
            m['listed_in']
            for m in movies
        )
        print('# Genre conversion map')
        print('{')
        print('\n'.join(
            '    %-32s: \'xxx\'  # %i' % (
                '\'%s\'' % g,
                gc,
            )
            for g, gc in genres.most_common()
        ))
        print('}')
    if '-g2' in args:
        # stats on the genre mapping
        fullGenres = baseGenres | set(genreMapping.values())
        print('Original genres: %i' % len(baseGenres))
        print('New count of genres: %i' % len(fullGenres))
        print('NEW GENRES to add to the mutation:')
        print('\n'.join('    "%s"' % g for g in (fullGenres - baseGenres)))
        # are all covered?
        print('Genres not represented in new input file:')
        print('\n'.join('    "%s"' % g for g in (baseGenres - set(genreMapping.values()))))
        allCovered = all(m['listed_in'] in genreMapping for m in movies)
        print('Coverage of new movies: %s' % (
            'all covered' if allCovered else 'SOME ARE NOT COVERED'
        ))
    if '-o' in args:
        # we create the final csv

        def _fakeDuration(rawM):
            return 105 + (len(str(rawM)) % 45)

        def _finalizeM(rawM):
            # genre
            # title
            # thumbnail: we use a placeholder
            # year
            # synopsis
            # duration: we pseudo-randomize it!
            return [
                genreMapping[rawM['listed_in']],
                rawM['title'],
                THUMBNAIL_PLACEHOLDER,
                rawM['release_year'],
                rawM['description'],
                _fakeDuration(rawM),
            ]

        finalMovies = [
            _finalizeM(m)
            for m in movies
        ]

        with open('OUTPUT.csv', 'w') as outFile:
            writer = csv.writer(outFile)
            writer.writerow(['genre','title','thumbnail','year','synopsis','duration'])
            for m in finalMovies:
                writer.writerow(m)
        print('Written %i entries to "OUTPUT.csv"' % len(finalMovies))
