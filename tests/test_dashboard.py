from pathlib import Path
from streamlit.testing.v1 import AppTest
from core import load_data


def test_filters_and_backlog_snapshot():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / 'app.py', default_timeout=20).run()
    assert not app.exception
    df = load_data()
    expected = df[df.month == df.month.max()].backlog.sum()
    assert app.metric[3].value == f'${expected/1e6:,.1f}M'
    app.sidebar.selectbox[1].set_value('Q2').run()
    app.sidebar.multiselect[0].set_value(['Europe']).run()
    scope = df[(df.month.dt.year == 2026) & (df.month.dt.quarter == 2) & (df.region == 'Europe')]
    assert app.metric[0].value == f'${scope.actual_revenue.sum()/1e6:,.1f}M'
    app.sidebar.multiselect[0].set_value([]).run()
    assert not app.exception
    assert 'No records' in app.info[0].value


def test_navigation_and_question_boundary():
    app = AppTest.from_file(Path(__file__).resolve().parents[1] / 'app.py', default_timeout=20).run()
    app.sidebar.toggle[0].set_value(True).run()
    app.sidebar.radio[0].set_value('Revenue detail').run()
    assert not app.exception and len(app.dataframe) == 1
    app.sidebar.radio[0].set_value('Finance questions').run()
    app.text_input[0].set_value('What is bookings in 2026?')
    app.button[0].click().run()
    assert not app.exception and 'Bookings' in app.success[0].value
    app.text_input[0].set_value('Why is profit down?')
    app.button[0].click().run()
    assert len(app.warning) == 1 and not app.success
