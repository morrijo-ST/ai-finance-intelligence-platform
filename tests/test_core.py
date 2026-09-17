from core import load_data, executive_brief, answer_question

def test_data_and_brief():
    df=load_data()
    assert len(df)>100
    assert "Revenue is" in executive_brief(df)

def test_question():
    df=load_data()
    ans=answer_question(df,"What is bookings in 2026?")
    assert "Bookings" in ans
