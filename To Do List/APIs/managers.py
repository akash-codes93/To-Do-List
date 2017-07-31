
from helper_methods import insert_query, list_query, delete_query


def create_task(name, desc):

    message = None

    query = "Insert into to_do_list.task_information (task_name, task_description) values (\"{0}\",\"{1}\");".format(name,desc)

    data = insert_query(query)

    if data == 1:
        message = "Task successfully created"

    else:
        message = data

    return message


def list_task():

    query = "select * from to_do_list.task_information;"

    data = list_query(query)

    return data


def delete_task(id):

    query = "Delete from to_do_list.task_information where task_id =\"{0}\" ;".format(id)

    data = delete_query(query)

    if data == 1:
        message = "Task successfully deleted"

    elif data ==0:
        message = "Task already deleted"

    else:
        message = data

    return message
