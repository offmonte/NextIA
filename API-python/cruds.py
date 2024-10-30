import cx_Oracle

def get_connection():
    try:
        connection = cx_Oracle.connect(
            user="RM551604",
            password="121102",
            dsn="oracle.fiap.com:1521/ORCL"
        )
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None

def create_cliente(cpf, nome, pontos=0):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO Clientes (CPF, nome, pontos) VALUES (:cpf, :nome, :pontos)",
                {"cpf": cpf, "nome": nome, "pontos": pontos}
            )
            connection.commit()
            print("Cliente inserido com sucesso!")
        except cx_Oracle.DatabaseError as e:
            print("Erro ao inserir cliente:", e)
        finally:
            cursor.close()
            connection.close()

def read_cliente(id_cliente):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Clientes WHERE id_cliente = :id_cliente", {"id_cliente": id_cliente})
            cliente = cursor.fetchone()
            print("Cliente:", cliente)
            return cliente
        except cx_Oracle.DatabaseError as e:
            print("Erro ao consultar cliente:", e)
        finally:
            cursor.close()
            connection.close()

def update_cliente(id_cliente, cpf=None, nome=None, pontos=None):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            update_fields = []
            params = {"id_cliente": id_cliente}
            if cpf:
                update_fields.append("CPF = :cpf")
                params["cpf"] = cpf
            if nome:
                update_fields.append("nome = :nome")
                params["nome"] = nome
            if pontos is not None:
                update_fields.append("pontos = :pontos")
                params["pontos"] = pontos

            query = f"UPDATE Clientes SET {', '.join(update_fields)} WHERE id_cliente = :id_cliente"
            cursor.execute(query, params)
            connection.commit()
            print("Cliente atualizado com sucesso!")
        except cx_Oracle.DatabaseError as e:
            print("Erro ao atualizar cliente:", e)
        finally:
            cursor.close()
            connection.close()

def delete_cliente(id_cliente):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Clientes WHERE id_cliente = :id_cliente", {"id_cliente": id_cliente})
            connection.commit()
            print("Cliente removido com sucesso!")
        except cx_Oracle.DatabaseError as e:
            print("Erro ao remover cliente:", e)
        finally:
            cursor.close()
            connection.close()

def create_recompensa(tipo_recompensa, descricao, data_resgate, id_cliente=None):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO Recompensas (tipo_recompensa, descricao, data_resgate, id_cliente)
                VALUES (:tipo_recompensa, :descricao, :data_resgate, :id_cliente)
                """,
                {"tipo_recompensa": tipo_recompensa, "descricao": descricao, "data_resgate": data_resgate, "id_cliente": id_cliente}
            )
            connection.commit()
            print("Recompensa inserida com sucesso!")
        except cx_Oracle.DatabaseError as e:
            print("Erro ao inserir recompensa:", e)
        finally:
            cursor.close()
            connection.close()

def read_recompensa(id_recompensa):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Recompensas WHERE id_recompensa = :id_recompensa", {"id_recompensa": id_recompensa})
            recompensa = cursor.fetchone()
            print("Recompensa:", recompensa)
            return recompensa
        except cx_Oracle.DatabaseError as e:
            print("Erro ao consultar recompensa:", e)
        finally:
            cursor.close()
            connection.close()

def update_recompensa(id_recompensa, tipo_recompensa=None, descricao=None, data_resgate=None, id_cliente=None):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            update_fields = []
            params = {"id_recompensa": id_recompensa}
            if tipo_recompensa:
                update_fields.append("tipo_recompensa = :tipo_recompensa")
                params["tipo_recompensa"] = tipo_recompensa
            if descricao:
                update_fields.append("descricao = :descricao")
                params["descricao"] = descricao
            if data_resgate:
                update_fields.append("data_resgate = :data_resgate")
                params["data_resgate"] = data_resgate
            if id_cliente is not None:
                update_fields.append("id_cliente = :id_cliente")
                params["id_cliente"] = id_cliente

            query = f"UPDATE Recompensas SET {', '.join(update_fields)} WHERE id_recompensa = :id_recompensa"
            cursor.execute(query, params)
            connection.commit()
            print("Recompensa atualizada com sucesso!")
        except cx_Oracle.DatabaseError as e:
            print("Erro ao atualizar recompensa:", e)
        finally:
            cursor.close()
            connection.close()

def delete_recompensa(id_recompensa):
    connection = get_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Recompensas WHERE id_recompensa = :id_recompensa", {"id_recompensa": id_recompensa})
            connection.commit()
            print("Recompensa removida com sucesso!")
        except cx_Oracle.DatabaseError as e:
            print("Erro ao remover recompensa:", e)
        finally:
            cursor.close()
            connection.close()
