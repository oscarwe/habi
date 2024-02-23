# UNVERSIONED FILE
# Database connection data for MySQL
# Note: Hardcoding sensitive data like database credentials in the code is not secure.
# For production use, consider storing these credentials in environment variables
# or using a secrets manager service provided by your cloud provider.

DB_CONFIG = {
    'host': '3.138.156.32',
    'port': '3309',
    'user': 'pruebas',
    'password': 'VGbt3Day5R',
    'database': 'habi_db'
}

SECRET_KEY = 'zr-OhBswJ-Cn3FOhILCmAYMomNimOlDvtYjrV_3N3LQ'

ALLOWED_PARAMS_PROPERY_FILTER = {
    'city': 'p',   # city belongs to the property table (p)
    'state': 's',  # state belongs to the status table (s)
    'year': 'p'    # year belongs to the property table (p)
}

FILTER_PROPERTY_QUERY = """ SELECT 
                            p.address AS direccion,
                            p.city AS ciudad, 
                            s.name AS estado, 
                            p.price AS precio, 
                            p.description AS descripcion 
                            FROM status_history sh
                            JOIN status s ON sh.status_id = s.id 
                            JOIN property p ON sh.property_id = p.id 
                            WHERE s.name IN ('pre_venta', 'en_venta', 'vendido') """
