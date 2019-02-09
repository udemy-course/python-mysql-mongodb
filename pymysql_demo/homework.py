# title, title_year, director_name, actor_1_name, actor_2_name, duration, country, content_rating, gross, imdb_score

movie_list = [
    ("Avatar", 2009, "James Cameron", "CCH Pounder", "Joel David Moore", 178, "USA", "PG-13", 760505847, 7.9),
    ("Pirates of the Caribbean: At World's End", 2007, "Gore Verbinski", "Johnny Depp", "Orlando Bloom", 169, "USA", "PG-13", 309404152, 7.1),
    ("Spectre", 2015, "Sam Mendes", "Christoph Waltz", "Rory Kinnear", 148, "UK", "PG-13", 200074175, 6.8),
    ("The Dark Knight Rises", 2012, "Christopher Nolan", "Tom Hardy", "Christian Bale", 164, "USA", "PG-13", 448130642, 8.5),
    ("John Carter", 2012, "Andrew Stanton", "Daryl Sabara", "Samantha Morton", 132, "USA", "PG-13", 73058679, 6.6),
    ("Spider-Man 3", 2007, "Sam Raimi", "J.K. Simmons", "James Franco", 156, "USA", "PG-13", 336530303, 6.2),
    ("Tangled", 2010, "Nathan Greno", "Brad Garrett", "Donna Murphy", 100, "USA", "PG", 200807262, 7.8),
    ("Avengers: Age of Ultron", 2015, "Joss Whedon", "Chris Hemsworth", "Robert Downey Jr.", 141, "USA", "PG-13", 458991599, 7.5),
    ("Harry Potter and the Half-Blood Prince", 2009, "David Yates", "Alan Rickman", "Daniel Radcliffe", 153, "UK", "PG", 301956980, 7.5),
    ("Batman v Superman: Dawn of Justice", 2016, "Zack Snyder", "Henry Cavill", "Lauren Cohan", 183, "USA", "PG-13", 330249062, 6.9),
    ("Superman Returns", 2006, "Bryan Singer", "Kevin Spacey", "Marlon Brando", 169, "USA", "PG-13", 200069408, 6.1),
    ("Quantum of Solace", 2008, "Marc Forster", "Giancarlo Giannini", "Mathieu Amalric", 106, "UK", "PG-13", 168368427, 6.7),
    ("Pirates of the Caribbean: Dead Man's Chest", 2006, "Gore Verbinski", "Johnny Depp", "Orlando Bloom", 151, "USA", "PG-13", 423032628, 7.3),
    ("The Lone Ranger", 2013, "Gore Verbinski", "Johnny Depp", "Ruth Wilson", 150, "USA", "PG-13", 89289910, 6.5),
    ("Man of Steel", 2013, "Zack Snyder", "Henry Cavill", "Christopher Meloni", 143, "USA", "PG-13", 291021565, 7.2),
    ("The Chronicles of Narnia: Prince Caspian", 2008, "Andrew Adamson", "Peter Dinklage", "Pierfrancesco Favino", 150, "USA", "PG", 141614023, 6.6),
    ("The Avengers", 2012, "Joss Whedon", "Chris Hemsworth", "Robert Downey Jr.", 173, "USA", "PG-13", 623279547, 8.1),
    ("Pirates of the Caribbean: On Stranger Tides", 2011, "Rob Marshall", "Johnny Depp", "Sam Claflin", 136, "USA", "PG-13", 241063875, 6.7),
    ("Men in Black 3", 2012, "Barry Sonnenfeld", "Will Smith", "Michael Stuhlbarg", 106, "USA", "PG-13", 179020854, 6.8),
    ("The Hobbit: The Battle of the Five Armies", 2014, "Peter Jackson", "Aidan Turner", "Adam Brown", 164, "New Zealand", "PG-13", 255108370, 7.5),
    ("The Amazing Spider-Man", 2012, "Marc Webb", "Emma Stone", "Andrew Garfield", 153, "USA", "PG-13", 262030663, 7),
    ("Robin Hood", 2010, "Ridley Scott", "Mark Addy", "William Hurt", 156, "USA", "PG-13", 105219735, 6.7),
    ("The Hobbit: The Desolation of Smaug", 2013, "Peter Jackson", "Aidan Turner", "Adam Brown", 186, "USA", "PG-13", 258355354, 7.9),
    ("The Golden Compass", 2007, "Chris Weitz", "Christopher Lee", "Eva Green", 113, "USA", "PG-13", 70083519, 6.1),
    ("King Kong", 2005, "Peter Jackson", "Naomi Watts", "Thomas Kretschmann", 201, "New Zealand", "PG-13", 218051260, 7.2),
    ("Titanic", 1997, "James Cameron", "Leonardo DiCaprio", "Kate Winslet", 194, "USA", "PG-13", 658672302, 7.7),
    ("Captain America: Civil War", 2016, "Anthony Russo", "Robert Downey Jr.", "Scarlett Johansson", 147, "USA", "PG-13", 407197282, 8.2),
    ("Battleship", 2012, "Peter Berg", "Liam Neeson", "Alexander Skarsgård", 131, "USA", "PG-13", 65173160, 5.9),
    ("Jurassic World", 2015, "Colin Trevorrow", "Bryce Dallas Howard", "Judy Greer", 124, "USA", "PG-13", 652177271, 7),
    ("Skyfall", 2012, "Sam Mendes", "Albert Finney", "Helen McCrory", 143, "UK", "PG-13", 304360277, 7.8),
    ("Spider-Man 2", 2004, "Sam Raimi", "J.K. Simmons", "James Franco", 135, "USA", "PG-13", 373377893, 7.3),
    ("Iron Man 3", 2013, "Shane Black", "Robert Downey Jr.", "Jon Favreau", 195, "USA", "PG-13", 408992272, 7.2),
    ("Alice in Wonderland", 2010, "Tim Burton", "Johnny Depp", "Alan Rickman", 108, "USA", "PG", 334185206, 6.5),
    ("X-Men: The Last Stand", 2006, "Brett Ratner", "Hugh Jackman", "Kelsey Grammer", 104, "Canada", "PG-13", 234360014, 6.8),
    ("Monsters University", 2013, "Dan Scanlon", "Steve Buscemi", "Tyler Labine", 104, "USA", "G", 268488329, 7.3),
    ("Transformers: Revenge of the Fallen", 2009, "Michael Bay", "Glenn Morshower", "Kevin Dunn", 150, "USA", "PG-13", 402076689, 6),
    ("Transformers: Age of Extinction", 2014, "Michael Bay", "Bingbing Li", "Sophia Myles", 165, "USA", "PG-13", 245428137, 5.7),
    ("Oz the Great and Powerful", 2013, "Sam Raimi", "Tim Holmes", "Mila Kunis", 130, "USA", "PG", 234903076, 6.4),
    ("The Amazing Spider-Man 2", 2014, "Marc Webb", "Emma Stone", "Andrew Garfield", 142, "USA", "PG-13", 202853933, 6.7),
    ("TRON: Legacy", 2010, "Joseph Kosinski", "Jeff Bridges", "Olivia Wilde", 125, "USA", "PG", 172051787, 6.8),
    ("Cars 2", 2011, "John Lasseter", "Joe Mantegna", "Thomas Kretschmann", 106, "USA", "G", 191450875, 6.3),
    ("Green Lantern", 2011, "Martin Campbell", "Ryan Reynolds", "Temuera Morrison", 123, "USA", "PG-13", 116593191, 5.6),
    ("Toy Story 3", 2010, "Lee Unkrich", "Tom Hanks", "John Ratzenberger", 103, "USA", "G", 414984497, 8.3),
    ("Terminator Salvation", 2009, "McG", "Christian Bale", "Bryce Dallas Howard", 118, "USA", "PG-13", 125320003, 6.6),
    ("Furious 7", 2015, "James Wan", "Jason Statham", "Paul Walker", 140, "USA", "PG-13", 350034110, 7.2),
    ("World War Z", 2013, "Marc Forster", "Peter Capaldi", "Brad Pitt", 123, "USA", "PG-13", 202351611, 7),
    ("X-Men: Days of Future Past", 2014, "Bryan Singer", "Jennifer Lawrence", "Peter Dinklage", 149, "USA", "PG-13", 233914986, 8),
    ("Star Trek Into Darkness", 2013, "J.J. Abrams", "Benedict Cumberbatch", "Bruce Greenwood", 132, "USA", "PG-13", 228756232, 7.8),
    ("Jack the Giant Slayer", 2013, "Bryan Singer", "Eddie Marsan", "Ewen Bremner", 114, "USA", "PG-13", 65171860, 6.3),
    ("The Great Gatsby", 2013, "Baz Luhrmann", "Leonardo DiCaprio", "Elizabeth Debicki", 143, "Australia", "PG-13", 144812796, 7.3),
    ("Prince of Persia: The Sands of Time", 2010, "Mike Newell", "Jake Gyllenhaal", "Richard Coyle", 116, "USA", "PG-13", 90755643, 6.6),
    ("Pacific Rim", 2013, "Guillermo del Toro", "Charlie Hunnam", "Clifton Collins Jr.", 131, "USA", "PG-13", 101785482, 7),
    ("Transformers: Dark of the Moon", 2011, "Michael Bay", "Glenn Morshower", "Lester Speight", 154, "USA", "PG-13", 352358779, 6.3),
    ("Indiana Jones and the Kingdom of the Crystal Skull", 2008, "Steven Spielberg", "Harrison Ford", "Ray Winstone", 122, "USA", "PG-13", 317011114, 6.2),
    ("The Good Dinosaur", 2015, "Peter Sohn", "A.J. Buckley", "Jack McGraw", 93, "USA", "PG", 123070338, 6.8),
    ("Brave", 2012, "Mark Andrews", "Kelly Macdonald", "John Ratzenberger", 93, "USA", "PG", 237282182, 7.2),
    ("Star Trek Beyond", 2016, "Justin Lin", "Sofia Boutella", "Melissa Roxburgh", 122, "USA", "PG-13", 130468626, 7.5),
    ("WALL·E", 2008, "Andrew Stanton", "John Ratzenberger", "Fred Willard", 98, "USA", "G", 223806889, 8.4),
    ("Rush Hour 3", 2007, "Brett Ratner", "Tzi Ma", "Dana Ivey", 91, "USA", "PG-13", 140080850, 6.2),
    ("2012", 2009, "Roland Emmerich", "Oliver Platt", "Liam James", 158, "USA", "PG-13", 166112167, 5.8),
    ("A Christmas Carol", 2009, "Robert Zemeckis", "Robin Wright", "Colin Firth", 96, "USA", "PG", 137850096, 6.8),
    ("Jupiter Ascending", 2015, "Lana Wachowski", "Channing Tatum", "Mila Kunis", 127, "USA", "PG-13", 47375327, 5.4),
    ("The Legend of Tarzan", 2016, "David Yates", "Christoph Waltz", "Alexander Skarsgård", 110, "USA", "PG-13", 124051759, 6.6),
    ("The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", 2005, "Andrew Adamson", "Jim Broadbent", "Kiran Shah", 150, "USA", "PG", 291709845, 6.9),
    ("X-Men: Apocalypse", 2016, "Bryan Singer", "Jennifer Lawrence", "Michael Fassbender", 144, "USA", "PG-13", 154985087, 7.3),
    ("The Dark Knight", 2008, "Christopher Nolan", "Christian Bale", "Heath Ledger", 152, "USA", "PG-13", 533316061, 9),
    ("Up", 2009, "Pete Docter", "John Ratzenberger", "Delroy Lindo", 96, "USA", "PG", 292979556, 8.3),
    ("Monsters vs. Aliens", 2009, "Rob Letterman", "Amy Poehler", "Rainn Wilson", 94, "USA", "PG", 198332128, 6.5),
    ("Iron Man", 2008, "Jon Favreau", "Robert Downey Jr.", "Jeff Bridges", 126, "USA", "PG-13", 318298180, 7.9),
    ("Hugo", 2011, "Martin Scorsese", "Chloe Grace Moretz", "Christopher Lee", 126, "USA", "PG", 73820094, 7.5),
    ("Wild Wild West", 1999, "Barry Sonnenfeld", "Will Smith", "Salma Hayek", 106, "USA", "PG-13", 113745408, 4.8),
    ("The Mummy: Tomb of the Dragon Emperor", 2008, "Rob Cohen", "Jet Li", "Brendan Fraser", 112, "USA", "PG-13", 102176165, 5.2),
    ("Suicide Squad", 2016, "David Ayer", "Will Smith", "Robin Atkin Downes", 123, "USA", "PG-13", 161087183, 6.9),
    ("Evan Almighty", 2007, "Tom Shadyac", "Jimmy Bennett", "Morgan Freeman", 96, "USA", "PG", 100289690, 5.4),
    ("Edge of Tomorrow", 2014, "Doug Liman", "Tom Cruise", "Lara Pulver", 113, "USA", "PG-13", 100189501, 7.9),
    ("Waterworld", 1995, "Kevin Reynolds", "Jeanne Tripplehorn", "Rick Aviles", 176, "USA", "PG-13", 88246220, 6.1),
    ("G.I. Joe: The Rise of Cobra", 2009, "Stephen Sommers", "Joseph Gordon-Levitt", "Dennis Quaid", 118, "USA", "PG-13", 150167630, 5.8),
    ("Inside Out", 2015, "Pete Docter", "Amy Poehler", "Mindy Kaling", 95, "USA", "PG", 356454367, 8.3),
    ("The Jungle Book", 2016, "Jon Favreau", "Scarlett Johansson", "Bill Murray", 106, "UK", "PG", 362645141, 7.8),
    ("Iron Man 2", 2010, "Jon Favreau", "Robert Downey Jr.", "Scarlett Johansson", 124, "USA", "PG-13", 312057433, 7),
    ("Snow White and the Huntsman", 2012, "Rupert Sanders", "Chris Hemsworth", "Kristen Stewart", 132, "USA", "PG-13", 155111815, 6.1),
    ("Maleficent", 2014, "Robert Stromberg", "Angelina Jolie Pitt", "Sharlto Copley", 97, "USA", "PG", 241407328, 7),
    ("Dawn of the Planet of the Apes", 2014, "Matt Reeves", "Gary Oldman", "Judy Greer", 130, "USA", "PG-13", 208543795, 7.6),
    ("47 Ronin", 2013, "Carl Rinsch", "Keanu Reeves", "Cary-Hiroyuki Tagawa", 128, "USA", "PG-13", 38297305, 6.3),
    ("Captain America: The Winter Soldier", 2014, "Anthony Russo", "Scarlett Johansson", "Chris Evans", 136, "USA", "PG-13", 259746958, 7.8),
    ("Shrek Forever After", 2010, "Mike Mitchell", "Jon Hamm", "Kathy Griffin", 93, "USA", "PG", 238371987, 6.4),
    ("Tomorrowland", 2015, "Brad Bird", "Judy Greer", "Chris Bauer", 130, "USA", "PG", 93417865, 6.5),
    ("Inception", 2010, "Christopher Nolan", "Leonardo DiCaprio", "Tom Hardy", 148, "USA", "PG-13", 292568851, 8.8),
    ("Big Hero 6", 2014, "Don Hall", "Damon Wayans Jr.", "Daniel Henney", 102, "USA", "PG", 222487711, 7.9),
    ("Wreck-It Ralph", 2012, "Rich Moore", "Jack McBrayer", "Sarah Silverman", 101, "USA", "PG", 189412677, 7.8),
    ("The Polar Express", 2004, "Robert Zemeckis", "Tom Hanks", "Eddie Deezen", 100, "USA", "G", 665426, 6.6),
    ("Independence Day: Resurgence", 2016, "Roland Emmerich", "Vivica A. Fox", "Sela Ward", 120, "USA", "PG-13", 102315545, 5.5),
    ("How to Train Your Dragon", 2010, "Dean DeBlois", "Gerard Butler", "America Ferrera", 98, "USA", "PG", 217387997, 8.2),
    ("Terminator 3: Rise of the Machines", 2003, "Jonathan Mostow", "Nick Stahl", "M.C. Gainey", 109, "USA", "R", 150350192, 6.4),
    ("Guardians of the Galaxy", 2014, "James Gunn", "Bradley Cooper", "Vin Diesel", 121, "USA", "PG-13", 333130696, 8.1),
    ("Interstellar", 2014, "Christopher Nolan", "Matthew McConaughey", "Anne Hathaway", 169, "USA", "PG-13", 187991439, 8.6),
    ("Australia", 2008, "Baz Luhrmann", "Essie Davis", "Bryan Brown", 165, "Australia", "PG-13", 49551662, 6.6),
    ("Warcraft", 2016, "Duncan Jones", "Dominic Cooper", "Callum Rennie", 123, "USA", "PG-13", 46978995, 7.3),
    ("X-Men: First Class", 2011, "Matthew Vaughn", "Jennifer Lawrence", "Michael Fassbender", 132, "USA", "PG-13", 146405371, 7.8),
    ("The Hobbit: An Unexpected Journey", 2012, "Peter Jackson", "Aidan Turner", "Adam Brown", 182, "USA", "PG-13", 303001229, 7.9)
]

"""

CREATE TABLE IF NOT EXISTS movie(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    title_year INT NOT NULL,
    director_name VARCHAR(50) NOT NULL,
    actor_1_name VARCHAR(50) NOT NULL,
    actor_2_name VARCHAR(50) NOT NULL,
    duration INT NOT NULL,
    country VARCHAR(50) NOT NULL,
    content_rating VARCHAR(10) NOT NULL,
    gross BIGINT NOT NULL,
    imdb_score FLOAT DEFAULT 0
);

"""

#------------------------------------------------------------
#                     answer
#------------------------------------------------------------

import pymysql

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='demo'
)

cursor = connection.cursor()

# table create

sql = """CREATE TABLE IF NOT EXISTS movie(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    title_year INT NOT NULL,
    director_name VARCHAR(50) NOT NULL,
    actor_1_name VARCHAR(50) NOT NULL,
    actor_2_name VARCHAR(50) NOT NULL,
    duration INT NOT NULL,
    country VARCHAR(50) NOT NULL,
    content_rating VARCHAR(10) NOT NULL,
    gross BIGINT NOT NULL,
    imdb_score FLOAT DEFAULT 0)
"""
cursor.execute(sql)
connection.commit()

# insert data into table

sql = """INSERT INTO 
movie(
    title, title_year, director_name, actor_1_name,
    actor_2_name, duration, country, content_rating, gross, imdb_score
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
for movie in movie_list:
    cursor.execute(sql, movie)
connection.commit()
connection.close()
