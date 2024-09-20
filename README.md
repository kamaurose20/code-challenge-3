### Concert code challenge
This project models a Concert Domain with three primary entities: Band, Venue, and Concert. These entities are connected using raw SQL queries through Python.

## Overview
- Band: Represents a musical band with attributes like name and hometown.
- Venue: Represents a venue where concerts are held, with attributes like title and city.
- Concert: Links Bands and Venues, representing concerts with an associated date.
- Database Schema
The database contains the following tables:

### Bands Table:

- id (Primary Key)
- name (String)
- hometown (String)

### Venues Table:
- id (Primary Key)
- title (String)
- city (String)
### Concerts Table:

- id (Primary Key)
- band_id (Foreign Key, references bands.id)
- venue_id (Foreign Key, references venues.id)
- date (String)

## Instructions
1. Clone the Repository
2. Run Tests

## Usage
### Band Class Methods
Band.concerts(band_id): Returns all concerts for the specified band.
Band.venues(band_id): Returns all venues where the band has performed.
Band.play_in_venue(venue_id, date): Creates a new concert for the band at the specified venue.
Band.all_introductions(): Returns all introduction strings for the band.
Band.most_performances(): Returns the band with the most concerts.

### Venue Class Methods
Venue.concerts(venue_id): Returns all concerts at the specified venue.
Venue.bands(venue_id): Returns all bands that have performed at the specified venue.
Venue.concert_on(date): Returns the first concert on the given date at the venue.
Venue.most_frequent_band(): Returns the band that has performed the most at the venue.

### Concert Class Methods
Concert.band(concert_id): Returns the band for the specified concert.
Concert.venue(concert_id): Returns the venue for the specified concert.
Concert.hometown_show(concert_id): Returns True if the concert is a hometown show, otherwise False.
Concert.introduction(concert_id): Returns the band’s introduction for the concert.
# code-challenge-3
