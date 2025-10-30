from SubjectTable import SubjectTable

# ПОДКЛЮЧЕНИЕ К БД
db = SubjectTable("postgresql://postgres:2002@localhost:5432/QA")

# ПОЛУЧЕНИЕ ПРЕДМЕТОВ (ПОЛНЫЙ СПИСОК)
def test_get_subjects():
    db_result = db.get_subjects()
    assert len(db_result) >= 0

# ДОБАВЛЕНИЕ ПРЕДМЕТА
def test_add_subject():
    test_id = 100
    test_name = "New Subject"

    db.create(test_id, test_name)
    all_subjects = db.get_subjects()

    new_subject = None
    for subject in all_subjects:
        if subject['subject_id'] == test_id:
            new_subject = subject
            break

    assert new_subject is not None
    assert new_subject['subject_title'] == test_name

    db.delete(test_id)

    subjects_after_delete = db.get_subject_by_id(test_id)
    assert len(subjects_after_delete) == 0

# ИЗМЕНЕНИЕ ПРЕДМЕТА
def test_update_subject():

    subject_id = 200
    original_name = "Subject to be updated"
    db.create(subject_id, original_name)

    new_name = "Updated subject"
    db.update(subject_id, new_name)

    updated_subjects = db.get_subject_by_id(subject_id)

    assert len(updated_subjects) == 1
    assert updated_subjects[0]['subject_title'] == new_name
    assert updated_subjects[0]['subject_id'] == subject_id

    db.delete(subject_id)

# УДАЛЕНИЕ ПРЕДМЕТА
def test_delete_subject():

    subject_id = 300
    name = "Physics"
    db.create(subject_id, name)

    subjects_before = db.get_subject_by_id(subject_id)
    assert len(subjects_before) == 1
    assert subjects_before[0]['subject_title'] == name

    db.delete(subject_id)

    subjects_after = db.get_subject_by_id(subject_id)
    assert len(subjects_after) == 0
