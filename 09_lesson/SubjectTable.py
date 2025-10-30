from sqlalchemy import create_engine, text

class SubjectTable:
    __scripts = {
        "select": text("SELECT * FROM subject"),
        "delete_by_id": text("DELETE FROM subject WHERE subject_id = :id_to_delete"),
        "insert_new": text("INSERT INTO subject(subject_id, subject_title) VALUES (:new_id, :new_title)"),
        "get_max_id": text("SELECT MAX(subject_id) FROM subject"),
        "select_by_id": text("SELECT * FROM subject WHERE subject_id = :select_id"),
        "update_by_id": text("UPDATE subject SET subject_title = :new_title WHERE subject_id = :id_to_update")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def delete(self, subject_id):
        self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=subject_id)

    def create(self, subject_id, subject_title):
        self.__db.execute(self.__scripts["insert_new"],
                         new_id=subject_id,
                         new_title=subject_title)

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]

    def get_subject_by_id(self, subject_id):
        return self.__db.execute(self.__scripts["select_by_id"], select_id=subject_id).fetchall()

    def update(self, subject_id, new_title):
        self.__db.execute(self.__scripts["update_by_id"],
                         id_to_update=subject_id,
                         new_title=new_title)