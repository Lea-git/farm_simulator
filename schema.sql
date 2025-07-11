CREATE TABLE IF NOT EXISTS fields (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER,
    state TEXT,
    crop_type TEXT,
    lot INTEGER
);

CREATE TABLE IF NOT EXISTS machines (
    name TEXT PRIMARY KEY,
    total_units INTEGER
);

CREATE TABLE IF NOT EXISTS storage (
    item TEXT PRIMARY KEY,
    quantity INTEGER
);

CREATE TABLE IF NOT EXISTS crops (
    name TEXT PRIMARY KEY,
    growth_time INTEGER,
    yield_per_field INTEGER
);

CREATE TABLE IF NOT EXISTS factories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_type TEXT,
    output_type TEXT,
    multiplier REAL
);
