#!python3.8.0
# -*-encoding:utf-8-*-


class Router:
    METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

    def __init__(self):
        self.storage = {}
        self.path_storage = set('')

    def __getattr__(self, attr):
        if attr.upper() in self.METHODS:
            return lambda path: self.request(attr.upper(), path)
        return f"Method {attr} is not defined for {self}"

    def add_path(self, path, method, func):
        self.path_storage.add(path)

        if (method, path) in self.storage.keys():
            if ((method, path), func) in self.storage.items():
                return f"Path {path} already associated with method {method}"
            else:
                self.storage.update([((method, path), func)])
                return f"Method {method} added  for path {path}"

        else:
            self.storage.update([((method, path), func)])

            return f"Method {method} added  for path {path} "

    def request(self, method, path):
        if (method, path) not in self.storage.keys():
            if path not in self.path_storage:
                return f'Error 404, path {path} not found'
            else:
                return f'Error 405, Method {method}  not allowed'

        else:
            func = self.storage[(method, path)]
            return func(path, method)


def my_info(path, method):
    return 200, {"Me": "Joanne"}


def update_me(path, method):
    return 200, "OK"


if __name__ == "__main__":
    router = Router()

    print(router.add_path('/me', 'GET', my_info))
    print(router.add_path('/me', 'PATCH', update_me))

    print(router.request('GET', '/me'))
    print(router.get('/me'))

    print(router.post('/me'))
    print(router.get('/us'))
