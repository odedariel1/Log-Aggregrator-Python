from flask import Flask, render_template, abort
from datetime import datetime
app = Flask(__name__)


def read_data(file_name):
    with open(file_name) as f:
        yield from f


def count_lines(file_name):
    with open(file_name) as f:
        return len(f.readlines())


def file_reader(log_counts, log_data):
    for status in ['info', 'warning', 'error']:
        log_counts[status] = 0
        log_data[status] = []
        log_file = f"Logs/{status}_logs.txt"
        try:
            data = read_data(log_file)
            log_counts[status] = count_lines(log_file)
            for data_list in range(log_counts[status]):
                content = next(data).split(";")
                content[0] = datetime.strptime(content[0], '%Y-%m-%dT%H:%M:%S.%f')
                log_data[status].append(content)

        except StopIteration:
            continue
        except FileNotFoundError:
            log_counts[status] = 0
        except Exception as e:
            app.logger.error(f"Failed to read {log_file}: {e}")
            abort(500, description=f"Error reading log file: {status}")


@app.route('/')
def dashboard():
    log_counts = {}
    log_data = {}
    file_reader(log_counts, log_data)
    return render_template('dashboard.html', log_data=log_data, log_counts=log_counts)


if __name__ == '__main__':
    app.run(debug=True)
