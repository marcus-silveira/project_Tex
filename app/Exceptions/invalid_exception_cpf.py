class InvalidCPFError(Exception):
    def __init__(self, message="CPF inválido"):
        self.message = message
        super().__init__(self.message)
