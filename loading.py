import os
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

# ============================================================
# Configuration
# ============================================================
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "maheen")
DB_HOST = os.getenv("POSTGRES_HOST", "localhost")
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "api_data_pipeline")

TABLE_NAME = "traffic_incidents"

INPUT_FILE = "calgary_traffic_incidents.xlsx"


def load_data():
    """Load transformed Calgary traffic incident data into PostgreSQL."""

    # Read transformed Excel data
    df = pd.read_excel(INPUT_FILE)

    # Clean column names for PostgreSQL
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Convert timestamp columns
    for column in ["recorded", "last_updated"]:
        if column in df.columns:
            df[column] = pd.to_datetime(df[column], errors="coerce")

    # Convert numeric columns
    for column in ["longitude", "latitude", "incident_count", "year", "day"]:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column], errors="coerce")

    # Remove duplicate incident IDs before loading
    if "incident_id" in df.columns:
        df = df.drop_duplicates(subset=["incident_id"])

    # PostgreSQL connection
    connection_string = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(connection_string)

    try:
        with engine.begin() as connection:

            # Create table if it does not already exist
            connection.execute(text(f"""
                CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                    location TEXT,
                    description TEXT,
                    recorded TIMESTAMP,
                    last_updated TIMESTAMP,
                    quadrant VARCHAR(2),
                    longitude DOUBLE PRECISION,
                    latitude DOUBLE PRECISION,
                    incident_count INTEGER,
                    incident_id TEXT PRIMARY KEY,
                    point TEXT,
                    year INTEGER,
                    month VARCHAR(20),
                    day INTEGER
                );
            """))

            # Insert records while ignoring duplicate incident IDs
            for _, row in df.iterrows():
                connection.execute(text(f"""
                    INSERT INTO {TABLE_NAME} (
                        location,
                        description,
                        recorded,
                        last_updated,
                        quadrant,
                        longitude,
                        latitude,
                        incident_count,
                        incident_id,
                        point,
                        year,
                        month,
                        day
                    )
                    VALUES (
                        :location,
                        :description,
                        :recorded,
                        :last_updated,
                        :quadrant,
                        :longitude,
                        :latitude,
                        :incident_count,
                        :incident_id,
                        :point,
                        :year,
                        :month,
                        :day
                    )
                    ON CONFLICT (incident_id) DO NOTHING;
                """), row.to_dict())

        print(f"Successfully processed {len(df)} records.")
        print(f"Data loaded into PostgreSQL table: {TABLE_NAME}")

    except SQLAlchemyError as e:
        print("Database error occurred:")
        print(e)

    finally:
        engine.dispose()


if __name__ == "__main__":
    load_data()
