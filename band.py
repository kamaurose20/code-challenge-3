from db import connect_db

class Band:
    @staticmethod
    def concerts(band_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM concerts WHERE band_id = ?", (band_id,))
        concerts = cur.fetchall()
        conn.close()
        return concerts

    @staticmethod
    def venues(band_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT venues.*
            FROM venues
            JOIN concerts ON venues.id = concerts.venue_id
            WHERE concerts.band_id = ?
        """, (band_id,))
        venues = cur.fetchall()
        conn.close()
        return venues

    @staticmethod
    def play_in_venue(band_id, venue_id, date):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)", (band_id, venue_id, date))
        conn.commit()
        conn.close()

    @staticmethod
    def all_introductions(band_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT venues.city, bands.name, bands.hometown
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.band_id = ?
        """, (band_id,))
        introductions = cur.fetchall()
        conn.close()
        return [f"Hello {city}!!!!! We are {band_name} and we're from {hometown}" for city, band_name, hometown in introductions]

    @staticmethod
    def most_performances():
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT bands.*, COUNT(concerts.id) as performance_count
            FROM bands
            JOIN concerts ON bands.id = concerts.band_id
            GROUP BY bands.id
            ORDER BY performance_count DESC
            LIMIT 1
        """)
        most_performed_band = cur.fetchone()
        conn.close()
        return most_performed_band
