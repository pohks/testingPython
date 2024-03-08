import requests
import pymysql

# Vulnerable library - pymysql (vulnerable to SQL injection if not used properly)
# Assuming there's a local MySQL database running with a table named 'users' having 'username' and 'password' columns

def fetch_data_from_database(username):
    # Establishing connection to the local MySQL database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='password',
                                 database='test_db',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
    try:
        with connection.cursor() as cursor:
            # Vulnerability: SQL Injection
            sql = f"SELECT * FROM users WHERE username = '{username}'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def fetch_url_content(url):
    try:
        # Vulnerability: SSRF
        response = requests.get(url)
        return response.text
    except Exception as e:
        return str(e)

def main():
    # Example usage with user input
    username = input("Enter username: ")

    # Fetching user data from the database
    user_data = fetch_data_from_database(username)
    if user_data:
        print("User data:", user_data)
    else:
        print("User not found.")

    # Example of SSRF vulnerability
    internal_url = 'http://localhost:8080/internal_data'
    internal_data = fetch_url_content(internal_url)
    print("Internal data:", internal_data)

if __name__ == "__main__":
    main()