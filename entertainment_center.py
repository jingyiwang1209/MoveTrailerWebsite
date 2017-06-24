import media
import fresh_mummy

# Mutiple instances (movies to be rendered on the web page) of media.Movie class.

mummy_1 = media.Movie('The Mummy', '1999', 'Brendan Fraser,'
                      'Rachel Weisz, John Hannah',
                      'The film follows adventurer Rick O\'Connell, '
                      'who travels to Hamunaptra, the city of the dead, '
                      'with an archaelogist and her brother. '
                      'There they accidentally awaken Imhotep, '
                      'a high priest from the reign of the pharaoh Seti I,'
                      'who has been cursed for eternity.',
                      'https://upload.wikimedia.org/wikipedia/'
                      'en/6/68/The_mummy.jpg',
                      'https://www.youtube.com/watch?v=f7oKxlaUBac')

mummy_2 = media.Movie('The Mummy Returns', '2001',
                      'Brendan Fraser, Rachel Weisz, '
                      'John Hannah',
                      'It is the year 1933 and Rick O\'Connell and '
                      'Evelyn Carnahan are married with an 8-year-old son, Alex.'
                      'When Alex triggers a curse and Imhotep is resurrected, '
                      'Rick and Evy must once again try to save the world and defeat the mummy.',
                      'https://upload.wikimedia.org/wikipedia/en'
                      '/b/b7/The_Mummy_Returns_poster.jpg',
                      'https://www.youtube.com/watch?v=3yXjs7BUKYc')

mummy_3 = media.Movie('The Mummy: Tomb of the Dragon Emperor',
                      '2008', 'Brendan Fraser, Jet Li, <br>Maria Bello',
                      'Set in 1946, the film continues the '
                      'adventures of Rick O\'Connell, '
                      'his wife Evy, and his son Alex against '
                      'a different mummy, the Dragon Emperor (Jet Li) of China.',
                      'https://upload.wikimedia.org/wikipedia/en/d/'
                      'df/The_Mummy_-_Tomb_of_the_Dragon_Emperor.jpg',
                      'https://www.youtube.com/watch?v=5-4qSE2Ch0Y')

scorpion_king_1 = media.Movie('The Scorpion King', '2002', 'Dwayne Johnson',
                              'This spin-off series follows'
                              ' the adventures of Mathayus,'
                              'who would later be known as the Scorpion King and, '
                              'eventually, become a foe in The Mummy Returns.',
                              'https://upload.wikimedia.org/wikipedia/en/'
                              '1/1d/The_Scorpion_King_poster.jpg',
                              'https://www.youtube.com/watch?v=CmEKTae2iys')

scorpion_king_2 = media.Movie('The Scorpion King 2: Rise of a Warrior',
                              '2008', 'Michael Copon',
                              'This spin-off series follows'
                              ' the adventures of Mathayus,'
                              'who would later be known as the Scorpion King and, '
                              'eventually, become a foe in The Mummy Returns.',
                              'https://upload.wikimedia.org/wikipedia/en/'
                              '7/72/Scorpion_King_2_DVD_Cover.jpg',
                              'https://www.youtube.com/watch?v=ozz_nfi6vKM')

scorpion_king_3 = media.Movie('The Scorpion King 3: Battle for Redemption',
                              '2012', 'Victor Webster',
                              'This spin-off series follows'
                              ' the adventures of Mathayus,'
                              'who would later be known as the Scorpion King and, '
                              'eventually, become a foe in The Mummy Returns.',
                              'https://upload.wikimedia.org/'
                              'wikipedia/en/6/65/'
                              'Scorpion_King_3_DVD_Cover.jpg',
                              'https://www.youtube.com/watch?v=rld-6rRDb-k')

scorpion_king_4 = media.Movie('The Scorpion King 4: Quest for Power',
                              '2015', 'Victor Webster',
                              'This spin-off series follows'
                              ' the adventures of Mathayus,'
                              'who would later be known as the Scorpion King and, '
                              'eventually, become a foe in The Mummy Returns.',
                              'https://upload.wikimedia.org/wikipedia/en/0/00/'
                              '%22The_Scorpion_King_4%'
                              '2C_Quest_for_Power%22_Blu-Ray_Cover.jpeg',
                              'https://www.youtube.com/watch?v=Whv2IvGwMqw')

movies = [mummy_1, mummy_2, mummy_3, scorpion_king_1,
          scorpion_king_2, scorpion_king_3, scorpion_king_4]

fresh_mummy.open_movies_page(movies)
