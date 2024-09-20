from db import connect_db

class Concert:
    @staticmethod
    def band(concert_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM bands WHERE id = (SELECT band_id FROM concerts WHERE id = ?)", (concert_id,))
        band = cur.fetchone()
        conn.close()
        return band

    @staticmethod
    def venue(concert_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM venues WHERE id = (SELECT venue_id FROM concerts WHERE id = ?)", (concert_id,))
        venue = cur.fetchone()
        conn.close()
        return venue

    @staticmethod
    def hometown_show(concert_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT concerts.id
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ? AND bands.hometown = venues.city
        """, (concert_id,))
        hometown_show = cur.fetchone()
        conn.close()
        return hometown_show is not None

    @staticmethod
    def introduction(concert_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT bands.name, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        """, (concert_id,))
        result = cur.fetchone()
        conn.close()
        if result:
            band_name, hometown, city = result
            return f"Hello {city}!!!!! We are {band_name} and we're from {hometown}"
        return None
