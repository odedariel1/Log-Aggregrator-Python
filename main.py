from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def dashboard():
    log_counts = {}
    log_messages = {}
    for status in ['info', 'warning', 'error']:
        log_file = f"Logs/{status}_logs.txt"
        try:
            with open(log_file, 'r') as file:
                log_counts[status] = len(file.readlines())

        except FileNotFoundError:
            log_counts[status] = 0
        except Exception as e:
            app.logger.error(f"Failed to read {log_file}: {e}")
            abort(500, description=f"Error reading log file: {status}")
    return render_template('dashboard.html',data={1,2,3}, log_counts=log_counts)

if __name__ == '__main__':
    app.run(debug=True)
