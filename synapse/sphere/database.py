import psycopg2


class UserRole:
    # TODO: переписать так, чтобы принимал юзерайди, чтоб не было статичных методов.
    @staticmethod
    def if_guest_account(user_id):
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            user="synapse_user",
            password="GXWcwhwaOgQ2PSnjt0q3I7c2TnkB4SBl",
            database="synapse",
        )
        try:
            with connection.cursor() as cursor:
                select_query = (
                    """SELECT guest_account FROM users WHERE name = %s"""
                )
                cursor.execute(select_query, [user_id])
                result = cursor.fetchone()
                if result[0] == 1:
                    return True
                else:
                    return False
        except psycopg2.Error as e:
            print("PSYCOPG error", e)
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def if_moderator_account(user_id):
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            user="synapse_user",
            password="GXWcwhwaOgQ2PSnjt0q3I7c2TnkB4SBl",
            database="synapse",
        )
        try:
            with connection.cursor() as cursor:
                select_query = (
                    """SELECT * FROM moderation WHERE user_id = %s"""
                )
                cursor.execute(select_query, [user_id])
                result = cursor.fetchone()

                if result is not None:
                    return True
                else:
                    return False
        except psycopg2.Error as e:
            print("PSYCOPG error", e)
        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def make_guest(user_id):
        """Делаем юзера гостем после того, как прошла регистрация
        и добавлена комната с ботом"""
        pass


class RoomData:
    def __init__(self, room_id) -> None:
        self.room_id = room_id

    def creator(self):
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            user="synapse_user",
            password="GXWcwhwaOgQ2PSnjt0q3I7c2TnkB4SBl",
            database="synapse",
        )
        try:
            with connection.cursor() as cursor:
                select_query = (
                    """SELECT creator FROM rooms WHERE room_id = %s"""
                )
                cursor.execute(select_query, [self.room_id])
                result = cursor.fetchone()
                return result[0]
        except psycopg2.Error as e:
            print("PSYCOPG error", e)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def guest_room(self):
        connection = psycopg2.connect(
            host="localhost",
            port=5432,
            user="synapse_user",
            password="GXWcwhwaOgQ2PSnjt0q3I7c2TnkB4SBl",
            database="synapse",
        )
        try:
            with connection.cursor() as cursor:
                select_query = (
                    """SELECT * FROM guest_rooms WHERE room_id = %s"""
                )
                cursor.execute(select_query, [self.room_id])
                result = cursor.fetchone()

                if result is not None:
                    return True
                else:
                    return False
        except psycopg2.Error as e:
            print("PSYCOPG error", e)
        finally:
            if connection:
                cursor.close()
                connection.close()
