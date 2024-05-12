def read_data(file_name):
    with open(file_name) as f:
        yield from f


def count_lines(file_name):
    with open(file_name) as f:
        return len(f.readlines())


def file_reader():
    log_counts = {}
    log_data = {}
    for status in ['info', 'warning', 'error']:
        log_counts[status] = 0
        log_file = f"Logs/{status}_logs.txt"
        try:
            data = read_data(log_file)
            log_counts[status] = count_lines(log_file)
            print(f'log {status} ({log_counts[status]})')
            for _ in range(log_counts[status]):
                log_data[status] = next(data).split(";")
                print(f'Date: {log_data[status][0]}, Message: {log_data[status][1]}')

        except StopIteration:
            continue
        except FileNotFoundError:
            print('didnt found file')


file_reader()
