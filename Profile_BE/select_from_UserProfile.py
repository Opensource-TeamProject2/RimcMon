import pymssql

def get_user_profile(user_id):
    connection = pymssql.connect(server="localhost:1433", user="sa", password="123aaa!@#", database="rmc_user")
    cursor = connection.cursor(as_dict=True)

    try:
        query = "SELECT user_name, user_bio, user_stack FROM UserProfile WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user_profile = cursor.fetchone()
        return user_profile
    except Exception as e:
        print(f"오류 발생: {e}")
        return None
    finally:
        cursor.close()
        connection.close()