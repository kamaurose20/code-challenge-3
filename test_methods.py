def test_methods():
    from band import Band
    from venue import Venue
    from concert import Concert
    
    band = Concert.band(1)
    print("Band for Concert 1:", band)
    
    venue = Concert.venue(1)
    print("Venue for Concert 1:", venue)
    
    concerts_at_venue = Venue.concerts(1)
    print("Concerts at Venue 1:", concerts_at_venue)
    
    bands_at_venue = Venue.bands(1)
    print("Bands at Venue 1:", bands_at_venue)
    
    concerts_for_band = Band.concerts(1)
    print("Concerts for Band 1:", concerts_for_band)
    
    venues_for_band = Band.venues(1)
    print("Venues for Band 1:", venues_for_band)
    
    Band.play_in_venue(1, 2, '2024-12-03')
    print("Concerts for Band 1 after new concert:", Band.concerts(1))
    
    is_hometown_show = Concert.hometown_show(1)
    print("Is Concert 1 in hometown?", is_hometown_show)
    
    intro = Concert.introduction(1)
    print("Introduction for Concert 1:", intro)

if __name__ == "__main__":
    test_methods()
