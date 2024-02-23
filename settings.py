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

SECRET_KEY = 'cJ0QPNT_le6pqN5eTO7gNMkj8kDpEJWRTRFVm42H-io'

ALLOWED_PARAMS_PROPERTY_FILTER = {
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
                            FROM 
                                property p
                            JOIN 
                                status_history sh ON p.id = sh.property_id
                            JOIN 
                                status s ON sh.status_id = s.id
                            JOIN
                                (SELECT property_id, MAX(update_date) AS max_update_date
                                FROM status_history
                                GROUP BY property_id) latest_sh
                            ON
                                sh.property_id = latest_sh.property_id
                                AND sh.update_date = latest_sh.max_update_date """
