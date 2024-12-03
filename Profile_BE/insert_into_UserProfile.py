import pymssql

def update_user_stack(user_id, new_stack):
    connection = pymssql.connect(server="localhost:1433", user="sa", password="123aaa!@#", database="rmc_user", charset="utf8")
    cursor = connection.cursor()

    try:
        query = """
        UPDATE UserProfile
        SET user_stack = %s
        WHERE user_id = %s
        """
        cursor.execute(query, (new_stack, user_id))
        connection.commit()
        print("스택이 성공적으로 업데이트되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        cursor.close()
        connection.close()

def update_user_bio(user_id, new_bio):
    connection = pymssql.connect(server="localhost:1433", user="sa", password="123aaa!@#", database="rmc_user", charset="utf8")
    cursor = connection.cursor()

    try:
        query = """
        UPDATE UserProfile
        SET user_bio = %s
        WHERE user_id = %s
        """
        cursor.execute(query, (new_bio, user_id))
        connection.commit()
        print("자기소개가 성공적으로 업데이트되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        cursor.close()
        connection.close()