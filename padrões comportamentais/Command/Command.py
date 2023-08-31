# Receiver
class Database:
    def __init__(self):
        self.data = []

    def insert_record(self, record):
        self.data.append(record)
        print(f"Registro '{record}' inserido.")

    def delete_record(self, record):
        if record in self.data:
            self.data.remove(record)
            print(f"Registro '{record}' deletado.")
        else:
            print(f"Registro '{record}' não encontrado.")

# Command Interface
class Command:
    def execute(self):
        pass

# ConcreteCommand
class InsertCommand(Command):
    def __init__(self, database, record):
        self.database = database
        self.record = record

    def execute(self):
        self.database.insert_record(self.record)

# ConcreteCommand
class DeleteCommand(Command):
    def __init__(self, database, record):
        self.database = database
        self.record = record

    def execute(self):
        self.database.delete_record(self.record)

# Invoker
class DatabaseInvoker:
    def __init__(self, command):
        self.command = command

    def call(self):
        self.command.execute()

# Client
db = Database()
insert_cmd = InsertCommand(db, "Registro1")
delete_cmd = DeleteCommand(db, "Registro1")

invoker = DatabaseInvoker(insert_cmd)
invoker.call()

invoker = DatabaseInvoker(delete_cmd)
invoker.call()
