import dash
import dash_html_components as html

app = dash.Dash()

crash_free = 0

def refresh_layout():
    global crash_free
    crash_free += 1
    return html.H1(
        'Crash free for {} refreshes'.format(crash_free)
    )

app.layout = refresh_layout

if __name__ == '__main__':
    app.run_server()