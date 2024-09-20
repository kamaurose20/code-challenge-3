from db import connect_db

class Venue:
    @staticmethod
    def concerts(venue_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM concerts WHERE venue_id = ?", (venue_id,))
        concerts = cur.fetchall()
        conn.close()
        return concerts

    @staticmethod
    def bands(venue_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT bands.*
            FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
        """, (venue_id,))
        bands = cur.fetchall()
        conn.close()
        return bands

    @staticmethod
    def concert_on(venue_id, date):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM concerts WHERE venue_id = ? AND date = ?", (venue_id, date))
        concert = cur.fetchone()
        conn.close()
        return concert

    @staticmethod
    def most_frequent_band(venue_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT bands.*, COUNT(concerts.id) AS concert_count
            FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            WHERE concerts.venue_id = ?
            GROUP BY bands.id
            ORDER BY concert_count DESC
            LIMIT 1
        """, (venue_id,))
        band = cur.fetchone()
        conn.close()
        return band
